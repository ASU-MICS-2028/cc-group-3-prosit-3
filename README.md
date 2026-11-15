# SmartCity Accra

**ICS 534 Cloud Computing, Prosit 3 · Group 3, Highlanders · Fall 2026**

An IoT, machine-learning and AI platform for the Accra Metropolitan Assembly (AMA). Sensors report on the city; the platform stores the readings, forecasts what comes next, warns people, and shows it all to AMA officials (web) and residents (mobile app).

We go deep on three sensor domains, each feeding one piece of ML or AI:

| Domain | Data | ML / AI it feeds |
|---|---|---|
| Air quality (PM2.5) | Simulator + real OpenAQ readings from Accra stations | 24–48 h forecast |
| Waste bin fill level | Simulator | Fill-rate prediction → collection routes |
| Flood / drain water level | Simulator | Anomaly detection and early warning |

Traffic, water-pipe and energy sensors, and computer vision, reinforcement learning, digital twins and federated learning are **not built**. The reasons will be recorded as a decision (issue #54).

## Team

| Person | GitHub | Area |
|---|---|---|
| Joseph Etse | `josetseph` | PM and process · sensor simulator · MQTT bridge · device credentials · API · final architecture document · personal GCP rebuild (`infra/gcp/`, not graded) |
| Eugene Sewor | `eugene-sew` | AWS: Terraform, auto-scaling, monitoring, load tests, cost, decommissioning |
| Elise Kennedy-Angbo | `Elise-Oyi` | Data: time-series DB, ML models · AMA web dashboard |
| Perfect Avugla | `PeaElorm` | UI/UX design system · citizen mobile app |

Community engagement (30% of the grade) is shared by all four; see issues labelled `area:community`.

## Start here

| What you want | Where |
|---|---|
| What to work on | [Open issues](https://github.com/ASU-MICS-2028/cc-group-3-prosit-3/issues) · [milestones (one per lab)](https://github.com/ASU-MICS-2028/cc-group-3-prosit-3/milestones) |
| How we work | [`CONTRIBUTING.md`](./CONTRIBUTING.md) |
| The plan for each issue | [`plans/`](./plans/README.md) |
| Every change, who did it, and what AI did | [`changes/`](./changes/README.md) |
| Every decision and why | [`decisions/`](./decisions/README.md) |
| What we were taught or given (lectures, labs, brief) | [`knowledge/`](./knowledge/README.md) |
| What we found out by doing it | [`learnings/`](./learnings/README.md) |
| The shared formats every part builds against | [`contracts/`](./contracts/README.md) |
| Design of this setup | [`docs/specs/`](./docs/specs/) |

The repo is public. Never commit secrets, real personal data, or course handouts.
