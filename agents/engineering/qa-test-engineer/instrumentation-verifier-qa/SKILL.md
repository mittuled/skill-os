---
name: instrumentation-verifier-qa
description: Prevents broken instrumentation from reaching staging by validating logging, metrics, and tracing in QA.
department: engineering
agent: qa-test-engineer
version: 1.0.0
complexity: simple
related-skills: []
---

# instrumentation-verifier-qa

## Agent

L2 QA and test engineer responsible for unit, integration, regression, performance, and security testing. Validates instrumentation and staging before production deployment.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

The QA / Test Engineer verifies that instrumentation (logging, metrics, tracing) is correctly implemented in the QA environment.

## When to Use

- A feature branch includes new or modified instrumentation and is ready for QA validation.
- The team is establishing instrumentation standards and needs baseline verification in QA.
- A previous release had instrumentation gaps traced back to missing QA checks.

## Workflow

1. Review the feature specification or PR to identify all expected instrumentation points.
2. Map each instrumentation point to an observable signal: log entry, metric emission, or trace span.
3. Execute test scenarios in the QA environment that exercise every instrumented code path.
4. Query the QA observability stack to confirm each expected signal was emitted with correct payload shape.
5. Validate that no extraneous or duplicated signals are present beyond the expected set.
6. Document results in a structured checklist with pass/fail per signal.
7. Report findings to the feature owner with a recommendation to promote or fix.
   - **Deliverable**: QA instrumentation verification checklist with pass/fail per signal.

## Anti-Patterns

- **Relying on code review alone to verify instrumentation correctness.** *Why*: Code review confirms intent but not runtime behavior; only execution in QA proves signals actually fire.
- **Testing instrumentation only on the happy path.** *Why*: Error paths and edge cases often have distinct instrumentation that will be invisible if only success flows are tested.
- **Ignoring payload shape validation.** *Why*: A signal that fires but carries malformed data is as dangerous as a missing signal because downstream consumers will break silently.

## Output

**Success**: A QA instrumentation verification checklist confirming all signals fire correctly with valid payloads.

**Failure**: A defect report listing each failing instrumentation point, expected vs. actual behavior, and a recommendation to block promotion until resolved.

## Related Skills

*None defined yet.*
