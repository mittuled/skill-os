---
name: pipeline-reliability-tester
description: >
  This skill tests data pipelines for reliability including failure handling, retry
  behavior, and data consistency under fault conditions. Use when asked to validate
  pipeline resilience, test failure modes, or verify idempotency. Also consider when
  a pipeline is promoted to production without chaos testing. Suggest when the user
  deploys a new pipeline without reliability validation.
department: engineering
agent: data-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../pipeline-builder/SKILL.md
  - ../data-quality-monitor/SKILL.md
  - ../pipeline-scale-planner/SKILL.md
---

# pipeline-reliability-tester

## Agent: Data Engineer

L2 data engineer (Nx) responsible for data pipeline design, data warehouse schema, pipeline building, reliability testing, data quality monitoring, and scale planning.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Tests data pipelines for reliability including failure handling, retry semantics, idempotency, and data consistency under fault injection conditions.

## When to Use

- When a newly built pipeline is ready for production promotion and requires reliability sign-off.
- When a pipeline has experienced repeated production failures and root cause is unclear.
- When infrastructure changes (e.g., cluster migration, engine upgrade) require regression testing of existing pipelines.

## Workflow

1. **Failure Mode Catalog**: Enumerate failure scenarios including source unavailability, network partitions, schema drift, out-of-order events, partial writes, and orchestrator crashes. Deliverable: failure mode inventory.
2. **Idempotency Verification**: Execute the pipeline twice with identical input and compare outputs. Verify no duplicate rows, no missing records, and identical aggregations. Deliverable: idempotency test results.
3. **Fault Injection**: Simulate each cataloged failure (kill tasks mid-run, inject bad records, throttle connections) and verify the pipeline recovers correctly on retry. Deliverable: fault injection test results with recovery evidence.
4. **Data Consistency Checks**: Validate referential integrity between fact and dimension tables, check for orphaned foreign keys, and verify row counts match source after recovery. Deliverable: consistency validation report.
5. **SLA Stress Test**: Run the pipeline under peak-volume conditions and verify it completes within the defined SLA window. Deliverable: SLA compliance evidence under load.

## Anti-Patterns

- **Happy-path-only testing**: Only testing the pipeline with clean data and stable connections. *Why*: production failures are caused by edge cases that only surface under fault conditions, making happy-path tests nearly useless for reliability.
- **Manual re-run as recovery strategy**: Relying on manual intervention to restart failed pipelines instead of testing automated retry. *Why*: manual recovery does not scale and introduces hours of delay during off-hours failures.
- **Testing against toy data**: Using trivially small datasets that do not exercise pagination, memory limits, or parallelism. *Why*: volume-dependent bugs (OOM, timeouts, partition skew) only appear at realistic scale.

## Output

**On success**: Produces a reliability test report containing idempotency verification, fault injection results, consistency validation, and SLA stress test evidence. Delivered as a test report artifact with pass/fail per scenario.

**On failure**: Report which reliability tests failed, the observed vs. expected behavior, root cause hypothesis, and recommended pipeline fixes.

## Related Skills

- [`pipeline-builder`](../pipeline-builder/SKILL.md) -- Builds the pipeline this skill tests.
- [`data-quality-monitor`](../data-quality-monitor/SKILL.md) -- Validates data quality dimensions that complement reliability testing.
