# Run log — after_fusion_fix

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `city_guides` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.56
- Runs per question: 3, caching off
- When: 2026-09-25 19:48

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Which places are most accessible? | pass | pass | pass |
| Where are the most expensive dining options? | fail | fail | fail |
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
Based on the documents, **Thornby Wells** is noted as the region's most accessible town on foot (from `guide_walking.md`) and the easiest town in the region for visitors with limited mobility, being flat, compact, and level throughout (from `guide_accessibility.md`).
```

### Which places are most accessible? — run 2

- Best distance: 0.4854 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_halden_bay.md, guide_regional_transport.md, guide_walking.md

```
Based on the documents, **Thornby Wells** is identified as the most accessible town in the region on foot and for those with limited mobility (*guide_walking.md* and *guide_accessibility.md*).
```

### Which places are most accessible? — run 3

- Best distance: 0.4854 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_halden_bay.md, guide_regional_transport.md, guide_walking.md

```
Based on the provided documents, **Thornby Wells** is described as the region's most accessible town on foot (from `guide_walking.md`) and the easiest town in the region for visitors with limited mobility (from `guide_accessibility.md`).
```

### Where are the most expensive dining options? — run 1

- Best distance: 0.5522 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_eating.md, guide_marchwood.md, guide_pellew_sands.md

```
Based on the provided documents:

* In Brightwater, the riverside strip is priced for people who walked there from the hotels, while Corry Lane serves comparable food for about a third less (*guide_eating.md*). 
* In Halden Bay, the harbour front is roughly double the price of Fell Street (*guide_eating.md*).
* In Pellew Sands, the better cooking is on Marine Terrace at roughly half the seafront price (*guide_pellew_sands.md* and *guide_eating.md*).
* In Marchwood, the area immediately around the station is uniformly poor and expensive (*guide_marchwood.md*).
```

### Where are the most expensive dining options? — run 2

- Best distance: 0.5522 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_eating.md, guide_marchwood.md, guide_pellew_sands.md

```
Based on the provided documents:

* In Brightwater, the riverside strip is priced for people who walked there from the hotels, whereas Corry Lane serves comparable food for about a third less (*guide_eating.md*). 
* In Halden Bay, the harbour front is roughly double the prices on Fell Street (*guide_eating.md*).
* In Pellew Sands, the better cooking is on Marine Terrace at roughly half the price of the seafront (*guide_pellew_sands.md* and *guide_eating.md*).
* In Marchwood, the area immediately around the station is uniformly poor and expensive, whereas the best eating is in the Northgate district (*guide_marchwood.md*).
```

### Where are the most expensive dining options? — run 3

- Best distance: 0.5522 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_eating.md, guide_marchwood.md, guide_pellew_sands.md

```
Based on the provided documents:

* In Brightwater, the riverside strip is priced for people who walked there from the hotels, while Corry Lane serves comparable food for about a third less (*guide_eating.md*). 
* In Halden Bay, the harbour front is roughly double the price of Fell Street (*guide_eating.md*).
* In Pellew Sands, the seafront offers chips and ice cream, while Marine Terrace features better cooking at roughly half the seafront price (*guide_pellew_sands.md* and *guide_eating.md*).
* In Marchwood, the area immediately around the station is uniformly poor and expensive (*guide_marchwood.md*).
```

### What is the best place to go for a hike with hills? — run 1

- Best distance: 0.5491 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_regional_transport.md, guide_walking.md

```
According to `guide_walking.md`, the **Corry Vale circuit** offers a moderate hike with hills, covering about nine miles with 500 metres of ascent. This same circuit is also mentioned in `guide_corry_vale.md`.
```

### What is the best place to go for a hike with hills? — run 2

- Best distance: 0.5491 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_regional_transport.md, guide_walking.md

```
Based on the documents, the Corry Vale circuit provides a moderate walk with hills, covering about nine miles with 500 metres of ascent (source: `guide_walking.md` and `guide_corry_vale.md`).
```

### What is the best place to go for a hike with hills? — run 3

- Best distance: 0.5491 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_regional_transport.md, guide_walking.md

```
Based on the provided documents, the Corry Vale circuit offers a moderate walk with hills, spanning about nine miles with 500 metres of ascent (guide_walking.md and guide_corry_vale.md).
```

### How long does it take to get to Marchwood from the airport? — run 1

- Best distance: 0.3254 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_marchwood.md

```
According to `guide_marchwood.md`, it takes 20 minutes to get to the airport (or from the airport) by a dedicated bus.
```

### How long does it take to get to Marchwood from the airport? — run 2

- Best distance: 0.3254 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_marchwood.md

```
According to `guide_marchwood.md`, it takes 20 minutes to get from the airport to Marchwood by a dedicated bus.
```

### How long does it take to get to Marchwood from the airport? — run 3

- Best distance: 0.3254 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_marchwood.md

```
It takes 20 minutes to get to Marchwood from the airport by a dedicated bus, according to `guide_marchwood.md`.
```

### How much is the price to enter the city museum? — run 1

- Best distance: 0.4952 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_givens_mill.md, guide_marchwood.md

```
Based on `guide_marchwood.md`, the city museum is free.
```

### How much is the price to enter the city museum? — run 2

- Best distance: 0.4952 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_givens_mill.md, guide_marchwood.md

```
Based on `guide_marchwood.md`, the city museum is free.
```

### How much is the price to enter the city museum? — run 3

- Best distance: 0.4952 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_givens_mill.md, guide_marchwood.md

```
Based on *guide_marchwood.md*, the city museum is free.
```
