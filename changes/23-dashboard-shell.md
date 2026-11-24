---
issue: 23
title: Scaffold the AMA dashboard
date: 2026-11-24
in_charge: Elise
reviewed_by: See PR approvals
---

## What changed

Added a React and TypeScript dashboard scaffold with Vite and local run instructions.

## Why

Give the Lab 12 dashboard a working starting point for its first sensor chart.

## How to check

```sh
cd web
npm ci
npm run build
npm run dev
```

Open the printed URL and look for the SmartCity Accra heading.

## AI use

- **Tool:** Codex
- **What it did:** Created the dashboard scaffold, run instructions, stack decision record, and change record.
- **Prompts / session summary:** Start #23 with a basic React scaffold and discuss the chart plan in the next chunk.
- **What the person checked or changed:**

## Decisions made

- [Dashboard web stack](../decisions/23-dashboard-web-stack.md)

## Not done

- Sensor chart, live updates and screenshot evidence.
