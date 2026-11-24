---
title: Cost per user falls in the city-wide budget scenario
tags: [cost, scaling]
source: "Issue #12"
---

In the Makola pilot estimate, roughly 86% of spending is in the database, API, broker and load balancer lines. With 110,000 monthly users in the city-wide scenario, egress is the largest line. Total monthly cost grows about fourfold while the user count grows elevenfold, so cost per user falls from 1.4 to 0.5 US cents.

The estimate depends on data per visit and the capacity allowances. Doubling data per visit raises the modeled city-wide total from about USD 556 to USD 767 a month.

## Related

- [Lab 11 budget model](../evidence/lab11/12-budget-model.md)
