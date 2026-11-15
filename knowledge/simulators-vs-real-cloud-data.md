---
title: Cloud research relies on simulators because providers rarely share real data
tags: [cloud-basics, course, lecture]
source: Lecture 9
---

The instructor explained that big providers (Google, Alibaba) optimise data centers heavily because efficiency is their business model, but seldom publish real traces. Academics therefore test in software simulators, ideally validated against provider data, and only later in a real data center.

His advice: if a paper tests with a handful of VMs, rerun it in a simulator at a realistic scale (hundreds of thousands of VMs), and when you run experiments yourself, report the hardware and test bed so others can reproduce them.

For SmartCity Accra: when load testing, state the instance types and request mix, and say plainly what a small test can and cannot show.

## Related
- [Dynamic VM scheduling by chaining five existing algorithms](dynamic-vm-scheduling-five-algorithms.md)
- [Reviewing technical papers and checking reproducibility](paper-review-and-reproducibility.md)
