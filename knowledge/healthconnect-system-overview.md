---
title: HealthConnect (Prosit 2) system overview: what was built and what was designed only
tags: [prosit-2, aws, community]
source: Prosit 2 knowledge/brief.md; Prosit 2 docs/decisions.md D-008, D-029, D-035; Prosit 2 knowledge/sessions/2026-11-09-aws-architecture-diagram.md; Prosit 2 learnings/patient-record-service.md
---

HealthConnect Ghana: a platform linking rural communities and Community Health Volunteers (CHVs) with doctors for records, telemedicine and disease monitoring, for eight app roles (CHV, patient, clinician, pharmacist, traditional healer, GHS official, facility admin, platform admin).

Built:
- Offline CHV/patient PWA (React/TypeScript/Vite, IndexedDB, encrypted records, service worker), hosted on S3 + CloudFront at an `app-hc.` name.
- One API `patient-record-service` (Node/TypeScript/Express) with route modules: auth, sync push/pull, appointments, patients, prescriptions, payments (votex365, simulated without a key), admin, insurance, surveillance.
- FHIR-R4-shaped Postgres on RDS with consent, audit and double-booking rules enforced in the database.
- Event flow: appointment booked, SNS, two SQS queues, two Lambdas (reminder, specialist notify), DLQs, DynamoDB dedupe.
- Telemedicine: WebRTC call page and signaling server on one server at a `call-hc.` name, ported into the app with an audio-only fallback.
- CI/CD with scanning; API at an `api-hc.` name.

Designed or sandboxed: HealthLake (not in af-south-1), TURN relay, real SMS, GMDC/NHIS/DHIMS2 integrations, ML prediction.

## Related
- [HealthConnect AWS infrastructure inventory (deployed state, November 2026)](healthconnect-aws-infrastructure-inventory.md)
- [HealthConnect's known weak points, useful input for a consolidated architecture review](healthconnect-known-weak-points.md)
- [AgroConnect (Prosit 1) system overview: offline-first PWA, one API, Postgres, three-tier VPC](agroconnect-system-overview.md)
