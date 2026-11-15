---
title: Cost and sustainability (map)
tags: [process]
source: index of the notes below
---

Billing audits, optimisation, budgets, teardown, carbon and region choice.

**Taught or given**

- [An S3 lifecycle rule can move objects to STANDARD_IA after 90 days](s3-lifecycle-policy-ia-transition.md)

- [Audit running compute on all three clouds before milestones](cross-provider-resource-audit-script.md)

- [Capex versus opex - why elastic cloud capacity beats owned servers](capex-vs-opex-elasticity.md)

- [Cloud benefits (responsiveness, lower upfront cost, availability) and risks (trust boundaries, lock-in, cost overruns)](cloud-benefits-and-risks.md)

- [Compare managed vs self-hosted broker cost and find the volume where the answer flips](broker-cost-comparison-flip-point.md)

- [Data centre siting, latency and energy trade-offs](data-centre-siting-latency-and-energy.md)

- [Decide what to cut first if the real budget is half your estimate](budget-cut-half-exercise.md)

- [Estimate carbon with the provider tool, or justify a lower-carbon region manually](region-carbon-intensity-sustainability-estimate.md)

- [Four acceptable optimizations: right-size, cheaper storage tier, delete unused, scheduled shutdown](cost-optimization-options-right-size-tier-delete-schedule.md)

- [Ground the monthly-active-user assumption in published Ghana population data](mau-assumption-from-ghana-statistics.md)

- [Itemize the monthly cost: broker, time-series DB, compute, egress, with stated assumptions](smartcity-ingestion-budget-model.md)

- [Pick one primary cloud for billable resources; keep the others empty](one-primary-cloud-platform-keeps-spend-down.md)

- [Pull real cost by service with aws ce get-cost-and-usage and cross-check by tag](audit-spend-with-cost-explorer-cli.md)

- [Serverless - pay per function invocation, not per server](serverless-pay-per-invocation.md)

- [Stop idle cloud resources to protect credits](stop-idle-resources-protect-credits.md)

- [Tag and name every cloud resource with the team name](tag-every-resource-with-team-name.md)

- [Two extension ideas: a month-to-date spend warning script and a per-Prosit showback report](budget-alert-script-and-showback-report.md)

- [Write the teardown plan now: resources, one named owner, 48-hour deadline after grades](decommissioning-plan-owner-and-date.md)

**Found out by doing** (in `learnings/`)

- [Cost tracking and teardown: what keeps billing and what to delete by hand](../learnings/cost-tracking-and-teardown-checklist.md)

- [fck-nat instance versus managed NAT Gateway: about $3 versus $32 a month](../learnings/fck-nat-vs-nat-gateway.md)

## Related
- [Lectures by week (map)](map-lectures.md)

- [SmartCity Accra brief and our scope (map)](map-smartcity-brief.md)

- [Labs 0–14 (map)](map-labs.md)

- [Course facts (map)](map-course.md)
