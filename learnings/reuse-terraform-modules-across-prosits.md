---
title: Copy and trim Terraform modules from the previous prosit instead of rebuilding
tags: [iac, process, prosit-2]
source: Prosit 2 docs/decisions.md D-002; Prosit 2 learnings/infra.md (section 2); Prosit 2 knowledge/prosit-1.md
---

Prosit 2 copied the AgroConnect modules into `infra/modules/`, removed everything farm-specific (SMS, payments, push secrets, Amplify hosting), gave the project its own VPC range, its own state key and the tag `Project=healthconnect`, and applied 66 resources the same week. The labs required a separate codebase, so copying (not sharing) was the rule.

What it saved: network, ALB, ASG, RDS, ECR, observability and CI/CD modules had already run in production.

What it cost: fixes made in one repo must be copied to the other by hand.

Changes needed on copy: non-overlapping CIDR (10.20 for AgroConnect, 10.30 for HealthConnect), a minimum of 2 app servers for the failover demo, and a new env var the start-up script did not set.

For SmartCity, copy from the HealthConnect modules (they also include events, CloudFront hosting and a scoped deploy role) and pick a fresh CIDR such as another 10.x range.

## Related
- [Terraform state lives in a bootstrapped S3 bucket with native locking, shared across projects by key](terraform-remote-state-s3-native-locking.md)
- [HealthConnect AWS infrastructure inventory (deployed state, November 2026)](../knowledge/healthconnect-aws-infrastructure-inventory.md)
