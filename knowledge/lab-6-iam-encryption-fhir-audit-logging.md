---
title: Lab 6 - least-privilege IAM, encryption, FHIR-aligned schema and audit logging
tags: [lab, prosit-2, security]
source: Lab 6 handout (week06_lab_Students); Prosit 2 knowledge/labs.md
---

Week 6, 3 h, team. Prosit 2 (HealthConnect) foundation. HealthConnect is a separate codebase; only the patterns carry over from AgroConnect.

**Objectives:** a scoped role attached to the service (no embedded credentials); a policy with an allowed and a denied action demonstrated; encryption at rest verified, TLS enforced; a simplified FHIR-shaped schema with gap analysis; audit logging of who accessed which patient record.

**Parts:** A IAM (rds-data and secretsmanager policy, verify_least_privilege.sh). B encryption (RDS setting, curl -v HTTP redirect, s3api get-bucket-encryption and get-public-access-block). C schema (patients, observations, access_log plus FHIR mapping and Act 843 minimization pass). D audit-log middleware.

**Deliverables:** policy plus allow/deny evidence; encryption and TLS proof; schema, FHIR write-up, populated access_log; 300-word report incl. a named Act 843 principle (before Week 7).

**Rubric:** least privilege 25%; encryption verified 25%; FHIR schema with honest gaps 25%; audit logging 15%; ethics/consent reflection 10%.

Extension: managed FHIR sandbox, secrets rotation drill, RBAC sketch.

**Also (Prosit 2 knowledge/labs.md):** Parts: A a new IAM role for the service only, attached by instance profile, with one allowed and one denied action shown; B verify (do not assume) encryption at rest, TLS on the API (HTTP rejected or redirected), S3 encrypted and not public; C FHIR-aligned `patients`, `observations`, `access_log`, mapping to FHIR resources, one named missing field (for example LOINC or SNOMED codes) and one-sentence data minimisation per `patients` column under Act 843; D audit rows showing who accessed which record and what they did.

Report: 300 words (IAM design, encryption, FHIR decisions and gaps, one named Act 843 principle). Rubric: least privilege 25, encryption 25, FHIR with honest gaps 25, audit 15, ethics 10.

Homework: FHIR sandbox with a 150-word comparison, a timed secrets-rotation drill, an RBAC table, read the Lambda docs.

Starter-code traps: Aurora Data API policy action; FK on the audit table breaks 404 logging; forgeable `x-user-id`; no transaction; SERIAL ids; editable audit log.

## Related
- [Least privilege - attach a scoped role and prove one allowed and one denied action](least-privilege-iam-prove-allow-and-deny.md)
- [Verify encryption at rest and TLS; do not assume defaults](verify-encryption-at-rest-and-in-transit.md)
- [FHIR-shaped schema now, with a written gap list for real interoperability](fhir-aligned-schema-with-gap-analysis.md)
- [Audit logging - record who did what to which record, and await the write](audit-log-who-what-when-await-the-write.md)
- [Lab 5 - VPC, load balancer and multi-country data residency (Prosit 1 wrap-up)](lab-5-vpc-load-balancer-data-residency.md)
- [Lab 7 - event-driven serverless reminders and a WebRTC video call](lab-7-event-driven-serverless-and-webrtc.md)
