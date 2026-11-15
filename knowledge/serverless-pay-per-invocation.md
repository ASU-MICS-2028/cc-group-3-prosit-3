---
title: Serverless - pay per function invocation, not per server
tags: [serverless, event-driven, cost]
source: Lecture 2
---

With event-driven serverless (AWS Lambda, also on GCP and Azure), a function runs when an event triggers it and you are billed per invocation rather than for a server that waits around. Good fit for sporadic work such as an SMS relay or a scheduled job; you give up some runtime control.

For SmartCity Accra: alert notifications or periodic model scoring are candidates; a continuously running broker is not.

## Related
- [Mix service models per component, not one for the whole system](mixing-service-models-per-component.md)
- [IaaS, PaaS, SaaS - control versus convenience](iaas-paas-saas-control-vs-convenience.md)
