---
title: Do daily work as a non-root IAM user, never the root account
tags: [iam, security, aws]
source: Lab 0 A.3; Lab 1 A.1; Lab 6 Part A
---

Create an IAM user for everyday work and keep the root login (with MFA) for emergencies only. Labs 0 and 1 attach AdministratorAccess as a temporary shortcut, with the explicit promise to scope it down in Lab 6.

Lab 6 then replaces it with a per-service role holding only the actions and resources that service needs.

SmartCity Accra: start with scoped roles per component (ingest, ML job, dashboard) instead of repeating the admin shortcut.

## Related
- [Least privilege - attach a scoped role and prove one allowed and one denied action](least-privilege-iam-prove-allow-and-deny.md)
- [Every cloud account gets MFA and a $5 billing alert on day one](cloud-account-baseline-mfa-billing-alert.md)
- [Lab 6 - least-privilege IAM, encryption, FHIR-aligned schema and audit logging](lab-6-iam-encryption-fhir-audit-logging.md)
