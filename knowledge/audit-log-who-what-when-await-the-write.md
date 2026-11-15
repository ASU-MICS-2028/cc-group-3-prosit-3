---
title: Audit logging - record who did what to which record, and await the write
tags: [security, monitoring, prosit-2]
source: Lab 6 Part D and Troubleshooting
---

Insert an access_log row (accessed_by, patient_id, action, accessed_at) on every read and write; the lab takes the user from an x-user-id header. Test by calling the API then SELECT-ing recent log rows.

Common bug: the logging call is added but never awaited, or runs after the response was sent, and fails silently.

SmartCity Accra: audit admin and data-export actions the same way.

## Related
- [Least privilege - attach a scoped role and prove one allowed and one denied action](least-privilege-iam-prove-allow-and-deny.md)
- [FHIR-shaped schema now, with a written gap list for real interoperability](fhir-aligned-schema-with-gap-analysis.md)
