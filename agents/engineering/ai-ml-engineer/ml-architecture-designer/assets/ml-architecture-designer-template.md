# ML System Architecture Document

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [AI/ML Engineer name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | ml-architecture-designer |
| System | [ML system name and use case] |
| Stakeholders | [Engineering Lead, Product Lead, Data Lead] |

## Executive Summary

[2-3 sentences describing the ML system, the key architectural decisions made, and the primary tradeoff.
GUIDANCE: Lead with the system purpose and the most important design decision. Example: "This document defines the architecture for a real-time fraud detection system serving 10,000 predictions/second at p99 ≤ 50ms. The primary architectural decision is a Lambda architecture feature store combining batch-computed behavioral features (T-24h) with streaming transaction features (T-30s). Training-serving parity is guaranteed through a shared feature computation library."]

## Requirements Synthesis

[Summary of requirements driving architecture decisions.

GUIDANCE:
- Good: Include specific numbers — latency budgets, throughput, accuracy thresholds, uptime SLA
- Bad: "The system needs to be fast, accurate, and reliable"]

| Requirement Type | Requirement | Source |
|-----------------|-------------|--------|
| Accuracy | [e.g., F1 ≥ 0.85 on held-out test set] | [Model requirements doc] |
| Latency | [e.g., p99 inference ≤ 50ms] | [Model requirements doc] |
| Throughput | [e.g., ≥ 10,000 predictions/second] | [Capacity planning doc] |
| Feature freshness | [e.g., Transaction features ≤ 30 seconds old] | [Product spec] |
| Availability | [e.g., 99.9% uptime] | [SLO document] |
| Compliance | [e.g., GDPR — no PII in model inputs] | [Legal review] |

## Feature Architecture

[Design of the feature engineering layer.

GUIDANCE:
- Good: Specify online vs. offline split, point-in-time correctness guarantees, and the shared computation mechanism that prevents training-serving skew
- Bad: "Features will be computed and served from a feature store"]

### Feature Layer Design

| Feature Group | Computation Pattern | Storage | Max Staleness | Parity Guarantee |
|--------------|---------------------|---------|--------------|-----------------|
| [e.g., User behavioral features] | [Batch — nightly Spark job] | [Feast offline store (S3)] | [24 hours] | [Shared PySpark transform library] |
| [e.g., Transaction features] | [Streaming — Flink or Spark Streaming] | [Feast online store (Redis)] | [30 seconds] | [Shared feature schema + validation] |

### Point-in-Time Correctness

[Describe how training features are joined at the correct point in time to prevent data leakage.

GUIDANCE: Specify the join key (entity ID + timestamp) and the maximum lookback window.]

## Training Infrastructure

[Training infrastructure components and configuration.

GUIDANCE:
- Good: Specify managed vs. self-hosted decision with rationale, experiment tracking system, and distributed training configuration
- Bad: "We will train on GPUs using a managed service"]

| Component | Selection | Rationale |
|-----------|-----------|-----------|
| Training platform | [e.g., Vertex AI Custom Training] | [e.g., Managed GPU fleet; no ops overhead] |
| Experiment tracking | [e.g., MLflow on GKE] | [e.g., Self-hosted for cost; full metadata control] |
| Hyperparameter tuning | [e.g., Optuna Bayesian search] | [e.g., 40% fewer trials vs. grid search] |
| Distributed training | [e.g., PyTorch DDP on 4× A100] | [e.g., Data parallelism sufficient; model fits in single GPU] |

## Serving Architecture

[Model serving design including server selection, deployment pattern, and latency allocation.

GUIDANCE:
- Good: Include latency budget breakdown and specific rollback mechanism
- Bad: "The model will be served via an API"]

### Serving Stack

| Component | Selection | Configuration |
|-----------|-----------|--------------|
| Model server | [e.g., Triton Inference Server] | [e.g., TensorRT optimization; dynamic batching max_batch_size=32] |
| Deployment pattern | [e.g., Canary: 5% → 25% → 100%] | [Bake time: 15min / 1h / 24h] |
| Rollback trigger | [e.g., p99 > 50ms or error rate > 1%] | [Automatic traffic revert to previous version] |
| A/B infrastructure | [e.g., None / Feature flags / Traffic split] | |

### Latency Budget Allocation

| Component | Budget | Notes |
|-----------|--------|-------|
| Feature retrieval | [e.g., 10ms] | [Redis online store lookup] |
| Preprocessing | [e.g., 5ms] | [Normalization + encoding] |
| Model inference | [e.g., 30ms] | [Triton + TensorRT] |
| Response serialization | [e.g., 5ms] | |
| **Total** | **[50ms p99]** | |

## Monitoring Design

[Monitoring coverage across all four dimensions.

GUIDANCE:
- Good: Specify the exact drift detection method, thresholds, and retraining trigger conditions
- Bad: "We will monitor the model in production"]

| Dimension | Method | Threshold | Alert | Automated Response |
|-----------|--------|-----------|-------|-------------------|
| Data drift | [PSI per feature] | [PSI > 0.20] | [Critical] | [Trigger retraining review] |
| Concept drift | [Rolling F1, 7-day window] | [F1 drops > 5%] | [Critical] | [Trigger retraining pipeline] |
| Latency | [p99 Prometheus histogram] | [> SLA budget] | [Page on-call] | [Traffic shift to fallback] |
| Feature freshness | [Max feature age per request] | [> staleness SLA] | [Warning] | [Alert data engineering] |

## Recommendations

[Prioritized recommendations based on architecture review findings.

GUIDANCE: Focus on single points of failure, cost tradeoffs, and risks to latency or accuracy SLOs.]

- **P1**: [Critical architectural risk or single point of failure that needs immediate resolution]
- **P2**: [Important improvement for production readiness]
- **P3**: [Long-term scalability or cost optimization]

## Appendices

### A. Architecture Decision Records

[Record each significant architectural decision with alternatives considered and reasons for rejection.]

| Decision | Options Considered | Choice | Rationale |
|----------|-------------------|--------|-----------|
| [e.g., Feature store] | [Option A, Option B, Option C] | [Choice] | [Key reason] |

### B. Infrastructure Cost Estimate

[Monthly cost estimate for training and serving at target scale.]

| Component | Unit Cost | Volume | Monthly Estimate |
|-----------|----------|--------|-----------------|
| Training (GPU-hours/month) | | | |
| Feature store (storage + compute) | | | |
| Serving infrastructure | | | |
| Monitoring + logging | | | |
| **Total** | | | **[$ estimate]** |
