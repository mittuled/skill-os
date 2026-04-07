---
name: effort-estimator-eng
description: >
  This skill estimates engineering effort required for features and initiatives. Use when asked to
  size a feature, provide a time estimate for a delivery, or forecast resource needs for a project.
  Also consider when a phase plan needs effort figures before team allocation. Suggest when
  stakeholders request delivery timelines without engineering input.
department: engineering
agent: vp-engineering
version: 1.0.0
complexity: medium
related-skills:
  - ../../../engineering/vp-engineering/team-allocator/SKILL.md
  - ../../../engineering/vp-engineering/phase-planner-eng/SKILL.md
triggers:
  - "estimate the effort for this"
  - "how long will this take to build"
  - "size this feature"
  - "give me a time estimate"
---

# effort-estimator-eng

## Agent: VP Engineering

L1 engineering leader (1x) responsible for spec intake review, team allocation, architecture oversight, velocity monitoring, and go-live approvals. Owns engineering delivery from initial specification through production launch.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Estimates engineering effort required for features, initiatives, and delivery phases using historical velocity data and complexity analysis.

## When to Use

- When a new feature or initiative needs a time-and-resource estimate before committing to a delivery date.
- When a phase plan requires effort breakdowns for team allocation decisions.
- When leadership requests a rough-order-of-magnitude estimate for roadmap planning.

## Workflow

1. **Scope review**: Read the specification, architecture decisions, and any spike outputs. Identify knowns, unknowns, and external dependencies. Deliverable: scoped estimation brief listing all work streams.
2. **Complexity assessment**: Classify each work stream by complexity (simple, medium, complex) based on novelty, integration surface, and uncertainty. Deliverable: complexity-tagged work stream list.
3. **Reference-class estimation**: Compare each work stream to historical analogues using DORA metrics and past velocity data. Apply calibration factors for team familiarity and tech stack maturity. Deliverable: point or person-week estimates per work stream with confidence intervals.
4. **Risk buffer calculation**: Add contingency based on the number of unknowns, external dependencies, and team ramp-up needs. Use a multiplier (1.2x for low risk, 1.5x for medium, 2x for high uncertainty). Deliverable: buffered estimate with stated assumptions.
5. **Consolidate and present**: Aggregate into a single estimate with breakdown by phase, team, and risk tier. Deliverable: effort estimate document with assumptions log.

## Anti-Patterns

- **Precision theater**: Providing single-point estimates without confidence ranges. *Why*: false precision erodes trust when reality diverges, and prevents stakeholders from making risk-informed decisions.
- **Anchoring to deadlines**: Starting from a desired date and working backwards to fit scope. *Why*: deadline-driven estimates produce systematic underestimates that lead to crunch and quality erosion.
- **Ignoring integration cost**: Estimating components in isolation without accounting for integration, testing, and deployment overhead. *Why*: integration work often exceeds component work in multi-service systems.

## Output

**On success**: Produces an effort estimate document containing per-work-stream estimates with confidence intervals, a total delivery estimate with risk buffer, stated assumptions, and comparison to historical analogues. Delivered to phase planning and team allocation stakeholders.

**On failure**: Report which work streams could not be estimated (e.g., pending spike results, undefined API contracts), the impact on overall estimate confidence, and recommended next steps to reduce uncertainty.

## Related Skills

- [`team-allocator`](../../../engineering/vp-engineering/team-allocator/SKILL.md) -- uses effort estimates to determine staffing assignments.
- [`phase-planner-eng`](../../../engineering/vp-engineering/phase-planner-eng/SKILL.md) -- effort estimates feed directly into phase planning timelines.
