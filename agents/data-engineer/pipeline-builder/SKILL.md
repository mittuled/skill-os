---
name: pipeline-builder
description: >
  This skill builds data pipelines according to the approved design, implementing
  extraction, transformation, and loading logic. Use when asked to implement a
  pipeline, write ETL/ELT code, or configure an orchestrator DAG. Also consider
  when a design document is approved and awaiting implementation. Suggest when the
  user has a signed-off design but no running pipeline.
department: engineering
agent: data-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../data-pipeline-designer/SKILL.md
  - ../pipeline-reliability-tester/SKILL.md
  - ../data-quality-monitor/SKILL.md
---

# pipeline-builder

## Agent: Data Engineer

L2 data engineer (Nx) responsible for data pipeline design, data warehouse schema, pipeline building, reliability testing, data quality monitoring, and scale planning.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Builds data pipelines according to the approved design, implementing extraction connectors, transformation logic, orchestration DAGs, and load procedures.

## When to Use

- When a pipeline design document has been approved and is ready for implementation.
- When an existing pipeline requires modification to support new transformations or sources.
- When migrating pipelines between orchestration platforms (e.g., Airflow to Dagster, cron to managed).

## Workflow

1. **Environment Setup**: Provision development environment with required connectors, credentials, and target sandbox schemas. Deliverable: working dev environment with connectivity verified.
2. **Extraction Implementation**: Build source connectors with pagination, rate-limit handling, and incremental extraction logic (CDC, watermark columns, or cursor-based). Deliverable: extraction modules with unit tests.
3. **Transformation Implementation**: Implement transformation logic (SQL models, Spark jobs, or dbt models) matching the source-to-target mapping specification. Ensure idempotent upsert semantics. Deliverable: transformation code with test fixtures.
4. **Orchestration Wiring**: Define the DAG in the orchestrator (Airflow, Dagster, Prefect) with task dependencies, retry policies, timeout limits, and SLA monitors. Deliverable: orchestration configuration with documented trigger schedule.
5. **Integration Testing**: Run the full pipeline end-to-end in staging against representative data. Validate row counts, schema conformance, and idempotency by re-running. Deliverable: integration test results with pass/fail evidence.
6. **Deployment**: Promote pipeline to production with blue-green or shadow deployment. Enable monitoring hooks. Deliverable: production-deployed pipeline with alerting active.

## Anti-Patterns

- **Building without an approved design**: Implementing pipelines ad hoc without a signed-off design document. *Why*: rework rates multiply when assumptions about schema mappings, SLAs, or idempotency are wrong.
- **Hardcoded credentials**: Embedding API keys, database passwords, or tokens in pipeline code. *Why*: leaked credentials create security incidents and block credential rotation.
- **Monolithic DAGs**: Placing all extraction, transformation, and load logic in a single task. *Why*: a failure in any step forces re-execution of the entire pipeline instead of retrying from the failed step.

## Output

**On success**: Produces a production-deployed data pipeline with extraction connectors, transformation logic, orchestration DAG, integration test evidence, and active monitoring. Delivered as code in the project repository and a running pipeline in the orchestrator.

**On failure**: Report which implementation phase failed (e.g., connector authentication, transformation logic error), what was attempted, and specific remediation steps.

## Related Skills

- [`data-pipeline-designer`](../data-pipeline-designer/SKILL.md) -- Provides the design this skill implements.
- [`pipeline-reliability-tester`](../pipeline-reliability-tester/SKILL.md) -- Tests the built pipeline for failure resilience.
- [`data-quality-monitor`](../data-quality-monitor/SKILL.md) -- Adds quality checks to the built pipeline.
