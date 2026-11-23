# SmartCity Accra budget model: Makola pilot (Lab 11 Part C)

**Scope: this is a pilot, not all of Accra.** 500 sensors in Makola / Central Accra, priced on AWS in `af-south-1` (Cape Town), On-Demand, as of 23 Nov 2026. A city-wide projection follows at the end.

- **Issue:** #12 · **Owner:** Elise (`Elise-Oyi`)
- **Spreadsheet:** [`12-budget-model.csv`](./12-budget-model.csv) (AWS Pricing Calculator export)
- **Calculator estimate:** https://calculator.aws/#/estimate?id=8085039305d1ab7c61c09a7a8e6965c631a25519

## Monthly budget

| Item | AWS service and size | USD/month | Share |
|---|---|---|---|
| Time-series database | EC2 `t3.medium`, 20 GB gp3, daily snapshots | 43.03 | 31% |
| API servers | EC2 `t3.small` × 2 (auto-scaling 1–4, expected 2) | 41.25 | 30% |
| Load balancer | 1 Application Load Balancer | 23.09 | 17% |
| Egress to users | 125 GB/month out to the internet | 19.25 | 14% |
| MQTT broker | EC2 `t3.micro` running Mosquitto, 8 GB gp3 | 10.77 | 8% |
| **Total** | | **137.39** | |

**USD 1,648.68 per year.** At USD 1 = GH₵11.8 (23 Nov 2026): **GH₵1,621 per month, GH₵19,454 per year.**

Range for the API line: USD 20.63 (1 server) to USD 82.50 (4 servers), so the total runs from about USD 117 to USD 179 a month.

## Assumptions

| Assumption | Value | Source or reasoning |
|---|---|---|
| Pilot area | Makola / Central Accra along the Odaw drain | Public bins (markets, lorry stations), a drain that floods, heavy traffic; inside the AMA; already a neighbourhood in `contracts/mqtt-topics.md` |
| Sensors | 500: 350 waste bins (70%), 100 drains (20%), 50 air quality (10%) | Bins are numerous and cheap; only flood-prone drains need sensors; one air sensor covers an area. Household bins in townships are private, so a pilot needs an area with public bins |
| Reading rate | 500 per minute; 21.6 M per month | 1 reading per device per minute (`contracts/mqtt-topics.md`); flood sensors rise to 1 per 10 s in storms |
| Retention | 90 days raw (64.8 M readings), hourly rollups kept | `contracts/storage.md` |
| Storage | 20 GB | ≈ 150 bytes per stored reading including the `(device_id, ts)` index → 9.7 GB, doubled for storms, rollups, alerts and predictions |
| Backups | Daily snapshots, ≈ 0.2 GB changed per day | ≈ 0.11 GB new readings + about the same deleted by retention |
| Database | TimescaleDB self-hosted on EC2 | Needs SQL tables for alerts, predictions and citizen reports too; RDS does not offer the TimescaleDB extension. **Pending #7** |
| Users | 10,000 monthly active users (MAU) | AMA district population 284,124 (2021 Population and Housing Census, via [citypopulation.de](https://citypopulation.de/en/ghana/admin/greater_accra/0304__accra_metropolitan/)) × 2% early adopters ≈ 5,700, rounded up for Makola's daytime crowd of traders, shoppers and commuters |
| Egress | 125 GB/month | 10,000 MAU × 25 visits × 0.5 MB per visit |
| Load balancer traffic | 125 GB/month, about 1 request per second | 250,000 visits a month is about 0.1 per second, rounded up |

## Not included (so the total is a lower bound)

| Item | Why it matters | To confirm with |
|---|---|---|
| NAT Gateway | Lets servers in private subnets reach the internet; Prosits 1 and 2 used one. Likely the largest missing item | Eugene |
| Public IPv4 addresses | Charged per address | Eugene |
| CloudWatch monitoring and alarms | Lab 10 dashboards and alerts | Eugene |
| Web dashboard hosting | Serving the AMA dashboard files | Joseph, Eugene |
| AWS's 100 GB/month free outbound data | Not applied by the calculator; would cut egress to about USD 3.85 | n/a: a saving, not a cost |
| Taxes, support plan, sensor hardware and installation | Outside the cloud bill | n/a |

## Is it realistic for the AMA?

Yes. At GH₵1,621 a month the pilot costs less than half of a decent monthly salary in Accra, or roughly the fuel for one refuse-truck round trip (approximate local estimates). It pays for itself if it avoids about one wasted truck trip a month. Per unit it is about USD 0.27 per sensor and 1.4 US cents per user each month.

What the AMA gets back:

- **Waste:** trucks go only to bins that are full, saving fuel and vehicle maintenance.
- **Flood:** Accra floods every year; people are stranded and property and lives are lost. Early warning lets officials act before and during the event.
- **Air quality:** cleaner air means fewer airborne-disease outbreaks and better public health.

**Adoption is a major risk.** About 86% of the pilot estimate is in the database, API, broker and load balancer lines. Those costs are mostly tied to keeping capacity online, so low usage raises the cost per user. The system needs policies and processes that make officials and residents act on it. If a donor funds the pilot, the AMA also needs a plan for when the grant ends.

## What we would cut at half the budget

Half is about USD 69 a month. We would cut:

| Cut | Saves (USD/month) | What we give up |
|---|---|---|
| API servers from 2 to 1 | 20.63 | Slower at busy times |
| Remove the load balancer | 23.09 | No failover. Fine for low pilot traffic, but if the one server fails the app and dashboard are down for a few minutes until it is replaced |
| **New total** | **≈ 93.67** | about 68% of the original |

We would **not** cut:

- **Broker onto the database server** (saves USD 10.77): we already give up redundancy in the API tier. Sharing one server would add another single point of failure: if the database server goes down, sensors cannot send either and readings are lost.
- **1-year Savings Plan** (largest saving with no loss of features): it is a pilot the AMA may stop or change, and a commitment is paid even if the pilot ends. We would switch once the pilot is proven.
- **Daily backups** (saves USD 1.37): too small a saving for the risk of losing the data the ML models train on.
- **Fewer sensors:** storage is cheap, so fewer sensors save little while making the system less useful.

**Conclusion:** halving the budget is not possible without giving up reliability. About USD 94 a month is the floor for a pilot we would still stand behind. In practice we would present these options to the AMA with our recommendation; the cut is their decision.

## City-wide projection

**Approximate projection scaled from the pilot. Only the pilot was priced in the AWS Pricing Calculator.** The city-wide scenario assumes 5,000 sensors and 110,000 monthly active users across Greater Accra. Both are planning inputs. At the pilot's reading rate and retention, this gives 216 million readings per 30-day month and 648 million retained readings. The pilot's storage sizing rule gives about 200 GB with headroom. The same 25 visits per user and 0.5 MB per visit give 1,375 GB of monthly outbound traffic.

| Item | Scaling assumption | USD/month |
|---|---|---:|
| Database | Allow four times the pilot line for compute, storage and snapshots | 172.12 |
| API servers | Budget for four pilot-sized instances on average, twice the pilot average | 82.50 |
| Load balancer | Keep one ALB and allow twice the pilot line for more traffic | 46.18 |
| Egress | 1,375 GB at the pilot's effective rate of USD 0.154 per GB | 211.75 |
| MQTT broker | Allow four times the pilot line for more device traffic | 43.08 |
| **Total** | | **555.63** |

The model projects **10× the sensors and 11× the users for about 4× the monthly cloud cost**. Egress becomes the largest line, and the cost per monthly active user falls from about **1.4 US cents to 0.5 US cents**. This scenario shows economies of scale because the modeled cost of keeping capacity online grows more slowly than the user count.

The city-wide scenario keeps the load balancer and API auto-scaling to handle peaks and retain API failover. The four-instance average and the database, broker and load balancer allowances need validation with workload tests and fresh pricing. If data per visit doubles, egress alone rises to about USD 424 per month and the total reaches about USD 767 under the same effective rate and other assumptions. The pilot exclusions also apply here.
