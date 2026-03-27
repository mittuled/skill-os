---
name: design-feasibility-reviewer
description: >
  This skill reviews design proposals to confirm they are technically implementable.
  Use when asked to validate a UX design against technical constraints, assess whether
  a proposed interaction is feasible, or identify design elements that require custom
  engineering. Also consider when design proposals assume capabilities that do not
  exist. Suggest when the user is finalizing designs without engineering validation.
department: engineering
agent: tech-architect
version: 1.0.0
complexity: medium
related-skills:
  - ../technical-feasibility-check/SKILL.md
  - ../architecture-designer/SKILL.md
---

# design-feasibility-reviewer

## Agent: Tech Architect

L2 technical architect (1x) responsible for feasibility assessment, system design, API contract definition, and infrastructure planning. Ensures technical decisions support product goals and scale requirements.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Reviews design proposals to confirm they are technically implementable by evaluating interaction patterns, data requirements, performance implications, and platform constraints against the current technical architecture.

## When to Use

- When the design team delivers high-fidelity mockups and engineering needs to validate feasibility before committing to a sprint.
- When a design proposal includes novel interaction patterns (real-time collaboration, complex animations, offline-first) that may require significant custom engineering.
- When designs assume data availability, latency, or capabilities that have not been verified against the actual system.

## Workflow

1. **Design Decomposition**: Break the design into its technical components: data requirements per screen, state management needs, interaction patterns, animation specifications, and platform-specific behaviors. Deliverable: technical decomposition of the design.
2. **Constraint Mapping**: Map each component against current technical constraints: API data availability, latency budgets, device capabilities, accessibility requirements, and framework limitations. Deliverable: constraint analysis per design component.
3. **Feasibility Verdict**: For each component, classify as feasible (can be built as designed), feasible with modifications (achievable with specified design adjustments), or infeasible (cannot be built within constraints). Provide specific alternatives for modified and infeasible items. Deliverable: feasibility verdict with alternatives.
4. **Effort Estimation**: For feasible components, estimate the engineering effort and identify any components that require disproportionate effort relative to user value. Deliverable: effort estimates with value-effort flags.

## Anti-Patterns

- **Blanket rejection**: Declaring designs infeasible without investigating technical solutions or proposing alternatives. *Why*: engineering should enable design intent; rejecting without alternatives blocks progress and erodes cross-functional trust.
- **Late-stage review**: Reviewing designs after pixel-perfect mockups are complete rather than during wireframe stage. *Why*: early review catches infeasible patterns when design changes are cheap; late review forces expensive redesign.
- **Ignoring performance**: Approving designs that are technically possible but would create unacceptable performance (rendering large lists, complex real-time updates) without flagging the trade-off. *Why*: feasible does not mean performant; users experience performance, not technical possibility.

## Output

**On success**: Produces a feasibility assessment with technical decomposition, constraint analysis, feasibility verdicts, alternatives, and effort estimates. Delivered during the design review cycle.

**On failure**: Report which design components could not be assessed (missing technical information, unclear interaction specifications), what partial assessment was completed, and what additional information is needed from the design team.

## Related Skills

- [`technical-feasibility-check`](../technical-feasibility-check/SKILL.md) -- Technical feasibility checks assess system-level feasibility while design reviews focus on interaction-level feasibility.
- [`architecture-designer`](../architecture-designer/SKILL.md) -- Architecture decisions constrain what designs are feasible; design reviews enforce those constraints.
