---
title: Use short-lived pre-signed URLs with a private bucket
tags: [storage, security]
source: Lab 4 Part B and Homework Extension
---

Buckets stay private by default and never publicly writable. Grant temporary access by generating a signed URL (the lab suggests 5 minutes) and test with curl upload, with no public permissions involved.

SmartCity Accra: devices or the dashboard can upload/download model artifacts or exports this way.

## Related
- [Verify encryption at rest and TLS; do not assume defaults](verify-encryption-at-rest-and-in-transit.md)
- [Least privilege - attach a scoped role and prove one allowed and one denied action](least-privilege-iam-prove-allow-and-deny.md)
