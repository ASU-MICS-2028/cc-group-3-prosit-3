---
title: Terraform state lives in a bootstrapped S3 bucket with native locking, shared across projects by key
tags: [iac, prosit-1, prosit-2]
source: Prosit 1 docs/cloud-infrastructure.md (section 3); Prosit 2 learnings/infra.md (section 6)
---

Prosit 1 created the state bucket from a separate `bootstrap/` Terraform root with its own local state (it cannot live inside the bucket it creates). The bucket has encryption, versioning and public access blocked. The main root uses `use_lockfile = true`, which needs Terraform 1.10 or newer, so no DynamoDB lock table is needed.

Prosit 2 reused the same bucket with a different state key (`healthconnect/dev/terraform.tfstate`). The bucket name still says `agroconnect`, which is correct, not a mistake.

Gotchas: CI must run the same Terraform version (Prosit 1 pinned 1.10.5); a crashed apply can leave the lock behind (see the recovery note).

SmartCity: reuse the bucket and give the new project its own key rather than building another.

## Related
- [Never stop a terraform apply half-way; recover with force-unlock and import](terraform-interrupted-apply-recovery.md)
- [Copy and trim Terraform modules from the previous prosit instead of rebuilding](reuse-terraform-modules-across-prosits.md)
