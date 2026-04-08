---
name: unit-test-runner
description: Catches logic errors at the smallest testable scope, giving engineers fast feedback on every change.
department: engineering
agent: qa-test-engineer
version: 1.0.0
complexity: simple
related-skills: []
triggers:
  - "unit tests"
  - "automated tests"
  - "write tests"
  - "test coverage"
---

# unit-test-runner

## Agent

L2 QA and test engineer responsible for unit, integration, regression, performance, and security testing. Validates instrumentation and staging before production deployment.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

The QA / Test Engineer executes unit test suites and reports coverage and failures.

## When to Use

- A developer has pushed code and the CI pipeline requires unit test validation.
- Coverage thresholds must be verified before a PR can merge.
- A refactoring effort needs confirmation that behavior has not changed at the unit level.

## Workflow

1. Identify the test suites relevant to the changed code paths.
2. Execute the unit test suite and capture pass/fail results, coverage metrics, and execution time.
3. Compare coverage against the configured threshold; flag any drops.
4. Triage failures: distinguish genuine logic errors from test issues (stale mocks, ordering dependencies).
5. Report results with a clear pass/fail verdict and any coverage delta.
   - **Deliverable**: Unit test execution report with pass/fail counts, coverage percentage, and failure details.

## Anti-Patterns

- **Writing unit tests that depend on external services or databases.** *Why*: Tests with external dependencies are slow, flaky, and belong in the integration test suite.
- **Chasing 100% coverage without considering test quality.** *Why*: Coverage measures execution, not correctness; trivial tests inflate coverage without catching bugs.
- **Ignoring test execution time.** *Why*: Slow unit tests delay the feedback loop, pushing developers to skip them or batch changes.

## Output

**Success**: A unit test report showing all tests pass and coverage meets or exceeds the configured threshold.

**Failure**: A failure report listing each failing test with the error, the affected code path, and a coverage delta if the threshold was missed.

## Related Skills

*None defined yet.*
