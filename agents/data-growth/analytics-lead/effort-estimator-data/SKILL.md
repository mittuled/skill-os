---
name: effort-estimator-data
description: >
  This skill estimates analytics and data engineering effort for product initiatives. Use when asked to size instrumentation work, estimate dashboard build time, or scope a data pipeline. Also consider when sprint planning requires analytics capacity allocation. Suggest when a PRD is approved without a data workstream estimate.
department: data-growth
agent: analytics-lead
version: 1.0.0
complexity: simple
related-skills:
  - instrumentation-planner-data
  - instrumentation-spec-data
triggers:
  - "estimate analytics effort"
  - "data project estimation"
  - "analytics work estimation"
  - "scope data initiative"
  - "effort sizing data"
---

# effort-estimator-data

## Agent: Analytics Lead

L1 analytics leader (1x) responsible for search demand validation, market sizing, goal framing, instrumentation strategy, and north star metric governance.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The effort estimator sizes the analytics and data engineering work required for an initiative, producing t-shirt estimates for instrumentation, pipeline, and dashboard deliverables so product and engineering can plan capacity accurately.

## When to Use

- When a new product initiative is entering sprint planning and the analytics workstream has no estimate.
- When a PRD includes metrics requirements but no data engineering scope.
- When the analytics team needs to negotiate capacity trade-offs across competing initiatives.

## Workflow

1. **Extract data requirements**: Parse the PRD or initiative brief for all metrics, dashboards, instrumentation, and reporting deliverables.
2. **Decompose into work units**: Break each deliverable into discrete tasks — event schema design, SDK integration, pipeline configuration, dashboard build, QA verification.
3. **Estimate per unit**: Assign t-shirt sizes (S/M/L/XL) to each task based on historical velocity and complexity factors (new event taxonomy vs. extending existing, number of platforms, real-time vs. batch).
4. **Identify dependencies**: Flag tasks blocked by engineering (SDK releases, API changes) or external teams (third-party integrations).
5. **Produce estimate summary**: Deliver a table of tasks, sizes, dependencies, and total capacity required in analyst-days.

## Anti-Patterns

- **Estimating without the spec**: Sizing effort before the instrumentation spec exists produces guesses, not estimates. *Why*: unknown event schemas and property sets make scope unpredictable.
- **Ignoring QA and verification**: Scoping only implementation without verification time leads to under-allocation. *Why*: instrumentation verification typically consumes 20-30% of total effort.
- **Single-point estimates**: Providing one number without a range hides uncertainty. *Why*: stakeholders treat single-point estimates as commitments rather than forecasts.

## Output

**Success:**
- An effort estimate table listing each analytics task, t-shirt size, dependency, and total analyst-days with a confidence range.

**Failure:**
- Estimates are consistently off by more than 40% from actuals. Report which task categories were mis-estimated and recalibrate the sizing model.

## Related Skills

- [`instrumentation-planner-data`](../instrumentation-planner-data/SKILL.md) -- the implementation plan feeds directly into effort estimation.
- [`instrumentation-spec-data`](../instrumentation-spec-data/SKILL.md) -- the spec defines the scope that this skill estimates.
