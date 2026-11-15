---
title: Log one JSON line per request so the dashboard has real error-rate and latency data
tags: [lab, monitoring]
source: Lab 10 (week10_lab_Students) Part B
---

The lab's starter is a small Express middleware: on the response 'finish' event it prints one JSON line with timestamp, method, path, status code and duration in milliseconds, then is registered with app.use. Those fields feed the error-rate and latency widgets.

Gotcha from the lab: structured logs may not reach the dashboard unless the container's logging driver actually ships stdout to CloudWatch Logs / Log Analytics / Cloud Logging; console.log alone is not enough on some container setups.

## Related
- [One dashboard must show latency, traffic, errors and saturation](four-golden-signals-dashboard.md)
- [Lab 10 overview - auto-scaling, golden-signal dashboard, k6 load test, ingestion-stack choice](lab-10-auto-scaling-monitoring-load-testing.md)
