---
title: k6 stages ramp virtual users up and down so you can watch scaling react
tags: [lab, scaling, monitoring]
source: Lab 10 (week10_lab_Students) Part C
---

The lab script uses k6 'stages': 30s ramp to 20 users, 1m ramp to 100, 30s ramp down to 0, each virtual user doing an HTTP GET on /health with a check for status 200 and a 1s sleep. Run with k6 run loadtest.js. JMeter or Locust are accepted alternatives.

While it runs, watch the dashboard and, in a second terminal, poll the ASG instance list every 5 seconds to see scale-out. Deliverable C is the k6 summary plus a dashboard screenshot showing the spike and scaling event.

Troubleshooting: if k6 reports connection errors rather than application errors, check the load balancer and security group allow that many concurrent connections. A free-tier database becoming the bottleneck immediately is a valid finding to report.

## Related
- [Rerun k6 at a much higher ramp (e.g. 500 users) to find what breaks first](stress-test-find-breaking-point.md)
- [A target-tracking policy keeps average CPU near a set value (Lab 10 uses 70%, min 1, max 4)](target-tracking-cpu-auto-scaling-policy.md)
- [Lab 10 overview - auto-scaling, golden-signal dashboard, k6 load test, ingestion-stack choice](lab-10-auto-scaling-monitoring-load-testing.md)
