---
title: Terraform workflow - init, plan, apply; import or destroy pre-existing resources
tags: [iac, lab]
source: Lab 9 Part D and Troubleshooting; Lecture 7
---

Write main.tf (the lab recreates a VPC with aws_vpc plus public and private aws_subnet), then terraform init, terraform plan (review, never skip), terraform apply. "Already exists": terraform import it, or destroy the manual copy and let Terraform recreate it (safer for class projects).

Writing IaC may reveal what your manual setup actually looked like. Extension: extract a module with variables (cidr_block, environment_name). Lab 2's cloud-init idea was the first step toward this.

SmartCity Accra: define VPC, brokers, databases and scaling groups as code from the start.

**Also (Lecture 7):** Terraform sits between you and the cloud API. You describe every resource you want in configuration files; Terraform talks to AWS and creates them, instead of you clicking through the console one by one.

The cycle explained in the presentation:
1. Write the configuration.
2. `terraform plan` shows what would change and changes nothing.
3. `terraform apply` creates or updates the resources.
4. `terraform destroy` removes everything it created, useful for temporary projects so nothing keeps billing.

One team organised its Terraform as modules (network with VPC and subnets, application with load balancer and auto scaling group, outbound networking, storage, front end hosting). Running `terraform fmt` and `validate` as a pull-request check keeps the code tidy.

For SmartCity Accra: keep the whole IoT and ML stack in Terraform so it can be rebuilt, costed and torn down after demos.

## Related
- [VPC layout - two public and two private subnets across two AZs](vpc-two-az-public-private-subnet-layout.md)
- [CI/CD pipeline shape - build, test, scan, approval-gated deploy](ci-pipeline-build-test-gated-deploy.md)
- [Turn a manual setup script into cloud-init](cloud-init-script-as-first-infrastructure-as-code.md)
- [Pull-request checks then image build then rolling refresh](ci-checks-and-deploy-pipeline-prosit-1.md)
- [fck-nat instance versus managed NAT Gateway: about $3 versus $32 a month](../learnings/fck-nat-vs-nat-gateway.md)
