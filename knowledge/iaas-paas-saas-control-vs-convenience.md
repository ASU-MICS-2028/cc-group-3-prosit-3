---
title: IaaS, PaaS, SaaS - control versus convenience
tags: [cloud-basics, lecture]
source: Lecture 2; Study Session 1
---

The more the provider manages, the less control you have but the faster you ship.

- IaaS: provider runs the physical server, storage, networking and virtualization. You manage OS, runtime, data and application. Examples: AWS EC2, Azure Virtual Machines, GCP Compute Engine.
- PaaS: provider also runs OS and runtime; you supply code and data. Trade-off: less control over the runtime and possibly higher cost per compute unit.
- SaaS: provider manages everything; you configure and use. Trade-off: you accept the vendor's data model, security posture and pricing.

Analogy used: IaaS is renting an empty room (bring your own furniture), PaaS is a room with basics supplied, SaaS is a furnished hotel. It is a spectrum, not one right answer, and since cloud is configurable you can move later as needs grow.

**Also (Study Session 1):** - IaaS: you manage OS, runtime, data, apps; provider manages servers, storage, networking, virtualization. Examples: EC2, Azure VMs, Compute Engine.
- PaaS: you manage data and code; provider manages OS, runtime, middleware. Examples: Elastic Beanstalk, Azure App Service, App Engine.
- SaaS: you manage configuration and data only. Examples: Gmail, Salesforce.
Also: EC2 is Elastic Compute Cloud, S3 is Simple Storage Service.

## Related
- [What you still own on IaaS (patching, firewall, backups, scaling)](iaas-responsibilities-you-still-own.md)
- [Mix service models per component, not one for the whole system](mixing-service-models-per-component.md)
- [Choosing a service model - time to market and data sensitivity](choosing-service-model-time-and-data-sensitivity.md)
- [Five essential characteristics of cloud computing](five-essential-cloud-characteristics.md)
- [Virtualization turns physical resources into virtual ones; a hypervisor manages the VMs](virtualization-and-hypervisor.md)
