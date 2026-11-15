---
title: What you still own on IaaS (patching, firewall, backups, scaling)
tags: [cloud-basics, security]
source: Lecture 2
---

On IaaS you request a VM (CPU, RAM, disk from a physical host) with an OS image of your choice. After that the provider is not responsible for: OS patching, installing the runtime, firewall rules, backup strategy, and scaling decisions. The provider protects the data centre; patching your OS is your job.

Why choose IaaS anyway: no framework lock-in, full control, and it is the substrate that containers, PaaS and even serverless ultimately run on. In the lecture, AgroConnect's two-VM deployment was IaaS, and feeling that operational burden directly motivated the move to containers.

For SmartCity Accra: any EC2 host (broker, database) needs a patch and backup plan written down.

## Related
- [IaaS, PaaS, SaaS - control versus convenience](iaas-paas-saas-control-vs-convenience.md)
- [Containers are lighter than VMs because they share the host kernel instead of bundling an OS](containers-vs-virtual-machines.md)
