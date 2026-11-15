---
title: Events arrive at least once; claim the id with a conditional write before acting
tags: [event-driven, serverless, prosit-2]
source: Prosit 2 docs/decisions.md D-027; Prosit 2 learnings/database.md (item 6 and section 5); Prosit 2 learnings/patient-record-service.md (section 6)
---

An offline phone retry, an API retry that publishes again, and SQS redelivery all produce duplicate `appointment.created` events; one patient got two reminders. Fix: the reminder function first writes the appointment id to a DynamoDB table with "only if it isn't there yet". Already there: log `duplicate_skipped` and send nothing. Send fails: remove the claim and raise so SQS retries. Items expire after 30 days (TTL).

Why DynamoDB and not Postgres: the functions run outside the private network and should be independent of the main database. Why not SQS deduplication: it remembers only 5 minutes (and applies to FIFO queues).

Costs: a function that dies after claiming but before sending is skipped on retry (at most one reminder chosen over sometimes two). Without the table variable the function refuses every message so they end in the DLQ. Another consumer (specialist notify) had no duplicate check.

Tests used a fake DynamoDB; switching the claim off made the duplicate tests fail.

SmartCity: alert notifications (flood, full bin) must also be deduplicated.

## Related
- [SNS fan-out to one SQS queue per consumer, batch size 1, dead-letter queue each](sns-fanout-sqs-per-consumer-and-dlq.md)
- [The outbox gap: saving data then publishing can lose the event](outbox-pattern-for-lost-events.md)
