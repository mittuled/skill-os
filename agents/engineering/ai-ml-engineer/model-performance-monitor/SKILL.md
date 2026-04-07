---
name: model-performance-monitor
description: >
  This skill monitors deployed model performance including prediction quality,
  data drift, concept drift, and inference latency. Use when asked to set up model
  monitoring, investigate prediction degradation, or configure drift detection. Also
  consider when a model runs in production without observability. Suggest when the
  user deploys a model without monitoring.
department: engineering
agent: ai-ml-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../mlops-pipeline-builder/SKILL.md
  - ../model-evaluation-runner/SKILL.md
---

# model-performance-monitor

## Agent: AI/ML Engineer

L2 AI/ML engineer (Nx) responsible for feasibility assessment, model requirements, ML architecture design, model training, MLOps pipeline building, evaluation, and performance monitoring.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Monitors deployed model performance including prediction quality, data drift, concept drift, inference latency, and feature freshness in production.

## When to Use

- When a model is deployed to production and requires ongoing performance observability.
- When prediction quality appears to degrade based on downstream metric changes.
- When the input data distribution is expected to shift over time (seasonal patterns, user behavior changes).

## Workflow

1. **Monitoring Metric Definition**: Define monitoring metrics: prediction quality proxies (delayed ground truth labels, implicit feedback signals), input data distribution statistics (PSI, KL divergence, KS test), inference latency (p50, p95, p99), throughput, and error rates. Deliverable: monitoring metric catalog with threshold definitions.
2. **Data Drift Detection**: Implement statistical tests comparing production input distributions against training data distributions at the feature level. Configure Population Stability Index (PSI) or Kolmogorov-Smirnov tests with alerting thresholds. Deliverable: data drift detection pipeline with per-feature monitors.
3. **Concept Drift Detection**: Monitor prediction quality over time using delayed labels or proxy metrics. Detect when the relationship between inputs and outcomes shifts. Deliverable: concept drift detection with retraining trigger alerts.
4. **Latency and Throughput Monitoring**: Track inference latency percentiles and throughput against SLA targets. Monitor for latency spikes correlated with input complexity or model version changes. Deliverable: serving performance dashboard with SLA compliance tracking.
5. **Alerting and Escalation**: Configure tiered alerts: warning (approaching threshold), critical (threshold breached), and emergency (complete model failure). Define escalation paths and automated responses (traffic rerouting to fallback model, automatic retraining trigger). Deliverable: alert configuration with escalation playbook.

## Anti-Patterns

- **Monitoring accuracy only with delayed labels**: Relying solely on ground-truth labels that arrive days or weeks later without interim proxy metrics. *Why*: by the time delayed labels reveal degradation, the model has been serving bad predictions for the entire delay window.
- **Global drift detection only**: Monitoring aggregate input distributions without per-feature or per-segment breakdowns. *Why*: localized drift in a single critical feature can degrade predictions for a specific user segment while aggregate statistics appear normal.
- **Static thresholds**: Setting fixed alert thresholds without accounting for seasonal patterns or expected distribution shifts. *Why*: static thresholds cause false alerts during known seasonal changes and miss true drift during high-variance periods.

## Output

**On success**: Produces a model monitoring system comprising data drift detection, concept drift detection, latency monitoring, and alerting with escalation playbooks. Delivered as monitoring infrastructure configuration and dashboards.

**On failure**: Report which monitoring dimensions could not be implemented (e.g., no ground-truth label pipeline, insufficient baseline data for drift detection), what partial coverage exists, and recommended instrumentation to enable full monitoring.

## Related Skills

- [`mlops-pipeline-builder`](../mlops-pipeline-builder/SKILL.md) -- Integrates monitoring triggers into the retraining pipeline.
- [`model-evaluation-runner`](../model-evaluation-runner/SKILL.md) -- Provides baseline metrics that monitoring compares against.
