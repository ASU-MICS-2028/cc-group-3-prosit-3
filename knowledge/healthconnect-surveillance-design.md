---
title: HealthConnect disease surveillance: aggregated counts, a rule-based signal and human-confirmed alerts
tags: [prosit-2, databases, data-governance]
source: Prosit 2 learnings/database.md (item 8 and section 6); Prosit 2 docs/decisions.md D-018, D-034
---

Design closest to SmartCity's monitoring problem. Data: `weekly_case_counts` (district, week starting Monday, condition, count; totals only, no patient ids; flagged `synthetic` or `reported`). A view `outbreak_signals` flags a district when a week has at least 5 cases and more than double the average of the previous 4 rows, with a reason sentence. A GHS official confirms or dismisses a signal in `outbreak_alerts`; after a decision the figures cannot change and a community alert is allowed only once confirmed (a second decision is refused with 409 so an alert is never sent twice).

Gotchas: missing weeks count as missing, not zero (send a 0 row); rank regions per district, not by total; the baseline is previous 4 rows not 4 calendar weeks; thresholds are illustrative and not signed off.

Seed data: 16 regions, 19 districts, 8 weeks, shaped by published DHS percentages with a planted outbreak.

SmartCity analogue: threshold or anomaly rule, a view or job producing signals, and an operator confirming before a public alert.

## Related
- [HealthConnect's FHIR R4 schema: tables, FHIR resources, consent purposes and audit](healthconnect-fhir-shaped-schema-and-consent.md)
- [HealthConnect event flow: appointment.created fans out to two independent Lambdas](healthconnect-event-flow-sns-sqs-lambda.md)
