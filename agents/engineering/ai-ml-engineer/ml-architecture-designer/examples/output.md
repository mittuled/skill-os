# ML System Architecture: Real-Time Fraud Detection System

| Field | Value |
|-------|-------|
| Date | 2026-03-31 |
| Engineer | AI/ML Engineer |
| System | Real-Time Fraud Detection System |
| Task Type | Classification |
| Serving Pattern | Real-Time (< 50ms) |
| Skill | ml-architecture-designer |

## Executive Summary

This architecture supports real-time fraud scoring at sub-50ms latency using an online feature store fed by streaming ingestion. The design separates offline training infrastructure from online serving to prevent training-serving skew — the most common production failure mode in real-time ML systems.

## Architecture Overview

```
Transaction Stream → Kafka → Flink (feature transforms) → Redis (online store)
                                                               ↓
User / Device / Merchant DBs ──────────────────────────→ Feature Join
                                                               ↓
                                                    Model Server (TorchServe)
                                                               ↓
                                                     Fraud Score (< 50ms)
```

## Component Specifications

### Feature Pipeline

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Offline store | BigQuery | Training feature materialisation |
| Online store | Redis (< 5ms lookup) | Low-latency feature serving |
| Streaming transforms | Apache Flink | Real-time feature computation from transaction stream |
| Offline transforms | dbt | Point-in-time correct training features |
| Feature sources | transaction_stream, user_history_db, device_fingerprint_service, merchant_metadata_db | |

**Feature store note**: Online feature store with streaming ingestion (Kafka → Redis/DynamoDB) required for sub-50ms serving.

### Training Infrastructure

| Component | Choice | Rationale |
|-----------|--------|-----------|
| Orchestration | Kubeflow Pipelines | Reproducible ML workflows with dependency management |
| Compute | GPU cluster (A100s, spot instances) | Cost-optimised training for gradient boosted and neural models |
| Experiment tracking | MLflow | Local + cloud tracking with artifact storage |
| Model registry | MLflow Registry (staging → production stages) | Gated promotion prevents unvalidated models reaching production |
| Data versioning | Delta Lake | Time-travel queries for training set reconstruction |

### Serving Infrastructure

| Attribute | Value |
|-----------|-------|
| Pattern | Real-time inference |
| Infrastructure | TorchServe model server |
| Latency target | < 50ms p99 |
| Caching | Feature cache in Redis (required) |
| Scaling | Horizontal pod autoscaling on TPS |

### Monitoring

| Dimension | Implementation |
|-----------|---------------|
| Prediction logging | All predictions + input features logged to S3/GCS |
| Drift detection | PSI and KS tests on feature distributions, run weekly |
| Performance tracking | Fraud rate correlation with model scores, reviewed daily |
| Alerting | PagerDuty alert when AUC-ROC drops > 3% or PSI > 0.2 |

## Architecture Decisions

1. **Separate offline and online feature paths** — prevents training-serving skew, the #1 silent failure in real-time ML
2. **Streaming ingestion to Redis** — ensures feature freshness < 1s for transaction velocity features
3. **Model registry gates all promotions** — no direct-to-production deployments allowed
4. **Shadow mode deployment** — run new model in parallel for 48 hours before traffic cutover

## Risk Register

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| Training-serving skew | HIGH | Shared feature transform library used by both offline dbt and online Flink |
| Feature staleness during Kafka lag | MEDIUM | Circuit breaker falls back to offline features; alert on consumer lag > 5s |
| Model version pinning failure | LOW | Immutable model artefacts in registry; canary deployments with rollback |
