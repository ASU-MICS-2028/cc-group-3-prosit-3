---
title: An S3 lifecycle rule can move objects to STANDARD_IA after 90 days
tags: [lab, cost, storage]
source: Lab 11 (week11_lab_Students) Part B
---

Example from the lab: aws s3api put-bucket-lifecycle-configuration on a media bucket with one enabled rule, empty prefix filter, and a transition to STANDARD_IA after 90 days. Small, almost invisible changes like this can still move the bill noticeably.

## Related
- [Four acceptable optimizations: right-size, cheaper storage tier, delete unused, scheduled shutdown](cost-optimization-options-right-size-tier-delete-schedule.md)
- [Lab 11 overview - audit real spend, two optimizations, SmartCity budget model, sustainability estimate](lab-11-cost-analysis-optimization-budget-model.md)
