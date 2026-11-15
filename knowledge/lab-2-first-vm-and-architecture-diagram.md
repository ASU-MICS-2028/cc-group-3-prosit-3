---
title: Lab 2 - first VM, basic monitoring and a six-pillar architecture diagram
tags: [lab, prosit-1, cloud-basics]
source: Lab 2 handout (week02_lab_Students)
---

Week 2, 3 h, team. Prosit 1 Foundation MVP.

**Objectives:** provision a tagged, network-restricted Ubuntu VM; SSH in and run a baseline setup script; generate CPU load and see it in the console; draw an architecture diagram annotated for all six Well-Architected pillars; justify instance size; name one way the design fails at higher load.

**Parts:** A VM (AWS t3.micro, Azure Standard_B1s, GCP e2-micro; SSH only from My IP; setup_baseline.sh installs git, curl, stress-ng, Docker). B monitoring (stress-ng for 60 s, screenshot the CPU graph). C diagram (client, API tier, data tier boxed "TBD", network boundary, one annotation per pillar).

**Deliverables:** instance screenshot with uname -a and docker --version; CPU spike screenshot plus stress-ng summary; diagram PNG/PDF; 300-word report (before Week 3).

**Rubric:** VM reachable 20%; baseline script 10%; monitoring with spike 15%; diagram completeness 30%; pillar annotations specific 15%; report honesty about limits 10%.

Pattern to reuse: provision, connect, verify, document.

## Related
- [Allow SSH only from your own IP, never 0.0.0.0/0](ssh-security-group-my-ip-only.md)
- [Generate controlled CPU load with stress-ng to see monitoring work](stress-ng-generate-cpu-load-for-monitoring.md)
- [Annotate the architecture diagram for all six Well-Architected pillars](well-architected-six-pillar-diagram-annotations.md)
- [Tag and name every cloud resource with the team name](tag-every-resource-with-team-name.md)
