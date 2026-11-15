---
title: A VM can be shipped as an appliance, but CPU architecture still matters
tags: [virtualization, lecture]
source: Lecture 4
---

A VM built in VirtualBox or VMware with all dependencies installed can be exported (for example as an .ova file) and given to others, who import it into VirtualBox without installing anything. The lecturer used this to hand students ready-made lab setups.

CPU architecture matters: software downloads for Apple often come in two versions, Intel and Apple Silicon, because they are different architectures. Compiled code (object code) depends on the instruction set architecture, the hardware-software boundary. Java gets around this with the JVM, which runs on any machine that has one.

Lesson for the labs: when a classmate's setup fails, check architecture and OS first.

## Related
- [Containers are lighter than VMs because they share the host kernel instead of bundling an OS](containers-vs-virtual-machines.md)
- [Containers fix the "works on my machine" dependency problem](works-on-my-machine-problem.md)
