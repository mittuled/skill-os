# Analytics Data Model

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Data Analyst name] |
| Version | [1.0] |
| Status | [Draft / Review / Approved] |
| Skill | data-model-designer-data |
| Domain | [Product domain, e.g., Onboarding, Billing, Core Feature] |

## Executive Summary

[2-3 sentences describing the model scope, the number of tables designed, and the top query patterns it enables.

GUIDANCE: Example: "This data model covers the onboarding and activation domain, defining 2 fact tables, 4 dimension tables, and 3 materialized views. It enables activation funnel analysis, cohort retention grids, and feature discovery reporting without any ad-hoc joins against the raw event table."]

## Query Requirements

[The top questions the model must support, gathered from stakeholders.

GUIDANCE:
- Good: Each requirement includes the question, the requester, the expected query frequency, and the latency target.
- Bad: "The model should support analytics."
- Format: Numbered list.]

| # | Question | Requester | Frequency | Latency Target |
|---|---------|----------|-----------|---------------|
| 1 | [What is the 7-day activation rate by acquisition channel this week?] | [PM / Analytics Lead] | [Daily] | [< 5s] |
| 2 | [How does retention differ between users who adopted feature X vs. those who did not?] | [PM] | [Weekly] | [< 30s] |

## Fact Table Definitions

[Schema definition for each fact table.

GUIDANCE:
- Good: Every table has a grain statement, every column has a type and description, all foreign keys are listed, and partition strategy is documented.
- Bad: Just a list of column names.
- Format: One section per table.]

### `fct_[event_name]`

**Grain:** One row per [event fired / transaction completed / session started] per user.
**Partition key:** `event_date`
**Row estimate:** [N rows/day] × [N days retention] = ~[N total rows]

| Column | Type | Nullable | Description | Source |
|--------|------|---------|------------|--------|
| `event_id` | VARCHAR | NOT NULL | Unique event identifier (UUID from SDK) | `stg_events.event_id` |
| `user_id` | VARCHAR | NOT NULL | Hashed user identifier | `stg_events.user_id` |
| `anonymous_id` | VARCHAR | NOT NULL | Anonymous session identifier | `stg_events.anonymous_id` |
| `event_date` | DATE | NOT NULL | UTC date of event (partition key) | CAST(event_timestamp AS DATE) |
| `event_timestamp` | TIMESTAMP | NOT NULL | UTC timestamp of event | `stg_events.event_timestamp` |
| `dim_user_key` | INTEGER | NOT NULL | FK to dim_users surrogate key | Join on user_id + event_date |
| [additional columns] | | | | |

## Dimension Table Definitions

[Schema definition for each dimension table.

GUIDANCE:
- Good: SCD strategy explicitly stated for each dimension; SCD2 tables must have valid_from, valid_to, is_current.
- Bad: Dimension tables without SCD handling documentation.
- Format: One section per dimension.]

### `dim_users`

**SCD Type:** Type 2 (plan_tier, segment history tracked)
**Refresh:** Daily

| Column | Type | Nullable | Description | SCD Strategy |
|--------|------|---------|------------|-------------|
| `user_key` | INTEGER | NOT NULL | Surrogate key (auto-increment) | — |
| `user_id` | VARCHAR | NOT NULL | Natural key (hashed ID from source) | — |
| `plan_tier` | VARCHAR | NOT NULL | Current plan: free/pro/enterprise | Type 2 — history tracked |
| `signup_date` | DATE | NOT NULL | Date user first created account | Type 1 — immutable |
| `acquisition_channel` | VARCHAR | NULL | Attributed acquisition channel | Type 1 — set at signup |
| `valid_from` | DATE | NOT NULL | Date this dimension record became active | SCD2 marker |
| `valid_to` | DATE | NULL | Date this record was superseded (NULL = current) | SCD2 marker |
| `is_current` | BOOLEAN | NOT NULL | TRUE if this is the current version | SCD2 convenience flag |

[Repeat for each additional dimension table]

## Materialized View Definitions

[Pre-aggregated views for high-frequency queries.

GUIDANCE:
- Good: Each view has a purpose, refresh cadence, grain, and the query it is designed to serve.
- Bad: Materialized views without a purpose statement or refresh schedule.
- Format: Table.]

| View Name | Grain | Refresh | Query It Serves | Source Tables |
|-----------|-------|---------|----------------|--------------|
| `rpt_dau_by_date` | One row per date × platform × plan_tier | Daily | DAU trend dashboard | `fct_events`, `dim_users`, `dim_date` |
| `rpt_funnel_[funnel_name]` | One row per date × funnel_step | Daily | Funnel analysis dashboard | `fct_events` |
| `rpt_cohort_retention` | One row per cohort_week × period_number | Weekly | Cohort retention grid | `fct_events`, `dim_users` |

## Entity-Relationship Summary

[Describe the relationships between tables.

GUIDANCE:
- Good: List each relationship as "fct_events.dim_user_key → dim_users.user_key (many-to-one)".
- Bad: A vague ER description without explicit keys.
- Format: Bullet list or table.]

| From Table | Key | Relationship | To Table | Key |
|-----------|-----|-------------|---------|-----|
| `fct_events` | `dim_user_key` | Many-to-one | `dim_users` | `user_key` |
| `fct_events` | `event_date` | Many-to-one | `dim_date` | `date_day` |

## Query Cookbook

[Example queries for the most common analytical questions.

GUIDANCE:
- Include at least one query per query requirement listed above.
- Each query should run correctly against the model as designed.
- Format: SQL code blocks with one-line purpose comment.]

```sql
-- 7-day activation rate by acquisition channel (uses rpt_funnel_activation + dim_users)
SELECT
    u.acquisition_channel,
    COUNT(DISTINCT CASE WHEN f.completed_step = 'activation_completed' THEN f.user_id END)
        / NULLIF(COUNT(DISTINCT f.user_id), 0) AS activation_rate
FROM rpt_funnel_activation f
JOIN dim_users u ON f.user_id = u.user_id AND u.is_current = TRUE
WHERE f.event_date >= CURRENT_DATE - 7
GROUP BY 1
ORDER BY 2 DESC;
```

## Migration Plan

[If this model modifies or replaces an existing schema, document the migration path.

GUIDANCE:
- Good: Step-by-step migration with backfill strategy, cutover date, and downstream impact list.
- Bad: "We'll migrate the schema" with no steps.
- Format: Numbered list with dates.]

## Recommendations

[Prioritized list of model improvements or next steps.

GUIDANCE:
- P1: Schema changes required before the model is production-ready.
- P2: Additional materialized views to add in the next iteration.
- P3: Performance optimizations deferred until query profiling reveals bottlenecks.]

## Appendices

### A. Methodology

[Kimball vs. Data Vault decision, SCD type decisions and rationale, warehouse engine (Snowflake/BigQuery/Redshift) and engine-specific optimizations applied.]

### B. Supporting Data

[ER diagram image/link, dbt model DAG, sample data for validation, query performance test results.]
