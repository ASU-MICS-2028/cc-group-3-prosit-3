---
title: HealthConnect keeps one API with route modules instead of sixteen services (D-035)
tags: [prosit-2, containers, aws]
source: Prosit 2 docs/decisions.md D-035, D-036, D-037, D-038, D-039
---

The brief's feature list (SVC-1 to SVC-16) became route modules inside `patient-record-service`, sharing its database, sign-in, audit and deployment. Partner systems stay behind a small adapter with a mock mode; the event functions stay separate. Same reasoning as AgroConnect's ADR-013 and the course rule of thumb of 3 to 5 microservices at most per team.

Sign-in: username and scrypt password, one-hour token, one-use 30-day refresh token (D-036). Sync: each pushed record saved twice in one transaction, the exact FHIR copy and the real table (D-037). Prescription fraud checks raise flags a pharmacist must acknowledge, with a sandbox licence register (D-038). Payments through votex365 with server-set amounts, simulated until a key is set (D-039).

SmartCity: ingest, query, alert and ML-serving parts have different scaling needs, so some separation (ingest versus API) may be justified; write the ADR.

## Related
- [One backend service implements every contract (AgroConnect ADR-013)](agroconnect-one-backend-service-for-all-contracts.md)
- [HealthConnect (Prosit 2) system overview: what was built and what was designed only](healthconnect-system-overview.md)
