---
title: k6 load test showed the database connection pool, not the API, was the limit
tags: [scaling, monitoring, prosit-2]
source: Lecture 11 (our Prosit 2 presentation)
---

Our HealthConnect load test: k6 with 1,000 concurrent users writing 50,000 records. The API autoscaled from 2 to 4 servers, uptime was 99.7%, alarms fired and emails were sent, but only 68.9% of records were stored in under 11 minutes. Cause: just 10 database connections in the pool.

Lesson: scale the stateful bottleneck (pool size, DB capacity, queueing) along with stateless compute, and read the test result for the real limiter. For SmartCity Accra, ingest bursts from many sensors will hit the same limit; buffer through a broker or queue.

## Related
- [MapReduce is the batch-processing paradigm for when a design that works at 1,000 users meets millions](mapreduce-batch-processing-for-scale.md)
- [SNS fan-out to one SQS queue per consumer, batch size 1, dead-letter queue each](../learnings/sns-fanout-sqs-per-consumer-and-dlq.md)
