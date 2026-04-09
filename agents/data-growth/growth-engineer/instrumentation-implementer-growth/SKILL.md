---
name: instrumentation-implementer-growth
description: >
  This skill implements growth tracking events and A/B test instrumentation. Use when asked to add growth event tracking, instrument an experiment, or wire up variant assignment events. Also consider when a growth experiment is designed but lacks tracking implementation. Suggest when a growth feature branch has no analytics code.
department: data-growth
agent: growth-engineer
version: 1.0.0
complexity: medium
related-skills:
  - instrumentation-spec-growth
  - instrumentation-verifier-growth
  - instrumentation-implementer-data
  - ../landing-page-builder/SKILL.md
triggers:
  - "implement growth tracking"
  - "add analytics events growth"
  - "instrument growth features"
  - "code tracking events"
  - "growth event implementation"
---

# instrumentation-implementer-growth

## Agent: Growth Engineer

L2 growth engineer (Nx) responsible for growth instrumentation, metrics dashboards, funnel analysis, and growth loop activation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The growth instrumentation implementer translates the growth instrumentation spec into working tracking code, implementing acquisition, activation, and retention events alongside A/B test variant assignment and goal events so that every growth experiment produces measurable results.

## When to Use

- When the growth instrumentation spec is approved and ready for implementation.
- When a new growth experiment requires variant assignment tracking and goal event instrumentation.
- When existing growth tracking has gaps that block funnel analysis or significance tracking.
- When a growth loop is being activated and needs node-level event instrumentation.

## Workflow

1. **Review the growth spec**: Read the instrumentation spec for growth-specific events — channel attribution, signup source, onboarding step completion, activation event, referral actions, and experiment events.
2. **Implement experiment instrumentation**: For each A/B test, add variant assignment events (experiment_assigned with experiment_id, variant_id, user_id) and goal events (the conversion action being measured).
3. **Implement funnel events**: Add tracking at each growth funnel step — landing page view, signup started, signup completed, onboarding step N, activation event. Include channel attribution properties (UTM parameters, referrer).
4. **Implement loop events**: For growth loops, add events at each node — trigger impression, trigger action, invite sent, invite opened, referred signup, referred activation.
5. **Add segmentation properties**: Attach experiment variant, acquisition channel, and cohort properties to all events for downstream segmentation.
6. **Submit for verification**: Deploy to dev/staging and hand off with a verification checklist mapping each event to its test scenario.

## Anti-Patterns

- **Missing variant assignment events**: Implementing goal events without variant assignment makes it impossible to attribute results to experiment arms. *Why*: without knowing which variant each user saw, the experiment data is useless.
- **Hardcoded UTM values**: Setting channel attribution to static values instead of reading from URL parameters corrupts channel-level analysis. *Why*: every user appears to come from the same channel, making CAC-per-channel uncomputable.
- **No experiment_id on goal events**: Firing generic goal events without linking to the experiment_id creates ambiguity when multiple experiments run simultaneously. *Why*: the same conversion event may be a goal for multiple experiments; the experiment_id enables correct attribution.

## Output

**Success:**
- Growth tracking code deployed to dev/staging with all spec-defined events firing at correct trigger points, experiment instrumentation complete, and a verification handoff checklist.

**Failure:**
- Events fire with incorrect variant assignment, missing UTM properties, or wrong experiment_id. Report the discrepancies and the fixes required.

## Related Skills

- [`instrumentation-spec-growth`](../instrumentation-spec-growth/SKILL.md) -- the spec that this skill implements.
- [`instrumentation-verifier-growth`](../instrumentation-verifier-growth/SKILL.md) -- verifies the implementation in dev/staging.
- [`instrumentation-implementer-data`](../../../data-growth/data-analyst/instrumentation-implementer-data/SKILL.md) -- the data analyst's implementer handles product instrumentation; this skill focuses on growth-specific events.
