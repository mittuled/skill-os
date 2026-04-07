# Framework: Data Warehouse Schema Designer

Defines dimensional modeling standards for designing production-grade data warehouse schemas.

## Modeling Methodology: Kimball Dimensional Modeling

### Step 1: Identify the Business Process

Define in one sentence: "This model measures [business process] at the grain of [one row per X]."

Example: "This model measures product purchase events at the grain of one row per line item per order."

Never proceed without a documented grain statement.

### Step 2: Identify Dimensions (The "Who, What, Where, When, How")

| Question | Dimension | Example |
|---------|----------|---------|
| Who | Customer / User | `dim_users` |
| What | Product / Feature | `dim_products` |
| Where | Location / Channel | `dim_channels` |
| When | Date / Time | `dim_date` |
| How | Method / Source | `dim_payment_methods` |

### Step 3: Identify Facts (Measurable Events)

Facts are numeric or boolean measures captured at the grain event:
- Revenue amount, quantity, duration, count
- Boolean flags (is_first_purchase, is_trial_conversion)

Never store descriptive text in a fact table — that belongs in a dimension.

## Slowly Changing Dimension (SCD) Decision Tree

```
Does this attribute ever change for a given entity?
  └── No → Store in dimension with updated_at; Type 1 (overwrite)
  └── Yes → Does historical analysis need the old value?
        └── No → Type 1 (overwrite; add updated_at)
        └── Yes → Type 2 (add valid_from, valid_to, is_current)
```

**SCD Type 2 mandatory for**: plan_tier, pricing_tier, account_owner, company_segment, geographic_region.
**SCD Type 1 acceptable for**: display_name, email, phone (current value only needed).

## Physical Schema Design by Engine

### Snowflake
```sql
-- Fact table: cluster by date and high-cardinality join key
CREATE TABLE fct_orders (
  order_key        INTEGER NOT NULL,
  order_date       DATE NOT NULL,
  user_key         INTEGER NOT NULL,
  ...
)
CLUSTER BY (order_date, user_key);

-- Dimension table: no clustering needed; small tables fit in micro-partitions
CREATE TABLE dim_users (
  user_key         INTEGER NOT NULL,
  user_id          VARCHAR(36) NOT NULL,
  ...
);
```

### BigQuery
```sql
-- Fact table: partition by ingestion date or event date; cluster on high-cardinality join
CREATE TABLE fct_orders
PARTITION BY order_date
CLUSTER BY user_id, product_id
AS ...;
```

### Redshift
```sql
-- Fact table: DISTKEY on most common join column; SORTKEY on date + join
CREATE TABLE fct_orders (
  ...
)
DISTSTYLE KEY DISTKEY(user_id)
SORTKEY(order_date, user_id);

-- Dimension table: DISTSTYLE ALL for small tables
CREATE TABLE dim_users (
  ...
)
DISTSTYLE ALL;
```

## Naming Conventions

| Object | Convention | Example |
|--------|-----------|---------|
| Fact tables | `fct_<business_process>` | `fct_orders`, `fct_events` |
| Dimension tables | `dim_<entity>` | `dim_users`, `dim_products` |
| Staging tables | `stg_<source>__<entity>` | `stg_salesforce__opportunities` |
| Intermediate models | `int_<description>` | `int_events_with_user_context` |
| Reporting views | `rpt_<report_name>` | `rpt_dau_by_date` |
| Surrogate keys | `<table>_key` | `user_key`, `order_key` |
| Natural keys | `<entity>_id` | `user_id`, `order_id` |
| Date dimensions | `<context>_date` | `order_date`, `event_date` |
| Timestamps | `<context>_at` | `created_at`, `updated_at`, `loaded_at` |

## Query Performance Validation Protocol

For each query requirement, document:
1. The query (written against the designed schema)
2. The expected execution plan (no full table scans on fact tables > 1M rows)
3. The measured latency (run against representative data volume)
4. The pass/fail status (target: <5s for dashboard queries, <30s for analytical queries)
