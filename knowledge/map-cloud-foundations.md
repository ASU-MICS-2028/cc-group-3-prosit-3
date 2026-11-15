---
title: Cloud foundations (map)
tags: [process]
source: index of the notes below
---

Definitions, service and deployment models, virtualization, containers, storage, networking, IaC, CI/CD, events.

**Taught or given**

- [A VM can be shipped as an appliance, but CPU architecture still matters](vm-appliance-and-cpu-architecture-portability.md)
- [Add a human testing stage where a teammate uses the app like a real user and logs issues](human-testing-stage-before-release.md)
- [Big data is described by Volume, Velocity, Variety (and Veracity)](big-data-four-vs.md)
- [Block, object and file storage serve different jobs](block-object-file-storage.md)
- [Choose SQL for fixed-schema data and NoSQL or object storage for flexible data, and justify it](sql-vs-nosql-choice.md)
- [Choosing a service model - time to market and data sensitivity](choosing-service-model-time-and-data-sensitivity.md)
- [CI/CD pipeline shape - build, test, scan, approval-gated deploy](ci-pipeline-build-test-gated-deploy.md)
- [Cloud work builds on operating systems and networking basics](cloud-engineers-need-os-and-networking-fundamentals.md)
- [Containers are lighter than VMs because they share the host kernel instead of bundling an OS](containers-vs-virtual-machines.md)
- [Containers fix the "works on my machine" dependency problem](works-on-my-machine-problem.md)
- [DevOps joins software development and IT operations](devops-joins-development-and-operations.md)
- [Docker core concepts: image, container, Dockerfile, registry](docker-image-container-dockerfile-registry.md)
- [Dockerfile pattern - copy manifests first, install, then copy code, run as non-root](dockerfile-layer-cache-and-non-root-user.md)
- [Five essential characteristics of cloud computing](five-essential-cloud-characteristics.md)
- [Geography-aware networking and CDNs](geography-aware-networking-and-cdns.md)
- [git push over HTTPS needs a token or SSH key, not your password](git-https-push-needs-personal-access-token.md)
- [History of computing - heavy lifting keeps moving to the provider](cloud-computing-history-heavy-lifting-shifts-to-provider.md)
- [IaaS, PaaS, SaaS - control versus convenience](iaas-paas-saas-control-vs-convenience.md)
- [Immutable infrastructure: replace the image, never patch a running container](immutable-infrastructure.md)
- [In-memory data in a container is lost on restart; make it persistent](persistent-data-vs-in-memory-containers.md)
- [Inside a container, localhost is the container itself](localhost-inside-a-container-is-the-container.md)
- [Mix service models per component, not one for the whole system](mixing-service-models-per-component.md)
- [NIST definition of cloud computing (SP 800-145)](nist-cloud-definition.md)
- [Public, private, hybrid and community cloud](cloud-deployment-models.md)
- [Publish one event, let independent functions react](publish-one-event-two-independent-consumers.md)
- [Pull-request checks then image build then rolling refresh](ci-checks-and-deploy-pipeline-prosit-1.md)
- [Rehearse 10-15 minutes timed, and record a backup demo under 5 minutes](final-presentation-rehearsal-and-backup-video.md)
- [Services find each other by Kubernetes DNS name, not IP](kubernetes-service-dns-name-between-services.md)
- [Structured, semi-structured and unstructured data need different stores](structured-semi-structured-unstructured-data.md)
- [TCP is reliable, UDP is fast and lossy, QUIC is Google's newer transport](tcp-vs-udp-vs-quic.md)
- [Terraform workflow - init, plan, apply; import or destroy pre-existing resources](terraform-init-plan-apply-and-import.md)
- [Tests pass locally but fail in CI - look for environment differences](ci-tests-pass-locally-fail-in-ci.md)
- [Turn a manual setup script into cloud-init](cloud-init-script-as-first-infrastructure-as-code.md)
- [Use managed payment APIs and keep payments as a separate service](use-managed-payment-apis.md)
- [Verify CLI access with one identity check per provider](verify-cli-access-to-all-three-clouds.md)
- [Virtualization turns physical resources into virtual ones; a hypervisor manages the VMs](virtualization-and-hypervisor.md)
- [VPC layout - two public and two private subnets across two AZs](vpc-two-az-public-private-subnet-layout.md)

## Related
- [Lectures by week (map)](map-lectures.md)
- [SmartCity Accra brief and our scope (map)](map-smartcity-brief.md)
- [Labs 0–14 (map)](map-labs.md)
- [Course facts (map)](map-course.md)
