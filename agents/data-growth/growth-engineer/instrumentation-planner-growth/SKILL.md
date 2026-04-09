---
name: instrumentation-planner-growth
description: >
  This skill plans the growth instrumentation implementation across product surfaces. Use when asked to create a growth tracking rollout plan, sequence growth event deployment, or coordinate A/B test instrumentation across platforms. Also consider when a growth spec is approved without an implementation plan. Suggest when growth experiments are designed but tracking is unplanned.
department: data-growth
agent: growth-engineer
version: 1.0.0
complexity: medium
related-skills:
triggers:
  - "plan growth instrumentation"
  - "growth tracking plan"
  - "analytics plan growth"
  - "instrumentation strategy growth"
  - "event tracking roadmap growth"
---

# instrumentation-planner-growth

## Agent: Growth Engineer

L2 growth engineer (Nx) responsible for growth instrumentation, metrics dashboards, funnel analysis, and growth loop activation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The growth instrumentation planner designs the rollout approach for growth tracking across product surfaces, sequencing experiment infrastructure, acquisition attribution, and funnel event deployment to ensure growth metrics are measurable before experiments launch.

## When to Use

- When a growth instrumentation spec is approved and needs a phased implementation plan.
- When multiple growth experiments require coordinated instrumentation across web, mobile, and server surfaces.
- When A/B test infrastructure needs initial setup or migration to a new experimentation platform.
- When growth tracking must align with a product launch timeline.

## Workflow

1. **Inventory growth surfaces**: List all product surfaces where growth events must fire — landing pages, signup flow, onboarding, activation points, referral mechanics, upgrade flows.
2. **Prioritize by experiment roadmap**: Sequence instrumentation to match the growth experiment calendar. Events needed for the next experiment ship first.
3. **Plan experiment infrastructure**: If A/B test tooling is not yet in place, plan SDK integration, variant assignment mechanism, and experiment configuration management.
4. **Design attribution pipeline**: Plan UTM capture, first-touch and multi-touch attribution, and channel-level CAC computation. Ensure attribution persists through the signup-to-activation journey.
5. **Define verification gates**: Set checkpoints after each implementation phase. No experiment may launch until its required events pass verification.
6. **Produce the plan**: Deliver a phased rollout document with task assignments, platform sequence, dependency map, and timeline aligned to the experiment roadmap.

## Anti-Patterns

- **Instrumentation after experiment launch**: Launching an experiment before its tracking is verified produces an experiment with no data. *Why*: the experiment runs, consumes traffic, and produces zero learnings — pure waste.
- **No attribution planning**: Implementing funnel events without planning end-to-end attribution makes channel-level analysis impossible. *Why*: without attribution, you know conversion happened but not which channel produced it.
- **Platform-by-platform isolation**: Planning web tracking independently of mobile tracking creates inconsistent event schemas across platforms. *Why*: cross-platform users generate fragmented journeys that cannot be stitched into a single funnel.

## Output

**Success:**
- A growth instrumentation rollout plan with phased task list, platform sequence, experiment infrastructure setup, attribution pipeline design, verification gates, and timeline.

**Failure:**
- An experiment launches before its instrumentation is verified. Report the data gap, the affected experiment, and the remediation plan.

## Related Skills

- [`instrumentation-spec-growth`](../instrumentation-spec-growth/SKILL.md) -- the spec defines what to implement; this skill plans how and when.
- [`instrumentation-implementer-growth`](../instrumentation-implementer-growth/SKILL.md) -- executes the plan this skill produces.
- [`instrumentation-planner-data`](../../../data-growth/analytics-lead/instrumentation-planner-data/SKILL.md) -- the analytics lead's planner covers product instrumentation; this skill focuses on growth-specific tracking.
