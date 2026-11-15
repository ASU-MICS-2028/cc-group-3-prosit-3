---
title: MapReduce is the batch-processing paradigm for when a design that works at 1,000 users meets millions
tags: [scaling, lecture, course]
source: Lecture 10; Lecture 11
---

The lecturer set a Google Research MapReduce paper as reading, one paper per group, with group presentation planned. The argument: a good architecture (load balancer, two zones, private database) can still fail at 15,000 farmers or millions of concurrent users; at that point you need a different processing model. MapReduce splits work into map and reduce steps over distributed machines, suited to batch processing at scale. It was framed as the "icing" on the cake after the labs.

For SmartCity Accra, sensor streams are continuous and large, so batch aggregation (hourly or daily summaries for forecasting) is a natural place to apply it.

## Related
- [Prosit 3 shifts focus from running in the cloud to scaling to millions of users](prosit-3-focus-scaling-and-distributed-processing.md)
- [k6 load test showed the database connection pool, not the API, was the limit](load-test-reveals-database-connection-pool-bottleneck.md)
