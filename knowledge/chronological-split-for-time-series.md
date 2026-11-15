---
title: Split time-series data by time (e.g. first 80% train), never by random shuffle
tags: [lab, ml]
source: Lab 13 (week13_lab_Students) Part C
---

The lab's training script adds hour-of-day and two lag features, drops NaNs, trains on the first 80% of rows and tests on the last 20%, with a comment that time-series data must never be random-shuffled (shuffling leaks the future into training).

## Related
- [A GradientBoostingRegressor with hour, lag_1 and lag_2 is the lab forecasting starter](gradient-boosted-lag-feature-forecast.md)
- [Beat "next reading equals last reading" (or a z-score rule) before any model ships](naive-baseline-before-model.md)
