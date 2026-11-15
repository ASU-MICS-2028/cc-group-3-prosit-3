---
title: HealthConnect PWA and sync architecture in one page
tags: [prosit-2, edge, security]
source: Prosit 2 docs/decisions.md D-031, D-032, D-033; Prosit 2 learnings/frontend.md; Prosit 2 learnings/patient-record-service.md
---

- **Phone:** tokens-only design system, role table (at most five tabs per role), test mode with eight synthetic accounts, PIN and passphrase tiers, WebAuthn fingerprint for staff screen-lock only, encrypted IndexedDB vault, FHIR records, photo shrunk to about 100 KB, voice notes up to 2 minutes, service worker, manifest, validation rules duplicated from the database.
- **Sync API:** `POST /sync/push` (statuses ok, duplicate, conflict, retry, rejected), `GET /sync/pull?since=N` (100 per page), `GET /sync/taken` (a doctor's busy times with no patient details). The server decides who may download what: own records, a CHV's patients, a doctor's patients with a booked visit.
- **Rule parity:** consent, plausible ranges, double booking, no deletes are enforced both on the phone and in Postgres.
- **Hosting:** static files on S3 and CloudFront, deployed on merge in about two minutes.
- **Limits:** a forgotten passphrase loses unsent records; prescriptions need a signal; QR scanning uses BarcodeDetector (Chrome Android only).

## Related
- [HealthConnect (Prosit 2) system overview: what was built and what was designed only](healthconnect-system-overview.md)
- [HealthConnect telemedicine: WebRTC with a signaling server and an audio-only fallback](healthconnect-telemedicine-call-architecture.md)
