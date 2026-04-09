---
name: integration-test-runner
description: Surfaces cross-component failures before they reach staging by exercising real service interactions. Use when asked to integration test runner. Suggest when relevant.
department: engineering
agent: qa-test-engineer
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "test plan"
  - "integration tests"
  - "write test plan"
  - "QA planning"
---

# integration-test-runner

## Agent: Social Media Manager

L2 QA and test engineer responsible for unit, integration, regression, performance, and security testing. Validates instrumentation and staging before production deployment.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

The QA / Test Engineer executes integration tests to validate interactions between system components.

## When to Use

- A feature touches multiple services or modules and unit tests alone cannot verify the interaction.
- An API contract has changed and consumers need to be validated against the new contract.
- A dependency has been upgraded and cross-boundary behavior must be re-verified.
- CI pipeline requires integration test gate before merge to main.

## Workflow

1. Identify the components under test and their integration boundaries (APIs, databases, queues, external services).
2. Review existing integration test coverage and identify gaps relative to the change set.
3. Write or update integration test cases that exercise each cross-boundary interaction, including happy path, error responses, and timeout scenarios.
4. Configure the test environment with required service dependencies (real or contract-verified stubs).
5. Execute the integration test suite and capture results, timings, and any flaky test signals.
6. Analyze failures to distinguish genuine integration defects from environment or test instability.
7. File defect reports for genuine failures with reproduction steps, logs, and affected component owners.
8. Report the overall integration test pass rate and any blocking issues to the team.
   - **Deliverable**: Integration test execution report with pass/fail counts, failure analysis, and defect tickets.

## Anti-Patterns

- **Mocking every dependency in integration tests.** *Why*: Over-mocking defeats the purpose; integration tests must exercise real boundaries to catch contract mismatches.
- **Running integration tests only on the full system instead of targeted component pairs.** *Why*: Full-system runs are slow and produce noisy failures that obscure the actual integration defect.
- **Ignoring flaky tests.** *Why*: Flaky tests erode trust in the suite and train engineers to dismiss real failures as noise.
- **Skipping error path testing.** *Why*: Most integration failures in production occur on error paths (timeouts, retries, malformed payloads) that happy-path-only tests never cover.

## Output

**Success**: An integration test report showing all cross-boundary interactions pass, with coverage mapped to the change set and no blocking defects.

**Failure**: A prioritized list of integration defects with reproduction steps, affected components, and a recommendation on whether to block the release.

## Related Skills

*None defined yet.*
