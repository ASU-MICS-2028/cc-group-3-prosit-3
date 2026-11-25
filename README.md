<h1 align="center">SmartCity Accra</h1>

<p align="center">
  <b>ICS 534 Cloud Computing · Prosit 3 · Group 3, Highlanders · Ashesi University · Fall 2026</b><br>
  An IoT and machine-learning platform for the Accra Metropolitan Assembly (AMA): sensors report on the city,<br>
  the platform stores the readings, forecasts what comes next, warns people, and shows it to AMA officials and residents.
</p>

<p align="center">
  <img alt="Closed issues" src="https://img.shields.io/github/issues-closed/ASU-MICS-2028/cc-group-3-prosit-3?style=flat-square&color=2e7d32">
  <img alt="Open issues" src="https://img.shields.io/github/issues/ASU-MICS-2028/cc-group-3-prosit-3?style=flat-square&color=d4a72c">
  <a href="https://github.com/ASU-MICS-2028/cc-group-3-prosit-3/pulls"><img alt="Open pull requests" src="https://img.shields.io/github/issues-pr/ASU-MICS-2028/cc-group-3-prosit-3?style=flat-square&color=1f4e79"></a>
  <img alt="Clouds" src="https://img.shields.io/badge/cloud-AWS_af--south--1_·_GCP_africa--south1-1f4e79?style=flat-square">
  <img alt="Final deadline" src="https://img.shields.io/badge/final-11_Dec_2026-b03a2e?style=flat-square">
</p>

<p align="center">
  <a href="#team">Team</a> ·
  <a href="#progress-by-lab">Progress</a> ·
  <a href="#whats-left-by-person">What's left</a> ·
  <a href="#what-we-build">What we build</a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="#repository-map">Repository map</a> ·
  <a href="#how-we-work">How we work</a>
</p>

---

## Team

<table>
  <tr>
    <td align="center" width="25%">
      <a href="https://github.com/josetseph"><img src="https://github.com/josetseph.png?size=160" width="96" alt="Joseph"><br><b>Joseph Etse</b></a><br>
      <sub><code>josetseph</code></sub><br>
      <sub>PM &amp; process · sensors, ingest &amp; API</sub>
    </td>
    <td align="center" width="25%">
      <a href="https://github.com/eugene-sew"><img src="https://github.com/eugene-sew.png?size=160" width="96" alt="Eugene"><br><b>Eugene Sewor</b></a><br>
      <sub><code>eugene-sew</code></sub><br>
      <sub>AWS infrastructure (graded build)</sub>
    </td>
    <td align="center" width="25%">
      <a href="https://github.com/Elise-Oyi"><img src="https://github.com/Elise-Oyi.png?size=160" width="96" alt="Elise"><br><b>Elise Kennedy-Angbo</b></a><br>
      <sub><code>Elise-Oyi</code></sub><br>
      <sub>Data, ML &amp; AMA web dashboard</sub>
    </td>
    <td align="center" width="25%">
      <a href="https://github.com/PeaElorm"><img src="https://github.com/PeaElorm.png?size=160" width="96" alt="Perfect"><br><b>Perfect Elorm Avugla</b></a><br>
      <sub><code>PeaElorm</code></sub><br>
      <sub>UI/UX &amp; citizen mobile app</sub>
    </td>
  </tr>
  <tr>
    <td valign="top"><sub>Sensor simulator, OpenAQ feeder, MQTT bridge with buffering, per-device credentials, API and prediction endpoint, flood early-warning alerts, final architecture document, AWS-vs-GCP test, personal GCP rebuild (not graded).<br><a href="sensors/"><code>sensors/</code></a> <a href="ingest/"><code>ingest/</code></a> <a href="api/"><code>api/</code></a> <a href="infra/gcp/"><code>infra/gcp/</code></a></sub></td>
    <td valign="top"><sub>Terraform, auto-scaling, monitoring and alerts, load tests, cost audit, deploying every part to AWS, decommissioning, stakeholder session. The only one who applies live AWS changes.<br><a href="infra/aws/"><code>infra/aws/</code></a> <a href="loadtest/"><code>loadtest/</code></a></sub></td>
    <td valign="top"><sub>Budget model, time-series storage and rollups, PM2.5 forecast with MLflow, waste fill-rate and collection routes, drift log, AMA dashboard, open-data portal, SDG 11 view, capstone integration design.<br><a href="db/"><code>db/</code></a> <a href="ml/"><code>ml/</code></a> <a href="web/"><code>web/</code></a></sub></td>
    <td valign="top"><sub>Design system and screens for web and mobile, citizen app with live readings and issue reporting, inclusion for low-end phones, final presentation and demo video.<br><a href="design/"><code>design/</code></a> <a href="mobile/"><code>mobile/</code></a></sub></td>
  </tr>
</table>

Community engagement (30% of the grade) is shared by all four through the [`area:community` issues](https://github.com/ASU-MICS-2028/cc-group-3-prosit-3/issues?q=is%3Aissue+label%3Aarea%3Acommunity). Any one approval from someone other than the author merges a pull request.

---

## Progress by lab

Live from GitHub: each badge counts the milestone's closed issues out of its total.

| Lab | Due | Progress | Covers |
| --- | --- | --- | --- |
| [Lab 10](https://github.com/ASU-MICS-2028/cc-group-3-prosit-3/milestone/1) | Mon 16 Nov | ![Lab 10](https://img.shields.io/github/milestones/progress/ASU-MICS-2028/cc-group-3-prosit-3/1?style=flat-square&label=closed) | Auto-scaling, golden-signal dashboard, load test, broker and time-series DB choice |
| [Lab 11](https://github.com/ASU-MICS-2028/cc-group-3-prosit-3/milestone/2) | Mon 23 Nov | ![Lab 11](https://img.shields.io/github/milestones/progress/ASU-MICS-2028/cc-group-3-prosit-3/2?style=flat-square&label=closed) | Cost audit, two optimisations, budget model, carbon estimate |
| [Lab 12](https://github.com/ASU-MICS-2028/cc-group-3-prosit-3/milestone/3) | Mon 30 Nov | ![Lab 12](https://img.shields.io/github/milestones/progress/ASU-MICS-2028/cc-group-3-prosit-3/3?style=flat-square&label=closed) | MQTT broker, simulator, bridge with buffering, live chart, device credentials |
| [Lab 13](https://github.com/ASU-MICS-2028/cc-group-3-prosit-3/milestone/4) | Mon 7 Dec | ![Lab 13](https://img.shields.io/github/milestones/progress/ASU-MICS-2028/cc-group-3-prosit-3/4?style=flat-square&label=closed) | Models, MLflow, prediction endpoint, drift, citizen issue reporting |
| [Lab 14 / final](https://github.com/ASU-MICS-2028/cc-group-3-prosit-3/milestone/5) | Fri 11 Dec | ![Lab 14](https://img.shields.io/github/milestones/progress/ASU-MICS-2028/cc-group-3-prosit-3/5?style=flat-square&label=closed) | AWS-vs-GCP test, capstone integration design, architecture document, decommissioning, final presentation |

Written reports: [`type:report` issues](https://github.com/ASU-MICS-2028/cc-group-3-prosit-3/issues?q=is%3Aissue+label%3Atype%3Areport). Each lab is due before the next Monday lecture.

---

## What's left, by person

| | Person | Open issues | Jump to |
| :---: | --- | :---: | --- |
| <img src="https://github.com/josetseph.png?size=60" width="28"> | **Joseph** · PM, sensors, ingest, API | ![open](https://img.shields.io/github/issues-search/ASU-MICS-2028/cc-group-3-prosit-3?query=is%3Aissue%20is%3Aopen%20assignee%3Ajosetseph&label=open&style=flat-square&color=d4a72c) | [Joseph's issues](https://github.com/ASU-MICS-2028/cc-group-3-prosit-3/issues?q=is%3Aissue+is%3Aopen+assignee%3Ajosetseph) |
| <img src="https://github.com/eugene-sew.png?size=60" width="28"> | **Eugene** · AWS | ![open](https://img.shields.io/github/issues-search/ASU-MICS-2028/cc-group-3-prosit-3?query=is%3Aissue%20is%3Aopen%20assignee%3Aeugene-sew&label=open&style=flat-square&color=d4a72c) | [Eugene's issues](https://github.com/ASU-MICS-2028/cc-group-3-prosit-3/issues?q=is%3Aissue+is%3Aopen+assignee%3Aeugene-sew) |
| <img src="https://github.com/Elise-Oyi.png?size=60" width="28"> | **Elise** · data, ML, web | ![open](https://img.shields.io/github/issues-search/ASU-MICS-2028/cc-group-3-prosit-3?query=is%3Aissue%20is%3Aopen%20assignee%3AElise-Oyi&label=open&style=flat-square&color=d4a72c) | [Elise's issues](https://github.com/ASU-MICS-2028/cc-group-3-prosit-3/issues?q=is%3Aissue+is%3Aopen+assignee%3AElise-Oyi) |
| <img src="https://github.com/PeaElorm.png?size=60" width="28"> | **Perfect** · UI/UX, mobile | ![open](https://img.shields.io/github/issues-search/ASU-MICS-2028/cc-group-3-prosit-3?query=is%3Aissue%20is%3Aopen%20assignee%3APeaElorm&label=open&style=flat-square&color=d4a72c) | [Perfect's issues](https://github.com/ASU-MICS-2028/cc-group-3-prosit-3/issues?q=is%3Aissue+is%3Aopen+assignee%3APeaElorm) |
| 👥 | **Everyone** · community engagement | ![open](https://img.shields.io/github/issues-search/ASU-MICS-2028/cc-group-3-prosit-3?query=is%3Aissue%20is%3Aopen%20label%3Aarea%3Acommunity&label=open&style=flat-square&color=d4a72c) | [Shared issues](https://github.com/ASU-MICS-2028/cc-group-3-prosit-3/issues?q=is%3Aissue+is%3Aopen+label%3Aarea%3Acommunity) |

Signed in? [Your own open issues](https://github.com/ASU-MICS-2028/cc-group-3-prosit-3/issues?q=is%3Aopen+assignee%3A%40me) · [pull requests waiting for a review](https://github.com/ASU-MICS-2028/cc-group-3-prosit-3/pulls?q=is%3Apr+is%3Aopen+review%3Arequired).

---

## What we build

We go deep on three sensor domains, each feeding one piece of ML:

| Domain | Data | ML it feeds |
| --- | --- | --- |
| Air quality (PM2.5) | Simulator + real OpenAQ readings from Accra stations | 24–48 h forecast |
| Waste bin fill level | Simulator | Fill-rate prediction → collection routes |
| Flood / drain water level | Simulator | Anomaly detection and early warning |

```text
sensors (simulated + OpenAQ) ──MQTT──▶ broker ──▶ bridge (buffers through outages) ──▶ time-series DB
                                                                                          │
                     AMA web dashboard ◀── API (readings, alerts, predictions) ◀── ML models
                     citizen mobile app ◀──┘
```

Traffic, water-pipe and energy sensors, and computer vision, reinforcement learning, digital twins and federated learning are **not built**. Why, item by item, and what we have instead: [`decisions/54-not-built.md`](./decisions/54-not-built.md).

The sensors measure places, not people. Who owns the data, what we never collect, and how a neighbourhood can switch its sensors off: [`docs/privacy.md`](./docs/privacy.md).

---

## Quick start

Needs Python 3.12+ and Docker. Each folder's README has the details.

```bash
git switch main && git pull
pip install -r contracts/requirements.txt -r sensors/requirements.txt
docker compose -f ingest/compose.yaml up -d                     # MQTT broker on localhost:1883
python3 sensors/simulator.py --speed 60                         # 11 simulated devices, an hour per minute
docker compose -f ingest/compose.yaml exec mosquitto mosquitto_sub -t 'accra/#' -v   # watch the readings
python3 -m unittest discover contracts/tests && python3 -m unittest discover sensors/tests   # tests
```

---

## Repository map

| Folder | What's in it | Owner |
| --- | --- | --- |
| [`contracts/`](./contracts/README.md) | Shared formats every part builds against: sensor reading, MQTT topics, API, storage | everyone |
| [`sensors/`](./sensors/README.md) · [`ingest/`](./ingest/README.md) · [`api/`](./api/README.md) | Simulator and OpenAQ feeder · broker, bridge, credentials · REST API | Joseph |
| [`infra/aws/`](./infra/aws/README.md) · [`loadtest/`](./loadtest/README.md) | Terraform for the graded AWS build · load tests | Eugene |
| [`infra/gcp/`](./infra/gcp/README.md) | Personal GCP rebuild (not graded) | Joseph |
| [`db/`](./db/README.md) · [`ml/`](./ml/README.md) · [`web/`](./web/README.md) | Time-series DB · models and MLflow · AMA dashboard | Elise |
| [`design/`](./design/README.md) · [`mobile/`](./mobile/README.md) | Design system · citizen app | Perfect |
| [`plans/`](./plans/README.md) | One plan per issue | issue owner |
| [`changes/`](./changes/README.md) | One change file per PR: what changed, who was in charge, what AI did | PR author |
| [`decisions/`](./decisions/README.md) | One file per decision, with the options and why | whoever decided |
| [`knowledge/`](./knowledge/README.md) · [`learnings/`](./learnings/README.md) | One-idea notes: what we were taught · what we found out by doing | everyone |
| [`evidence/`](./evidence/README.md) | Lab evidence: screenshots, terminal output and the scripts that made them | whoever ran it |
| [`docs/`](./docs/README.md) | Design of this setup, architecture document | Joseph |

---

## How we work

1. **Open pull requests first.** Before starting anything, review and merge what's waiting; unreviewed work blocks teammates.
2. **One issue, one plan, one branch, one pull request.** Fill `plans/<issue>-<slug>.md`, branch `<area>/<issue>-<slug>`, and say `Closes #<issue>` in the PR.
3. **Every PR adds one change file** saying who was in charge and what AI did. AI is allowed and declared there.
4. **Build against `contracts/`** with fake data; nobody waits for anybody. Changing a contract is its own PR with a decision file.
5. **One approval from anyone but the author** merges. Required checks: notes, change-file, links, unit, contracts. Never `--admin`.
6. **Only Eugene applies live AWS changes.** Owners package their part (container + README); Eugene writes the Terraform.

Full rules: [`CONTRIBUTING.md`](./CONTRIBUTING.md). Coding assistants also follow [`AGENTS.md`](./AGENTS.md).

The repo is public. Never commit secrets, real personal data, or course handouts.
