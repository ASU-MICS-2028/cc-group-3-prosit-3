---
title: ML and MLOps (map)
tags: [process]
source: index of the notes below
---

Baselines, forecasting, anomaly detection, MLflow, serving, drift, explainability.

**Taught or given**

- [A GradientBoostingRegressor with hour, lag_1 and lag_2 is the lab forecasting starter](gradient-boosted-lag-feature-forecast.md)
- [A retraining script should promote a new model only if its MAE beats the deployed one](retrain-promote-only-if-better.md)
- [Averaging two parties model weights may lose to a local model, and that is a legitimate result](federated-averaging-demo-honest-result.md)
- [Beat "next reading equals last reading" (or a z-score rule) before any model ships](naive-baseline-before-model.md)
- [Compare IsolationForest flags to the z-score baseline: same events, or noise?](anomaly-detection-zscore-vs-isolation-forest.md)
- [Data leakage, repeated runs and sanity-checking ML metrics](ml-evaluation-leakage-and-repeated-runs.md)
- [Deadline-aware GPU scheduling across mixed GPU types](gpu-deadline-scheduling-mixed-gpus.md)
- [Federated learning with edge-level averaging keeps data local](federated-learning-at-the-edge.md)
- [Heavy ML inference belongs on the server, not on low-end devices](heavy-ml-runs-server-side.md)
- [If the model does not beat the baseline, report it and explain why; do not fabricate](honest-reporting-model-loses-to-baseline.md)
- [Keep a human approving high-stakes ML recommendations](human-in-the-loop-ml-recommendations.md)
- [Log predictions, join to later actuals, plot rolling MAE against a retrain threshold line](drift-monitoring-rolling-mae-threshold.md)
- [MLflow logs params, metrics and a registered model version the endpoint loads](mlflow-experiment-tracking-and-registry.md)
- [Route about 10% of requests to a second model version and compare errors](canary-model-comparison-10-percent.md)
- [Split time-series data by time (e.g. first 80% train), never by random shuffle](chronological-split-for-time-series.md)
- [Three ways to make synthetic data: LLM prompts with a schema, GANs, or distribution parameters](synthetic-data-for-testing-without-real-data.md)
- [Turn feature_importances_ into two or three plain sentences for an AMA official](explaining-feature-importance-to-non-technical-official.md)
- [Wrap the registered model in FastAPI with /health and /predict](fastapi-prediction-endpoint.md)

## Related
- [Lectures by week (map)](map-lectures.md)
- [SmartCity Accra brief and our scope (map)](map-smartcity-brief.md)
- [Labs 0–14 (map)](map-labs.md)
- [Course facts (map)](map-course.md)
