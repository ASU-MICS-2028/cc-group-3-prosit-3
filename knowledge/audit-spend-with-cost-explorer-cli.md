---
title: Pull real cost by service with aws ce get-cost-and-usage and cross-check by tag
tags: [lab, cost, aws]
source: Lab 11 (week11_lab_Students) Part A
---

The lab's audit_spend.sh calls aws ce get-cost-and-usage for the last 8 weeks, MONTHLY granularity, metric UnblendedCost, grouped by SERVICE, filtering out zero-cost rows. Azure and GCP have costmanagement / billing equivalents. Then cross-check in the console filtered by the team's resource tags and list the top 3 cost line items and any resource still running that is no longer needed (stopped-but-not-terminated instances, unused load balancers, orphaned storage).

Gotchas: cost data can lag up to 24 hours (use the pricing calculator for recent resources); an access-denied error may mean the IAM policy lacks ce:GetCostAndUsage, since Cost Explorer API access is separate from billing console access.

## Related
- [Lab 11 overview - audit real spend, two optimizations, SmartCity budget model, sustainability estimate](lab-11-cost-analysis-optimization-budget-model.md)
- [Four acceptable optimizations: right-size, cheaper storage tier, delete unused, scheduled shutdown](cost-optimization-options-right-size-tier-delete-schedule.md)
- [Two extension ideas: a month-to-date spend warning script and a per-Prosit showback report](budget-alert-script-and-showback-report.md)
