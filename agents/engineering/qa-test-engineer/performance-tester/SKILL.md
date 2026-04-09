---
name: performance-tester
description: Guards the performance budget by catching latency regressions and throughput bottlenecks before release.
department: engineering
agent: qa-test-engineer
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "run performance tests"
  - "performance testing"
  - "perf test"
  - "load and performance tests"
  - "benchmark application"
---

# performance-tester

## Agent

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
