---
title: A scheduled function in another region pings /health so outages are noticed even if dashboards are down
tags: [lab, monitoring, serverless]
source: Lab 10 (week10_lab_Students) homework extension
---

Optional Lab 10 extension: a scheduled serverless function calls the service's /health endpoint every minute from a different region than the service. Because it is external, it reports an outage even when internal dashboards are down too. Verify it by temporarily stopping the service and confirming the canary reports failure.

## Related
- [One dashboard must show latency, traffic, errors and saturation](four-golden-signals-dashboard.md)
- [Lab 10 overview - auto-scaling, golden-signal dashboard, k6 load test, ingestion-stack choice](lab-10-auto-scaling-monitoring-load-testing.md)
