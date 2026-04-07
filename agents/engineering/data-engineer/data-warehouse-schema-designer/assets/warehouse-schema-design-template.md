# Warehouse Schema Design

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Data Engineer name] |
| Version | [1.0] |
| Status | [Draft / Review / Approved] |
| Skill | data-warehouse-schema-designer |
| Domain | [Business domain, e.g., Orders, User Behaviour, Subscriptions] |
| Target Engine | [Snowflake / BigQuery / Redshift / DuckDB] |

## Executive Summary

[2-3 sentences describing the business process modeled, the grain, and the top query patterns enabled.

GUIDANCE: Example: "This schema models the subscription lifecycle at the grain of one row per plan tier change per subscriber, enabling monthly cohort retention analysis, upgrade/downgrade funnel tracking, and MRR movement attribution without requiring cross-table joins at query time."]

**Business process:** [Description]
**Grain statement:** One row per [event/transaction/entity change] per [unit].

## Business Process and Grain

[Formal grain documentation.

GUIDANCE:
- Good: "One row per product purchase line item. An order with 3 line items produces 3 rows. Subscription renewals are separate rows from initial purchases."
- Bad: "One row per order" without specifying whether line items are rolled up.
- Format: Prose grain statement + known edge cases.]

**Grain:** [Grain statement]
**Known edge cases:**
- [Edge case and how it is handled]

## Dimensional Model Diagram

[Entity-relationship overview.

GUIDANCE: Include a textual representation of the star schema if a visual diagram is not attached. List each table and its connections.
- Format: Bulleted list of relationships, or reference to attached diagram.]

**Fact tables:** [List]
**Dimension tables:** [List]
**Key relationships:**
- `fct_[name].[key]` → `dim_[name].[key]` (many-to-one)

## Fact Table Definitions

[DDL and documentation for each fact table.

GUIDANCE:
- Good: Every column has type, nullability, description, and source lineage.
- Bad: Column list without types or source.
- Format: DDL block + column dictionary table.]

### `fct_[business_process]`

**Row estimate:** [N rows/day × N days] ≈ [N total]
**Partition key:** `[date_column]`
**Engine-specific config:** [CLUSTER BY / PARTITION BY / DISTKEY / SORTKEY — specify for target engine]

```sql
CREATE TABLE fct_[business_process] (
  [table_key]      INTEGER       NOT NULL,   -- Surrogate key
  [date_column]    DATE          NOT NULL,   -- Partition key
  [user_key]       INTEGER       NOT NULL,   -- FK to dim_users
  [measure_1]      DECIMAL(18,2) NOT NULL,   -- [Business measure description]
  [flag_1]         BOOLEAN       NOT NULL    -- [Flag description]
  -- add columns as needed
)
[ENGINE-SPECIFIC PARTITIONING/CLUSTERING];
```

| Column | Type | Nullable | Description | Source |
|--------|------|---------|------------|--------|
| [column] | [type] | [NOT NULL / NULL] | [Description] | [Source table.field] |

## Dimension Table Definitions

[DDL and documentation for each dimension table.

GUIDANCE:
- Good: SCD type explicitly stated; SCD2 tables have valid_from, valid_to, is_current.
- Bad: Dimension tables without SCD documentation.
- Format: One section per dimension.]

### `dim_[entity]`

**SCD Type:** [1 / 2 / 3]
**Refresh:** [Daily / Real-time]

```sql
CREATE TABLE dim_[entity] (
  [entity]_key     INTEGER      NOT NULL,    -- Surrogate key
  [entity]_id      VARCHAR(36)  NOT NULL,    -- Natural key
  [attribute_1]    VARCHAR(50)  NOT NULL,    -- [Description] — [SCD1/SCD2]
  [attribute_2]    VARCHAR(20)  NULL,        -- [Description] — [SCD1/SCD2]
  valid_from       DATE         NOT NULL,    -- SCD2: start of validity
  valid_to         DATE         NULL,        -- SCD2: end of validity (NULL = current)
  is_current       BOOLEAN      NOT NULL     -- SCD2: TRUE if current version
);
```

## Naming Convention Compliance

[Confirm all objects follow the naming standard.

GUIDANCE:
- Fact tables: `fct_` prefix
- Dimension tables: `dim_` prefix
- Staging: `stg_` prefix
- Surrogate keys: `<table>_key`
- Natural keys: `<entity>_id`
- Format: Checklist.]

- [ ] All fact tables use `fct_` prefix
- [ ] All dimension tables use `dim_` prefix
- [ ] All surrogate keys named `<table>_key`
- [ ] All timestamps named `<context>_at` in UTC
- [ ] All date columns named `<context>_date`

## Query Performance Validation

[Results of running representative queries against the designed schema.

GUIDANCE:
- Good: Each query requirement from the requirements gathering step is tested with observed latency.
- Bad: "Queries look fast."
- Format: Table.]

| Query # | Description | Observed Latency | Target Latency | Status |
|---------|------------|----------------|---------------|--------|
| 1 | [Description] | [Xs] | [< N s] | [PASS / FAIL] |

## Recommendations

[Prioritized design improvements or implementation notes.

GUIDANCE:
- P1: Schema changes required before production deployment.
- P2: Indexing or clustering improvements deferred until query profiling confirms need.
- P3: Additional dimensions or reporting views to add in future iterations.]

## Appendices

### A. Methodology

[Kimball methodology reference, SCD type decisions and rationale, engine-specific optimization choices and why they were made.]

### B. Supporting Data

[ER diagram image, representative query set used for validation, DDL migration scripts, data dictionary export.]
