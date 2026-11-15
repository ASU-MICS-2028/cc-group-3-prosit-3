---
title: AgroConnect mapped Ghana's Act 843 principles to concrete controls and listed its gaps
tags: [prosit-1, privacy, data-governance]
source: Prosit 1 docs/architecture-decisions.md ADR-016
---

Table used in Prosit 1 (a reusable template for any personal-data system):
- **Consent:** registration cannot be saved without recorded consent (`consent_at`); the statement can be played aloud in the farmer's language.
- **Minimality:** only the brief's data; every profile question optional.
- **In transit:** TLS everywhere, HSTS, verified TLS from API to RDS.
- **At rest:** RDS encryption; private S3 with SSE reached only through the API; PINs and passwords hashed (scrypt), never logged.
- **Access control:** role tokens; agents see only farmers they registered; out-of-scope records answer 404.
- **Accountability:** audit trigger records who changed what; exports audited.
- **On the phone:** data in IndexedDB; PIN opens the app; 5 wrong PINs wipe the session.
- **Residency:** personal data in af-south-1; only static files served from eu-west-1.

Known gaps: no retention schedule or deletion workflow, no self-service access/correction, no registration with the Data Protection Commission.

SmartCity: sensors are mostly not personal data, but citizen reports, locations and any camera or phone data are.

## Related
- [HealthConnect treats Ghana's Act 843 as the law and HIPAA only as a safeguards checklist](healthconnect-act-843-and-hipaa-stance.md)
- [AgroConnect (Prosit 1) system overview: offline-first PWA, one API, Postgres, three-tier VPC](agroconnect-system-overview.md)
