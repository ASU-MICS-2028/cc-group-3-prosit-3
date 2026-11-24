---
issue: 54
title: What we are not building, and why
date: 2026-11-24
decided_by: Joseph (proposed; open for team comment)
status: proposed
---

## Context

The brief describes far more than four people can build well in the time left (final submission before 12 Dec). It lists six sensor domains and a long run of AI features. We chose depth over breadth: three sensor domains, each feeding one piece of ML or AI, built end to end (sensor → broker → database → API → dashboard and app). This file records what that leaves out, so the presentation and the architecture document (#47) can say so plainly instead of leaving gaps unexplained.

## Options

1. **Build a thin version of everything in the brief.** It covers every heading, but each piece would be a mock with nothing real behind it, and none would be finished well enough to demonstrate.
2. **Go deep on three domains and name the rest as not built (chosen).** There is less on the slide, but everything shown works, has evidence, and can be questioned.

## Decision

We build **air quality (PM2.5), waste bin fill level and flood/drain level**. The rest of the brief is not built, for these reasons:

| Not built | Why | What we have instead |
|---|---|---|
| **Traffic sensors** (and traffic-light AI) | We have no open source of Accra traffic data to check a simulator against, and traffic control is safety-critical, so it shouldn't be prototyped on made-up data. It is also the domain RL and multi-agent work would need. | Air quality already reflects traffic: the simulator's morning and evening peaks are traffic-driven. |
| **Water-pipe sensors** | Pipe pressure and leak data belongs to the water utility and isn't public. A fourth simulated domain would add breadth with nothing real to compare it to. | The flood domain covers the water problem residents feel most directly. |
| **Energy sensors** | Same reason: metering data belongs to the utility. Energy forecasting would repeat the PM2.5 forecast's method on a different series. | The PM2.5 forecast shows the forecasting pipeline once, done properly. |
| **Computer vision** | It needs cameras in public places, labelled images and GPU compute. Filming residents also raises privacy and consent questions we can't answer responsibly in a pilot (#40). | Bin fill and drain level come from simple sensors that record no people. |
| **NLP** | The only text we collect is citizen reports, too few to train or test on. | Reports are short and categorised (`CitizenReport.category`), so officials can sort them without NLP. |
| **Chatbots** | A chatbot that answers wrongly during a flood is worse than none. Our alerts are rule-based, so their wording can't drift. | Every alert carries a fixed plain-words `reason` with the numbers (#25), and residents can question it (#41). |
| **Reinforcement learning** | RL needs a faithful simulator of the thing it controls, plus many training runs. It also fits traffic lights, which we don't build. | Waste routes come from predicted fill levels with a simple routing rule (#33), which can be explained. |
| **Digital twin** (full) | A live model of the city's physical systems is a project in its own right. | A small what-if replay of recorded readings against a different alert line is possible with our data (see below). |
| **Federated learning** | Its reason to exist is keeping private data on devices, and our sensor data is public and held centrally anyway. The lab's two-party demo is expected to lose to a local model. | One model trained centrally on all readings (#30). |

**Lab 14 advanced-feature test (Part A):** none of the above. It is the **multi-cloud fallback**: the same pipeline on AWS and on Joseph's GCP rebuild (#45), because we already have both. If the GCP rebuild (#16) isn't ready in time, the fallback is the **what-if replay**: re-run recorded flood readings against a lower warning line and count the extra alerts. It needs only data and code we already have (`api/alerts.py`'s `decide()`).

## Consequences

- The presentation and the architecture document name these as out of scope, with these reasons, so nobody has to improvise an answer when asked.
- If the AMA wanted one of them later, traffic is the natural next domain: it would feed the brief's traffic-light AI. It needs a real data source first.
- If a teammate wants to change the Lab 14 choice, edit this file in a PR and mark it accepted or replaced. Don't just change #45.
