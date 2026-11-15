---
title: HealthConnect event flow: appointment.created fans out to two independent Lambdas
tags: [prosit-2, event-driven, serverless]
source: Prosit 2 docs/decisions.md D-010, D-027; Prosit 2 learnings/infra.md (items 10 and 13 and section 8)
---

`POST /appointments` saves the appointment and its audit row in one transaction, then publishes `appointment.created` to an SNS topic. The topic copies it into two SQS queues (`reminders`, `specialist-notify`), each triggering its own Python Lambda; neither function knows the other or the API. The patient's phone is in the message only if they consented to reminders. Failed three times, a message goes to that queue's DLQ for 14 days.

Measured in a live run: each function did 1 to 20 ms of work, at most 32 MB, and 4 of 9 runs were cold starts; SNS showed 3 published and 6 delivered, 0 failed.

Serverless fit paragraph used in the report: short, occasional, can wait seconds, free when idle, so Lambda; the patient-record API stays on always-on servers because requests need a fast answer and a database transaction with its audit row.

SmartCity: a sensor alert (flood level, full bin) can reuse this fan-out shape.

## Related
- [HealthConnect (Prosit 2) system overview: what was built and what was designed only](healthconnect-system-overview.md)
- [HealthConnect's known weak points, useful input for a consolidated architecture review](healthconnect-known-weak-points.md)
