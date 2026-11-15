---
title: One dashboard must show latency, traffic, errors and saturation
tags: [lab, monitoring]
source: Lab 10 (week10_lab_Students) Part B
---

Lab 10 requires a single dashboard (CloudWatch, Azure Monitor Workbook, GCP Cloud Monitoring, or self-hosted Grafana) covering:
- Latency: average and p95 response time
- Traffic: requests per second
- Errors: 4xx/5xx rate
- Saturation: CPU and/or memory, plus database connection count if available

Plus one alert tied to a specific threshold that would notify a real on-call person (email, SMS or webhook; a free-tier channel is fine), for example error rate above 5% for 5 minutes.

The lab's reflection asks which signal was hardest to get real data for, and whether the alert would tell a 2am engineer enough to act. For SmartCity this is the evidence that we can see the platform's health.

## Related
- [Log one JSON line per request so the dashboard has real error-rate and latency data](structured-request-logging-middleware.md)
- [Lab 10 overview - auto-scaling, golden-signal dashboard, k6 load test, ingestion-stack choice](lab-10-auto-scaling-monitoring-load-testing.md)
- [Write one SLO for the ingestion tier and compute its monthly error budget](slo-and-error-budget-exercise.md)
