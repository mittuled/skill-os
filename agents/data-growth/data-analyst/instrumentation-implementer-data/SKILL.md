---
name: instrumentation-implementer-data
description: >
  This skill implements tracking events and properties in the analytics platform. Use when asked to add event tracking, implement analytics SDK calls, or wire up event properties. Also consider when an instrumentation spec is approved and ready for implementation. Suggest when a feature branch is nearing merge without tracking code.
department: data-growth
agent: data-analyst
version: 1.0.0
complexity: medium
related-skills:
triggers:
  - "implement data tracking"
  - "add analytics events data"
  - "instrument data layer"
  - "code analytics events"
  - "data event implementation"
---

# instrumentation-implementer-data

## Agent: Data Analyst

L2 data analyst (Nx) responsible for data modelling, instrumentation implementation, metrics dashboards, funnel analysis, and signal synthesis.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The instrumentation implementer translates an approved instrumentation spec into working tracking code by integrating analytics SDK calls at the correct trigger points, populating event properties from application state, and ensuring events fire with the specified schema on every supported platform.

## When to Use

- When an instrumentation spec is approved and the implementation plan assigns tasks to the data analyst.
- When a new product feature is in development and requires event tracking before release.
- When existing tracking has gaps identified during a clarity review or funnel analysis.
- When migrating from one analytics platform to another and events need re-implementation.

## Workflow

1. **Review the spec**: Read the instrumentation spec for event names, trigger conditions, property schemas, and data types. Clarify ambiguities with the analytics lead before writing code.
2. **Identify trigger points**: Map each event to the specific code location (UI interaction handler, API endpoint, state transition) where it should fire.
3. **Implement SDK calls**: Write the analytics SDK call at each trigger point. Populate all required properties from application state, ensuring correct data types and enum values.
4. **Add context properties**: Attach standard context (user_id, session_id, timestamp, platform, app_version) using the SDK's middleware or global context configuration.
5. **Handle edge cases**: Implement error handling for cases where a required property is unavailable (log a warning, send the event with a null marker rather than dropping it silently).
6. **Submit for verification**: Deploy to the development environment and hand off to instrumentation verification with a checklist of expected events and test scenarios.

## Anti-Patterns

- **Implementing without the spec**: Writing tracking code based on verbal descriptions or assumptions produces events that don't match the approved schema. *Why*: spec mismatches create data quality issues that are discovered only when analysts try to query the data weeks later.
- **Silent event dropping**: Suppressing events when a property is missing instead of sending with a null marker hides data gaps. *Why*: dropped events create invisible holes in funnels that are impossible to diagnose without instrumentation verification.
- **Hardcoded property values**: Setting properties to static strings instead of reading from application state produces misleading data. *Why*: a hardcoded "plan_tier: free" for all users makes tier-based analysis impossible.

## Output

**Success:**
- Tracking code deployed to the development environment with all spec-defined events firing at correct trigger points with properly typed properties.
- A verification handoff checklist listing each event, expected trigger scenario, and expected properties.

**Failure:**
- Events fire with incorrect property types, missing required properties, or at wrong trigger points. Report the discrepancies against the spec and the fixes required.

## Related Skills

- [`instrumentation-spec-data`](../../../data-growth/analytics-lead/instrumentation-spec-data/SKILL.md) -- the spec that this skill implements.
- [`instrumentation-planner-data`](../../../data-growth/analytics-lead/instrumentation-planner-data/SKILL.md) -- the plan that assigns implementation tasks and sequences.
- [`instrumentation-verifier-data`](../instrumentation-verifier-data/SKILL.md) -- verifies the implementation in dev/staging before production release.
