---
title: Beat "next reading equals last reading" (or a z-score rule) before any model ships
tags: [lab, ml, mlops]
source: Lab 13 (week13_lab_Students) Part B
---

Forecasting baseline: shift the value by one step and take the mean absolute error (naive MAE). Anomaly baseline: rolling window of 20, z-score, flag when absolute z exceeds 3. A model is only worth deploying if its MAE is lower than the naive MAE. SmartCity example: an air-quality PM2.5 forecast must beat persistence.

## Related
- [Split time-series data by time (e.g. first 80% train), never by random shuffle](chronological-split-for-time-series.md)
- [If the model does not beat the baseline, report it and explain why; do not fabricate](honest-reporting-model-loses-to-baseline.md)
- [Lab 13 overview: baseline, train, track in MLflow, serve, and seed drift monitoring](lab-13-ml-train-deploy-monitor.md)
