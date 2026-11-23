# Plan: SmartCity budget model at stated sensor volume (L11-C)

- **Issue:** #12
- **Owner:** Elise (`Elise-Oyi`)
- **Milestone:** Lab 11
- **Status:** in progress

## Goal
Estimate what SmartCity costs to run per month on AWS (Lab 11 Part C, 30%), and say whether that is affordable for the AMA and what we would cut at half the budget. Scope is a **pilot**: 500 sensors in Makola / Central Accra. A city-wide projection is added at the end with the same formulas.

## What gets built
- `evidence/lab11/12-budget-model.csv`: AWS Pricing Calculator export (the spreadsheet deliverable).
- `evidence/lab11/12-budget-model.md`: the itemised budget, every assumption with its source, the "not included" list, the affordability and half-budget analysis, and the city-wide projection.
- `decisions/12-makola-pilot-budget-assumptions.md`: the scope and sizing choices.

## Assumptions (the numbers everything rests on)

| Assumption | Value | Source / reasoning |
|---|---|---|
| Scope | Pilot, Makola / Central Accra along the Odaw drain | Public bins, flood-prone drain and heavy traffic in one place; inside the AMA |
| Sensors | 500: 350 waste (70%), 100 flood (20%), 50 air (10%) | Bins are numerous; drains only where they flood; one air sensor covers an area |
| Readings | 500/min = 21.6 M/month; 64.8 M held at 90-day retention | 1 reading/min per device (`contracts/mqtt-topics.md`); flood spikes to 1 per 10 s in storms |
| DB storage | 20 GB (≈ 9.7 GB needed × 2 headroom) | ≈ 150 bytes per stored reading incl. index |
| Region | `af-south-1` (Cape Town) | Closest AWS region to Ghana; as in Prosits 1–2. Must match #13 |
| Users | 10,000 MAU | 2% of AMA district population 284,124 (2021 PHC) ≈ 5,700, rounded up for Makola's daytime crowd |
| Egress | 125 GB/month | 10,000 MAU × 25 visits × 0.5 MB |

## Assumptions that need Eugene's and Joseph's confirmation
- **Database (#7, Eugene):** TimescaleDB self-hosted on one EC2 `t3.medium`, 20 GB gp3, daily snapshots. RDS does not offer the TimescaleDB extension.
- **API scaling (#4, Eugene):** `t3.small`, auto-scaling 1–4, budgeted at an expected 2.
- **Broker (#18 Joseph, #28 Eugene):** Mosquitto on its own EC2 `t3.micro`.
- **Not priced (Eugene, Joseph):** NAT Gateway, public IPv4 addresses, CloudWatch, web dashboard hosting. Listed as "not included"; the total is a lower bound.

## Depends on
- #7 decision (database). The budget states its database assumption so it does not wait.

## Done when
- Itemised monthly budget: broker, DB with 90-day retention, compute across the 1–4 scaling range, egress from a sourced MAU, and the load balancer.
- Affordability analysis, including what we'd cut at half the budget.
- Every figure traceable to the calculator export or a stated assumption.

## Evidence to capture
- `evidence/lab11/12-budget-model.csv` (calculator export, $137.39/month).
- Calculator share link: https://calculator.aws/#/estimate?id=8085039305d1ab7c61c09a7a8e6965c631a25519

## Not doing
- Pricing NAT Gateway, public IPs, CloudWatch and dashboard hosting: listed for review instead (see above).
- Taxes and AWS support plans.
- Sensor hardware, installation and mobile data for devices: outside the cloud bill.
