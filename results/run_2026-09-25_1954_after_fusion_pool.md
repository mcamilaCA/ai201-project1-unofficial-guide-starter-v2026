# Run log — after_fusion_pool

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `city_guides` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.56
- Runs per question: 3, caching off
- When: 2026-09-25 19:54

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Which places are most accessible? | pass | pass | pass |
| Where are the most expensive dining options? | fail | fail | pass |
| What is the best place to go for a hike with hills? | pass | pass | pass |
| How long does it take to get to Marchwood from the airport? | pass | pass | pass |
| How much is the price to enter the city museum? | pass | pass | pass |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.56. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is harry potter about? | 0.832 | refused |
| Where is Denmark? | 0.819 | refused |
| what is the best type of  coffee in autumn? | 0.648 | refused |
| what does rosemary do? | 0.843 | refused |
| which display is the best to create an ebook? | 0.861 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### Which places are most accessible? — run 1

- Best distance: 0.4854 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_halden_bay.md, guide_regional_transport.md, guide_walking.md

```
Based on the provided documents, **Thornby Wells** is the most accessible town in the region, featuring flat, formal gardens, level streets, and level areas throughout the pump room and gardens (guide_walking.md and guide_accessibility.md).
```

### Which places are most accessible? — run 2

- Best distance: 0.4854 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_halden_bay.md, guide_regional_transport.md, guide_walking.md

```
Based on the provided documents, **Thornby Wells** is described as the region's most accessible town on foot (from `guide_walking.md`) and the easiest town in the region for those with limited mobility (from `guide_accessibility.md`).
```

### Which places are most accessible? — run 3

- Best distance: 0.4854 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_halden_bay.md, guide_regional_transport.md, guide_walking.md

```
**Thornby Wells** is the most accessible town in the region on foot and for people with limited mobility, as it features flat, formal gardens, level streets, and is compact and flat (from *guide_walking.md* and *guide_accessibility.md*).
```

### Where are the most expensive dining options? — run 1

- Best distance: 0.5522 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_eating.md, guide_marchwood.md, guide_pellew_sands.md

```
Based on the provided documents, the most expensive dining options are found on the seafronts and tourist strips:
- In Brightwater, the riverside strip is priced for people walking from the hotels, whereas Corry Lane serves comparable food for about a third less (*guide_eating.md*).
- In Halden Bay, the harbour front is roughly double the price of Fell Street (*guide_eating.md*).
- In Marchwood, the area immediately around the station is uniformly poor and expensive (*guide_marchwood.md*).
```

### Where are the most expensive dining options? — run 2

- Best distance: 0.5522 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_eating.md, guide_marchwood.md, guide_pellew_sands.md

```
Based on the provided documents, the most expensive dining options are found on the seafronts and tourist strips:

* In Brightwater, the riverside strip is priced for people walking from the hotels, which is more expensive than Corry Lane (guide_eating.md).
* In Halden Bay, the harbour front is roughly double the price of Fell Street (guide_eating.md).
* In Marchwood, the area immediately around the station is uniformly poor and expensive (guide_marchwood.md).
```

### Where are the most expensive dining options? — run 3

- Best distance: 0.5522 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_eating.md, guide_marchwood.md, guide_pellew_sands.md

```
Based on the provided documents, the most expensive dining options are found on the seafronts and riverside strips where visitors walk from hotels (such as Brightwater's riverside strip and Halden Bay's harbour front), as well as the area immediately around the Marchwood station, which is noted as expensive (*guide_eating.md* and *guide_marchwood.md*).
```

### What is the best place to go for a hike with hills? — run 1

- Best distance: 0.5491 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_regional_transport.md, guide_walking.md

```
Based on the documents, the Corry Vale circuit is a moderate hike with hills, taking in three of the four villages over about nine miles with 500 metres of ascent (*guide_walking.md* and *guide_corry_vale.md*).
```

### What is the best place to go for a hike with hills? — run 2

- Best distance: 0.5491 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_regional_transport.md, guide_walking.md

```
Based on the documents, the Corry Vale circuit is a moderate hike with hills, covering about nine miles with 500 metres of ascent (source: `guide_walking.md` and `guide_corry_vale.md`).
```

### What is the best place to go for a hike with hills? — run 3

- Best distance: 0.5491 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_regional_transport.md, guide_walking.md

```
Based on the documents, the Corry Vale circuit is a moderate hike with hills, covering about nine miles with 500 metres of ascent (guide_walking.md and guide_corry_vale.md).
```

### How long does it take to get to Marchwood from the airport? — run 1

- Best distance: 0.3254 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_marchwood.md

```
It takes 20 minutes to get to Marchwood from the airport by a dedicated bus. 

Source: `guide_marchwood.md`
```

### How long does it take to get to Marchwood from the airport? — run 2

- Best distance: 0.3254 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_marchwood.md

```
It takes 20 minutes to get to Marchwood from the airport by a dedicated bus. 

Source: guide_marchwood.md
```

### How long does it take to get to Marchwood from the airport? — run 3

- Best distance: 0.3254 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_marchwood.md

```
It takes 20 minutes to get from the airport to Marchwood by a dedicated bus. (Source: guide_marchwood.md)
```

### How much is the price to enter the city museum? — run 1

- Best distance: 0.4952 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_givens_mill.md, guide_marchwood.md

```
Based on the provided documents, the city museum is free (source: `guide_marchwood.md`).
```

### How much is the price to enter the city museum? — run 2

- Best distance: 0.4952 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_givens_mill.md, guide_marchwood.md

```
Based on the documents provided, the city museum is free (guide_marchwood.md).
```

### How much is the price to enter the city museum? — run 3

- Best distance: 0.4952 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_givens_mill.md, guide_marchwood.md

```
The city museum is free according to `guide_marchwood.md`.
```
