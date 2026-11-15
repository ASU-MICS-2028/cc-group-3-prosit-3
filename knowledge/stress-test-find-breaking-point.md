---
title: Rerun k6 at a much higher ramp (e.g. 500 users) to find what breaks first
tags: [lab, scaling, reliability]
source: Lab 10 (week10_lab_Students) homework extension
---

Optional Lab 10 extension: repeat the k6 script with a far more aggressive target (500 instead of 100) to find the real breaking point, not just expected-load behaviour. Document what broke first: the app tier, the database, or the load balancer. Useful as honest evidence of where SmartCity's 100,000+ device target is out of reach.

## Related
- [k6 stages ramp virtual users up and down so you can watch scaling react](k6-ramping-load-test.md)
- [Lab 10 overview - auto-scaling, golden-signal dashboard, k6 load test, ingestion-stack choice](lab-10-auto-scaling-monitoring-load-testing.md)
