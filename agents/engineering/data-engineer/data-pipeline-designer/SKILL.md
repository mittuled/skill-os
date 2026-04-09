---
name: data-pipeline-designer
description: >
  This skill designs the architecture and logic for data ingestion, transformation,
  and loading pipelines. Use when asked to design an ETL/ELT pipeline, architect a
  data flow, or plan source-to-target mappings. Also consider when a new data source
  must be integrated. Suggest when the user is about to build a pipeline without a
  documented design.
department: engineering
agent: data-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../pipeline-builder/SKILL.md
  - ../data-warehouse-schema-designer/SKILL.md
  - ../data-pipeline-feasibility-check/SKILL.md
  - ../pipeline-scale-planner/SKILL.md
  - ../data-quality-monitor/SKILL.md
triggers:
  - "design data pipeline"
  - "data pipeline architecture"
  - "ETL pipeline design"
  - "data flow design"
  - "pipeline architecture"
---

# data-pipeline-designer

## Agent: Data Engineer

L2 data engineer (Nx) responsible for data pipeline design, data warehouse schema, pipeline building, reliability testing, data quality monitoring, and scale planning.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Designs the architecture and logic for data ingestion, transformation, and loading pipelines covering source extraction, staging, transformation layers, and target loading.

## When to Use

- When a new data source must be integrated into the warehouse or lakehouse.
- When an existing pipeline requires a redesign due to changed business logic, schema evolution, or performance degradation.
- When a cross-functional team requests a data product and no pipeline design exists.

## Workflow

1. **Source Inventory**: Catalog every source system, API, file drop, or event stream involved. Deliverable: source registry with schema snapshots, volume estimates, and SLA metadata.
2. **Requirements Gathering**: Extract latency, freshness, completeness, and access-control requirements from stakeholders. Deliverable: pipeline requirements document with acceptance criteria.
3. **Architecture Selection**: Choose ETL vs. ELT, batch vs. streaming vs. micro-batch based on latency and volume requirements. Deliverable: architecture decision record (ADR) with tradeoff rationale.
4. **DAG Design**: Define the directed acyclic graph of extraction, staging, transformation, and load steps. Specify idempotency guarantees, retry semantics, and backfill strategy. Deliverable: DAG specification with step-level SLAs.
5. **Schema Mapping**: Map source fields to target schema, document type coercions, null-handling rules, and deduplication logic. Deliverable: source-to-target mapping sheet.
6. **Review and Handoff**: Walk through the design with the pipeline-builder and data-quality-monitor agents. Deliverable: approved design document ready for implementation.

## Anti-Patterns

- **Designing without volume estimates**: Skipping data profiling and assuming small volumes. *Why*: a pipeline that works at 1 GB/day may collapse at 100 GB/day, forcing a costly redesign after production failures.
- **Tight coupling to source schema**: Mapping source fields directly to target columns without a staging layer. *Why*: any upstream schema change breaks the pipeline end-to-end; a staging layer absorbs schema drift.
- **Ignoring idempotency**: Designing steps that produce duplicates on retry. *Why*: non-idempotent pipelines cause data inflation that silently corrupts downstream analytics.

## Output

**On success**: Produces a pipeline design document containing the DAG specification, source-to-target mappings, ADR, and step-level SLA targets. Delivered as a versioned markdown artifact in the project repository.

**On failure**: Report which design phase stalled (e.g., missing source access, unresolved schema conflicts), what alternatives were evaluated, and recommended next steps to unblock.

## Related Skills

- [`pipeline-builder`](../pipeline-builder/SKILL.md) -- Implements the pipeline from this design.
- [`data-warehouse-schema-designer`](../data-warehouse-schema-designer/SKILL.md) -- Designs the target schema this pipeline loads into.
- [`data-pipeline-feasibility-check`](../data-pipeline-feasibility-check/SKILL.md) -- Validates feasibility before committing to a full design.
