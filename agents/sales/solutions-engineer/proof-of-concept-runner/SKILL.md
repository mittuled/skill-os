---
name: proof-of-concept-runner
description: >
  This skill designs and executes proof-of-concept engagements to demonstrate
  product value to technical buyers. Use when asked to run a POC, scope a
  technical evaluation, or design success criteria for a trial. Also consider
  when a deal is stalling at the evaluation stage without a concrete next step.
  Suggest when a prospect requests a POC without defined scope or success criteria.
department: sales
agent: solutions-engineer
version: 1.0.0
complexity: complex
related-skills:
  - ../technical-feasibility-for-sales/SKILL.md
  - ../../../sales/solutions-engineering-manager/solutions-playbook-builder/SKILL.md
---

# proof-of-concept-runner

## Agent: Solutions Engineer

L3 solutions engineer (Nx) responsible for technical feasibility assessment for sales opportunities and proof-of-concept execution.

Department ethos: [ideal-sales.md](../../../../departments/sales/ideal-sales.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Designs and executes proof-of-concept engagements to demonstrate product value to technical buyers with defined scope, success criteria, and decision timelines.

## When to Use

- When a qualified opportunity requires a technical evaluation before the buyer commits to purchase.
- When a deal is stalling at the evaluation stage and a structured POC can create momentum toward a decision.
- When the buyer's technical team needs hands-on validation that the product meets their specific requirements.

## Workflow

1. **POC Qualification**: Verify that the deal meets POC entry criteria: minimum ACV threshold, MEDDIC qualification score, confirmed executive sponsor, and committed decision timeline post-POC. Decline or defer POCs that do not meet criteria. Deliverable: POC qualification decision with rationale.
2. **Scope Definition**: Collaborate with the prospect's technical team to define POC scope: use cases to validate (maximum 3), integration requirements, data sets, environment specifications, and success metrics with measurable pass/fail thresholds. Get written agreement on scope from both the technical evaluator and the economic buyer. Deliverable: signed POC scope document.
3. **Environment Provisioning**: Set up the POC environment: dedicated instance or sandbox, sample data loaded, integrations configured, and access credentials distributed. Verify the environment is functional before the evaluation period begins. Deliverable: provisioned POC environment with validation checklist.
4. **Guided Evaluation**: Run the evaluation with structured touchpoints: kickoff session (orient the technical team), mid-point check-in (address blockers, validate progress), and final review (measure results against success criteria). Provide responsive technical support throughout. Deliverable: evaluation touchpoint records with blocker resolution log.
5. **Results Documentation**: Document POC results against each success metric. Produce a results summary that maps technical outcomes to business value. Present results to both the technical evaluator and the economic buyer in a joint session. Deliverable: POC results report with business value mapping.
6. **Decision Facilitation**: Use the results presentation to drive a go/no-go decision. If go, transition to commercial negotiation with the AE. If no-go, document the specific gaps and determine if they are addressable on a defined timeline. Deliverable: decision outcome with next steps.

## Anti-Patterns

- **POC without success criteria**: Starting a POC without agreed-upon, measurable success metrics. *Why*: without predefined criteria, the evaluation becomes open-ended; the prospect can always find a reason to delay a decision because there is no objective standard to evaluate against.
- **Scope creep acceptance**: Allowing the prospect to add use cases or requirements mid-POC beyond the agreed scope. *Why*: scope creep extends timelines, consumes SE capacity, and signals to the buyer that the POC is free consulting rather than a structured evaluation.
- **Technical-only results**: Presenting POC results in purely technical terms without connecting to business outcomes. *Why*: the technical evaluator may be convinced, but the economic buyer approves budget based on business impact; a technical-only report does not close the deal.
- **Running POCs for unqualified deals**: Investing SE time in POCs for deals that have not passed MEDDIC qualification. *Why*: POCs for unqualified deals have low conversion rates and consume the same SE capacity as qualified ones; the opportunity cost is high.

## Output

**On success**: Produces a POC qualification record, signed scope document, provisioned environment, evaluation records, results report with business value mapping, and decision outcome. Delivered as a completed POC that advances the deal to commercial negotiation.

**On failure**: Report what caused the POC to fail or stall (e.g., technical gap, integration blocker, prospect disengagement, scope creep), what was attempted to resolve it, and recommended next steps (product feedback, timeline for re-engagement, deal disqualification).

## Related Skills

- [`technical-feasibility-for-sales`](../technical-feasibility-for-sales/SKILL.md) -- Assesses feasibility before committing to a POC, reducing the risk of failed evaluations.
- [`solutions-playbook-builder`](../../../sales/solutions-engineering-manager/solutions-playbook-builder/SKILL.md) -- Provides the POC criteria and frameworks this skill executes against.
