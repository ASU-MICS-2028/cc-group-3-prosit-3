# Plan: Sustainability estimate and region choice (L11-D)

- **Issue:** #13
- **Owner:** Joseph (`josetseph`)
- **Milestone:** Lab 11
- **Status:** done in this PR

## Goal
Estimate the carbon footprint of our region choice, comparing AWS af-south-1 with GCP africa-south1 (Lab 11 Part D, 15%).

## What gets built
- `evidence/lab11/13-carbon-estimate.py` and its output: Cloud Carbon Footprint method over an assumed stack, five regions (AWS af-south-1, us-east-1; GCP africa-south1, europe-west1, europe-west9).
- `decisions/13-region-choice-carbon.md`: region choice with the cost-vs-carbon-vs-latency trade-off.
- One learnings note.

## Depends on
- nothing (re-run once #12 has real sizes)

## Done when
- Carbon/region estimate from a provider tool or documented manually
- Region choice justified, with one cost-vs-carbon trade-off

## Evidence to capture
- Script and output in `evidence/lab11/`.

## Not doing
- Provider tool figures: AWS's tool shows only past account usage, and the GCP project (#16) isn't set up. Re-run with them later.
- Embodied, storage and network emissions: CCF covers compute embodied only, and we have no usage data yet.
