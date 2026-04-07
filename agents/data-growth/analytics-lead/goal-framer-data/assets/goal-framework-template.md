# Analytics Goal Framework

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Analytics Lead name] |
| Planning Period | [Q1 2025 / H1 2025 / FY 2025] |
| Version | [1.0] |
| Status | [Draft / Aligned / Locked] |
| Skill | goal-framer-data |

## Executive Summary

[2-3 sentences describing the scope of this goal framework — which business objectives are covered, how many metrics are defined, and the planning period.

GUIDANCE: Lead with the planning period and coverage. Example: "This framework defines 12 analytics goals across 4 business objectives for Q2 2025. Metrics span acquisition, activation, retention, and revenue, each with explicit calculation definitions, baselines, and targets aligned to the annual plan."]

## Business Objectives

[List the top 3-5 outcomes the organization is optimizing for this period.

GUIDANCE:
- Good: Specific, time-bound objectives tied to company strategy.
- Bad: Generic statements ("grow the business").
- Format: Numbered list with one-sentence description per objective.]

1. [Objective 1: e.g., Increase paid conversion rate from free trial]
2. [Objective 2: e.g., Improve 30-day retention for new users]
3. [Objective 3: e.g., Expand average revenue per account]

## Metric Definitions

[For each objective, define the metrics. Repeat the table block per objective.]

### Objective 1: [Name]

| Field | Value |
|-------|-------|
| Primary Metric | [Metric name] |
| Metric Type | [Leading / Lagging] |
| Calculation | [Numerator ÷ Denominator × 100; time window; cohort definition] |
| Data Source | [Warehouse table or analytics platform] |
| Refresh Cadence | [Daily / Weekly / Monthly] |

### Objective 2: [Name]

| Field | Value |
|-------|-------|
| Primary Metric | [Metric name] |
| Metric Type | [Leading / Lagging] |
| Calculation | [Numerator ÷ Denominator × 100; time window; cohort definition] |
| Data Source | [Warehouse table or analytics platform] |
| Refresh Cadence | [Daily / Weekly / Monthly] |

### Objective 3: [Name]

| Field | Value |
|-------|-------|
| Primary Metric | [Metric name] |
| Metric Type | [Leading / Lagging] |
| Calculation | [Numerator ÷ Denominator × 100; time window; cohort definition] |
| Data Source | [Warehouse table or analytics platform] |
| Refresh Cadence | [Daily / Weekly / Monthly] |

## Baseline and Target Summary

| Objective | Metric | Baseline (30d) | Baseline (90d) | Minimum Target | Stretch Target | Target Date |
|-----------|--------|---------------|---------------|----------------|----------------|-------------|
| [Obj 1] | [metric_name] | [value] | [value] | [+X%] | [+X%] | [YYYY-MM-DD] |
| [Obj 2] | [metric_name] | [value] | [value] | [+X%] | [+X%] | [YYYY-MM-DD] |
| [Obj 3] | [metric_name] | [value] | [value] | [+X%] | [+X%] | [YYYY-MM-DD] |

GUIDANCE for targets:
- Minimum target = achievable with current trajectory + focused effort.
- Stretch target = achievable with optimal execution and favorable conditions.
- Document the method used to set targets (historical rate, industry benchmark, model-based).

## Seasonality and Context Notes

[Document any trends, seasonality, or external context that affects baseline interpretation or target realism.

GUIDANCE: Note quarter-end spikes, holiday effects, market headwinds, or prior-period anomalies. Example: "Q4 2024 conversion baseline is elevated due to a Black Friday promotion; Q1 2025 targets adjust for normalization."]

- [Seasonality note 1]
- [Seasonality note 2]

## Measurement Plan

| Metric | Data Source Table | Query Owner | Dashboard Location | Alert Threshold | Instrumentation Confirmed? |
|--------|------------------|-------------|-------------------|-----------------|---------------------------|
| [metric_name] | [db.schema.table] | [Name] | [URL or dashboard name] | [value] | [Yes / No — see gap below] |
| [metric_name] | [db.schema.table] | [Name] | [URL or dashboard name] | [value] | [Yes / No] |

## Instrumentation Gaps

[List any metrics that cannot currently be measured due to missing events or properties.

GUIDANCE: For each gap, specify the missing event, the platform where it needs to be instrumented, and the instrumentation spec reference.]

| Metric | Missing Event or Property | Platform | Instrumentation Spec Reference | Estimated Fix Date |
|--------|--------------------------|----------|-------------------------------|-------------------|
| [metric_name] | [event_name / property] | [iOS / Web / Server] | [Link to spec] | [YYYY-MM-DD] |

## Stakeholder Sign-Off

| Stakeholder | Role | Status | Date |
|-------------|------|--------|------|
| [Name] | [CEO / CPO / Head of Product] | [Pending / Approved] | [YYYY-MM-DD] |
| [Name] | [VP Growth / Analytics Lead] | [Pending / Approved] | [YYYY-MM-DD] |

## Change Log

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | [YYYY-MM-DD] | [Name] | Initial draft |
