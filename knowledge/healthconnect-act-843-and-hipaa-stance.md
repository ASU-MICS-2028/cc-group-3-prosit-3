---
title: HealthConnect treats Ghana's Act 843 as the law and HIPAA only as a safeguards checklist
tags: [prosit-2, privacy, data-governance]
source: Prosit 2 docs/decisions.md D-005, D-018, D-028, D-034; Prosit 2 knowledge/sessions/2026-10-18-planning.md
---

The brief said "HIPAA-compliant". HIPAA is a US law, so the team designed for Ghana's Data Protection Act 2012 (Act 843) as the legal basis and mapped each HIPAA Security Rule safeguard group (access control, audit controls, integrity, person authentication, transmission security, backup) to a control. Wording rule: "designed against HIPAA safeguards", never "HIPAA-compliant" or "certified".

Related decisions: synthetic data only (the open question of real data is closed by D-034); health data in af-south-1 crosses a border because Ghana has no region, and the residency write-up says so; stated purposes are triage, scheduling, advisory and anonymised public-health reporting; HSTS and TLS in transit, encrypted RDS at rest.

Lab 6 asks the report to name one specific Act 843 principle (data minimisation, purpose limitation or right to be informed) and to justify each `patients` column.

SmartCity: write the equivalent line for any citizen-facing data and say what is not personal data.

## Related
- [AgroConnect mapped Ghana's Act 843 principles to concrete controls and listed its gaps](agroconnect-act-843-privacy-controls.md)
- [HealthConnect's FHIR R4 schema: tables, FHIR resources, consent purposes and audit](healthconnect-fhir-shaped-schema-and-consent.md)
