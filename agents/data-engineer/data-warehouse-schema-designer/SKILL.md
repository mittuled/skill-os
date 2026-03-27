---
name: data-warehouse-schema-designer
description: >
  This skill designs the data warehouse schema including tables, partitions, and
  relationships using dimensional modeling techniques. Use when asked to design a
  star schema, define fact and dimension tables, or plan warehouse partitioning.
  Also consider when query performance degrades due to schema design. Suggest when
  the user is about to load data without a target schema design.
department: engineering
agent: data-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../data-pipeline-designer/SKILL.md
  - ../pipeline-builder/SKILL.md
---

# data-warehouse-schema-designer

## Agent: Data Engineer

L2 data engineer (Nx) responsible for data pipeline design, data warehouse schema, pipeline building, reliability testing, data quality monitoring, and scale planning.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Designs the data warehouse schema including fact tables, dimension tables, partitioning strategies, and relationships using dimensional modeling principles.

## When to Use

- When a new data domain requires warehouse tables and no schema exists.
- When query performance degrades and the root cause traces to schema design (e.g., missing partitions, over-normalized joins).
- When business requirements change and existing schemas cannot support new analytical dimensions.

## Workflow

1. **Business Process Identification**: Identify the business process to model and its grain (the most atomic event to capture). Deliverable: grain statement and business process scope document.
2. **Dimensional Analysis**: Identify dimensions (who, what, where, when, how) and facts (measurable events). Apply Kimball methodology to classify Type 1 (overwrite), Type 2 (history-tracking), or Type 3 (previous-value) slowly changing dimensions. Deliverable: dimensional model diagram.
3. **Physical Schema Design**: Translate the logical model into physical DDL with partitioning keys, clustering columns, sort keys, and distribution strategies optimized for the target warehouse engine (Snowflake, BigQuery, Redshift). Deliverable: DDL scripts with partitioning rationale.
4. **Naming and Convention Enforcement**: Apply consistent naming conventions (e.g., `fct_`, `dim_`, `stg_` prefixes) and document column-level lineage. Deliverable: data dictionary with lineage annotations.
5. **Review and Validation**: Validate schema against expected query patterns by dry-running representative queries and checking execution plans. Deliverable: query performance validation report.

## Anti-Patterns

- **Over-normalization in analytical schemas**: Applying OLTP normalization (3NF) to warehouse tables. *Why*: excessive joins destroy query performance in columnar engines designed for denormalized reads.
- **Ignoring slowly changing dimensions**: Treating all dimensions as Type 1 (overwrite) by default. *Why*: historical analysis becomes impossible when dimension changes are silently overwritten instead of tracked.
- **Partitioning by high-cardinality columns**: Choosing partition keys with millions of distinct values. *Why*: creates millions of tiny partitions that degrade scan performance and inflate metadata overhead.

## Output

**On success**: Produces a warehouse schema design containing the dimensional model diagram, DDL scripts, data dictionary with lineage, and query performance validation. Delivered as versioned artifacts in the project repository.

**On failure**: Report which design phase blocked (e.g., ambiguous grain, conflicting query patterns), what alternatives were considered, and recommended stakeholder decisions to unblock.

## Related Skills

- [`data-pipeline-designer`](../data-pipeline-designer/SKILL.md) -- Designs the pipelines that load data into this schema.
- [`pipeline-builder`](../pipeline-builder/SKILL.md) -- Implements the load logic targeting this schema.
