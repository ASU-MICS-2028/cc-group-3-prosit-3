---
title: Lab 10 overview - auto-scaling, golden-signal dashboard, k6 load test, ingestion-stack choice
tags: [lab, scaling, monitoring]
source: Lab 10 (week10_lab_Students)
---

Week 10 lab (3 hours plus a 90-minute homework extension) that launches SmartCity Accra. It is a new, separate codebase; the VPC, CI/CD and monitoring patterns from Prosits 1-2 are templates to adapt, not code to import.

Objectives: configure a target-tracking auto-scaling policy, build a dashboard for all four golden signals, wire one actionable alert, run a ramping k6 load test, prove a scale-out event happened, and pick a broker plus time-series DB pairing.

Parts and team deliverables:
- Part A (45 min): auto-scaling group, min 1 / max 4, CPU target tracking at 70%. Deliverable A: screenshot of min/max/target.
- Part B (60 min): dashboard (latency avg and p95, traffic RPS, 4xx/5xx errors, saturation) plus one alert, e.g. error rate over 5% for 5 minutes. Deliverable B: dashboard and alert screenshots.
- Part C (45 min): k6 run, watch the dashboard live, confirm scale-out. Deliverable C: k6 summary plus dashboard screenshot.
- Part D (30 min): one-page decision document (broker, time-series DB). Deliverable D.

Lab report (300 words, due before the Week 11 Monday lecture, so Mon of 17-21 Nov): what the load test revealed, the ingestion-stack choice and why, one golden signal still poorly covered. Submit via Canvas: PDF, screenshots, k6 output, decision doc.

Rubric: auto-scaling configured and shown triggering 25%; dashboard with all four signals and a working alert 30%; load test run and interpreted correctly 25%; ingestion-stack decision specific and justified 20%. Reflection questions are unscored and count toward the 5% participation mark. The homework extension is optional (canary, stress test, SLO, reading).

## Related
- [A target-tracking policy keeps average CPU near a set value (Lab 10 uses 70%, min 1, max 4)](target-tracking-cpu-auto-scaling-policy.md)
- [One dashboard must show latency, traffic, errors and saturation](four-golden-signals-dashboard.md)
- [k6 stages ramp virtual users up and down so you can watch scaling react](k6-ramping-load-test.md)
- [Lab 10 Part D: a one-page choice of message broker and time-series database](ingestion-stack-decision-document.md)
