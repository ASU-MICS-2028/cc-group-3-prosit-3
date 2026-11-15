---
title: Wrap the registered model in FastAPI with /health and /predict
tags: [lab, mlops, ml]
source: Lab 13 (week13_lab_Students) Part D
---

Starter service: load the model from the MLflow registry at startup, GET /health returns status ok, POST /predict takes hour, lag_1, lag_2 and returns the prediction. Run with uvicorn on port 8000 and test with curl; deliverable B is that request and response. Same package, deploy, verify, monitor pattern as the Week 3 containers.

## Related
- [MLflow logs params, metrics and a registered model version the endpoint loads](mlflow-experiment-tracking-and-registry.md)
- [Lab 13 overview: baseline, train, track in MLflow, serve, and seed drift monitoring](lab-13-ml-train-deploy-monitor.md)
