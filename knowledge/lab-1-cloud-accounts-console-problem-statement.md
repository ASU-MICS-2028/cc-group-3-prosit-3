---
title: Lab 1 - three cloud accounts, CLI check, console comparison, problem statement
tags: [lab, prosit-1, cloud-basics]
source: Lab 1 handout (week01_lab)
---

Week 1, 3 h, team of 3-4. Kicks off Prosit 1 (AgroConnect Ghana).

**Objectives:** accounts on AWS, Azure and GCP with billing alerts; MFA and a non-root identity; find compute, storage, IAM and billing in each console; verify CLI access to all three; write an evidence-based problem statement; justify a first-pass platform choice with at least two technical factors.

**Parts:** A account setup (AWS, Azure resource group, GCP project, $5 alerts); B install aws/az/gcloud CLIs and run verify_cloud_access.sh; C console exploration and AWS/Azure/GCP comparison table; D team roles (Cloud/Infrastructure, Application/PWA, Data, Community and Documentation; a 3-person team merges the last one but must name an owner).

**Deliverables:** shared doc of account IDs plus alert screenshots; CLI identity output; one-page comparison table; 300-word problem statement PDF (before Week 2).

**Rubric:** account evidence 20%; CLI verification 15%; comparison table 15%; problem statement 25%; platform justification 15%; roles 10%. This lab counts toward the 25% lab-assignments component.

Key rule: pick ONE primary platform for billable resources; keep the other two secured but empty.

## Related
- [Every cloud account gets MFA and a $5 billing alert on day one](cloud-account-baseline-mfa-billing-alert.md)
- [Verify CLI access with one identity check per provider](verify-cli-access-to-all-three-clouds.md)
- [Pick one primary cloud for billable resources; keep the others empty](one-primary-cloud-platform-keeps-spend-down.md)
- [Each prosit is a separate codebase; the infrastructure pattern carries forward](three-prosit-codebases-separate-pattern-carries.md)
