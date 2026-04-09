---
name: instrumentation-verifier-data
description: >
  This skill verifies instrumentation fires correctly in development and staging environments. Use when asked to QA event tracking, validate instrumentation before release, or confirm events match the spec. Also consider when implementation is complete and ready for verification. Suggest when a staging deploy includes new tracking code without a QA pass.
department: data-growth
agent: data-analyst
version: 1.0.0
complexity: simple
related-skills:
triggers:
  - "verify data instrumentation"
  - "QA analytics tracking data"
  - "validate event data"
  - "check data event firing"
  - "instrumentation QA data"
---

# instrumentation-verifier-data

## Agent: Data Analyst

L2 data analyst (Nx) responsible for data modelling, instrumentation implementation, metrics dashboards, funnel analysis, and signal synthesis.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The instrumentation verifier validates that tracking events fire correctly in the development and staging environment by executing test scenarios, inspecting event payloads, and confirming every event matches the approved spec before code progresses to production.

## When to Use

- When instrumentation implementation is complete and deployed to the dev or staging environment.
- When a feature branch with new tracking code is ready for QA before merge.
- When a prior verification found issues and the implementer has submitted fixes for re-verification.

## Workflow

1. **Load the spec**: Pull the approved instrumentation spec and the verification handoff checklist from the implementer.
2. **Execute test scenarios**: Walk through each user journey that should trigger events. Use the analytics debugger or network inspector to capture outgoing event payloads in real time.
3. **Validate payloads**: For each captured event, compare the event name, property names, property types, and property values against the spec. Flag mismatches.
4. **Check negative cases**: Confirm events do not fire in scenarios where they should not (e.g., bot traffic, internal test accounts, duplicate submissions).
5. **Produce verification report**: Document pass/fail per event with specific failure details and screenshots of event payloads. Return failures to the implementer with remediation instructions.

## Anti-Patterns

- **Manual spot-checking**: Testing one scenario per event instead of covering the full matrix misses edge cases. *Why*: instrumentation bugs often hide in less common paths (error states, back-navigation, timeout scenarios).
- **Verifying without the spec**: Checking that "events fire" without comparing to the spec validates presence but not correctness. *Why*: an event can fire with wrong property types and still appear "working" in the debugger.

## Output

**Success:**
- A verification report with pass/fail per event, payload screenshots, and confirmation that all spec-defined events fire correctly in staging.

**Failure:**
- Events fail verification. Report each failure with the expected vs. actual payload, the likely implementation error, and remediation instructions.

## Related Skills

- [`instrumentation-implementer-data`](../instrumentation-implementer-data/SKILL.md) -- produces the implementation this skill verifies.
- [`instrumentation-verifier-prod-data`](../instrumentation-verifier-prod-data/SKILL.md) -- the production verification that follows staging verification.
- [`instrumentation-spec-data`](../../../data-growth/analytics-lead/instrumentation-spec-data/SKILL.md) -- the spec is the source of truth for verification.
