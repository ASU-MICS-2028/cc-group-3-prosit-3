---
title: HealthConnect AWS infrastructure inventory (deployed state, November 2026)
tags: [prosit-2, aws, iac]
source: Prosit 2 knowledge/sessions/2026-11-09-aws-architecture-diagram.md; Prosit 2 learnings/infra.md; Prosit 2 docs/decisions.md D-003, D-010, D-022, D-023, D-033
---

Region af-south-1, VPC 10.30.0.0/16, two AZs with public, private-app and data subnets in each. Tags `Project=healthconnect`; its own state key in the shared state bucket.

- **Edge:** one ACM certificate (api and call names) on the ALB, TLS 1.3 preferred, HTTP redirects to HTTPS; DNS at the registrar. CloudFront (`PriceClass_200`) plus a private S3 bucket (Origin Access Control) serves the PWA; its certificate is in us-east-1.
- **Compute:** ASG of 2 to 4 `t3.micro` running the API image from ECR; one `t3.micro` call server (host-header rule, own role); `fck-nat` on `t4g.nano`.
- **Data:** RDS PostgreSQL 16 `db.t4g.micro`, encrypted, single-AZ, no internet route; photo bucket; DynamoDB `reminders-sent` (pay per request, TTL 30 days).
- **Events:** SNS topic, two SQS queues and DLQs (14-day retention), two Python 3.12 Lambdas.
- **Security:** Secrets Manager (DB, signing key, optional payment key), per-job IAM roles, SSM sessions.
- **Operations:** 8 CloudWatch alarms; budget alarm ($50 forecast, $100 actual); GitHub OIDC deploy role limited to main.
- Cost about $70 to $90 per month while running.

## Related
- [HealthConnect (Prosit 2) system overview: what was built and what was designed only](healthconnect-system-overview.md)
- [AgroConnect AWS infrastructure inventory: network, compute, data, security, observability, cost](agroconnect-aws-infrastructure-inventory.md)
- [HealthConnect's known weak points, useful input for a consolidated architecture review](healthconnect-known-weak-points.md)
