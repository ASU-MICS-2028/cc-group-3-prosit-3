---
title: Lab 13 overview: baseline, train, track in MLflow, serve, and seed drift monitoring
tags: [lab, ml, mlops]
source: Lab 13 (week13_lab_Students)
---

Week 13 lab (3 hours plus 90-minute extension): compress the MLOps lifecycle into one session using the Lab 12 sensor data (backfill synthetic data if too little, and say so). Pick forecasting or anomaly detection to match your domain. Rule: do not deploy a model that does not beat its naive baseline; losing honestly is a valid, gradeable outcome.

Parts and deliverables:
- Part A (30 min) pull data to a DataFrame; Part B (45 min) baseline; Part C (60 min) train the real model and log it to MLflow. Deliverable A: baseline vs model MAE (or anomaly comparison) plus the MLflow run.
- Part D (45 min) serve behind an endpoint. Deliverable B: a successful request/response.
- Part E (20 min) log predictions against later actuals, rolling MAE, retrain threshold line on a chart. Deliverable C: script/query plus the drift chart.

Lab report (300 words, due before the Week 14 Monday lecture, so Mon of 8-11 Dec): ML feature, baseline vs model and whether it earned its complexity; explaining a prediction to a non-technical AMA official; retrain trigger and cadence. Submit PDF, notebook/script, MLflow screenshot, endpoint evidence.

Rubric: honest baseline evaluation 30%; versioned and tracked 20%; serving endpoint 25%; drift seed 10%; report 15%.

## Related
- [Beat "next reading equals last reading" (or a z-score rule) before any model ships](naive-baseline-before-model.md)
- [MLflow logs params, metrics and a registered model version the endpoint loads](mlflow-experiment-tracking-and-registry.md)
- [Wrap the registered model in FastAPI with /health and /predict](fastapi-prediction-endpoint.md)
- [Log predictions, join to later actuals, plot rolling MAE against a retrain threshold line](drift-monitoring-rolling-mae-threshold.md)
