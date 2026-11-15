---
title: Synthetic data and sandbox integrations must be labelled on screen and in the report
tags: [data-governance, privacy, prosit-2]
source: Prosit 2 docs/decisions.md D-004, D-034, D-038, D-039; Prosit 2 learnings/database.md; Prosit 2 learnings/patient-record-service.md
---

No real patient data was ever stored. To keep demos believable the team used published regional DHS figures (cited in the seed file) for surveillance counts, with a planted outbreak; rows carry `synthetic` or `reported`, every screen says "synthetic", and the report must too.

Partner systems (licence register, pharmacy list, NHIS check, insurance plans, payments) ran behind an adapter with a mock mode. Payments without a key reply `simulated: true` and revenue totals keep simulated money apart so test money cannot pass as income. Thresholds (outbreak rule, fraud flags, vitals ranges) were "illustrative, not signed off".

Seed data lives in a seed file, not a migration. Test accounts' password is not in the repo.

SmartCity: sensor data will be simulated too; label simulated streams and the thresholds (PM2.5 limits, bin and water levels) as assumptions until sourced.

## Related
- [Capture evidence honestly: report the real result, label what is faked, never rewrite history](honest-evidence-capture.md)
- [Create secrets empty in Terraform and fill the value from the CLI so it never enters state or git](secrets-set-by-hand-stay-out-of-state.md)
