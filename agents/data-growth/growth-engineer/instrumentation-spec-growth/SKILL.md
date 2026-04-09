---
name: instrumentation-spec-growth
description: >
  This skill writes the growth instrumentation specification covering acquisition, activation, and retention events. Use when asked to define growth tracking events, spec experiment instrumentation, or document the growth event taxonomy. Also consider when growth experiments lack a tracking spec. Suggest when a new growth loop or experiment is designed without event definitions.
department: data-growth
agent: growth-engineer
version: 1.0.0
complexity: complex
related-skills:
triggers:
  - "write growth instrumentation spec"
  - "growth tracking specification"
  - "define growth events spec"
  - "analytics spec growth"
  - "growth event taxonomy"
---

# instrumentation-spec-growth

## Agent: Growth Engineer

L2 growth engineer (Nx) responsible for growth instrumentation, metrics dashboards, funnel analysis, and growth loop activation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The growth instrumentation spec writer produces the authoritative document defining every growth-specific event — channel attribution, experiment assignment, funnel step completion, loop node actions, and retention signals — with property schemas, data types, and trigger conditions so that every growth metric and experiment can be computed from the captured data.

## When to Use

- When growth experiments are planned and need tracking event definitions before implementation.
- When the growth funnel lacks consistent event coverage across acquisition, activation, and retention stages.
- When a new growth loop is designed and each node needs event specification.
- When the growth team migrates to a new experimentation or analytics platform and events need re-specification.

## Workflow

1. **Gather growth measurement requirements**: Extract every growth metric, experiment goal, and funnel step from the growth model, experiment roadmap, and loop designs. List the queries the spec must support.
2. **Define acquisition events**: Specify events for first touch, landing page view, UTM capture, signup started, signup completed. Include attribution properties (utm_source, utm_medium, utm_campaign, referrer).
3. **Define activation events**: Specify events for each onboarding step and the activation moment. Include properties for time-to-complete and cohort assignment.
4. **Define experiment events**: Specify experiment_assigned (experiment_id, variant_id, user_id, timestamp) and goal events for each active and planned experiment.
5. **Define loop events**: For each growth loop, specify trigger impression, trigger action, distribution event, referred user events, and reward events with referrer_id linkage.
6. **Define retention events**: Specify session start, key engagement actions, and re-engagement trigger events (email opened, push clicked, re-activated).
7. **Map events to metrics**: Create a traceability matrix linking each growth metric to the events required to compute it. Identify gaps and add events to close them.
8. **Submit for review**: Send the spec to the instrumentation clarity reviewer for approval before implementation begins.

## Anti-Patterns

- **Duplicating product events**: Re-specifying events that already exist in the product instrumentation spec creates duplicate data and naming conflicts. *Why*: use existing product events and extend with growth-specific properties rather than creating parallel event streams.
- **No experiment event standard**: Specifying experiment events inconsistently across experiments makes cross-experiment analysis impossible. *Why*: a standard experiment_assigned schema enables the significance tracker to process any experiment uniformly.
- **Missing referrer linkage**: Specifying referral events without a consistent referrer_id property breaks loop attribution. *Why*: without the link between referrer and referred user, viral coefficient is uncomputable.
- **Ignoring consent requirements**: Specifying user-level tracking without consent gating violates privacy regulations in opt-in jurisdictions. *Why*: non-compliant tracking creates legal risk and may require retroactive data deletion.

## Output

**Success:**
- A growth instrumentation spec with acquisition, activation, experiment, loop, and retention event definitions, property schemas, traceability matrix, and clarity reviewer approval.

**Failure:**
- The spec has gaps that prevent a growth metric from being computed. Report the uncomputable metric, the missing events, and the additions required.

## Related Skills

- [`instrumentation-spec-data`](../../../data-growth/analytics-lead/instrumentation-spec-data/SKILL.md) -- the product instrumentation spec that growth events extend rather than duplicate.
- [`instrumentation-implementer-growth`](../instrumentation-implementer-growth/SKILL.md) -- implements the events defined in this spec.
- [`instrumentation-clarity-reviewer`](../../../data-growth/analytics-lead/instrumentation-clarity-reviewer/SKILL.md) -- reviews this spec for completeness and measurability.
- [`growth-model-designer`](../../../data-growth/growth-lead/growth-model-designer/SKILL.md) -- the growth model's metrics drive the measurement requirements this spec fulfils.
