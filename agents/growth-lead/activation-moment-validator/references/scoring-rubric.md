# Scoring Rubric: activation-moment-validator

Evaluates whether a defined activation signal is a statistically valid and practically meaningful predictor of long-term user retention.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Retention Lift Magnitude | 35% | Size of Day 30 retention gap between activated and non-activated cohorts |
| 2 | Statistical Significance | 25% | Strength of evidence that the observed lift is not due to chance |
| 3 | Cohort Sample Adequacy | 20% | Minimum user count in each cohort for reliable inference |
| 4 | Signal Specificity | 10% | Degree to which the signal discriminates between retained and churned users (not too easy, not too hard) |
| 5 | Temporal Stability | 10% | Consistency of retention lift across different signup cohorts over time |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | D30 retention lift ≥ 25pp, p < 0.001, stable across ≥ 6 cohorts | Adopt as canonical activation metric; align all onboarding experiments to this signal |
| A | 8.0 – 8.9 | Strong | D30 lift ≥ 15pp, p < 0.01, stable across ≥ 4 cohorts | Adopt as activation metric; schedule quarterly revalidation |
| B | 7.0 – 7.9 | Good | D30 lift 10–15pp, p < 0.05, ≥ 3 cohorts tested | Adopt provisionally; monitor for cohort drift and revalidate in 60 days |
| C | 5.0 – 6.9 | Adequate | D30 lift 5–10pp or marginal significance; limited cohort evidence | Use as secondary signal only; continue candidate testing to find stronger predictor |
| D | 3.0 – 4.9 | Weak | D30 lift < 5pp or p > 0.05; insufficient cohort size | Do not adopt; run alternative candidate analysis |
| F | 0.0 – 2.9 | Failing | No measurable lift; signal may be inversely correlated or unanalysable | Reject; redefine activation signal from scratch using qualitative user research |

## Signal Tables

### Retention Lift Magnitude

| Score | Evidence |
|-------|----------|
| 9-10 | Activated cohort has Day 30 retention ≥ 25 percentage points above non-activated cohort; Day 90 lift also ≥ 20pp; survival curves visually diverge sharply and maintain separation |
| 7-8 | D30 retention lift 15–25pp; D90 lift ≥ 10pp; survival curves show clear separation throughout the observation window |
| 5-6 | D30 retention lift 5–15pp; D90 lift < 10pp; curves separate initially but converge by Day 60 |
| 3-4 | D30 retention lift < 5pp; curves are nearly parallel; signal has minimal discriminative value |
| 0-2 | No lift or negative lift (non-activated users retain at same or higher rate); signal is not predictive of retention |

### Statistical Significance

| Score | Evidence |
|-------|----------|
| 9-10 | Log-rank test p < 0.001; 95% confidence interval for D30 lift lower bound ≥ 10pp; chi-squared test on Day 30 activation rates confirms significance |
| 7-8 | Log-rank test p < 0.01; 95% CI lower bound for D30 lift ≥ 5pp; result replicable on held-out cohort |
| 5-6 | Log-rank test p < 0.05; 95% CI includes values as low as 2pp lift; borderline significance |
| 3-4 | Log-rank test p 0.05–0.15; result not consistently replicable across cohorts |
| 0-2 | p > 0.15; no evidence of statistical significance; result indistinguishable from noise |

### Cohort Sample Adequacy

| Score | Evidence |
|-------|----------|
| 9-10 | Each cohort (activated and non-activated) contains ≥ 5,000 users; power analysis confirms ≥ 90% power to detect 10pp lift |
| 7-8 | Each cohort ≥ 1,000 users; power analysis confirms ≥ 80% power to detect 10pp lift |
| 5-6 | Each cohort 500–1,000 users; 80% power only for detecting lifts ≥ 15pp |
| 3-4 | One or both cohorts 100–500 users; analysis underpowered for all but very large effects |
| 0-2 | Cohorts < 100 users; analysis is statistically unreliable; confidence intervals span more than 30pp |

### Signal Specificity

| Score | Evidence |
|-------|----------|
| 9-10 | 20–50% of users complete the activation action; action is product-core (not trivial login, not advanced power-feature); retained users complete it at 3× rate of churned users |
| 7-8 | 15–60% activation rate; action correlates directly with the core value proposition; 2–3× completion rate differential between retained and churned |
| 5-6 | Activation rate < 10% (too hard) or > 70% (too easy); action is adjacent to core value but not perfectly aligned |
| 3-4 | Activation rate < 5% or > 85%; action is trivial (e.g., email verification) or advanced (power-feature) |
| 0-2 | Activation rate < 2% or > 95%; signal has no discriminative power regardless of retention correlation |

### Temporal Stability

| Score | Evidence |
|-------|----------|
| 9-10 | Retention lift is consistent (within ±5pp) across ≥ 6 consecutive monthly cohorts; no trend toward declining lift |
| 7-8 | Lift consistent within ±10pp across ≥ 4 cohorts; minor variance but no systematic trend |
| 5-6 | Lift tested on only 2–3 cohorts; or variance > 10pp but no clear declining trend |
| 3-4 | Lift tested on only 1 cohort; temporal stability unknown |
| 0-2 | Lift is declining across consecutive cohorts; signal is weakening over time suggesting product or user base changes |
