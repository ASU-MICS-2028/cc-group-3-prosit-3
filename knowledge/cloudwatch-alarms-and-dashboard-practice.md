---
title: What a useful CloudWatch dashboard and alarm set looked like in Prosit 1
tags: [monitoring, aws, lecture]
source: Lecture 7
---

A Prosit 1 group showed a CloudWatch dashboard covering each tier:
- Load balancer: request volume, latency, status codes, and target health (which instances in the group are failing).
- Database: CPU, freeable memory, live connections, disk read/write latency.
- Instances: CPU, memory, disk; API container logs exported to CloudWatch Logs.

Alarms emailed the whole team when a threshold was crossed (for example database CPU) and when a load-balancer target went unhealthy. Another group used logs for audit (who did what, detecting bot abuse, checking that field officers were actually on site), but peers noted they never explained how metrics were used.

Lesson: for each metric, state the decision it supports (scale, alert, investigate).

For SmartCity Accra: add device-side signals such as message rate, broker connections and sensor silence alarms.

## Related
- [AgroConnect scales on ALBRequestCountPerTarget (500 per minute), not CPU](agroconnect-target-tracking-request-count-decision.md)
- [Questions the instructor and peers asked at the Prosit 1 presentations](prosit-1-presentation-qa-themes.md)
