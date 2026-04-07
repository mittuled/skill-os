# A/B Experiment Results: Onboarding Flow v2 vs v1

| Field | Value |
|-------|-------|
| Date | 2026-03-31 |
| Analytics Lead | Analytics Lead |
| Experiment | Onboarding Flow v2 vs v1 |
| Days Running | 10 of 14 minimum |
| Confidence Level | 95% |
| Verdict | WAIT — Significant but peeking bias risk; continue until minimum duration |
| Skill | statistical-significance-tracker |

## Results Summary

| Metric | Control | Treatment | Difference |
|--------|---------|-----------|-----------|
| Sample size | 1,850 | 1,823 | — |
| Conversions | 629 | 712 | +83 |
| Conversion rate | 34.0% | 39.1% | +5.0 pp |
| **Relative lift** | — | — | **+14.7%** |

## Statistical Analysis

| Metric | Value |
|--------|-------|
| Z-score | 3.12 |
| P-value | 0.0018 |
| Is significant (p < 0.05) | Yes |
| Sample Ratio Mismatch | No (actual ratio: 49.6% vs expected 50%) |

## Flags

| Flag | Status | Detail |
|------|--------|--------|
| Statistical significance | REACHED | p = 0.0018 (< 0.05) |
| Sample Ratio Mismatch | CLEAR | No assignment bias detected |
| Peeking bias risk | FLAGGED | Test is significant but only 10 of 14 minimum days have elapsed |

## Why Wait Despite Significance?

Early stopping due to peeking inflates Type I error rate (false positives). The 95% confidence level assumes the test runs for the pre-specified minimum duration. Stopping at day 10 of 14 means the true confidence is lower than stated. Continue the experiment for 4 more days to validate the result is stable.

## Decision Framework

| Condition | Action |
|-----------|--------|
| Day 14 reached + p < 0.05 + lift > 0 | SHIP treatment |
| Day 14 reached + not significant | CONTINUE for 7 more days or end as inconclusive |
| SRM detected at any point | PAUSE and investigate assignment mechanism |
| Lift turns negative | Consider early stop for harm |
