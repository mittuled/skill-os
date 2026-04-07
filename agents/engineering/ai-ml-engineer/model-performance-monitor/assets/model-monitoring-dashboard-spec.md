# Model Performance Monitoring Dashboard Spec: [Model Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | AI/ML Engineer |
| Model | [Model name and version] |
| Monitoring Tool | [Evidently / Arize / Grafana + Prometheus / WhyLabs] |
| Skill | model-performance-monitor |
| Alert Destination | [PagerDuty / Slack channel] |
| Status | [Spec / Implemented / Active] |

## Monitoring Objectives

[What this monitoring setup detects and prevents:]

1. **Performance drift**: Primary metric degrades from deployment baseline
2. **Data drift**: Input feature distributions shift from training distribution
3. **Prediction drift**: Output distribution shifts unexpectedly
4. **Infrastructure failure**: Inference latency or error rate exceeds SLO

## Dashboard Panels

### Panel 1: Model Performance (Primary Metric)

| Property | Value |
|----------|-------|
| Metric | [MAPE / Accuracy / F1 / Precision@K] |
| Granularity | [Hourly / Daily] |
| Aggregation | [Rolling 7-day average] |
| Display | [Time series line chart] |
| Reference line | [Deployment baseline value] |
| Alert threshold | [> X% worse than baseline triggers alert] |

### Panel 2: Prediction Volume

| Property | Value |
|----------|-------|
| Metric | `model_predictions_total{model, version}` |
| Granularity | [Hourly] |
| Display | [Time series + 7-day rolling average] |
| Alert threshold | [< 50% of expected volume = data pipeline failure] |

### Panel 3: Inference Latency

| Property | Value |
|----------|-------|
| Metrics | p50, p95, p99 latency |
| Granularity | [1-minute rolling] |
| Display | [Three time-series lines on same chart] |
| Alert thresholds | p99 > [X ms] = warning; p99 > [2×X ms] = critical |

### Panel 4: Error Rate

| Property | Value |
|----------|-------|
| Metric | `model_errors_total / model_requests_total` |
| Granularity | [5-minute rolling] |
| Display | [Percentage time series] |
| Alert threshold | [Error rate > 1%] |

### Panel 5: Feature Drift (PSI)

| Property | Value |
|----------|-------|
| Metric | PSI per top-N features vs. training baseline |
| Granularity | [Daily] |
| Display | [Heatmap: features × days, colored by PSI severity] |
| Color scale | Green (< 0.1) → Yellow (0.1–0.2) → Red (> 0.2) |
| Alert threshold | [Any feature PSI > 0.2 on 3 consecutive days] |

### Panel 6: Prediction Distribution

| Property | Value |
|----------|-------|
| Metric | Distribution of model output values vs. training distribution |
| Granularity | [Daily histogram] |
| Display | [Overlay histogram: current (blue) vs. baseline (grey)] |
| Alert threshold | [KS test p-value < 0.05 for 3 consecutive days] |

### Panel 7: Segment Performance (if applicable)

| Property | Value |
|----------|-------|
| Metric | Primary metric broken down by key segments |
| Segments | [User type / Geography / Product category / etc.] |
| Display | [Bar chart comparing segments vs. overall] |
| Alert threshold | [Any segment > 20% worse than overall metric] |

## Alert Definitions

| Alert | Condition | Severity | Recipient | Action |
|-------|-----------|----------|-----------|--------|
| Performance degradation | Primary metric degrades > [X%] from baseline for > [N] days | P1 | ML team + on-call | Investigate → potential rollback |
| Volume drop | Predictions < 50% of expected for > 1 hr | P1 | ML team | Check data pipeline |
| Latency spike | p99 > [X ms] for > 5 min | P2 | ML team + infra | Scale inference fleet |
| Feature drift | PSI > 0.2 on 3+ features simultaneously | P2 | ML team | Trigger retraining pipeline |
| Error rate | Model error rate > 1% for > 10 min | P1 | ML team | Check model server logs |
| Prediction distribution shift | KS p-value < 0.05 for 3 consecutive days | P2 | ML team | Root cause analysis |

## Retraining Triggers

| Trigger | Condition | Action |
|---------|-----------|--------|
| Performance trigger | Primary metric degrades > [X%] from baseline for > [N] days | Initiate retraining on updated dataset |
| Drift trigger | PSI > 0.2 on > 30% of top features | Initiate retraining |
| Calendar trigger | [Monthly / Quarterly] scheduled retraining | Initiate regardless of drift |
| Emergency trigger | P1 alert unresolved after [X hrs] | Emergency retrain or rollback |

## Data Pipeline Dependencies

| Dependency | Owner | Health Check | Impact of Failure |
|-----------|-------|-------------|------------------|
| [Feature store] | [Team] | [Endpoint or metric] | [Model inputs unavailable] |
| [Label pipeline] | [Team] | [Pipeline status] | [Cannot compute performance metrics] |
| [Inference logging] | [Team] | [Log volume metric] | [Monitoring blind — escalate immediately] |

## Baseline Reference Values

Record the baseline at deployment time:

| Metric | Baseline Value | Recorded At |
|--------|---------------|-------------|
| Primary metric | [X] | [YYYY-MM-DD deployment timestamp] |
| Prediction volume (daily) | [X predictions/day] | |
| p99 inference latency | [X ms] | |
| Feature distributions | [Stored in monitoring platform as reference dataset] | |
