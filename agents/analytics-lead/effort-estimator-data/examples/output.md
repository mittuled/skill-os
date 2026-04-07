# Analytics Effort Estimate: Onboarding Funnel Analytics

| Field | Value |
|-------|-------|
| Date | 2026-03-31 |
| Analytics Lead | Analytics Lead |
| Initiative | Onboarding Funnel Analytics |
| Complexity | Medium (1.3x multiplier) |
| Total Estimate | 30 days (6.0 weeks) |
| Skill | effort-estimator-data |

## Component Breakdown

| Component | Type | Size | Base Days | Adjusted Days | Description |
|-----------|------|------|-----------|--------------|-------------|
| Onboarding event instrumentation | Instrumentation | M | 7 | 9 | 11-25 events, custom properties, cross-platform |
| Funnel data pipeline (dbt) | Pipeline | M | 7 | 9 | New data source ingestion + model |
| Onboarding conversion dashboard | Dashboard | M | 5 | 7 | New dashboard with new metrics |
| **Subtotal** | | | **19** | **25** | |
| Testing + QA buffer (20%) | | | | **5** | |
| **Total** | | | | **30 days** | |

## Summary

| Metric | Value |
|--------|-------|
| Subtotal (before buffer) | 25 days |
| Testing and QA buffer | 5 days |
| **Total estimate** | **30 days (6.0 weeks)** |
| Complexity multiplier applied | 1.3x (medium) |
| Confidence level | Medium |

## Assumptions and Risks

- Requirements are stable — scope changes will require re-estimation
- No blocking data quality issues in existing event schemas
- Instrumentation assumes existing analytics SDK is installed; new SDK setup adds 3-5 days
- dbt pipeline assumes BigQuery/Snowflake is already configured as the data warehouse
- Dashboard assumes Looker, Metabase, or similar BI tool is already set up

## Confidence Note

Medium confidence. Estimate will be revised after instrumentation spec review — complex property schemas or cross-platform edge cases may increase instrumentation size to L.
