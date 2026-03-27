---
name: instrumentation-verifier-growth
description: >
  This skill verifies growth instrumentation fires correctly in development and staging. Use when asked to QA growth tracking, validate experiment events, or confirm growth funnel events match the spec. Also consider when growth tracking implementation is complete and ready for QA. Suggest when a growth experiment is about to launch without instrumentation verification.
department: data-growth
agent: growth-engineer
version: 1.0.0
complexity: simple
related-skills:
  - instrumentation-implementer-growth
  - instrumentation-verifier-prod-growth
  - instrumentation-spec-growth
---

# instrumentation-verifier-growth

## Agent: Growth Engineer

L2 growth engineer (Nx) responsible for growth instrumentation, metrics dashboards, funnel analysis, and growth loop activation.

Department ethos: [ideal-data-growth.md](../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The growth instrumentation verifier validates that all growth tracking events — funnel steps, experiment assignments, loop node actions, and attribution properties — fire correctly in the development and staging environment before code progresses to production or experiments launch.

## When to Use

- When growth instrumentation implementation is complete and deployed to dev/staging.
- When a growth experiment is about to launch and its tracking needs final QA.
- When a prior verification found issues and the implementer has submitted fixes.

## Workflow

1. **Load the spec and checklist**: Pull the growth instrumentation spec and the implementation handoff checklist.
2. **Test funnel events**: Walk through the acquisition-to-activation funnel. Capture each event payload and compare against the spec for event name, property names, types, and values.
3. **Test experiment events**: Trigger variant assignment by entering the experiment. Verify experiment_assigned fires with correct experiment_id and variant_id. Complete the goal action and verify the goal event fires.
4. **Test loop events**: Execute the full loop cycle (trigger, distribute, sign up as referred user, activate). Verify every node event fires with correct referrer_id linkage.
5. **Produce verification report**: Document pass/fail per event with payload evidence. Return failures to the implementer with specific remediation instructions.

## Anti-Patterns

- **Verifying only the happy path**: Testing only the primary flow misses edge cases (duplicate submissions, expired referral links, blocked cookies). *Why*: growth flows encounter these edge cases at scale; unverified edge cases produce silent data corruption.
- **Skipping experiment verification**: Assuming experiment events work because the UI renders variants ignores that tracking may be missing or misconfigured. *Why*: an experiment without correct variant assignment tracking produces unattributable data.

## Output

**Success:**
- A verification report with pass/fail per growth event, experiment event validation, loop event validation, and payload evidence confirming spec compliance.

**Failure:**
- Growth events fail verification. Report each failure with expected vs. actual payload and remediation instructions.

## Related Skills

- [`instrumentation-implementer-growth`](../instrumentation-implementer-growth/SKILL.md) -- the implementation this skill verifies.
- [`instrumentation-verifier-prod-growth`](../instrumentation-verifier-prod-growth/SKILL.md) -- the production verification that follows staging verification.
- [`instrumentation-spec-growth`](../instrumentation-spec-growth/SKILL.md) -- the spec is the source of truth for verification.
