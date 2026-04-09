---
name: instrumentation-planner-data
description: >
  This skill plans the instrumentation implementation approach across client and server. Use when asked to create an instrumentation rollout plan, coordinate SDK integration, or sequence event deployment across platforms. Also consider when a new product surface launches without a data collection strategy. Suggest when an instrumentation spec is approved but no implementation plan exists.
department: data-growth
agent: analytics-lead
version: 1.0.0
complexity: medium
related-skills:
triggers:
  - "plan the instrumentation rollout"
  - "how should we implement tracking"
  - "create an analytics implementation plan"
  - "sequence the event deployment"
---

# instrumentation-planner-data

## Agent: Analytics Lead

L1 analytics leader (1x) responsible for search demand validation, market sizing, goal framing, instrumentation strategy, and north star metric governance.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The instrumentation planner designs the implementation approach for event tracking across client and server surfaces, determining SDK selection, event routing architecture, platform sequencing, and rollout phases so that data collection ships reliably alongside product features.

## When to Use

- When an approved instrumentation spec needs an implementation plan before engineering can begin work.
- When a new product surface (mobile app, API, embedded widget) requires instrumentation from scratch.
- When instrumentation must coordinate across multiple engineering teams or codebases.
- When an existing instrumentation architecture needs migration to a new analytics platform.

## Workflow

1. **Audit current state**: Inventory existing SDKs, event pipelines, and data destinations. Document platform coverage gaps (e.g., server events exist but client-side tracking is absent).
2. **Select tooling**: Choose or confirm the analytics SDK, CDP, and event router for each platform. Document trade-offs (client-side vs. server-side, first-party vs. third-party).
3. **Design event routing**: Map the flow from event trigger to final data warehouse table. Specify buffering, batching, retry, and deduplication behaviour.
4. **Sequence by platform**: Order implementation across platforms by data criticality and engineering availability. Prioritize the platform that generates the highest-volume user interactions.
5. **Define rollout phases**: Break implementation into phases — Phase 1: core funnel events, Phase 2: engagement events, Phase 3: edge-case and error events. Each phase has a verification gate. Apply the scoring rubric at `references/scoring-rubric.md`.
6. **Coordinate with engineering**: Produce a task list per engineering team with event names, trigger points in code, and property sources. Align on sprint allocation.

## Anti-Patterns

- **Big-bang instrumentation**: Deploying all events in a single release makes verification impossible and debugging painful. *Why*: when 50 events ship at once, identifying which one fires incorrectly requires exhaustive testing.
- **Client-only tracking**: Relying solely on client-side events misses server-side actions and is vulnerable to ad blockers. *Why*: client-side data loss rates of 10-30% silently degrade metric accuracy.
- **No verification gates**: Planning implementation without verification checkpoints between phases ships unvalidated data to production. *Why*: instrumentation bugs compound — a broken event in Phase 1 corrupts funnel analysis built in Phase 2.

## Output

**Success:**
- An instrumentation implementation plan specifying SDK selection, event routing architecture, platform sequence, phase breakdown, verification gates, and per-team task assignments.

**Failure:**
- Implementation begins without a plan, causing duplicate events, missing properties, or platform coverage gaps. Report the gaps discovered and the remediation plan.

## Related Skills

- [`instrumentation-spec-data`](../instrumentation-spec-data/SKILL.md) -- the spec defines what to track; this skill plans how to track it.
- [`instrumentation-implementer-data`](../../../data-growth/data-analyst/instrumentation-implementer-data/SKILL.md) -- executes the plan this skill produces.
- [`effort-estimator-data`](../effort-estimator-data/SKILL.md) -- consumes the plan to produce capacity estimates.
