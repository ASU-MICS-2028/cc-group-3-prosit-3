---
title: Verify CLI access with one identity check per provider
tags: [cloud-basics, aws]
source: Lab 1 Part B
---

A small script run after configuring each CLI proves programmatic access: aws sts get-caller-identity, az account show, gcloud config list (project and account). Use set -e so it stops on the first failure.

Fixes from the lab: "Unable to locate credentials" means run aws configure with the IAM access key; gcloud hanging usually means the wrong or stale default project, so rerun gcloud init.

Homework extension: add resource listings (aws ec2 describe-instances, az vm list, gcloud compute instances list) and expect empty output on non-primary accounts.

## Related
- [Pick one primary cloud for billable resources; keep the others empty](one-primary-cloud-platform-keeps-spend-down.md)
- [Audit running compute on all three clouds before milestones](cross-provider-resource-audit-script.md)
- [Lab 1 - three cloud accounts, CLI check, console comparison, problem statement](lab-1-cloud-accounts-console-problem-statement.md)
