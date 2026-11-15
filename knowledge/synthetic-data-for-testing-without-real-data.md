---
title: Three ways to make synthetic data: LLM prompts with a schema, GANs, or distribution parameters
tags: [ml, process, iot]
source: Lecture 11 (lecturer feedback)
---

When real data is unavailable or sensitive, the lecturer suggested:
1. Prompt an LLM with the table structure (columns, record shape), and ask for realistic rows for Ghana. It works from publicly known generalities to produce specifics.
2. Generative models such as GANs (a generator tries to fool a discriminator, like counterfeiting) trained on a small real sample.
3. Distribution parameters: take mean, median, mode and standard deviation, then use a random number generator to draw 10,000 or 20,000 samples whose average matches what you put in.

For SmartCity Accra, option 3 is the simplest for PM2.5, bin fill level and drain water level; add daily patterns, drift and occasional spikes or dropouts so alerts and forecasts get exercised. Our HealthConnect work used synthetic data scaled from published regional statistics.

## Related
- [Build the Smart City pipeline end to end on synthetic data now; plug in sensors later](smart-city-build-pipeline-first-hardware-later.md)
- [Validate at front end, API and database; range limits catch impossible values](database-as-last-line-of-defense-range-checks.md)
