---
title: AgroConnect (Prosit 1) system overview: offline-first PWA, one API, Postgres, three-tier VPC
tags: [prosit-1, aws, community]
source: Prosit 1 docs/system-overview.md; Prosit 1 docs/api-tier.md; Prosit 1 docs/data-tier.md; Prosit 1 docs/cloud-infrastructure.md
---

AgroConnect Ghana: an offline-first PWA for field extension agents who register smallholder farmers (profiles, plots, photos, payments, crop checks, listings), with intermittent 2G/3G and bursty registration windows (about 50 to 500 req/s during subsidy periods).

Tiers:
- **Client:** React 19, Vite, TypeScript, Dexie (IndexedDB) outbox, client UUIDs, PIN unlock, Background Sync; languages English, Twi, Ewe. Hosted on Amplify (eu-west-1 origin) behind CloudFront at an `app.` name.
- **API:** one Node 24 / Express 5 / TypeScript service in Docker on EC2 (port 8000), stateless, behind an ALB at an `api.` name; `pg`, JWT via `jose`, scrypt hashes; Arkesel SMS and votex365 checkout.
- **Data:** PostgreSQL 16 on RDS (`db.t4g.micro`, isolated subnets, single AZ for the lab); a private S3 bucket for photos; rows hold object keys, never images.
- **Infra:** 11 Terraform modules in af-south-1, remote state in S3, CI/CD via GitHub Actions OIDC.

Principles: the app never waits for the network; client-generated permanent identity; strict subnet segmentation and least privilege; lean right-sized operations. The design was written against all six Well-Architected pillars.

SmartCity: the same API, data and infra tiers are the starting template.

## Related
- [AgroConnect AWS infrastructure inventory: network, compute, data, security, observability, cost](agroconnect-aws-infrastructure-inventory.md)
- [One backend service implements every contract (AgroConnect ADR-013)](agroconnect-one-backend-service-for-all-contracts.md)
- [HealthConnect (Prosit 2) system overview: what was built and what was designed only](healthconnect-system-overview.md)
