---
name: data-model-designer-data
description: >
  This skill designs the analytics data model including event schemas and dimension tables. Use when asked to design an event schema, create dimension tables, or structure a data warehouse for analytics queries. Also consider when a new product domain lacks a data model. Suggest when analysts report slow or impossible queries due to schema gaps.
department: data-growth
agent: data-analyst
version: 1.0.0
complexity: complex
related-skills:
  - instrumentation-spec-data
  - instrumentation-implementer-data
  - metrics-dashboard-builder
---

# data-model-designer-data

## Agent: Data Analyst

L2 data analyst (Nx) responsible for data modelling, instrumentation implementation, metrics dashboards, funnel analysis, and signal synthesis.

Department ethos: [ideal-data-growth.md](../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The data model designer structures the analytics data warehouse by defining event fact tables, dimension tables, and materialized views that enable analysts to query user behaviour, compute metrics, and build cohorts without writing complex multi-join SQL for every question.

## When to Use

- When a new product domain or feature area requires a data model before instrumentation implementation.
- When analysts report that common queries require excessive joins, subqueries, or manual transformations.
- When the team migrates to a new data warehouse or analytics platform and needs to redesign the schema.
- When event volume growth degrades query performance and the model needs denormalization or pre-aggregation.

## Workflow

1. **Gather query requirements**: Interview analysts, PMs, and growth leads to collect the top 20 questions the data model must support. Classify by frequency (daily, weekly, ad-hoc).
2. **Define fact tables**: Design event fact tables with grain (one row per event), foreign keys to dimensions, and measures. Apply star schema conventions for query simplicity.
3. **Define dimension tables**: Create dimension tables for users, sessions, products, channels, and time. Include slowly changing dimension (SCD) handling for attributes that evolve (plan tier, segment).
4. **Design materialized views**: For high-frequency queries (daily active users, funnel step counts, cohort retention), create materialized views or summary tables with defined refresh cadence.
5. **Validate with sample queries**: Write the top 10 queries against the proposed model. Verify each completes within acceptable latency and produces correct results against raw data.
6. **Document the model**: Produce an entity-relationship diagram, a data dictionary with column descriptions and types, and a query cookbook with examples for common analyses.
7. **Plan migration**: If modifying an existing model, define the migration path, backfill strategy, and cutover plan. Ensure downstream dashboards are updated.

## Anti-Patterns

- **Snowflake over-normalization**: Normalizing every attribute into its own dimension table creates excessive joins that slow queries and confuse analysts. *Why*: analytics workloads favour wide, denormalized tables optimized for read speed over transactional normalization.
- **No SCD handling**: Treating user dimensions as static ignores that users change plans, segments, and attributes over time. *Why*: without SCD, historical analyses attribute past behaviour to current attributes, producing misleading cohort metrics.
- **Schema-on-read only**: Deferring all structure to query time makes every analysis a bespoke engineering effort. *Why*: pre-modelled data enables self-serve analytics; schema-on-read requires SQL expertise for every question.
- **Missing grain documentation**: Not specifying the grain of each fact table leads to analysts accidentally double-counting events. *Why*: if the grain is ambiguous, a "count of purchases" query may return one row per item or one row per order depending on interpretation.

## Output

**Success:**
- An analytics data model containing fact table definitions, dimension table definitions with SCD strategy, materialized view specifications, an ER diagram, a data dictionary, and a query cookbook.

**Failure:**
- The model cannot support a required query within acceptable latency. Report the query, the bottleneck, and the schema modification or pre-aggregation needed to resolve it.

## Related Skills

- [`instrumentation-spec-data`](../../analytics-lead/instrumentation-spec-data/SKILL.md) -- the event schema in the spec must align with the fact table definitions in the data model.
- [`instrumentation-implementer-data`](../instrumentation-implementer-data/SKILL.md) -- implementation produces the raw events that the data model structures.
- [`metrics-dashboard-builder`](../metrics-dashboard-builder/SKILL.md) -- dashboards query the data model; model changes affect dashboard queries.
