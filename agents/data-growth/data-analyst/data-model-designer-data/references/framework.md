# Framework: Analytics Data Model Designer

Defines the dimensional modeling standards for analytics data warehouse schemas.

## Schema Architecture Layers

| Layer | Purpose | Naming Prefix | Tools |
|-------|---------|--------------|-------|
| Raw / Source | Unmodified source data as landed | `raw_` | Fivetran, Stitch, Airbyte |
| Staging | Cleaned, typed, renamed source data | `stg_` | dbt models |
| Intermediate | Joined or enriched but not yet aggregated | `int_` | dbt models |
| Mart (Facts) | Business events at atomic grain | `fct_` | dbt models |
| Mart (Dimensions) | Entity attributes with SCD handling | `dim_` | dbt models |
| Reporting | Pre-aggregated for dashboard queries | `rpt_` | dbt models or BI materializations |

## Star Schema Design Principles

### Fact Table Design

| Principle | Rule |
|-----------|------|
| Grain | Define the grain before adding any columns: "one row per [event/transaction/session]" |
| Keys | Foreign keys to all relevant dimensions; surrogate keys (integer) not natural keys |
| Measures | Only numeric or boolean facts; no descriptive attributes (those belong in dimensions) |
| Timestamps | Store in UTC; include both `event_timestamp` (raw) and `event_date` (date-only partition key) |
| Partition key | `event_date` for time-series facts; `created_date` for transactional facts |

### Dimension Table Design

| Principle | Rule |
|-----------|------|
| SCD Type 1 | Attributes that can be overwritten (e.g., display_name). Add `updated_at` column. |
| SCD Type 2 | Attributes where history matters (e.g., plan_tier, company_segment). Add `valid_from`, `valid_to`, `is_current`. |
| User dimension | Always SCD Type 2 for plan_tier, segment, and account_owner |
| Date dimension | Static calendar table with date, week, month, quarter, year, is_weekday, fiscal_period |

## Materialized View Strategy

| View Name Pattern | Content | Refresh Cadence | Use Case |
|------------------|---------|----------------|---------|
| `rpt_dau_by_date` | Daily active users per date, platform, plan tier | Daily | DAU trend dashboards |
| `rpt_funnel_step_<funnel>` | Step-level conversion counts per day | Daily | Funnel dashboards |
| `rpt_cohort_retention` | Retention rates by cohort week and period | Weekly | Cohort retention grids |
| `rpt_feature_adoption` | Feature adoption by cohort and adoption criteria | Weekly | Feature adoption dashboards |

## Query Performance Standards

| Scenario | Optimization |
|---------|-------------|
| DAU query over 1 year | Partition by `event_date`; query `rpt_dau_by_date` not `fct_events` |
| Cohort retention (12+ months) | Pre-compute in `rpt_cohort_retention`; avoid re-computing from raw events |
| Funnel analysis | Use `rpt_funnel_step_*` views; avoid scanning raw event table for each step |
| User-level join (events + attributes) | Join `fct_events` to `dim_users` on `user_id` + `valid_from <= event_date <= valid_to` for SCD2 accuracy |

## Data Dictionary Requirements

Every column in every mart table must have:

| Field | Example |
|-------|---------|
| Column name | `plan_tier` |
| Data type | `VARCHAR(20)` |
| Description | "User's subscription plan at the time of the event (SCD2)" |
| Allowed values / enum | `['free', 'pro', 'enterprise', 'unknown']` |
| Nullable | `NOT NULL` |
| Source lineage | `stg_stripe.subscription_tier` |

## Grain Documentation Template

```
Table: fct_events
Grain: One row per analytics event fire, per user, per session.
Duplicates: User-session-event triples are deduplicated; a single user action may
            produce at most one row per event name per session.
Known gaps: Events fired offline on mobile are batched and may arrive out of order;
            event_timestamp reflects fire time, not receipt time.
```
