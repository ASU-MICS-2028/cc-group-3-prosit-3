---
title: Use managed payment APIs and keep payments as a separate service
tags: [cloud-basics, lecture]
source: Lecture 1; Lecture 2
---

Both lectures made the same point: do not build your own payment processor. Mobile money (via the networks), Paystack, Visa and similar providers offer ready-made interfaces to plug in. Lecture 1 added that payments should be handled by a separate back-end service (a microservice idea covered later), and a classmate's payment gateway integrating several providers was cited as an example.

For SmartCity Accra there is no payment path in the brief, but the principle (consume a managed service for commodity functions) applies, e.g. managed messaging or monitoring.

## Related
- [Mix service models per component, not one for the whole system](mixing-service-models-per-component.md)
- [IaaS, PaaS, SaaS - control versus convenience](iaas-paas-saas-control-vs-convenience.md)
