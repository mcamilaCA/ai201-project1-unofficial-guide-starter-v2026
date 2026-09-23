"""
Decide whether an answer was actually correct.

`run_eval.py` looks for a function here called `judge(question, expects,
answer, results) -> bool` and, if it finds one, uses it to fill in the Run
columns of the report instead of leaving them blank.

The approach: `expects` holds one or more short phrases you'd expect a
correct answer to contain (see questions.py). We normalize away case and
punctuation differences, split `expects` into independent candidate phrases
when it lists more than one thing, and pass if the answer contains at least
one of them as a whole phrase.

Known gaps, left unsolved on purpose because they're rare and fixing them
adds real complexity: no digit/word-number equivalence ("30" won't match
"thirty"), and phrases must appear in the same word order they were written
in (an answer that reorders "Corry Vale circuit" as "circuit around Corry
Vale" won't match).
"""

import re

from gate import REFUSAL

# Comma, or the standalone word "and" — splits both "A, B, and C" and "A and B".
_ITEM_SPLIT_RE = re.compile(r",|\band\b", re.IGNORECASE)

# Anything that isn't a letter, digit, or whitespace, once possessives are gone.
_PUNCT_RE = re.compile(r"[^\w\s]")
_POSSESSIVE_RE = re.compile(r"'s\b")
_WHITESPACE_RE = re.compile(r"\s+")


def normalize(text: str) -> str:
    """Lowercase and strip punctuation so comparisons ignore case/formatting."""
    text = text.lower().replace("’", "'")
    text = _POSSESSIVE_RE.sub("", text)
    text = _PUNCT_RE.sub(" ", text)
    return _WHITESPACE_RE.sub(" ", text).strip()


def split_expected_items(expects: str) -> list[str]:
    """Split `expects` into independent candidate phrases.

    "Thornby Wells, Marchwood, and Brightwater" -> three separate places.
    "About 30 minutes" -> stays whole; it has no comma or standalone "and".
    """
    parts = _ITEM_SPLIT_RE.split(expects)
    return [p.strip() for p in parts if p.strip()]


def contains_phrase(answer_norm: str, item_norm: str) -> bool:
    """Whether `item_norm` appears in `answer_norm` as whole, contiguous words."""
    if not item_norm:
        return False
    pattern = r"\b" + re.escape(item_norm) + r"\b"
    return re.search(pattern, answer_norm) is not None


def is_refusal(answer: str) -> bool:
    """Whether the answer is the gate's canned refusal rather than a real one."""
    return answer.strip() == REFUSAL


def judge(question: str, expects: str, answer: str, results: list) -> bool:
    """Whether `answer` contains at least one of the phrases named in `expects`."""
    if is_refusal(answer):
        return False

    items = split_expected_items(expects)
    if not items:
        return False

    answer_norm = normalize(answer)
    return any(contains_phrase(answer_norm, normalize(item)) for item in items)
