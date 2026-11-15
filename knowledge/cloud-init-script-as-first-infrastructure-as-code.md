---
title: Turn a manual setup script into cloud-init
tags: [iac, cloud-basics]
source: Lab 2 Homework Extension
---

Rewrite setup_baseline.sh as a #cloud-config YAML that the provider runs at boot, so provisioning is scripted rather than SSH by hand. Rough first IaC habit, formalized with Terraform in Lab 9.

## Related
- [Terraform workflow - init, plan, apply; import or destroy pre-existing resources](terraform-init-plan-apply-and-import.md)
- [Allow SSH only from your own IP, never 0.0.0.0/0](ssh-security-group-my-ip-only.md)
