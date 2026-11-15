---
title: What HealthConnect reused from AgroConnect, as a map for reusing both in SmartCity
tags: [prosit-1, prosit-2, iac]
source: Prosit 2 knowledge/prosit-1.md; Prosit 2 docs/decisions.md D-002
---

| Need | Reused from Prosit 1 |
|---|---|
| VPC, 3 tiers, 2 AZs | `modules/network` (10.20 became 10.30) |
| Cheap NAT | `modules/nat` (fck-nat on t4g.nano) |
| ALB, TLS, health checks | `modules/alb`, `modules/compute` |
| Private DB | `modules/database` (RDS Postgres, not public) |
| Encryption, secrets | RDS encryption, S3 block public access, Secrets Manager |
| Audit | database audit trigger pattern |
| CI/CD | GitHub Actions with OIDC, ECR, instance refresh (`modules/cicd`) |
| Monitoring | CloudWatch dashboard and alarms (`modules/observability`) |
| Offline PWA | React, Vite, IndexedDB outbox, PIN unlock, client UUIDs |
| API | Node, Express, TypeScript, scrypt, votex365 client |

Not copied: farm-specific secrets and Amplify hosting (Amplify is not offered in af-south-1). Added by Prosit 2: events module (SNS, SQS, Lambda, DynamoDB), CloudFront hosting, scoped deploy role, security scanning.

AgroConnect facts worth knowing: af-south-1 chosen at 74 ms median; 11 Terraform modules; estimated $27 to $52 per month; 365 automated tests on every PR; 16 ADRs.

## Related
- [AgroConnect AWS infrastructure inventory: network, compute, data, security, observability, cost](agroconnect-aws-infrastructure-inventory.md)
- [HealthConnect AWS infrastructure inventory (deployed state, November 2026)](healthconnect-aws-infrastructure-inventory.md)
