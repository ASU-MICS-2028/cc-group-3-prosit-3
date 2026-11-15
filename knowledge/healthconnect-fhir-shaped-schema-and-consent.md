---
title: HealthConnect's FHIR R4 schema: tables, FHIR resources, consent purposes and audit
tags: [prosit-2, databases, data-governance]
source: Prosit 2 learnings/database.md; Prosit 2 docs/decisions.md D-011 to D-019; Prosit 2 docs/data-decisions.md DATA-001 to DATA-005
---

Tables and the FHIR resource each copies: `patients` (Patient), `practitioners` (Practitioner, with a role), `consents` (Consent), `observations` (Observation), `appointments` (Appointment), `referrals` (ServiceRequest), `prescriptions` (MedicationRequest), `access_log` (who looked) and `audit_trail` (who changed what), plus `loinc_codes` (9 accepted measurement types with UCUM unit and plausible range), `facilities`, `emergencies`, `weekly_case_counts` and `outbreak_signals` (a view).

Decisions: FHIR R4 (HealthLake supports only R4); UUIDs from the device; consent per purpose (`clinical_care`, `appointment_reminders`, `health_advisory`) and a fourth purpose, public health reporting with aggregated anonymised counts only; clinical rows are corrected (`entered-in-error`), never deleted; `access_log.patient_id` has no foreign key so 404 probes are still logged; emergencies need no consent check (implied consent) but never de-escalate.

Known gap: tables are FHIR-shaped, not a FHIR API; no business identifier to match people across systems.

SmartCity analogue: a device registry, a readings hypertable, and a threshold/alert table with similar integrity rules.

## Related
- [HealthConnect treats Ghana's Act 843 as the law and HIPAA only as a safeguards checklist](healthconnect-act-843-and-hipaa-stance.md)
- [HealthConnect disease surveillance: aggregated counts, a rule-based signal and human-confirmed alerts](healthconnect-surveillance-design.md)
