---
name: ga-instrumentation-reviewer
description: >
  This skill reviews instrumentation completeness before general availability launch. Use when asked to audit tracking readiness for GA, verify launch instrumentation coverage, or confirm growth metrics will be measurable post-launch. Also consider when a GA date is set without an instrumentation audit. Suggest when a launch checklist lacks a data coverage item.
department: data-growth
agent: growth-engineer
version: 1.0.0
complexity: simple
related-skills:
  - instrumentation-spec-growth
  - instrumentation-verifier-growth
  - instrumentation-clarity-reviewer
triggers:
  - "review GA instrumentation"
  - "audit Google Analytics setup"
  - "GA4 implementation review"
  - "validate GA tracking"
  - "Google Analytics audit"
---

# ga-instrumentation-reviewer

## Agent: Growth Engineer

L2 growth engineer (Nx) responsible for growth instrumentation, metrics dashboards, funnel analysis, and growth loop activation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The GA instrumentation reviewer conducts a pre-launch audit of all growth-related tracking to confirm that acquisition, activation, retention, and revenue events are instrumented, verified, and flowing to the data warehouse before the product reaches general availability.

## When to Use

- When a product is approaching GA and the launch checklist requires instrumentation sign-off.
- When a beta-to-GA transition introduces new surfaces or flows that need tracking coverage.
- When prior launches shipped with instrumentation gaps that caused data blind spots.

## Workflow

1. **Pull the growth instrumentation spec**: Retrieve the approved spec covering all acquisition, activation, retention, and revenue events.
2. **Audit coverage**: Compare the spec against the live instrumentation. For each event, verify it fires in staging with correct properties.
3. **Check growth dashboard readiness**: Confirm every metric on the growth dashboard has a working data source and displays correct values.
4. **Verify A/B test infrastructure**: If experiments will run at GA, confirm the experiment framework is instrumented with variant assignment events and goal events.
5. **Produce readiness report**: Deliver a pass/fail verdict per event and dashboard metric. Block GA if critical events (signup, activation, purchase) are missing.

## Anti-Patterns

- **Last-minute review**: Conducting the instrumentation audit the day before GA leaves no time to fix gaps. *Why*: instrumentation fixes require implementation, verification, and deployment — typically a 2-3 day cycle.
- **Reviewing only happy paths**: Auditing only the primary user flow misses error states, edge cases, and alternative paths that produce important signals. *Why*: error tracking and edge-case behaviour often reveal the most actionable growth insights.

## Output

**Success:**
- A GA instrumentation readiness report with pass/fail per event, dashboard readiness status, A/B test infrastructure check, and a clear go/no-go verdict.

**Failure:**
- Critical growth events are missing before GA. Report the gaps, estimated fix time, and whether GA should be delayed or proceed with known data limitations.

## Related Skills

- [`instrumentation-spec-growth`](../instrumentation-spec-growth/SKILL.md) -- the spec is the source of truth against which this review is conducted.
- [`instrumentation-verifier-growth`](../instrumentation-verifier-growth/SKILL.md) -- verification results feed into this review.
- [`instrumentation-clarity-reviewer`](../../../data-growth/analytics-lead/instrumentation-clarity-reviewer/SKILL.md) -- the analytics lead's clarity review covers spec quality; this skill covers implementation completeness.
