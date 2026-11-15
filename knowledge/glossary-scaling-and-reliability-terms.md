---
title: Glossary: auto scaling, horizontal vs vertical, SLA/SLI/SLO, RTO/RPO, MTTR
tags: [course, scaling, reliability]
source: Cloud Computing Glossary
---

Auto scaling adjusts resources to demand. Horizontal scaling (scale out) adds instances; vertical (scale up) enlarges one. Elastic load balancing spreads traffic over targets; caching keeps hot data fast to cut latency. SLA is the contract; SLI the measured indicator; SLO the target for it. RTO is the longest tolerable downtime; RPO the longest tolerable data loss measured in time. MTTR is average time to repair; MTBF average time between failures; DR/BCP are recovery plans. SmartCity uses them in Lab 10 (scaling, SLO).

## Related
- [A target-tracking policy keeps average CPU near a set value (Lab 10 uses 70%, min 1, max 4)](target-tracking-cpu-auto-scaling-policy.md)
- [Write one SLO for the ingestion tier and compute its monthly error budget](slo-and-error-budget-exercise.md)
