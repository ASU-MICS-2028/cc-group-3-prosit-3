---
title: AgroConnect scales on ALBRequestCountPerTarget (500 per minute), not CPU
tags: [prosit-1, scaling, aws]
source: Prosit 1 docs/architecture-decisions.md ADR-008; Prosit 1 docs/cloud-infrastructure.md; Lecture 7
---

An IO-bound API spends its time waiting on the database, so CPU stays low even when throughput is saturated; a CPU policy (first tried at 60%) never trips. Prosit 1 replaced it with a target-tracking policy on `ALBRequestCountPerTarget`, target 500 requests per target per minute (about 8 req/s per instance), ASG min 1, desired 1, max 3.

Reasoning: a `t3.micro` can sustain roughly 200 req/s, so 8 req/s leaves wide headroom for bursts. The target is one variable. The two CloudWatch alarms behind target tracking are AWS-managed and deliberately not in Terraform. Resource label built from ALB and target-group ARN suffixes so it stays tied to the right pair.

Limit: for CPU-bound work (image resizing, ML inference) request count is the wrong signal; swap to CPU or use two metrics.

SmartCity: Lab 10's auto-scaling should pick the signal per component: request count for ingest/API, queue depth or CPU for ML or batch workers.

**Also (Lecture 7):** When asked what their scaling policy was, a Prosit 1 group first answered loosely, then clarified: target tracking on the number of requests per target. You set a target value for requests each instance handles; auto scaling adds instances when the average goes above it and removes them when it falls below.

The instructor's point was that you must be able to say which metric drives scaling (CPU, connection count, request count) and why. Other options raised by a peer were CPU utilisation and number of connections.

Note from the same session: the database was not auto scaled; it only had alarms that emailed the team at a threshold. Stateful tiers usually scale differently from stateless web tiers.

For SmartCity Accra: for bursty sensor ingestion, a message-count or queue-depth based metric may fit better than CPU; be ready to justify the choice.

## Related
- [AgroConnect AWS infrastructure inventory: network, compute, data, security, observability, cost](agroconnect-aws-infrastructure-inventory.md)
- [AgroConnect (Prosit 1) system overview: offline-first PWA, one API, Postgres, three-tier VPC](agroconnect-system-overview.md)
- [What a useful CloudWatch dashboard and alarm set looked like in Prosit 1](cloudwatch-alarms-and-dashboard-practice.md)
- [Questions the instructor and peers asked at the Prosit 1 presentations](prosit-1-presentation-qa-themes.md)
