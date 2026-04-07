---
name: instrumentation-spec-data
description: >
  This skill writes the instrumentation specification defining what events and properties to track. Use when asked to design an event taxonomy, define tracking properties, or create a measurement plan. Also consider when a new feature enters development without a tracking spec. Suggest when a PRD has success metrics but no corresponding event definitions.
department: data-growth
agent: analytics-lead
version: 1.0.0
complexity: complex
related-skills:
  - instrumentation-clarity-reviewer
  - instrumentation-planner-data
  - instrumentation-implementer-data
  - goal-framer-data
---

# instrumentation-spec-data

## Agent: Analytics Lead

L1 analytics leader (1x) responsible for search demand validation, market sizing, goal framing, instrumentation strategy, and north star metric governance.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The instrumentation spec writer produces the authoritative document defining every event name, trigger condition, property schema, and data type required to measure a product surface, ensuring that analysts can construct any required funnel, cohort, or retention query from the captured data.

## When to Use

- When a new product feature enters development and needs event tracking defined before implementation.
- When a PRD contains success metrics that require new or modified instrumentation.
- When an existing product surface has ad-hoc tracking that needs formalization into a consistent taxonomy.
- When a platform migration requires re-specifying the event schema for a new analytics tool.

## Workflow

1. **Gather measurement requirements**: Extract every metric, funnel step, and analytics question from the PRD, goal framework, and stakeholder interviews. List the queries the data must support.
2. **Map user journeys**: Document each user journey through the product surface step by step. Identify the action or state change at each step that constitutes a trackable event.
3. **Define event taxonomy**: Name each event using the object_action convention (e.g., `checkout_started`, `item_added`). Group events by journey phase. Assign a unique event ID.
4. **Specify properties per event**: For each event, define every property with its name, data type, allowed values (enum or range), nullability, and description. Include standard context properties (user_id, session_id, timestamp, platform, app_version).
5. **Map events to metrics**: Create a traceability matrix linking each analytics goal to the events and properties required to compute it. Identify any goal that lacks full coverage and add events to close the gap.
6. **Define data quality rules**: Specify validation rules per event — required properties, value ranges, expected volume per hour. These rules feed into instrumentation verification.
7. **Document privacy classification**: Tag each property with a privacy tier (anonymous, pseudonymous, PII). Flag properties requiring consent gating or suppression in certain jurisdictions.
8. **Review and publish**: Submit the spec for clarity review. Incorporate feedback. Publish the approved spec as the source of truth for implementation.

## Anti-Patterns

- **Tracking everything**: Specifying events for every micro-interaction without tying them to an analytics question creates storage cost and query noise. *Why*: unused events dilute the signal-to-noise ratio and increase pipeline maintenance burden.
- **Vague property definitions**: Defining a property as "value: string" when it holds a numeric amount causes downstream type-casting failures and aggregation errors. *Why*: loose typing breaks silently — dashboards show null or NaN instead of erroring visibly.
- **No traceability matrix**: Writing events without mapping them to the metrics they support makes it impossible to verify completeness. *Why*: you discover coverage gaps only when an analyst tries to build a query and finds the data missing.
- **Ignoring server-side events**: Specifying only client-side events misses backend actions (payment processing, subscription changes, API calls). *Why*: critical business events often happen server-side and are invisible to client tracking.
- **Skipping privacy classification**: Omitting privacy tiers from the spec risks shipping PII-laden events that violate GDPR or CCPA. *Why*: retroactive PII scrubbing from event stores is expensive and often incomplete.

## Output

**Success:**
- A complete instrumentation spec document containing event taxonomy, property schemas with types and constraints, traceability matrix, data quality rules, and privacy classifications.
- Stakeholder and clarity-reviewer approval confirming the spec is implementation-ready.

**Failure:**
- The spec ships with coverage gaps that block metric computation. Report which metrics are uncomputable, which events are missing, and the revised spec required.
- Properties are mis-typed or under-constrained, causing data quality issues in production. Report the affected events and corrected definitions.

## Related Skills

- [`instrumentation-clarity-reviewer`](../instrumentation-clarity-reviewer/SKILL.md) -- reviews this spec for completeness and measurability before implementation.
- [`instrumentation-planner-data`](../instrumentation-planner-data/SKILL.md) -- translates the spec into an implementation plan.
- [`instrumentation-implementer-data`](../../../data-growth/data-analyst/instrumentation-implementer-data/SKILL.md) -- implements the events defined in this spec.
- [`goal-framer-data`](../goal-framer-data/SKILL.md) -- the analytics goals drive the measurement requirements this spec fulfils.
