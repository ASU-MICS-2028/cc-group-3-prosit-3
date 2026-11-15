---
title: MLflow logs params, metrics and a registered model version the endpoint loads
tags: [lab, mlops, ml]
source: Lab 13 (week13_lab_Students) Parts C-D
---

Set an experiment (smartcity-forecasting), start a run, log params and metrics, and log the model with a registered name; the serving code loads models:/smartcity-forecast/1. Gotcha: if loading fails, the model name and version must match exactly what log_model printed.

## Related
- [Wrap the registered model in FastAPI with /health and /predict](fastapi-prediction-endpoint.md)
- [A retraining script should promote a new model only if its MAE beats the deployed one](retrain-promote-only-if-better.md)
- [Lab 13 overview: baseline, train, track in MLflow, serve, and seed drift monitoring](lab-13-ml-train-deploy-monitor.md)
