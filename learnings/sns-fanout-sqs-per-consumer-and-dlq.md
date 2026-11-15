---
title: SNS fan-out to one SQS queue per consumer, batch size 1, dead-letter queue each
tags: [event-driven, serverless, prosit-2]
source: Prosit 2 docs/decisions.md D-010; Prosit 2 learnings/infra.md (item 10 and section 3); Prosit 2 knowledge/labs.md (Lab 7); Lecture 10; Lecture 11 (our Prosit 2 design)
---

Two Lambda functions on one SQS queue compete: each message goes to only one. To make both react to one event, publish to an SNS topic that copies the message into a separate queue per function. Each queue also holds messages if its function is down.

Settings that mattered: batch size 1 (a bad message fails alone), `maxReceiveCount` 3 then the message moves to that queue's DLQ for 14 days, raw message delivery on the subscription, and each function with its own role (read its own queue, write its own logs). Functions that only log or send SMS stay outside the VPC (no NAT cost, faster start).

Check: publish a good event and see both log groups; publish a bad one and see it fail 3 times about a minute apart, then appear in both DLQs (`get-queue-attributes`). Nothing alerts on DLQ messages by default.

EventBridge with two rules would also work. SmartCity: a sensor alert topic can feed notification, dashboard and ML-feature consumers independently.

**Also (Lecture 10; Lecture 11 (our Prosit 2 design)):** Pattern we used: the API saves a booking and publishes one event to an SNS topic; two SQS queues subscribe (reminders, notifications); a Lambda per queue processes messages.
- Queues deliver at least once, so a message can arrive twice. Before processing, the Lambda checks a DynamoDB table for an atomic record of that event id; if absent, create it, process, mark done. No duplicate reminders.
- After 3 failed attempts the message goes to a dead-letter queue (14-day retention). Failures often mean a malformed payload or bad configuration, so a human looks at it.

Fits SmartCity Accra for alert fan-out (e.g. flood level to notification, dashboard and logging).

## Related
- [Events arrive at least once; claim the id with a conditional write before acting](at-least-once-events-need-idempotent-consumers.md)
- [Unconfirmed SNS email subscriptions are silently deleted after three days](alarm-email-subscriptions-expire-after-3-days.md)
- [k6 load test showed the database connection pool, not the API, was the limit](../knowledge/load-test-reveals-database-connection-pool-bottleneck.md)
- [Client-generated IDs, record versions and cursor downloads make sync safe on flaky networks](../knowledge/idempotent-ids-and-versions-for-flaky-connectivity.md)
