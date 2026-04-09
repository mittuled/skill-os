---
name: instrumentation-clarity-reviewer
description: >
  This skill reviews instrumentation plans for clarity, completeness, and measurability. Use when asked to QA an instrumentation spec, review event naming conventions, or validate property coverage. Also consider when a new instrumentation spec is drafted. Suggest when implementation is about to begin on an unreviewed spec.
department: data-growth
agent: analytics-lead
version: 1.0.0
complexity: medium
related-skills:
triggers:
  - "review instrumentation clarity"
  - "audit tracking clarity"
  - "event naming review"
  - "instrumentation legibility check"
  - "tracking schema review"
---

# instrumentation-clarity-reviewer

## Agent: Analytics Lead

L1 analytics leader (1x) responsible for search demand validation, market sizing, goal framing, instrumentation strategy, and north star metric governance.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The instrumentation clarity reviewer audits instrumentation specs and plans to ensure every event is clearly named, every property is typed and defined, every user journey is covered, and the resulting data can answer the questions the spec was designed to address.

## When to Use

- When a new instrumentation spec is drafted and needs review before implementation begins.
- When an instrumentation implementation produces data that does not match the spec.
- When analysts report gaps in event coverage that block dashboard or funnel construction.
- When event naming conventions have drifted across product surfaces and need normalization.

## Workflow

1. **Review event taxonomy**: Verify every event follows the naming convention (object_action format), has a unique name, and maps to a specific user action or system state change.
2. **Validate property completeness**: For each event, confirm all required properties are defined with data type, allowed values, and nullability. Flag properties that are ambiguous or redundant.
3. **Check journey coverage**: Map the instrumentation spec against the user journey. Identify steps with no event coverage (blind spots) and steps with redundant events.
4. **Assess measurability**: For each stated analytics goal, trace the query path through the proposed events and properties. Flag goals that cannot be answered with the specified instrumentation.
5. **Review privacy compliance**: Confirm no PII is captured in event properties unless explicitly scoped and consented. Flag any properties that could be used for re-identification.
6. **Produce review report**: Document findings as pass/fail per event, with specific remediation instructions for each failure.

## Anti-Patterns

- **Rubber-stamp reviews**: Approving specs without tracing query paths gives false confidence that the data will support analysis. *Why*: gaps discovered post-implementation require re-instrumentation cycles that delay insights by weeks.
- **Reviewing in isolation**: Reviewing the spec without consulting the analysts who will query the data misses practical usability issues. *Why*: the spec author's mental model may not match the analyst's query patterns.
- **Ignoring property types**: Accepting loosely typed properties (e.g., "value: string" for a numeric field) creates downstream casting errors. *Why*: type mismatches break dashboards silently and corrupt aggregations.

## Output

**Success:**
- A review report with pass/fail per event, property-level feedback, journey coverage score, and measurability assessment for each analytics goal.
- A clear approved/needs-revision verdict with specific remediation items.

**Failure:**
- An instrumentation spec ships to implementation with unresolved coverage gaps. Report which journey steps lack coverage and which analytics goals are blocked.

## Related Skills

- [`instrumentation-spec-data`](../instrumentation-spec-data/SKILL.md) -- produces the specs this skill reviews.
- [`instrumentation-planner-data`](../instrumentation-planner-data/SKILL.md) -- the implementation plan is reviewed alongside the spec for feasibility.
- [`instrumentation-spec-growth`](../../../data-growth/growth-engineer/instrumentation-spec-growth/SKILL.md) -- growth instrumentation specs also require clarity review.
