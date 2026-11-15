---
title: If CPU stays low under load, scale on requests per target instead
tags: [lab, scaling]
source: Lab 10 (week10_lab_Students) Troubleshooting
---

If the auto-scaling policy never fires during the load test, the load may not be moving the metric you chose. An I/O-bound endpoint (waiting on a database or network) keeps CPU low even at high request volume. The lab's fix is to scale on request count per target on the load balancer rather than CPU. Relevant to SmartCity because ingestion endpoints mostly wait on the broker and database.

## Related
- [A target-tracking policy keeps average CPU near a set value (Lab 10 uses 70%, min 1, max 4)](target-tracking-cpu-auto-scaling-policy.md)
- [k6 stages ramp virtual users up and down so you can watch scaling react](k6-ramping-load-test.md)
