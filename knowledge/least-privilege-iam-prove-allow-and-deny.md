---
title: Least privilege - attach a scoped role and prove one allowed and one denied action
tags: [iam, security, aws]
source: Lab 6 Part A and Troubleshooting
---

Make a dedicated role for the service (instance profile on AWS, managed identity on Azure, service account on GCP) instead of embedded credentials. Policy lists only needed actions and specific resource ARNs (the lab uses rds-data execute and secretsmanager GetSecretValue). Then run a script showing a read succeeds and a destructive call (delete-db-cluster) is denied.

If the scoped role breaks the service, read CloudTrail/Activity Log/Audit Logs for the exact denied action and add only that permission.

SmartCity Accra: separate roles for ingest, ML training and dashboards.

## Related
- [Do daily work as a non-root IAM user, never the root account](never-use-root-account-for-daily-work.md)
- [Verify encryption at rest and TLS; do not assume defaults](verify-encryption-at-rest-and-in-transit.md)
- [Lab 6 - least-privilege IAM, encryption, FHIR-aligned schema and audit logging](lab-6-iam-encryption-fhir-audit-logging.md)
