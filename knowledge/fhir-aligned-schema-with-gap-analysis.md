---
title: FHIR-shaped schema now, with a written gap list for real interoperability
tags: [databases, data-governance, prosit-2]
source: Lab 6 Part C
---

Design tables shaped like FHIR resources (patients to Patient, observations to Observation, plus access_log), with a fhir_resource_type column and a consent_given_at timestamp that is NULL until consent. Write a mapping note and at least one gap (e.g. coded terminology such as LOINC/SNOMED instead of free-text observation_type).

Data minimization (Ghana Data Protection Act 2012, Act 843): justify each column against the stated purpose; if you cannot, flag it for removal.

SmartCity Accra: similar discipline for any standard schema.

## Related
- [Audit logging - record who did what to which record, and await the write](audit-log-who-what-when-await-the-write.md)
- [Data residency plan - shard by country and keep personal data in its home region](data-residency-plan-sharding-by-country.md)
