---
title: Mix service models per component, not one for the whole system
tags: [cloud-basics, serverless, containers]
source: Lecture 2
---

Key skill of the semester: choose models deliberately for each part rather than defaulting to the biggest instance. The AgroConnect example:

- Core services: IaaS with containers.
- Event-driven pieces (e.g. an SMS relay triggered by a schedule): PaaS / serverless (AWS Lambda).
- Payments: SaaS or a managed API (mobile money, Paystack, Visa). Never rebuild a payment processor.
- Farmer registration had to work offline or on 2G, so it needed a progressive web app and edge-friendly compute, which pushed away from pure SaaS.

For SmartCity Accra: e.g. containers for the broker and API, serverless for sporadic alert or ML-batch jobs, a managed service where one exists.

## Related
- [IaaS, PaaS, SaaS - control versus convenience](iaas-paas-saas-control-vs-convenience.md)
- [Serverless - pay per function invocation, not per server](serverless-pay-per-invocation.md)
- [Use managed payment APIs and keep payments as a separate service](use-managed-payment-apis.md)
