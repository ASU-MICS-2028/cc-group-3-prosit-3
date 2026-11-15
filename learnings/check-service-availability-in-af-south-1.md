---
title: Check that a service and instance type exist in af-south-1 before designing around it
tags: [aws, reliability, prosit-1, prosit-2]
source: Prosit 1 docs/learnings.md L-001; Prosit 2 knowledge/sessions/2026-10-22-infra-bring-up.md and 2026-10-22-lab5-submission.md; Lecture 11
---

Things the team found missing or limited in Cape Town:
- **Amplify Hosting**: not offered (Prosit 1; it was served from eu-west-1 instead).
- **AWS HealthLake**: no endpoint (it answers in eu-west-1, eu-west-2, us-east-1), which became a data-residency point (D-019).
- **Capacity**: in a second account in eu-north-1 there was no `t4g.nano` or `t4g.micro` capacity in one zone, so the NAT instance never launched; a managed NAT Gateway was added by hand for that copy.
- **Region not enabled**: one teammate's own account did not have Cape Town enabled (opt-in regions must be turned on).
- **Global names**: S3 bucket names are global, so a copy in another account cannot reuse a name already taken.

Habit: check the AWS Regional Services list, and try `terraform plan` in the target account early. For SmartCity, check IoT Core, Timestream, SageMaker and managed MQTT/Kafka options for af-south-1 before committing.

**Also (Lecture 11):** AWS HealthLake was unavailable in af-south-1 and too costly for the budget, so we built a small equivalent inside our region. For Prosit 3, verify region availability and pricing of IoT, time-series and ML services early; fall back to self-built pieces if needed.

## Related
- [Infrastructure as Code has edges: Amplify hosting could not be fully created by Terraform](amplify-terraform-github-app-gap.md)
- [fck-nat instance versus managed NAT Gateway: about $3 versus $32 a month](fck-nat-vs-nat-gateway.md)
- [k6 load test showed the database connection pool, not the API, was the limit](../knowledge/load-test-reveals-database-connection-pool-bottleneck.md)
