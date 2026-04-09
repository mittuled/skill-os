---
name: technical-feasibility-check
description: >
  This skill assesses whether a proposed feature or system is technically feasible within
  constraints. Use when asked to evaluate if something can be built, estimate technical risk,
  or validate assumptions before committing resources. Also consider when a product proposal
  relies on unproven technology. Suggest when stakeholders are about to greenlight a feature
  without engineering validation.
department: engineering
agent: tech-architect
version: 1.0.0
complexity: medium
related-skills:
  - ../../../engineering/tech-architect/architecture-designer/SKILL.md
  - ../../../engineering/tech-architect/design-feasibility-reviewer/SKILL.md
  - ../../vp-engineering/architecture-reviewer/SKILL.md
  - ../api-contract-definer/SKILL.md
  - ../moat-analyzer-tech/SKILL.md
triggers:
  - "check technical feasibility"
  - "technical feasibility"
  - "can we build this"
  - "tech feasibility assessment"
  - "feasibility analysis"
---

# technical-feasibility-check

## Agent: Tech Architect

L2 technical architect (1x) responsible for feasibility assessment, system design, API contract definition, and infrastructure planning. Ensures technical decisions support product goals and scale requirements.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Assesses whether a proposed feature or system is technically feasible given current technology, team capabilities, timeline, and infrastructure constraints.

## When to Use

- When a new feature proposal arrives from product and engineering needs to confirm it can be built within the stated constraints.
- When a project depends on an unproven technology, third-party API, or novel architecture pattern that carries execution risk.
- When leadership asks for a go/no-go recommendation before allocating engineering resources to a multi-sprint initiative.

## Workflow

1. **Decompose the proposal**: Break the feature or system into its core technical components. Identify which parts are well-understood and which carry uncertainty. Deliverable: component breakdown with risk annotations.
2. **Assess constraints**: Evaluate timeline, team skill set, infrastructure limits, third-party dependencies, and regulatory requirements. Deliverable: constraint matrix.
3. **Identify technical risks**: For each uncertain component, document the specific risk (e.g., latency, data volume, API limitations) and its potential impact on delivery. Deliverable: risk register.
4. **Prototype or research critical unknowns**: For high-risk components, conduct a time-boxed spike, proof-of-concept, or vendor evaluation. Deliverable: spike findings or PoC results.
5. **Render verdict**: Produce a feasibility assessment with a clear recommendation (feasible, feasible with caveats, or not feasible) supported by evidence. Deliverable: feasibility report with go/no-go recommendation.

## Anti-Patterns

- **Gut-feel feasibility**: Declaring something feasible or infeasible based on intuition without investigating unknowns. *Why*: unchecked assumptions create false confidence or unnecessary pessimism, both of which waste resources.
- **Feasibility without constraints**: Assessing technical possibility in a vacuum without considering timeline, team, or cost. *Why*: anything is technically possible with infinite time and money; feasibility is only meaningful relative to actual constraints.
- **Skipping the spike**: Approving a risky approach without prototyping because the team is eager to start. *Why*: discovering infeasibility mid-sprint costs far more than a two-day spike upfront.

## Output

**On success**: Produces a feasibility report containing the component breakdown, constraint matrix, risk register, spike findings (if applicable), and a clear go/no-go recommendation. Delivered to product and engineering leadership.

**On failure**: Report which components could not be assessed (e.g., unavailable third-party documentation, unclear requirements), what information is missing, and recommended steps to complete the assessment.

## Related Skills

- [`architecture-designer`](../../../engineering/tech-architect/architecture-designer/SKILL.md) -- feasibility checks inform and constrain the architecture design that follows a go decision.
- [`design-feasibility-reviewer`](../../../engineering/tech-architect/design-feasibility-reviewer/SKILL.md) -- design feasibility reviews complement technical checks by validating UX and interaction assumptions.
