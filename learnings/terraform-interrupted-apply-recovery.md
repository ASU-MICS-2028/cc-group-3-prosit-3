---
title: Never stop a terraform apply half-way; recover with force-unlock and import
tags: [iac, prosit-2, aws]
source: Prosit 2 learnings/infra.md (section 6); Prosit 2 knowledge/sessions/2026-10-26-lab7-event-infra.md
---

An interrupted `terraform apply` leaves AWS with resources that Terraform's state never recorded, and the state stays locked. Re-running the apply then fails with "already exists".

What happened in Prosit 2: an apply was stopped part-way, 9 resources existed in AWS but not in state, and the lock stayed.

Recovery that worked:
1. Confirm nobody else is still running an apply.
2. `terraform force-unlock <lock-id>`.
3. Bring the orphans back with `import` (import blocks work well), one per resource that already exists.
4. Run `terraform plan` again; it should show no changes.

Rule: let an apply finish, or kill it only when you are ready to import. For SmartCity Accra, with more resources (broker, time-series DB, ML endpoint), an interrupted apply costs more to untangle, so apply in smaller targeted steps when unsure.

## Related
- [Use terraform apply -target for a one-off change, then do the full apply later](terraform-target-for-one-off-applies.md)
- [Terraform state lives in a bootstrapped S3 bucket with native locking, shared across projects by key](terraform-remote-state-s3-native-locking.md)
