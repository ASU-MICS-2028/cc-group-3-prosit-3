---
title: Data residency laws and consent drive where data may live
tags: [data-governance, privacy]
source: Lecture 2
---

Providers may have strong physical and technical security (the lecture cited many layers of access control before the server floor), yet laws can still restrict where data is stored or sent. Points made:

- Rules can forbid keeping citizens' data outside the country, or using it for something like model training, without the data subject's consent. Ghana's data-protection rules were cited.
- Banks, health bodies and government payroll data are typically kept on premises for this reason.
- Political example: US restrictions on where American users' data is hosted.
- "Better safe than sorry": keep data local if there is doubt, and process locally even when using SaaS.

For SmartCity Accra: sensor data is mostly environmental, but any resident-linked data (locations, reports) needs a stated storage region and consent basis; af-south-1 choice should be justified.

## Related
- [Public, private, hybrid and community cloud](cloud-deployment-models.md)
- [Ground rules for community-engaged prosits (consent, sign-off)](agroconnect-community-ground-rules.md)
