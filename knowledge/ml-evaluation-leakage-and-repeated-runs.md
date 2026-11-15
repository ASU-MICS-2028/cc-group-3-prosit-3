---
title: Data leakage, repeated runs and sanity-checking ML metrics
tags: [ml, mlops, lecture]
source: Lecture 9
---

Problems a student found in a CNN-LSTM sentiment paper (95.98 percent accuracy):
- Unclear train/test split. If hyperparameters or preprocessing are chosen before the split, test information leaks into training and inflates scores.
- Single run reported. Models vary between runs, so report the average over repeated runs.
- Unfair comparison: the paper's movie-review results were compared with tweet-based papers.
- Inconsistent metrics. F1 is the harmonic mean of precision and recall; with precision 91.44 and recall 89.63 it is about 90.5, not the reported 90.87. Recall also disagreed with the paper's own confusion matrix.
- Accuracy gaps (0.12 percent behind a transformer) mean little without cost data.

For SmartCity Accra forecasting: split by time (never random shuffle time series), fix preprocessing on the training window only, and report repeated runs.

## Related
- [Reviewing technical papers and checking reproducibility](paper-review-and-reproducibility.md)
