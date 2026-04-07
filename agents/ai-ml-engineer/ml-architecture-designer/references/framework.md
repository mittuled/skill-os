# Framework: ML System Architecture Design

Defines the structural components and design decisions for production ML systems, covering feature engineering, training infrastructure, model serving, and monitoring integration.

## ML System Architecture Layers

```
┌─────────────────────────────────────────────────┐
│               Business Applications              │
├─────────────────────────────────────────────────┤
│             Model Serving Layer                  │
│   (Real-time inference / Batch prediction)       │
├─────────────────────────────────────────────────┤
│            Model Registry & Lineage              │
├─────────────────────────────────────────────────┤
│      Training Infrastructure & Experiments       │
├─────────────────────────────────────────────────┤
│              Feature Store Layer                 │
│     (Offline features / Online features)         │
├─────────────────────────────────────────────────┤
│            Data Sources & Pipelines              │
└─────────────────────────────────────────────────┘
```

## Feature Architecture Decision Matrix

### Feature Store Selection

| Requirement | Recommended Option | Rationale |
|-------------|-------------------|-----------|
| Low-latency online features (< 10ms) | Feast (Redis backend) or Tecton | Redis-backed online store provides single-digit ms lookups |
| High-throughput batch features only | Custom feature pipeline + S3/GCS | No real-time requirement; managed store overhead not justified |
| Multi-team feature reuse at scale | Tecton or Vertex AI Feature Store | Platform manages sharing, versioning, and access control |
| Point-in-time correctness required | Feast or Tecton | Critical for avoiding training-serving skew in time-series use cases |

### Feature Pipeline Pattern

| Pattern | When to Use | Tradeoff |
|---------|-------------|---------|
| Lambda Architecture (batch + streaming) | Features needed in both historical training and real-time serving | High complexity; ensures training-serving parity |
| Kappa Architecture (streaming only) | All features can be computed from an event stream | Simpler; requires full stream replay for retraining |
| Batch-only | Latency tolerance > feature computation window | Lowest complexity; risk of stale features |

**Training-serving parity rule**: The same feature computation code must run in both training (offline) and serving (online). Separate implementations for each context are the primary cause of training-serving skew.

## Training Infrastructure Decision Matrix

| Requirement | Option | Notes |
|-------------|--------|-------|
| Managed training, no GPU ops team | Vertex AI Training / SageMaker | Reduced operational overhead; higher cost at scale |
| GPU cluster control required | Kubernetes + GPU nodes | Full control; requires MLOps operator expertise |
| Cost-optimized large-scale training | Spot/preemptible instances with checkpointing | 60–80% cost savings; requires fault-tolerant training code |
| Distributed training (data parallelism) | PyTorch DDP / Horovod | Standard for large model training |
| Hyperparameter tuning | Optuna (Bayesian) / Vertex AI Vizier / Ray Tune | Bayesian preferred over grid for high-dimensional spaces |

### Experiment Tracking Requirements

Every training run must log:

| Category | Required Fields |
|----------|----------------|
| Parameters | model_type, all hyperparameters, random_seed, training_data_version |
| Metrics | all evaluation metrics at best epoch, learning curve (loss per epoch) |
| Artifacts | model checkpoint, feature schema, preprocessing pipeline |
| Environment | Python version, dependency hash, GPU type, training duration |

Recommended tools: MLflow (self-hosted or managed), Weights & Biases

## Serving Architecture Decision Matrix

### Model Server Selection

| Server | Best For | Language Support |
|--------|----------|-----------------|
| TorchServe | PyTorch models, custom handlers | Python |
| Triton Inference Server | Multi-framework, GPU optimization, high throughput | Framework-agnostic |
| TF Serving | TensorFlow models, simple deployment | Python/TensorFlow |
| BentoML | Custom business logic, ensemble serving | Python (any framework) |
| Ray Serve | Dynamic batching, complex pipelines, Python-first | Python |

### Serving Topology

| Pattern | Use Case | Rollback Speed |
|---------|----------|---------------|
| Canary (5% → 25% → 100%) | Standard production rollout | Instant — reduce canary to 0% |
| Shadow mode | High-stakes (medical, legal, financial) | N/A — shadow receives no production traffic |
| A/B test | Model comparison with statistical significance | Instant per variant |
| Blue-green | Batch prediction replacement | Switch DNS/load balancer |

**Latency budget allocation** (for synchronous serving):

```
Total request budget: 200ms
  ├── Feature retrieval: 20ms (10%)
  ├── Preprocessing: 10ms (5%)
  ├── Model inference: 150ms (75%)
  └── Response serialization: 20ms (10%)
```

## Monitoring Integration Design

| Monitoring Dimension | Metric | Collection Method |
|---------------------|--------|-----------------|
| Input data drift | PSI per feature | Batch statistical tests, hourly |
| Prediction distribution shift | Prediction histogram vs. baseline | Real-time aggregation |
| Concept drift (if labels available) | Rolling accuracy / F1 | Delayed label pipeline |
| Inference latency | p50, p99 histograms | Prometheus histogram metric |
| Feature freshness | Max feature age in each request | Feature store metadata |
| Model staleness | Days since last retraining | Model registry metadata |

## Architecture Review Checklist

Before submitting architecture for stakeholder approval:

- [ ] Training-serving feature parity guaranteed by shared computation code
- [ ] Single point of failure analysis completed; redundancy defined for critical components
- [ ] Latency budget allocated per serving path and verified against model requirements
- [ ] Feature freshness requirements met by chosen feature architecture
- [ ] Monitoring covers all four dimensions: data drift, concept drift, latency, feature freshness
- [ ] Rollback mechanism defined with target RTO (recovery time objective)
- [ ] Infrastructure cost estimate produced for training and serving
- [ ] Stakeholders (engineering + product) have reviewed and approved
