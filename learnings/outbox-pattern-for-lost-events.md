---
title: The outbox gap: saving data then publishing can lose the event
tags: [event-driven, reliability, prosit-2]
source: Prosit 2 learnings/database.md (section 8); Prosit 2 learnings/patient-record-service.md (section 5); Prosit 2 knowledge/labs.md (Lab 7)
---

HealthConnect saves an appointment, then publishes to SNS after COMMIT. If SNS is down or the server crashes between the two steps, the booking exists but no reminder goes out; the API only answers `"event": "not_published"` and logs, with no retry. Publishing after the commit is deliberate (nobody is told about a rolled-back booking).

Fix not built: an outbox table. Write the event row in the same transaction as the data; a small relay publishes unsent rows until SNS accepts them, marking them sent. Delivery becomes at-least-once, so consumers must dedupe.

This was the "open resilience question" in the Lab 7 report and a good answer to Lab 8's "what if the network drops" question.

SmartCity: ingest from MQTT to a broker to a database has the same gap; decide where durability starts (broker persistence, queue, or outbox).

## Related
- [Events arrive at least once; claim the id with a conditional write before acting](at-least-once-events-need-idempotent-consumers.md)
- [SNS fan-out to one SQS queue per consumer, batch size 1, dead-letter queue each](sns-fanout-sqs-per-consumer-and-dlq.md)
