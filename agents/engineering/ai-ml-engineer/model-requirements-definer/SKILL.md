---
name: model-requirements-definer
description: >
  This skill defines the requirements for an ML model including input/output schema,
  accuracy targets, latency budgets, and fairness constraints. Use when asked to
  specify model requirements, define ML acceptance criteria, or translate business
  needs into model constraints. Also consider when a model is trained without
  documented requirements. Suggest when the user starts model development without
  success criteria.
department: engineering
agent: ai-ml-engineer
version: 1.0.0
complexity: simple
related-skills:
  - ../ai-feasibility-assessor/SKILL.md
  - ../model-evaluation-runner/SKILL.md
---

# model-requirements-definer

## Agent: AI/ML Engineer

L2 AI/ML engineer (Nx) responsible for feasibility assessment, model requirements, ML architecture design, model training, MLOps pipeline building, evaluation, and performance monitoring.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Defines the requirements for an ML model including input/output schema, accuracy targets, latency budgets, fairness constraints, and operational boundaries.

## When to Use

- When a new ML project begins and model success criteria have not been formalized.
- When product stakeholders have business objectives that need translation into measurable model metrics.
- When an existing model lacks documented requirements and needs retroactive specification for governance.

## Workflow

1. **Business Objective Translation**: Convert business goals (e.g., "reduce false positives by 30%") into measurable model metrics (e.g., "precision >= 0.85 at recall >= 0.70"). Deliverable: metric mapping document linking business objectives to model metrics.
2. **Input/Output Schema Definition**: Define the model's input feature schema (feature names, types, ranges, nullability) and output schema (prediction type, confidence scores, explanation fields). Deliverable: I/O schema specification.
3. **Performance Constraints**: Specify latency budgets (p50, p99 inference time), throughput requirements (predictions per second), model size limits (for edge deployment), and availability SLA. Deliverable: performance constraint document.
4. **Fairness and Safety Constraints**: Define fairness requirements (maximum disparity across protected groups), safety boundaries (confidence thresholds for fallback to human review), and regulatory constraints (explainability requirements, right to explanation). Deliverable: fairness and safety specification.

## Anti-Patterns

- **Undefined success criteria**: Starting model training without quantitative accuracy targets. *Why*: without targets, there is no objective basis for promotion decisions, and teams iterate indefinitely without convergence.
- **Latency as afterthought**: Defining accuracy requirements without latency budgets. *Why*: the most accurate model may be too slow for the serving context, forcing a last-minute architecture change or accuracy compromise.

## Output

**On success**: Produces a model requirements document containing the business-to-metric mapping, I/O schema, performance constraints, and fairness/safety specifications. Delivered to the ML architecture and training teams.

**On failure**: Report which requirements could not be defined (e.g., business objectives too vague, no fairness policy), what assumptions were made, and what stakeholder decisions are needed.

## Related Skills

- [`ai-feasibility-assessor`](../ai-feasibility-assessor/SKILL.md) -- Feasibility assessment that precedes or informs requirement definition.
- [`model-evaluation-runner`](../model-evaluation-runner/SKILL.md) -- Evaluates models against the requirements defined here.
