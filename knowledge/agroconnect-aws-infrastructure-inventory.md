---
title: AgroConnect AWS infrastructure inventory: network, compute, data, security, observability, cost
tags: [prosit-1, aws, iac]
source: Prosit 1 docs/cloud-infrastructure.md; Prosit 1 docs/system-overview.md
---

Region af-south-1, VPC 10.20.0.0/16, two AZs, six subnets: public (ALB, NAT), private app (ASG), private data (RDS, no internet route).

- **Chained security groups:** internet to ALB on 443, ALB to app on 8000, app to RDS on 5432. No port 22; shell via SSM Session Manager; IMDSv2 required (hop limit 2 so the SDK in the container can use the instance role).
- **Compute:** Ubuntu 24.04 `t3.micro`, ASG min 1, desired 1, max 3, target tracking on request count; Docker `awslogs` driver to CloudWatch Logs; ECR with scan on push.
- **Data:** RDS PostgreSQL 16 `db.t4g.micro`, 20 GB gp3 autoscaling to 100 GB, KMS encrypted, 7-day backups, managed master secret in Secrets Manager; S3 media bucket (AES256, versioned, public access blocked, multipart cleanup).
- **Observability:** SNS alarm topic with email; ALB unhealthy hosts, 5xx, p95 latency, RDS memory/storage/CPU, NAT and ASG status checks; one CloudWatch dashboard; $100 budget (50% forecast, 100% actual).
- **Tags:** Project, Env, Team, ManagedBy.
- **Cost:** about $27 to $52 per month (NAT $3, ALB $19, compute 0 to 10, RDS 0 to 14, public IPv4 $3.60, CloudWatch $3.5).

## Related
- [AgroConnect (Prosit 1) system overview: offline-first PWA, one API, Postgres, three-tier VPC](agroconnect-system-overview.md)
- [AgroConnect scales on ALBRequestCountPerTarget (500 per minute), not CPU](agroconnect-target-tracking-request-count-decision.md)
- [HealthConnect AWS infrastructure inventory (deployed state, November 2026)](healthconnect-aws-infrastructure-inventory.md)
