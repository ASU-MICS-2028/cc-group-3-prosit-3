---
title: Lab 11 overview - audit real spend, two optimizations, SmartCity budget model, sustainability estimate
tags: [lab, cost, sustainability]
source: Lab 11 (week11_lab_Students)
---

Week 11 lab (3 hours plus 90-minute extension): become accountable for the team's spend, then budget SmartCity.

Parts and team deliverables:
- Part A (45 min): pull real billing data via CLI/console, compare with the team's Cost_Tracking_Template, find top 3 cost drivers and unused resources. Deliverable A: screenshot plus the top-3 list.
- Part B (45 min): implement at least two optimizations with before/after (a projected calculator figure is acceptable). Deliverable B.
- Part C (60 min): itemized monthly budget for the ingestion tier at a stated sensor volume. Deliverable C: spreadsheet plus written affordability analysis.
- Part D (20 min): carbon estimate with the provider tool, or a documented lower-carbon region choice. Deliverable D.

Lab report (300 words, due before the Week 12 Monday lecture, so Mon of 24-28 Nov): top 3 cost drivers and actions, the SmartCity monthly estimate and whether it is realistic, one sustainability trade-off.

Rubric: cost audit accurate and specific 25%; two optimizations with measurable before/after 30%; budget model complete and grounded in stated assumptions 30%; sustainability analysis 15%. Optional extension: broker cost comparison, budget-alert script, showback report per Prosit, reading ahead (Edge Computing: Vision and Challenges; LoRaWAN docs).

## Related
- [Pull real cost by service with aws ce get-cost-and-usage and cross-check by tag](audit-spend-with-cost-explorer-cli.md)
- [Four acceptable optimizations: right-size, cheaper storage tier, delete unused, scheduled shutdown](cost-optimization-options-right-size-tier-delete-schedule.md)
- [Itemize the monthly cost: broker, time-series DB, compute, egress, with stated assumptions](smartcity-ingestion-budget-model.md)
- [Estimate carbon with the provider tool, or justify a lower-carbon region manually](region-carbon-intensity-sustainability-estimate.md)
