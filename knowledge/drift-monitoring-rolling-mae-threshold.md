---
title: Log predictions, join to later actuals, plot rolling MAE against a retrain threshold line
tags: [lab, mlops, monitoring]
source: Lab 13 (week13_lab_Students) Part E
---

Seed of drift detection: append each prediction (sensor, value, time) to a log, later join to actual readings by sensor and nearest timestamp, compute rolling MAE over the last N pairs (window 10 in the lab), and plot it with a horizontal retrain-alert threshold (the lab uses 6.0 as a placeholder to justify). A threshold only written in the report is easy to forget, hence the chart (Screenshot E1).

## Related
- [A retraining script should promote a new model only if its MAE beats the deployed one](retrain-promote-only-if-better.md)
- [Lab 13 overview: baseline, train, track in MLflow, serve, and seed drift monitoring](lab-13-ml-train-deploy-monitor.md)
