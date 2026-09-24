# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->
This is a Q&A system based on the city_guides corpora. Its main function is to analyze the data, which contains information about several key areas of a city, as well as different towns in it and recommendations in areas dinning, transportation, entertainment, etc. 
It aims to answer questions in an easy fashion and facilitate the document where more information can be found, which is also where the given answer comes from.

## Chunking Strategy

**Chunk size:**
**Overlap:**

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

======================================================================
Chunk 1  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents
======================================================================
# Getting around the region with limited mobility
## Overview

An honest assessment rather than a promotional one. Some of these places are difficult and it is better to know in advance.

======================================================================
Chunk 2  |  source: guide_corry_vale.md#4  |  produced by: chunker.py::split_documents
======================================================================
# Corry Vale
## What to see

The valley itself is the attraction. The footpath network is dense and well marked, and a circuit taking in three of the four villages is about nine miles with 500 metres of ascent. The chapel in the second village is 12th century and always unlocked.

======================================================================
Chunk 3  |  source: guide_givens_mill.md#4  |  produced by: chunker.py::split_documents
======================================================================
# Givens Mill
## What to see

The mill runs tours on the hour from 11 to 3 and the machinery is operating during them, which is loud and much more impressive than a static exhibit. The church has a Saxon doorway. The river walk downstream reaches Brightwater in about three hours.

======================================================================
Chunk 4  |  source: guide_marchwood.md#3  |  produced by: chunker.py::split_documents
======================================================================
# Marchwood
## Eat and drink

The best eating is in the Northgate district, a 12-minute tram ride from the station, where about thirty restaurants sit within four streets. The area immediately around the station is uniformly poor and expensive. Marchwood keeps later hours than anywhere elsein the region — kitchens serve until 10:30pm, and until midnight on Fridays and Saturdays.

======================================================================
Chunk 5  |  source: guide_seasons.md#2  |  produced by: chunker.py::split_documents
======================================================================
# When to visit the region
## Summer, June to August

June is excellent everywhere. July and August split: Halden Bay becomes very busy and the parking problem dominates, Kestrelford fills with walkers, and Brightwater goes quiet to the point of dullness with the university empty.

For each one, ask: could someone answer a question using only this,
without reading what came before or after?
(.venv) camila@Camilas-MacBook-Air ai201-project1-unofficial-guide-starter-v2026 % python app.py chunks
115 chunks total. Showing 5, spread across the corpus.

Paste these into your README under Sample Chunks. The rubric asks
for the source file and the function that produced them — both are
printed for you below.

======================================================================
Chunk 1  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents
======================================================================
# Getting around the region with limited mobility
## Overview

An honest assessment rather than a promotional one. Some of these places are difficult and it is better to know in advance.

======================================================================
Chunk 2  |  source: guide_corry_vale.md#4  |  produced by: chunker.py::split_documents
======================================================================
# Corry Vale
## What to see

The valley itself is the attraction. The footpath network is dense and well marked, and a circuit taking in three of the four villages is about nine miles with 500 metres of ascent. The chapel in the second village is 12th century and always unlocked.

======================================================================
Chunk 3  |  source: guide_givens_mill.md#4  |  produced by: chunker.py::split_documents
======================================================================
# Givens Mill
## What to see

The mill runs tours on the hour from 11 to 3 and the machinery is operating during them, which is loud and much more impressive than a static exhibit. The church has a Saxon doorway. The river walk downstream reaches Brightwater in about three hours.

======================================================================
Chunk 4  |  source: guide_marchwood.md#3  |  produced by: chunker.py::split_documents
======================================================================
# Marchwood
## Eat and drink

The best eating is in the Northgate district, a 12-minute tram ride from the station, where about thirty restaurants sit within four streets. The area immediately around the station is uniformly poor and expensive. Marchwood keeps later hours than anywhere elsein the region — kitchens serve until 10:30pm, and until midnight on Fridays and Saturdays.

======================================================================
Chunk 5  |  source: guide_seasons.md#2  |  produced by: chunker.py::split_documents
======================================================================
# When to visit the region
## Summer, June to August

June is excellent everywhere. July and August split: Halden Bay becomes very busy and the parking problem dominates, Kestrelford fills with walkers, and Brightwater goes quiet to the point of dullness with the university empty.


## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**(.venv) camila@Camilas-MacBook-Air ai201-project1-unofficial-guide-starter-v2026 % python app.py ask "how many people are there in Brightwater?" --show-prompt
 
**Answer:**
(best distance 0.271, cutoff 0.55)

======================================================================
System instruction sent with the prompt
======================================================================
You answer questions using only the documents provided to you.

Rules:
- Use only the information in the documents below. Do not use anything you know from elsewhere.
- If the documents don't cover the question, say you don't have enough information. Do not guess.
- Name the document your answer came from, using the filename given in each excerpt.
- Be brief. Two or three sentences is usually enough.

======================================================================
The assembled prompt, exactly as sent
======================================================================
Documents:

[from guide_brightwater.md]
# Brightwater
## Overview

Brightwater is a river town of about 40,000 people, roughly doubling in term time. It grew around a mill that closed in 1974 and spent twenty years working out what to be instead. The answer turned out to be the university.

[from guide_accessibility.md]
# Getting around the region with limited mobility
## Straightforward

**Brightwater** is level along the river and through the centre. The mill museum is step-free. The station is a 15-minute walk from campus on flat ground, or the shuttle meets the four busiest arrivals.

[from guide_marchwood.md]
# Marchwood
## Getting there

Every railway line in the region meets here, which is the city's defining feature. Trains to Brightwater run every 40 minutes until 11pm. The airport is 20 minutes out by a dedicated bus that runs every 15 minutes and costs more than the equivalent taxi shared between three people.

[from guide_brightwater.md]
# Brightwater
## Getting there

The train runs to the regional hub eleven times a day on weekdays and six times on Sundays, taking 50 minutes. The station is a 15-minute walk from campus, or the shuttle meets the four busiest arrivals. Long-distance coaches stop on Verrill Street rather than at the station, which catches people out. There is no airport; the nearest is 90 minutes by road.

[from guide_thornby_wells.md]
# Thornby Wells
## Getting there

On the Marchwood line, 25 minutes from the hub, with trains every hour and every two hours on Sundays. The station is in the centre. Driving from Brightwater is 45 minutes on good roads. Parking is free for two hours everywhere in town, which is unusual and generous.

---

Question: how many people are there in Brightwater?

Answer using only the documents above, and name the file you used.
======================================================================

Brightwater has a population of about 40,000 people, which roughly doubles during term time (from guide_brightwater.md).

Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_marchwood.md, guide_thornby_wells.md

1 model calls this session, 567 tokens (536 in, 31 out)


**My relevance cutoff:**
THRESHOLD = 0.56

I chose this number as a threshold after the findings when testing the two groups: 
- Non-corpus questions best distance average: 0.7962
- Corpes questions best distance average: 0.4812

Even though the average of the corpus responses is 0.48 there are questions that are answered correctly and have a higher best distance that does not seem to surpase 0.56 

| Question                                                   | In corpus? | Best distance |
|------------------------------------------------------------|------------|---------------|
|Which places are most accessible?                           |    True    |      0.485    |
|where are the most expensive dining options?                |    True    |      0.552    |
|what is the best place to go for a hike with hills?         |    True    |      0.549    |
|how long does it take to get to Marchwood from the airport? |    True    |      0.325    |
|How much is the price to enter the city museum?             |    True    |      0.495    |
|-----------------------------------------------------------------------------------------|
|What is harry potter about?                                 |    False   |      0.810    |
|Where is Denmark?                                           |    False   |      0.819    |
|what is the best type of  coffee in autumn?                 |    False   |      0.648    |
|what does rosemary do?                                      |    False   |      0.843    |
|which display is the best to create an ebook?               |    False   |      0.861    |
|-----------------------------------------------------------------------------------------|


## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.** 
I asked Claude to find weaknesses on my initial chunking idea (using the Markdown style to chunk). It helped me clarify the approach since the data contains two styles of documens: 9 towm guides and 5 themed documents (whose themes are entertainment, dining, accessibility, etc across different areas of the city). Hence I proceeded to follow a common analysis for both documents with the slight difference of on the themed documents dividing by the city areas mentioned. 

**2.**

I gave Claude five system output chunks and asked whether questions could be answered based on those chunks and which ones. This was mainly for double-checking the chunking method efficiency and did not require to modify the code or implement anything on top of what was already done.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

|                      Criterion                          | Target | Run 1  |  Run 2 |  Run 3 | Verdict |
|---------------------------------------------------------|--------|--------|--------|--------|---------|
| 1. Retrieved chunk contains the answer                  | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 |  Met    | in all the cases answer is contained in the chunk retrieved
| 2. Every answer names a source                          | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 |  Met    | all of the answers contain a minimum of one source cited 
| 3. Gate stops out-of-corpus questions                   | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 |  Met    | out-of-corpus questions were all rejected by the gate
| 4. None of the chunks cut mid-sentence or mid-word      | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 |  Met    |  each answer had a complete idea, no cutting mid sentence or mid word
| 5. System names all documents where information is found| 3 of 5 | 5 of 5 | 5 of 5 | 5 of 5 |  Met    |  raw retrieved-vs-cited file counts show more retrieved than cited every time (top-k over-fetches), but that's the wrong yardstick — tracing each answer's claims back to the documents shows no answer ever uses a fact from an uncited source (see below)

Criterion Change (measurement method, not the target):
Original measurement: compare count of retrieved files to count of cited files per answer.
Revised measurement: trace whether every specific claim in an answer appears in one of its *cited* documents, by reading the answer against the retrieved files.
Why: the file-count comparison came out 0 of 5 on every run, because top-k retrieval always returns more files than the answer actually draws from — that comparison can never distinguish "used an uncited source" from "retrieved something irrelevant and correctly ignored it." Rereading each answer against the documents answers the actual question. For example, on "where are the most expensive dining options?", several runs mention Pellew Sands' seafront pricing without citing `guide_pellew_sands.md` — but that exact fact ("the seafront is chips and ice cream... Marine Terrace... roughly half the seafront price") is already stated in `guide_eating.md`, which *is* cited. So the system isn't drawing from an uncited file, it's just picking one of two documents that duplicate the same fact. Checked this way, all 5 questions across all 3 run logs pass.


<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

Source: run_2026-09-23_1831.md      Command: python run_eval.py       Function: run_eval.py::main

### Which places are most accessible? — run 1

- Best distance: 0.4854 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_regional_transport.md, guide_walking.md

```
According to `guide_walking.md`, **Thornby Wells** is the region's most accessible town on foot, featuring flat, formal gardens and level streets. Additionally, `guide_accessibility.md` notes that Thornby Wells is the easiest town in the region for limited mobility, being flat, compact, and level throughout its pump room and gardens.
```

### Which places are most accessible? — run 2

- Best distance: 0.4854 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_regional_transport.md, guide_walking.md

```
According to **guide_walking.md**, **Thornby Wells** is the region's most accessible town on foot. Similarly, **guide_accessibility.md** states that **Thornby Wells** is the easiest town in the region.
```

### Which places are most accessible? — run 3

- Best distance: 0.4854 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_regional_transport.md, guide_walking.md

```
Based on the provided documents, **Thornby Wells** is the region's most accessible town on foot and the easiest town in the region for limited mobility. 

Sources: `guide_walking.md` and `guide_accessibility.md`.
```

### Where are the most expensive dining options? — run 1

- Best distance: 0.5522 (passed the gate)
- Sources retrieved: guide_eating.md, guide_halden_bay.md, guide_pellew_sands.md

```
The most expensive dining options are found on the harbour front in Halden Bay (which are roughly double the prices on Fell Street) and on visitor-oriented strips like Brightwater's riverside strip. 

Source: `guide_eating.md` and `guide_halden_bay.md`
```

### Where are the most expensive dining options? — run 2

- Best distance: 0.5522 (passed the gate)
- Sources retrieved: guide_eating.md, guide_halden_bay.md, guide_pellew_sands.md

```
The most expensive dining options are found on the visitor-heavy strips, specifically Brightwater's riverside strip, Halden Bay's harbour front (which is roughly double the prices on Fell Street), and Pellew Sands's seafront. 

Sources: `guide_eating.md` and `guide_halden_bay.md`
```

### Where are the most expensive dining options? — run 3

- Best distance: 0.5522 (passed the gate)
- Sources retrieved: guide_eating.md, guide_halden_bay.md, guide_pellew_sands.md

```
The most expensive dining options are found on Halden Bay's harbour front (which is roughly double the prices on Fell Street) and Brightwater's riverside strip, as well as Pellew Sands's seafront compared to Marine Terrace. 

Sources: `guide_eating.md` and `guide_halden_bay.md`.
```

### What is the best place to go for a hike with hills? — run 1

- Best distance: 0.5491 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_regional_transport.md, guide_walking.md

```
Based on the documents, the Corry Vale circuit is a moderate walk with hills (covering about nine miles with 500 metres of ascent). 

This comes from **guide_walking.md** (and is also mentioned in **guide_corry_vale.md**).
```

### What is the best place to go for a hike with hills? — run 2

- Best distance: 0.5491 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_regional_transport.md, guide_walking.md

```
Based on the documents, the Corry Vale circuit provides a moderate walk with hills, covering about nine miles with 500 metres of ascent (source: guide_walking.md and guide_corry_vale.md).
```

### What is the best place to go for a hike with hills? — run 3

- Best distance: 0.5491 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_regional_transport.md, guide_walking.md

```
Based on the documents, the Corry Vale circuit provides a moderate walk with hills (covering about nine miles with 500 metres of ascent). 

Source: `guide_walking.md` (and `guide_corry_vale.md`)
```

### How long does it take to get to Marchwood from the airport? — run 1

- Best distance: 0.3254 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_marchwood.md, guide_thornby_wells.md

```
It takes 20 minutes to get to Marchwood from the airport by a dedicated bus. (Source: guide_marchwood.md)
```

### How long does it take to get to Marchwood from the airport? — run 2

- Best distance: 0.3254 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_marchwood.md, guide_thornby_wells.md

```
It takes 20 minutes to get to Marchwood from the airport by a dedicated bus (source: guide_marchwood.md).
```

### How long does it take to get to Marchwood from the airport? — run 3

- Best distance: 0.3254 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_marchwood.md, guide_thornby_wells.md

```
It takes 20 minutes to get to Marchwood from the airport by a dedicated bus (source: guide_marchwood.md).
```

### How much is the price to enter the city museum? — run 1

- Best distance: 0.4952 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_givens_mill.md, guide_kestrelford.md, guide_marchwood.md

```
Based on the provided documents, the city museum is free (guide_marchwood.md).
```

### How much is the price to enter the city museum? — run 2

- Best distance: 0.4952 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_givens_mill.md, guide_kestrelford.md, guide_marchwood.md

```
Based on the provided documents, the city museum in Marchwood is free (guide_marchwood.md).
```

### How much is the price to enter the city museum? — run 3

- Best distance: 0.4952 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_givens_mill.md, guide_kestrelford.md, guide_marchwood.md

```
Based on the provided documents, the city museum in Marchwood is free (guide_marchwood.md).
```


## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # |                          Criterion                    | Verdict |                 How I decided                               |
|---|-------------------------------------------------------|---------|-------------------------------------------------------------|
| 1 | Retrieved chunk contains the answer                   |   Met   |  in all the cases answer is contained in the chunk retrieved|
| 2 | Every answer names a source                           |   Met   |  all of the answers contain a minimum of one source cited   |
| 3 | Gate stops out-of-corpus questions                    |   Met   |  out-of-corpus questions were all rejected by the gate      |
| 4 | None of the chunks cut mid-sentence or mid-word       |   Met   |  each answer had a complete idea, no cutting mid sentence or mid word|
| 5 | System names all documents where information is found | Met     | raw retrieved-vs-cited counts are a floored, always-fails proxy given top-k over-fetch; tracing each answer's actual claims against the documents shows no answer ever draws from an uncited file (see Criterion Change note under the run log above) |
