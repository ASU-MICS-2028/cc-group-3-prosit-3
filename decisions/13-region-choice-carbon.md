---
issue: 13
title: Stay in af-south-1 (and africa-south1 for the GCP rebuild) despite the dirtier grid
date: 2026-11-15
decided_by: Joseph (proposed; Eugene to confirm for the graded AWS build)
status: proposed
---

## Context

Lab 11 Part D asks for a carbon estimate of our region choice, or a documented lower-carbon region choice, plus one trade-off. The provider tools can't help yet: AWS's Customer Carbon Footprint Tool only reports past usage on the account, and our GCP project (#16) doesn't exist yet. So we estimated it by hand with the Cloud Carbon Footprint method. Inputs, script and output: [`evidence/lab11/13-carbon-estimate.py`](../evidence/lab11/13-carbon-estimate.py) and [`13-carbon-estimate-output.txt`](../evidence/lab11/13-carbon-estimate-output.txt).

Assumed stack (until #12 sets the real sizes): broker+bridge, 2 API servers, a time-series DB, 2 h of ML training a day, about 5,960 vCPU-hours and 10,700 GB-hours a month at 50% CPU. That's about 19–21 kWh a month.

| Region | Grid (gCO2e/kWh) | kg CO2e/month | t4g.small on-demand $/h | Latency from Ghana (Prosit 1, median) |
|---|---|---|---|---|
| AWS af-south-1, Cape Town | 757 | 14.5 | 0.0217 | 74 ms |
| AWS us-east-1, N. Virginia | 365 | 7.0 | 0.0168 | 175 ms |
| GCP africa-south1, Johannesburg (15% CFE) | 641 | 13.4 | — | not measured |
| GCP europe-west1, Belgium (79% CFE) | 126 | 2.6 | — | not measured |
| GCP europe-west9, Paris (96% CFE) | 16 | 0.3 | — | 127 ms |

Prices from the AWS Price List API (15 Nov 2026); grid factors from Cloud Carbon Footprint (AWS) and Google's 2025 region data (GCP); latency from [the Prosit 1 measurement](../knowledge/agroconnect-region-selection-by-latency.md).

## Options
1. **af-south-1 / africa-south1 (South Africa).** For: lowest latency from Accra, data stays on the continent, the brief names af-south-1. Against: South Africa's coal-heavy grid; the most CO2e of the five; af-south-1 is 29% dearer than us-east-1 per t4g.small hour.
2. **us-east-1.** For: half the CO2e and 23% cheaper. Against: 175 ms from Ghana, AMA data leaves Africa.
3. **europe-west9 (Paris) for the GCP rebuild.** For: about 1/40 of the CO2e (96% carbon-free). Against: 127 ms, data leaves Africa, and it would make the AWS-vs-GCP comparison (#45) a comparison of grids, not providers.

## Decision

Stay in South Africa on both clouds. The trade-off we accept: **af-south-1 costs more and emits about twice as much as us-east-1 for the same servers, in exchange for half the latency and keeping Accra's data in Africa.** Flood warnings are time-critical and AMA residents' data shouldn't leave the continent without a reason, and in absolute terms the difference is small: about 7.5 kg CO2e a month at our size.

We cut carbon the way that also cuts cost: turn off what isn't used. Scale the API to its minimum at night, run ML training as a scheduled job rather than an always-on server, filter and batch at the edge (the bridge) so fewer bytes are stored, and tear down each lab's resources when it's done.

## Consequences
- Re-run the script once #12 has real sizes, and again with real AWS usage from the Customer Carbon Footprint Tool after a month of billing.
- If a component ever needs no low latency (e.g. nightly batch training on archived, anonymised data), Paris or Belgium is the low-carbon place to run it; that's a deliberate exception, recorded as its own decision.
- The estimate is operational only: no embodied hardware emissions, storage or network energy. It's location-based (grid average), not the market-based figure after providers' renewable purchases.
