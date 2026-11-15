---
title: Create secrets empty in Terraform and fill the value from the CLI so it never enters state or git
tags: [security, iac, prosit-2]
source: Prosit 2 learnings/infra.md (item 11 and section 6); Prosit 2 learnings/patient-record-service.md (section 6)
---

The token-signing key's secret container is created by Terraform with no value; a random 64-character value is put in from the command line, so it is in neither the repo nor state. Servers receive only the secret's ARN and read the value with their role.

Gotchas: if the secret is ever recreated it comes back empty and every protected route answers 401 until the value is set again (changing it signs everyone out). Fail closed: with no key the server still starts so `/health` passes, but protected routes refuse everyone. Payment test keys follow the same pattern (`VOTEX_SECRET_ARN`), and the payments client runs in a labelled simulated mode until a key exists.

A plaintext database password file was once found in the shared Drive and removed; rotate any credential that was ever exposed.

SmartCity: broker credentials and device certificates follow the same rule.

## Related
- [Least privilege in practice: one IAM role per job, each permission naming one resource](least-privilege-one-role-per-job.md)
- [Synthetic data and sandbox integrations must be labelled on screen and in the report](synthetic-data-and-labelled-sandbox-integrations.md)
