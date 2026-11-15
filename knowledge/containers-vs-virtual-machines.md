---
title: Containers are lighter than VMs because they share the host kernel instead of bundling an OS
tags: [containers, virtualization, lecture]
source: Lecture 4; Lecture 2
---

A virtual machine includes a full guest OS and you must choose the OS, RAM and so on up front; the OS takes a big share of resources. A container packages the app and its dependencies without a full OS and shares the host kernel.

Comparison given in the lecture:
- Isolation: VMs have full isolation; containers share the kernel.
- Boot time: VMs take a while; containers start in about a second.
- Size and density: containers are much smaller, so many more fit on one host.
- Use case: VMs for strong isolation or a different OS; containers for fast, portable, consistent application deployment.

The kernel is the always-running core of the OS (the most essential services); containers use the host's.

For SmartCity Accra: many small services on few instances is cheaper with containers.

**Also (Lecture 2):** Virtualization splits one physical machine into isolated VMs, each carrying a full OS. Problem shown in class: run a trivial "Hello World" service in a VM, send it more and more requests, and it becomes slow. A program that works on your own machine is only the beginning; you must think about network accessibility, speed under many users, and deployment.

Containers are lightweight packages (Docker, Heroku-style platforms) so many copies run side by side, and requests can be routed to different containers, e.g. by region. This ties into distributed computing built into cloud platforms.

For SmartCity Accra: package broker, API and ML services as containers so they can scale independently.

## Related
- [Containers fix the "works on my machine" dependency problem](works-on-my-machine-problem.md)
- [A VM can be shipped as an appliance, but CPU architecture still matters](vm-appliance-and-cpu-architecture-portability.md)
- [Docker core concepts: image, container, Dockerfile, registry](docker-image-container-dockerfile-registry.md)
- [What you still own on IaaS (patching, firewall, backups, scaling)](iaas-responsibilities-you-still-own.md)
- [History of computing - heavy lifting keeps moving to the provider](cloud-computing-history-heavy-lifting-shifts-to-provider.md)
- [Week zero prerequisites (Linux, Docker, GitHub, databases)](week-zero-prerequisites.md)
