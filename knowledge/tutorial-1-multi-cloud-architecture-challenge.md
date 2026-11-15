---
title: Tutorial 1 (course reference): the multi-cloud architecture design challenge
tags: [course, cloud-basics]
source: Prosit 2 knowledge/course-reference.md
---

A three-week team project (3 to 4 students): migrate a mid-sized online retailer from ageing on-premises servers (10x Black Friday spikes, no disaster recovery, tape backups with 24-hour RPO) to a hybrid multi-cloud design.

Week 1: current-state analysis, provider research with a weighted comparison matrix (compute, database migration, global reach, 3-year cost, security, support). Week 2: high-level design under constraints (budget cap, 99.9% uptime, under 2 s page loads, GDPR, survive 10x spikes, RTO under 4 h, RPO under 1 h) and role specs; subnet exercise (carve a 10.0.0.0/16 VPC into public, private and database subnets across 3 AZs). Week 3: proof of concept with Terraform, load test with Apache Bench, stop a primary and watch failover, then cost optimisation with Cost Explorer.

Assessment: individual 40%, team 35%, technical implementation 25%. Takeaways: start from numbers, tier the network, IaC everything, prove resilience by breaking things, treat cost as a requirement, security is a checklist.

SmartCity: a reusable method for Lab 10 (load test) and Lab 11 (cost).

## Related
- [Syllabus plan for Weeks 10 to 15 (Prosit 3 and exams)](course-schedule-weeks-10-to-15.md)
- [Course availability targets: HealthConnect 99.7%, SmartCity 99.5%, and what nines mean](course-availability-targets-by-prosit.md)
