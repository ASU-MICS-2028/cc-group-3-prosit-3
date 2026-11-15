---
title: Each prosit is a separate codebase; the infrastructure pattern carries forward
tags: [course, process, prosit-3-brief]
source: Lab 1 intro; Lab 6 intro
---

AgroConnect, HealthConnect and SmartCity Accra are three separate repositories with different stakeholders, data and sensitivity. When a lab says to extend an earlier microservice pattern, copy the working pattern forward and adapt it; do not bolt new routes onto the old repo.

What carries over: VPC layout, CI/CD pipeline shape, IAM least privilege, containerization conventions, baseline setup scripts, the cost-tracking template.

SmartCity Accra: reuse the Lab 5 VPC and Lab 9 pipeline/Terraform as starting templates.

## Related
- [VPC layout - two public and two private subnets across two AZs](vpc-two-az-public-private-subnet-layout.md)
- [CI/CD pipeline shape - build, test, scan, approval-gated deploy](ci-pipeline-build-test-gated-deploy.md)
- [Terraform workflow - init, plan, apply; import or destroy pre-existing resources](terraform-init-plan-apply-and-import.md)
