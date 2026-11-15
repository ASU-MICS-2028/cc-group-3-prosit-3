---
title: A retraining script should promote a new model only if its MAE beats the deployed one
tags: [lab, mlops]
source: Lab 13 (week13_lab_Students) homework extension
---

Optional sketch: given fresh data, retrain, compare to the currently deployed version's MAE, and promote only if better: a minimal version of the evaluate-before-deploy pipeline from lecture.

## Related
- [Log predictions, join to later actuals, plot rolling MAE against a retrain threshold line](drift-monitoring-rolling-mae-threshold.md)
- [MLflow logs params, metrics and a registered model version the endpoint loads](mlflow-experiment-tracking-and-registry.md)
