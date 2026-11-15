---
title: Generate controlled CPU load with stress-ng to see monitoring work
tags: [monitoring, lab]
source: Lab 2 Part B
---

Run stress-ng --cpu 1 --timeout 60s --metrics-brief on the VM, then open the provider's metrics (CloudWatch CPUUtilization, Azure Monitor, Cloud Monitoring) and confirm a visible spike. Basic metrics are on by default on AWS.

Deliberately breaking things in a controlled way proves the dashboard reflects reality. Lab 2 calls this the first step toward the golden-signals dashboard of Week 10.

SmartCity Accra: the same tool is a quick way to trigger and test CPU-based auto-scaling policies.

## Related
- [Annotate the architecture diagram for all six Well-Architected pillars](well-architected-six-pillar-diagram-annotations.md)
- [Lab 2 - first VM, basic monitoring and a six-pillar architecture diagram](lab-2-first-vm-and-architecture-diagram.md)
