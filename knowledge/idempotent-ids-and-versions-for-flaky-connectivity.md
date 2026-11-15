---
title: Client-generated IDs, record versions and cursor downloads make sync safe on flaky networks
tags: [reliability, prosit-2, iot]
source: Lecture 11 (our Prosit 2 design)
---

Offline-first rules we presented: (1) IDs are generated on the device, so sending a record twice stores it once; (2) each record carries a version, and on conflict a person chooses which copy to keep; (3) each record is saved with a backup copy in one transaction; (4) downloads use a cursor/bookmark, because if record 6 commits before 5 a naive timestamp pull could skip 5 forever.

Same logic applies to a sensor gateway that buffers readings during a network outage and resends: use reading IDs so retries do not double count.

## Related
- [SNS fan-out to one SQS queue per consumer, batch size 1, dead-letter queue each](../learnings/sns-fanout-sqs-per-consumer-and-dlq.md)
- [Validate at front end, API and database; range limits catch impossible values](database-as-last-line-of-defense-range-checks.md)
