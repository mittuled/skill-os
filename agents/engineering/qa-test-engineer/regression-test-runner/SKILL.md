---
name: regression-test-runner
description: Prevents shipped features from breaking by running the full regression suite against every change set.
department: engineering
agent: qa-test-engineer
version: 1.0.0
complexity: medium
related-skills: []
---

# regression-test-runner

## Agent

L2 QA and test engineer responsible for unit, integration, regression, performance, and security testing. Validates instrumentation and staging before production deployment.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

The QA / Test Engineer runs regression tests to ensure new changes have not broken existing functionality.

## When to Use

- A feature branch is ready for merge and must pass the regression gate.
- A hotfix has been applied and existing functionality needs re-verification.
- A dependency upgrade or refactor changes shared code paths.
- The team is preparing a release candidate and needs full regression sign-off.

## Workflow

1. Determine the scope of regression testing based on the change set and affected modules.
2. Select the appropriate regression test suite (full or targeted) based on risk and time constraints.
3. Verify the test environment matches the expected configuration and data state.
4. Execute the regression test suite and capture pass/fail results, execution times, and logs.
5. Triage failures: categorize each as a genuine regression, a flaky test, or an environment issue.
6. For genuine regressions, file defect tickets with reproduction steps, expected vs. actual behavior, and severity.
7. Re-run flaky tests in isolation to confirm or dismiss them.
8. Report the regression test summary with pass rate, blocking defects, and release recommendation.
   - **Deliverable**: Regression test report with pass/fail summary, defect tickets, and release recommendation.

## Anti-Patterns

- **Running only a subset of regressions to save time without a risk assessment.** *Why*: Skipping tests without understanding risk leaves blind spots that surface as production incidents.
- **Treating all failures as flaky without investigation.** *Why*: Dismissing failures as flaky normalizes ignoring real regressions and degrades suite trust.
- **Not updating the regression suite after new features ship.** *Why*: A stale regression suite provides false confidence because it does not cover recent functionality.
- **Running regressions against stale test data.** *Why*: Tests that pass on outdated data may fail on production-like data, hiding real defects.

## Output

**Success**: A regression test report confirming no genuine regressions, with a clear release recommendation.

**Failure**: A blocking defect list with severity, reproduction steps, and affected features, plus a recommendation to hold the release until resolved.

## Related Skills

*None defined yet.*
