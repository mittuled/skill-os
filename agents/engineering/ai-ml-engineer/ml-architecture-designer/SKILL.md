---
name: ml-architecture-designer
description: >
  This skill designs the ML system architecture including feature engineering,
  training infrastructure, model serving, and monitoring. Use when asked to architect
  an ML system, design a feature store, or plan model serving infrastructure. Also
  consider when an ML project moves from prototype to production. Suggest when the
  user trains models without a serving architecture plan.
department: engineering
agent: ai-ml-engineer
version: 1.0.0
complexity: complex
related-skills:
  - ../ai-feasibility-assessor/SKILL.md
  - ../mlops-pipeline-builder/SKILL.md
  - ../model-trainer/SKILL.md
---

# ml-architecture-designer

## Agent: AI/ML Engineer

L2 AI/ML engineer (Nx) responsible for feasibility assessment, model requirements, ML architecture design, model training, MLOps pipeline building, evaluation, and performance monitoring.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Designs the ML system architecture including feature engineering pipelines, feature stores, training infrastructure, model serving topology, and monitoring integration.

## When to Use

- When an ML project moves from feasibility to implementation and requires a system design.
- When an existing ML system needs re-architecture for scale, latency, or reliability improvements.
- When multiple models share features and a unified feature engineering layer is needed.

## Workflow

1. **Requirements Synthesis**: Consolidate model requirements (latency budgets, throughput targets, accuracy thresholds), data requirements (feature freshness, volume), and operational requirements (uptime SLA, rollback speed). Deliverable: ML system requirements document.
2. **Feature Architecture**: Design the feature engineering layer: offline feature computation (batch), online feature serving (low-latency), feature store selection (Feast, Tecton, or custom), and feature versioning strategy. Define the feature schema and point-in-time correctness guarantees. Deliverable: feature architecture document with schema definitions.
3. **Training Infrastructure Design**: Select training infrastructure (managed services like SageMaker/Vertex AI vs. self-hosted Kubernetes + GPUs), define experiment tracking (MLflow, W&B), hyperparameter tuning strategy, and distributed training topology. Deliverable: training infrastructure specification.
4. **Serving Architecture Design**: Design the model serving layer: real-time inference (model server selection: TorchServe, Triton, TFServing), batch prediction, A/B testing infrastructure, shadow deployment, canary rollout, and model versioning. Define latency budgets per serving path. Deliverable: serving architecture document with latency guarantees.
5. **Monitoring Integration Design**: Design monitoring for data drift (input distribution shifts), concept drift (prediction quality degradation), feature freshness, inference latency, and model staleness. Define alerting thresholds and retraining triggers. Deliverable: monitoring architecture with alert definitions.
6. **Architecture Review**: Walk through the complete ML architecture with engineering and product stakeholders. Validate against requirements and identify single points of failure. Deliverable: approved ML architecture document.

## Anti-Patterns

- **Training-serving skew**: Designing separate feature computation for training (offline) and serving (online) without parity guarantees. *Why*: feature computation differences between training and serving cause silent accuracy degradation that is extremely difficult to debug.
- **Monolithic model server**: Deploying all models through a single serving instance without isolation. *Why*: a single model's latency spike or crash takes down all models, and scaling is coarse-grained.
- **Ignoring feature freshness requirements**: Serving stale features from a batch-computed feature store when the use case requires real-time features. *Why*: stale features degrade prediction quality for time-sensitive use cases (fraud detection, recommendations) without any visible error signal.

## Output

**On success**: Produces a complete ML system architecture document containing feature architecture, training infrastructure specification, serving architecture, monitoring design, and stakeholder approval. Delivered as a versioned design artifact.

**On failure**: Report which architecture dimension could not be designed (e.g., conflicting latency and cost requirements, unavailable infrastructure), what partial design exists, and recommended tradeoff decisions for stakeholders.

## Related Skills

- [`ai-feasibility-assessor`](../ai-feasibility-assessor/SKILL.md) -- Provides the feasibility assessment that precedes architecture design.
- [`mlops-pipeline-builder`](../mlops-pipeline-builder/SKILL.md) -- Implements the MLOps pipelines specified in this architecture.
- [`model-trainer`](../model-trainer/SKILL.md) -- Uses the training infrastructure designed here.
