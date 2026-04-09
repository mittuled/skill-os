---
name: data-quality-monitor
description: >
  This skill monitors data quality metrics including completeness, accuracy, and
  freshness across pipelines and warehouse tables. Use when asked to set up data
  quality checks, investigate data anomalies, or validate pipeline output integrity.
  Also consider when downstream consumers report unexpected nulls or stale data.
  Suggest when the user deploys a pipeline without quality gates.
department: engineering
agent: data-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../pipeline-builder/SKILL.md
  - ../data-pipeline-designer/SKILL.md
  - ../pipeline-reliability-tester/SKILL.md
triggers:
  - "monitor data quality"
  - "data quality check"
  - "data validation"
  - "track data quality"
  - "data health monitoring"
---

# data-quality-monitor

## Agent: Data Engineer

L2 data engineer (Nx) responsible for data pipeline design, data warehouse schema, pipeline building, reliability testing, data quality monitoring, and scale planning.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Monitors data quality metrics including completeness, accuracy, freshness, uniqueness, and consistency across pipelines and warehouse tables.

## When to Use

- When a new pipeline reaches production and requires ongoing quality validation.
- When downstream analytics teams report data anomalies such as unexpected nulls, duplicates, or stale records.
- When regulatory or compliance requirements mandate data quality audit trails.

## Workflow

1. **Metric Definition**: Define quality dimensions (completeness, accuracy, freshness, uniqueness, consistency) and set thresholds per table or dataset. Deliverable: data quality contract with SLA thresholds.
2. **Check Implementation**: Implement quality checks using tools like Great Expectations, dbt tests, or custom SQL assertions. Place checks at ingestion, transformation, and serving boundaries. Deliverable: quality check suite integrated into the pipeline DAG.
3. **Alerting Configuration**: Wire check failures to alerting channels with severity tiers (warning vs. critical) and escalation paths. Deliverable: alert routing rules with on-call mappings.
4. **Dashboard Setup**: Build a data quality dashboard showing pass/fail rates, trend lines, and SLA compliance over time. Deliverable: observable quality dashboard.
5. **Incident Response Playbook**: Document triage steps for common quality failures including root-cause patterns and remediation procedures. Deliverable: data quality incident runbook.

## Anti-Patterns

- **Percentage-only thresholds**: Setting quality thresholds as percentages without absolute floor counts. *Why*: a 99% completeness rate on a table that dropped from 1M to 1K rows still passes but masks catastrophic data loss.
- **Post-hoc monitoring only**: Adding quality checks after downstream consumers complain instead of at pipeline deployment. *Why*: reactive monitoring means bad data has already polluted dashboards and models before detection.
- **Alert fatigue**: Routing all quality failures to the same channel at the same severity. *Why*: teams learn to ignore alerts, causing real critical failures to go unnoticed.

## Output

**On success**: Produces a data quality monitoring suite comprising check definitions, alert routing rules, a quality dashboard, and an incident runbook. Delivered as pipeline-integrated configuration and documentation.

**On failure**: Report which quality dimension could not be monitored (e.g., no freshness metadata available), what alternatives were attempted, and recommended instrumentation to unblock.

## Related Skills

- [`pipeline-builder`](../pipeline-builder/SKILL.md) -- Integrates quality checks into the pipeline execution flow.
- [`data-pipeline-designer`](../data-pipeline-designer/SKILL.md) -- Defines quality requirements during the design phase.
- [`pipeline-reliability-tester`](../pipeline-reliability-tester/SKILL.md) -- Tests that quality checks fire correctly under failure conditions.
