---
name: ai-feasibility-assessor
description: >
  This skill assesses whether an AI/ML approach is feasible for a given problem
  given data, compute, and time constraints. Use when asked to evaluate if ML is
  the right approach, assess data readiness, or estimate ML project viability. Also
  consider when stakeholders propose AI solutions without validating assumptions.
  Suggest when the user jumps to model training without a feasibility check.
department: engineering
agent: ai-ml-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../model-requirements-definer/SKILL.md
  - ../ml-architecture-designer/SKILL.md
---

# ai-feasibility-assessor

## Agent: AI/ML Engineer

L2 AI/ML engineer (Nx) responsible for feasibility assessment, model requirements, ML architecture design, model training, MLOps pipeline building, evaluation, and performance monitoring.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Assesses whether an AI/ML approach is feasible for a given problem given data availability, data quality, compute budget, latency constraints, and timeline.

## When to Use

- When a product team proposes an ML-powered feature and needs a viability assessment before committing resources.
- When available training data is uncertain in quality, volume, or label coverage.
- When the problem might be solvable with heuristics or rules and ML may be overkill.

## Workflow

1. **Problem Framing**: Clarify the prediction task, success criteria, and business impact. Determine if the problem is classification, regression, ranking, generation, or anomaly detection. Deliverable: problem statement with task type and success metrics.
2. **Data Readiness Assessment**: Audit available datasets for volume (minimum viable training size), label quality (noise rate, annotation consistency), feature coverage, and temporal relevance. Check for class imbalance and distribution shift. Deliverable: data readiness scorecard.
3. **Baseline Estimation**: Estimate performance of simple baselines (rule-based, heuristic, random, majority class) to establish the minimum bar ML must beat. Deliverable: baseline performance benchmarks.
4. **Compute and Latency Analysis**: Estimate training compute (GPU-hours), inference latency requirements (p50, p99), and serving infrastructure costs. Compare against budget constraints. Deliverable: compute cost estimate with infrastructure requirements.
5. **Risk and Timeline Assessment**: Identify risks (data drift, adversarial inputs, regulatory constraints on automated decisions) and estimate timeline to first model. Deliverable: feasibility verdict with risk register and timeline estimate.

## Anti-Patterns

- **ML for everything**: Recommending ML when a deterministic rule or lookup table solves the problem. *Why*: ML adds training infrastructure, monitoring overhead, and interpretability challenges that deterministic solutions avoid entirely.
- **Ignoring data quality**: Declaring feasibility based on data volume alone without assessing label quality or distribution. *Why*: a large dataset with noisy labels or severe class imbalance produces a model that fails in production despite passing offline metrics.
- **Optimistic timeline estimates**: Projecting timelines based on model training alone, excluding data preparation, feature engineering, evaluation, and MLOps setup. *Why*: data preparation and MLOps typically consume 60-80% of ML project effort.

## Output

**On success**: Produces a feasibility assessment containing the problem framing, data readiness scorecard, baseline benchmarks, compute estimates, and a go/no-go verdict with conditions. Delivered as a decision document to stakeholders.

**On failure**: Report which feasibility dimension blocked (e.g., insufficient labeled data, prohibitive compute costs), what alternatives were considered (heuristics, simpler models), and recommended steps to improve feasibility.

## Related Skills

- [`model-requirements-definer`](../model-requirements-definer/SKILL.md) -- Defines detailed model requirements once feasibility is confirmed.
- [`ml-architecture-designer`](../ml-architecture-designer/SKILL.md) -- Designs the ML system architecture after feasibility approval.
