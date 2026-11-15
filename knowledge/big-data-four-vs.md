---
title: Big data is described by Volume, Velocity, Variety (and Veracity)
tags: [lecture, databases]
source: Lecture 5
---

- **Volume**: how much data. Lecture examples from a "data never sleeps" style dashboard: about 16 thousand TikTok video uploads per minute, hundreds of thousands of Netflix streaming hours per minute, about 18.8 million text messages per minute.
- **Velocity**: how fast it arrives and must be processed.
- **Variety**: structured, semi-structured and unstructured forms (see [structured-semi-structured-unstructured-data.md](structured-semi-structured-unstructured-data.md)).
- **Veracity**: how trustworthy or clean the data is.

Why it matters: you cannot process big data by loading it into one machine's RAM; it must be split across many servers (see [data-intensive-computing-distribute-chunks.md](data-intensive-computing-distribute-chunks.md)).

For SmartCity Accra: many sensors reporting every few seconds is a velocity problem; mixed readings, images and logs is variety; faulty sensors are a veracity problem.

## Related
- [Data-intensive computing moves work to data spread across servers, not data into one machine's RAM](data-intensive-computing-distribute-chunks.md)
- [Structured, semi-structured and unstructured data need different stores](structured-semi-structured-unstructured-data.md)
