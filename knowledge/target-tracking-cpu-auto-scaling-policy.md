---
title: A target-tracking policy keeps average CPU near a set value (Lab 10 uses 70%, min 1, max 4)
tags: [lab, scaling, aws]
source: Lab 10 (week10_lab_Students) Part A
---

Target tracking means you name a metric and a target value, and the platform adds or removes instances to hold the metric near it. Lab 10 uses an Auto Scaling Group with min 1, max 4, desired 1, attached to the load balancer target group, and the predefined metric ASGAverageCPUUtilization at 70.0.

Azure equivalent: a VM Scale Set with an autoscale rule on CPU. GCP equivalent: a Managed Instance Group with an autoscaler on CPU utilization.

Why it matters for SmartCity: sensor traffic is bursty, so a fixed fleet either wastes budget or falls over. The deliverable is a screenshot of the policy (min/max/target), then proof it fires under load.

Example from the lab: the instance count going 1 -> 3 while k6 ramps to 100 virtual users.

## Related
- [Lab 10 overview - auto-scaling, golden-signal dashboard, k6 load test, ingestion-stack choice](lab-10-auto-scaling-monitoring-load-testing.md)
- [k6 stages ramp virtual users up and down so you can watch scaling react](k6-ramping-load-test.md)
- [If CPU stays low under load, scale on requests per target instead](scaling-not-triggering-io-bound-use-request-count.md)
