---
title: Geography-aware networking and CDNs
tags: [networking, cloud-basics, lecture]
source: Lecture 7
---

The instructor used Prosit 1 feedback to introduce cloud networking. When users sit in different countries (he used Kenya, Nigeria and Ghana), each should reach a nearby server instead of travelling to one distant region. That needs the network design to know about geography: for example allocating address ranges or domains per region so latency problems are resolved quickly. A CDN cannot work properly without that location awareness.

He also said the group's networking questions (firewalls, how instances are connected) would be taught later in the course.

For SmartCity Accra: sensors are all in Accra, but dashboard users and edge caching still benefit from this thinking.

## Related
- [AgroConnect picked af-south-1 by measuring latency from Ghana (74 ms median)](agroconnect-region-selection-by-latency.md)
- [Keep servers and databases in private subnets behind the load balancer](private-subnets-behind-load-balancer.md)
