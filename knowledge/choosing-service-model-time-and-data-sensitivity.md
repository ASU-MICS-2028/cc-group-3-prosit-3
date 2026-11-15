---
title: Choosing a service model - time to market and data sensitivity
tags: [cloud-basics, lecture]
source: Lecture 2
---

Class exercise: a bank must launch a savings product in six weeks. IaaS, PaaS or SaaS for the core ledger, and what changes at six months?

Reasoning the lecturer rewarded (the reasoning matters, not a single right answer):
- Short deadline favours PaaS or SaaS: something already built, with less control. A long deadline allows IaaS and custom work.
- Counter-argument against SaaS for a financial ledger: sensitive data and rules about where data may be stored.
- Rebuttal: some software (open source) can run with your own back end and on-premises database, so the choice blends IaaS and SaaS.
- Outcome: banks typically go hybrid, keeping personal data on premises and using public services for non-sensitive work.

The lecturer asked that choices be justified technically ("not by feeling") and written up.

For SmartCity Accra: justify each component's service model by deadline, control needed and data sensitivity.

## Related
- [IaaS, PaaS, SaaS - control versus convenience](iaas-paas-saas-control-vs-convenience.md)
- [Public, private, hybrid and community cloud](cloud-deployment-models.md)
- [Data residency laws and consent drive where data may live](data-residency-and-consent.md)
