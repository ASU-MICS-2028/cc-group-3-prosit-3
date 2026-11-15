---
title: Compare IsolationForest flags to the z-score baseline: same events, or noise?
tags: [lab, ml]
source: Lab 13 (week13_lab_Students) Part C
---

For the anomaly option, run sklearn IsolationForest (contamination 0.05) and compare with the rolling z-score baseline: count of flags each and the agreement rate. The question to answer is whether differences are meaningful or noise. A flood-level alert is the SmartCity use case.

## Related
- [Beat "next reading equals last reading" (or a z-score rule) before any model ships](naive-baseline-before-model.md)
- [Lab 13 overview: baseline, train, track in MLflow, serve, and seed drift monitoring](lab-13-ml-train-deploy-monitor.md)
