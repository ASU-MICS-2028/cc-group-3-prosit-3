---
issue: 13
title: Sustainability estimate and region choice (Lab 11 Part D)
date: 2026-11-15
pr: "(this PR)"
in_charge: Joseph Etse
reviewed_by: (whoever approves this PR)
---

## What changed

- `evidence/lab11/13-carbon-estimate.py` + output: monthly operational CO2e for an assumed SmartCity stack in five regions, by the Cloud Carbon Footprint method. af-south-1 is 14.5 kg, us-east-1 7.0, africa-south1 13.4, europe-west1 2.6 and europe-west9 0.3 kg CO2e a month.
- `decisions/13-region-choice-carbon.md` (proposed): stay in South Africa on both clouds. Trade-off: af-south-1 costs 29% more per t4g.small hour and emits about 2× us-east-1, for half the latency and data kept in Africa. Carbon is cut by running less (night scale-down, scheduled training, teardown).
- `learnings/af-south-1-costs-more-and-emits-twice-us-east-1.md`.

## Why

Lab 11 Part D (15%); feeds the Lab 11 report (#14) and the cost plan (#15).

## How to check
```bash
python3 evidence/lab11/13-carbon-estimate.py    # prints the table; asserts the region ordering
```
Sources to spot-check: CCF methodology (PUE, watts per vCPU, AWS grid factors), Google `region-carbon-info` `data/yearly/2025.csv`, and the AWS Price List API for t4g.small (af-south-1 $0.0217/h, us-east-1 $0.0168/h).

## AI use
- **Tool:** Claude Code
- **What it did:** looked up the coefficients (CCF methodology page, Google's 2025 region CSV, the AWS Price List API), wrote the estimate script, the decision, the learnings note and this file.
- **Prompts / session summary:** "you can start work on each one" (#13 was third in the queue). The stack sizing is an assumption Claude made, not from #12. AWS grid factors for European regions were left out because they could only be read from a summary, not verified on the page.
- **What the person checked or changed:** Joseph skims every file produced.

## Decisions made
- [Stay in af-south-1 (and africa-south1) despite the dirtier grid](../decisions/13-region-choice-carbon.md) (proposed)

## Not done
- Re-run with #12's real sizes, and with the AWS Customer Carbon Footprint Tool after a month of usage.
- GCP prices aren't in the table (the GCP project is #16).
