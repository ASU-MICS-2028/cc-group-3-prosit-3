---
title: Unconfirmed SNS email subscriptions are silently deleted after three days
tags: [monitoring, reliability, prosit-2]
source: Prosit 2 learnings/infra.md (section 6); Prosit 2 knowledge/sessions/2026-10-26-lab7-event-infra.md
---

CloudWatch alarms and budget alerts email through an SNS topic. Each recipient must click "Confirm subscription" within 3 days, or AWS deletes the subscription without telling anyone. In Prosit 2 only one of four subscriptions survived on 26 Oct, and it happened again on 29 Oct.

Terraform then re-creates the missing ones on the next apply and re-sends the emails, which is why one apply was done with `-target`.

Habit: after any apply that adds subscribers, ask everyone to confirm that day; check the topic's subscriptions list before relying on alarms for a demo or load test.

Also noted: messages parked in a dead-letter queue sit there for 14 days with no alert unless you add an alarm on the queue depth.

## Related
- [Use terraform apply -target for a one-off change, then do the full apply later](terraform-target-for-one-off-applies.md)
- [SNS fan-out to one SQS queue per consumer, batch size 1, dead-letter queue each](sns-fanout-sqs-per-consumer-and-dlq.md)
