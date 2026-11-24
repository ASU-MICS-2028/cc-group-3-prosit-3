---
issue: 54
title: Decision on what we are not building, and why
date: 2026-11-24
pr: "(this PR)"
in_charge: Joseph Etse
reviewed_by: (whoever approves this PR)
---

## What changed

- `decisions/54-not-built.md`: the brief's items we don't build, each with its reason and what we have instead. Traffic, water-pipe and energy sensors; computer vision, NLP, chatbots, reinforcement learning, digital twin and federated learning.
- It also states the Lab 14 advanced-feature test: multi-cloud (#45), with the what-if replay as the fallback.
- README now links to it. Plan `plans/54-not-built-decision.md`.

## Why

So the presentation and architecture document (#47) explain the gaps instead of leaving them unexplained.

## How to check
Read `decisions/54-not-built.md`; every "what we have instead" names an issue or file that exists.

## AI use
- **Tool:** Claude Code
- **What it did:** drafted the decision, plan and this file from the issue, the README scope line and the knowledge notes on the brief and Lab 14.
- **Prompts / session summary:** "go ahead with #54".
- **What the person checked or changed:** Joseph skims every file produced.

## Decisions made
- [What we are not building, and why](../decisions/54-not-built.md) (proposed)

## Not done
- none
