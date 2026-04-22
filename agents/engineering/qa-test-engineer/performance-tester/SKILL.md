---
name: performance-tester
description: Guards the performance budget by catching latency regressions and throughput bottlenecks before release. Use when asked to performance tester. Suggest when relevant.
department: engineering
agent: qa-test-engineer
version: 1.0.0
complexity: medium
related-skills:
  - instrumentation-verifier-prod
  - instrumentation-verifier-qa
  - integration-test-runner
  - unit-test-runner
  - regression-test-runner
  - security-auditor
  - staging-validator
triggers:
  - "run performance tests"
  - "performance testing"
  - "perf test"
  - "load and performance tests"
  - "benchmark application"
---

# performance-tester

## Agent: Social Media Manager

L2 QA and test engineer responsible for unit, integration, regression, performance, and security testing. Validates instrumentation and staging before production deployment.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

The QA / Test Engineer runs performance and load tests to validate the system meets its performance budget.

## When to Use

- A release includes changes to critical user flows or high-throughput endpoints.
- The team has established performance budgets (latency P50/P95/P99, throughput) that must be verified.
- Infrastructure changes (scaling, migration) require re-baselining performance.
- A previous release introduced a latency regression that was caught in production.

## Workflow

1. Identify the critical user flows and endpoints that require performance validation.
2. Retrieve the current performance budget (latency percentiles, throughput targets, error rate thresholds).
3. Configure the load testing tool with realistic traffic patterns, ramp-up profiles, and data volumes.
4. Execute the performance test suite against the target environment.
5. Collect results: latency distributions, throughput, error rates, and resource utilization.
6. Compare results against the performance budget and the previous baseline.
7. Identify any regressions or budget violations with supporting evidence (flame graphs, slow queries, resource saturation).
8. Report findings to the engineering team with a clear pass/fail verdict.
   - **Deliverable**: Performance test report with metrics vs. budget, regression analysis, and pass/fail verdict.

## Anti-Patterns

- **Testing with unrealistic traffic patterns.** *Why*: Synthetic traffic that does not match production access patterns produces misleading results and hides real bottlenecks.
- **Running performance tests on under-provisioned environments.** *Why*: Environment differences make results non-comparable to production, wasting the entire test effort.
- **Reporting only averages instead of percentiles.** *Why*: Averages hide tail latency that affects the worst-off users and mask intermittent bottlenecks.
- **Skipping resource utilization capture.** *Why*: Latency numbers without CPU, memory, and I/O data make it impossible to diagnose the root cause of a regression.

## Output

**Success**: A performance test report confirming all critical flows meet the performance budget with no regressions from the previous baseline.

**Failure**: A regression report identifying which budgets were violated, by how much, with supporting diagnostic data and a recommendation to block or accept the release.

## Related Skills

*None defined yet.*
- [`instrumentation-verifier-prod`](../instrumentation-verifier-prod/SKILL.md) — sibling skill under the same agent — combine with instrumentation-verifier-prod for end-to-end coverage
- [`instrumentation-verifier-qa`](../instrumentation-verifier-qa/SKILL.md) — sibling skill under the same agent — combine with instrumentation-verifier-qa for end-to-end coverage
- [`integration-test-runner`](../integration-test-runner/SKILL.md) — sibling skill under the same agent — combine with integration-test-runner for end-to-end coverage
- [`unit-test-runner`](../unit-test-runner/SKILL.md) — sibling skill under the same agent — combine with unit-test-runner for end-to-end coverage
- [`regression-test-runner`](../regression-test-runner/SKILL.md) — sibling skill under the same agent — combine with regression-test-runner for end-to-end coverage
- [`security-auditor`](../security-auditor/SKILL.md) — sibling skill under the same agent — combine with security-auditor for end-to-end coverage
- [`staging-validator`](../staging-validator/SKILL.md) — sibling skill under the same agent — combine with staging-validator for end-to-end coverage
