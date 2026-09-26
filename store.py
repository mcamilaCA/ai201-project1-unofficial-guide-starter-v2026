"""
Stages 3 and 4 of the pipeline: embedding chunks and retrieving them.

Three things in here are worth knowing about, because they'd quietly break the
rest of the project if they were wrong:

1. The Chroma collection is created with cosine distance, explicitly. Chroma
   defaults to squared L2, and the 0.6 threshold the course uses is calibrated
   against cosine. Getting this wrong makes every distance number meaningless.

2. `search` returns the distance alongside each chunk. Milestone 4 has you
   compare distances, so they have to be visible.

3. The embedding model is the one Chroma bundles, not one loaded through
   `sentence-transformers`. It is the same model — `all-MiniLM-L6-v2`, 384
   dimensions — but it arrives as an ONNX build from Chroma's own CDN, so the
   install needs neither PyTorch nor a reachable Hugging Face. See `_embedder`.

4. `search` is hybrid: semantic (embeddings) ranks every chunk, and keyword
   (BM25) reranks only the top `FUSION_POOL_SIZE` of those — not the whole
   collection. The two rankings are merged by Reciprocal Rank Fusion — by
   rank position, not raw score, because cosine distance and BM25 score live
   on incompatible scales with no shared zero point. Each `Result` still
   carries its real cosine distance, never a fused score, so the gate's
   threshold in `gate.py` keeps meaning exactly what it always meant.
   Capping BM25 to the semantic pool matters: BM25 has no notion of topical
   relevance, only literal token overlap, so ranking it against the entire
   corpus let a chunk that merely shared one rare word with the question
   outrank a chunk semantic search correctly identified as the closest
   match, purely because the closer chunk paraphrased the answer instead of
   reusing the question's own wording.
"""

import os
import re
import shutil
from dataclasses import dataclass

# Must be set BEFORE chromadb is imported. Without it, some Chroma versions
# print "Failed to send telemetry event ..." on every single call — which looks
# exactly like a real error, isn't one, and cost a previous cohort a lot of
# confused help-channel messages.
os.environ.setdefault("ANONYMIZED_TELEMETRY", "False")

import chromadb  # noqa: E402
from rank_bm25 import BM25Okapi  # noqa: E402

import config
from chunker import Chunk


@dataclass
class Result:
    """One retrieved chunk and how far it was from the question."""

    text: str
    source: str
    label: str
    distance: float   # LOWER IS BETTER. 0.3 is close, 0.9 is unrelated.
    produced_by: str


_model = None

# The model Chroma bundles. Anything else in config.EMBEDDING_MODEL means
# "fetch that one from Hugging Face instead" — see `_embedder`.
BUNDLED_MODEL = "all-MiniLM-L6-v2"


class _OnnxEmbedder:
    """
    Chroma's built-in embedder, wrapped to look like the other two.

    Chroma's embedding functions are called directly and hand back numpy
    arrays. The rest of this file wants `.encode(texts)`, so the adapter lives
    here rather than making every caller care which embedder it got.
    """

    def __init__(self):
        from chromadb.utils.embedding_functions import ONNXMiniLM_L6_V2

        self._ef = ONNXMiniLM_L6_V2()

    def encode(self, texts, show_progress_bar: bool = False):
        return [vector.tolist() for vector in self._ef(list(texts))]


def _sentence_transformer(name: str):
    """
    The escape hatch: any model that isn't the bundled one.

    Unit 2's "try a second embedding model" stretch option comes through here,
    and so does anything you set `EMBEDDING_MODEL` to. This path *does* need
    `sentence-transformers` and a reachable Hugging Face, neither of which the
    default install has — which is the whole point of the default install.
    """
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:
        raise RuntimeError(
            f"config.EMBEDDING_MODEL is set to {name!r}, which isn't the model "
            f"Chroma bundles ({BUNDLED_MODEL!r}), so it has to be downloaded "
            f"from Hugging Face.\n"
            f"Install the optional dependency first:\n"
            f"    pip install 'sentence-transformers>=3.4,<3.5'\n"
            f"Or set EMBEDDING_MODEL back to {BUNDLED_MODEL!r}."
        ) from exc

    return SentenceTransformer(name)


def _embedder():
    """
    Load the embedding model once and keep it.

    First call is slow — it downloads about 80 MB. That's why setup happens
    before class.
    """
    global _model

    if _model is not None:
        return _model

    # Used only by this repo's own smoke test, which runs where no model can be
    # downloaded at all. Never set this yourself.
    if os.getenv("AI201_FAKE_EMBEDDINGS") == "1":
        from _smoke_embedder import FakeEmbedder

        _model = FakeEmbedder()
    elif config.EMBEDDING_MODEL == BUNDLED_MODEL:
        _model = _OnnxEmbedder()
    else:
        _model = _sentence_transformer(config.EMBEDDING_MODEL)

    return _model


def embed(texts: list[str]) -> list[list[float]]:
    """Turn text into vectors. Runs on your machine, costs no API quota."""
    vectors = _embedder().encode(texts, show_progress_bar=False)
    # sentence-transformers and the smoke stand-in return something with a
    # .tolist(); _OnnxEmbedder has already done that conversion itself.
    return vectors.tolist() if hasattr(vectors, "tolist") else vectors


def _tokenize(text: str) -> list[str]:
    """Lowercase word split. BM25 just needs consistent tokens, not linguistics."""
    return re.findall(r"\w+", text.lower())


# Keyed by collection name. Rebuilding this from scratch is a few milliseconds
# at this corpus's scale, but there's no reason to redo it on every question.
_bm25_cache: dict[str, tuple[BM25Okapi, list[str]]] = {}


def _bm25_index(collection, name: str) -> tuple[BM25Okapi, list[str]]:
    """
    Keyword index for one collection, built from its stored chunks.

    Chroma has no keyword index of its own. Rather than maintain a second
    persisted index file that has to stay in sync with `build_index`, this
    rebuilds from `collection.get()` on first use per collection and caches
    the result — cheap enough at hundreds of chunks that it isn't worth the
    extra moving part.
    """
    cached = _bm25_cache.get(name)
    if cached is not None:
        return cached

    stored = collection.get()
    ids = stored["ids"]
    tokenized_corpus = [_tokenize(doc) for doc in stored["documents"]]

    index = (BM25Okapi(tokenized_corpus), ids)
    _bm25_cache[name] = index
    return index


def _client():
    return chromadb.PersistentClient(
        path=str(config.CHROMA_DIR),
        settings=chromadb.config.Settings(anonymized_telemetry=False),
    )


def build_index(
    chunks: list[Chunk],
    corpus: str | None = None,
    variant: str = "default",
) -> int:
    """
    Embed every chunk and store it.

    `variant` lets you keep more than one index of the same corpus at the same
    time. In unit 2, when you compare two chunking strategies, index the second
    one as variant="v2" and you can query both instead of deleting the first
    and starting over.
    """
    name = config.collection_name(corpus, variant)
    client = _client()

    _bm25_cache.pop(name, None)

    try:
        client.delete_collection(name)
    except Exception:
        pass

    collection = client.create_collection(
        name=name,
        # ⚠️ Do not remove. Chroma defaults to squared L2, and every distance
        # number in this course assumes cosine.
        metadata={"hnsw:space": "cosine"},
    )

    batch = 256
    for start in range(0, len(chunks), batch):
        window = chunks[start : start + batch]
        collection.add(
            ids=[f"{c.source}#{c.index}" for c in window],
            documents=[c.text for c in window],
            embeddings=embed([c.text for c in window]),
            metadatas=[
                {"source": c.source, "index": c.index, "produced_by": c.produced_by}
                for c in window
            ],
        )

    return len(chunks)


# How many semantic candidates BM25 is allowed to rerank. A chunk that isn't
# even in this neighborhood can't win purely on an incidental keyword match —
# see the module docstring, point 4, for why that matters.
FUSION_POOL_SIZE = 20


def search(
    question: str,
    top_k: int | None = None,
    corpus: str | None = None,
    variant: str = "default",
) -> list[Result]:
    """
    Retrieve the chunks most relevant to a question — meaning and keywords.

    Semantic search (embeddings) ranks every chunk in the collection. Keyword
    search (BM25) then reranks only the top `FUSION_POOL_SIZE` of those —
    not the whole collection — and the two rankings are merged with
    Reciprocal Rank Fusion: a chunk's fused score is the sum, across both
    rankings, of 1 / (60 + its rank there). Fusing by rank rather than raw
    score sidesteps the fact that cosine distance and BM25 score aren't on
    comparable scales.

    Restricting BM25 to the semantic candidate pool (rather than ranking it
    against every chunk in the corpus) matters because BM25 has no concept of
    topical relevance, only literal token overlap: a chunk that happens to
    share one moderately rare word with the question can outscore a chunk
    that paraphrases the answer without using the question's exact wording,
    even when the paraphrase is the one semantic search correctly identified
    as the closest match. Confined to the semantic neighborhood, BM25 can
    still promote a buried-but-relevant chunk (its intended job) without
    reaching outside that neighborhood to pull in something semantically
    unrelated.

    Returned nearest-first by fused rank. `distance` on each `Result` is
    always the real cosine distance from the semantic ranking, never a fused
    score — the relevance gate depends on that staying true.
    """
    top_k = top_k or config.TOP_K
    name = config.collection_name(corpus, variant)

    try:
        collection = _client().get_collection(name)
    except Exception as exc:
        raise RuntimeError(
            f"No index called '{name}'. Run `python app.py index` first."
        ) from exc

    count = collection.count()
    if count == 0:
        return []

    pool_size = min(count, max(top_k, FUSION_POOL_SIZE))
    raw = collection.query(query_embeddings=embed([question]), n_results=pool_size)
    ids = raw["ids"][0]
    documents = dict(zip(ids, raw["documents"][0]))
    metadatas = dict(zip(ids, raw["metadatas"][0]))
    distances = dict(zip(ids, raw["distances"][0]))
    semantic_rank = {id_: rank for rank, id_ in enumerate(ids)}

    # Full-corpus BM25 scores (correct IDF statistics need the whole corpus),
    # but only this pool's ids get ranked against each other.
    bm25, bm25_ids = _bm25_index(collection, name)
    bm25_scores = dict(zip(bm25_ids, bm25.get_scores(_tokenize(question))))
    pool_bm25_order = sorted(ids, key=lambda id_: bm25_scores.get(id_, 0.0), reverse=True)
    bm25_rank = {id_: rank for rank, id_ in enumerate(pool_bm25_order)}

    RRF_K = 60
    fused_ids = sorted(
        ids,
        key=lambda id_: 1 / (RRF_K + semantic_rank[id_]) + 1 / (RRF_K + bm25_rank[id_]),
        reverse=True,
    )[:top_k]

    results: list[Result] = []
    for id_ in fused_ids:
        meta = metadatas[id_]
        results.append(
            Result(
                text=documents[id_],
                source=str(meta.get("source", "unknown")),
                label=f"{meta.get('source', 'unknown')}#{meta.get('index', 0)}",
                distance=float(distances[id_]),
                produced_by=str(meta.get("produced_by", "unknown")),
            )
        )
    return results


def index_exists(corpus: str | None = None, variant: str = "default") -> bool:
    """Is there an index here to search, without searching it?

    `serve.py`'s health check asks this. It deliberately does not embed
    anything: loading the embedding model takes 80 MB and a few seconds, and a
    health check that heavy is a health check nobody can afford to call.
    """
    try:
        collection = _client().get_collection(config.collection_name(corpus, variant))
        return collection.count() > 0
    except Exception:
        return False


def reset():
    """Delete every index. Occasionally the fastest way out of a mess."""
    _bm25_cache.clear()
    if config.CHROMA_DIR.exists():
        shutil.rmtree(config.CHROMA_DIR)
