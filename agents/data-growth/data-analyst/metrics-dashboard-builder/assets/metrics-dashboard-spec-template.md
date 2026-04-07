# Metrics Dashboard Spec

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Data Analyst name] |
| Version | [1.0] |
| Status | [Draft / Review / Published] |
| Skill | metrics-dashboard-builder |
| Dashboard Name | [Dashboard name] |
| Dashboard URL | [Link once published] |

## Executive Summary

[2-3 sentences describing the dashboard purpose, audience, and key metrics it surfaces.

GUIDANCE: Example: "The Activation Dashboard provides the product team with daily visibility into the onboarding funnel, feature discovery rates, and time-to-activation by cohort. It replaces three ad-hoc SQL queries run weekly by the PM and engineering teams."]

## Requirements

[Who uses this dashboard and what questions it must answer.

GUIDANCE:
- Good: "PM Rania needs to know daily whether activation rate is trending toward the Q2 target; engineer Soji needs to spot error-rate regressions within hours."
- Bad: "Stakeholders need to see metrics."
- Format: Bullet list with audience and specific question.]

**Audience:** [Role(s)]
**Primary questions this dashboard must answer:**
- [Question 1]
- [Question 2]

**Refresh cadence:** [Real-time / Hourly / Daily at HH:MM UTC / Weekly]

## Metric Definitions

[Full definition for every metric on the dashboard.

GUIDANCE:
- Good: SQL definition + data source + refresh cadence + owner for every metric.
- Bad: Just the metric name.
- Format: Table.]

| Metric Name | Business Definition | Technical Definition (SQL or BI expression) | Data Source | Refresh | Owner |
|------------|--------------------|--------------------------------------------|------------|---------|-------|
| [Metric name] | [Plain English definition] | `[SQL or BI expression]` | [Table name] | [Cadence] | [Name] |

## Layout Design

[Dashboard structure with section descriptions and chart assignments.

GUIDANCE:
- Good: Section headers with chart type, metric, and purpose for each visualization.
- Bad: "Charts will be arranged on the dashboard."
- Format: Numbered sections with chart list.]

### Section 1: [Theme, e.g., North Star]
1. **[Chart title]** — [Chart type] — Metric: [name] — Comparison: [WoW / target line / cohort baseline] — Purpose: [one sentence]

### Section 2: [Theme]
2. **[Chart title]** — [Chart type] — Metric: [name] — Comparison: [type]
3. **[Chart title]** — [Chart type] — Metric: [name] — Comparison: [type]

### Section [N]: [Theme]
[Continue as needed]

## Filter / Segment Configuration

[All interactive filters available to dashboard users.

GUIDANCE:
- Good: Every filter has a default value and a list of valid options.
- Bad: "Date filter and some segment options."
- Format: Table.]

| Filter | Type | Default Value | Options |
|--------|------|--------------|---------|
| Date range | Date picker | Last 30 days | Custom range, MTD, QTD, YTD |
| Cohort | Dropdown | All | [Acquisition channel / Plan tier / Signup week] |
| Platform | Multi-select | All | Web, iOS, Android |

## Accuracy Validation Results

[Results of cross-check against raw SQL for the same period.

GUIDANCE:
- Good: Table showing dashboard value vs. raw query value for each metric for a specific validation date.
- Bad: "Values look correct."
- Format: Table with validation date.]

**Validation date:** [YYYY-MM-DD]

| Metric | Dashboard Value | Raw SQL Value | Variance | Status |
|--------|----------------|--------------|---------|--------|
| [Metric name] | [value] | [value] | [< 1% / N] | [PASS / FAIL] |

## Recommendations

[Prioritized improvements or follow-on work.

GUIDANCE:
- P1: Any accuracy issues found during validation that must be fixed before the dashboard is shared widely.
- P2: Missing metrics that stakeholders requested but were deferred.
- P3: Performance improvements (slow queries, caching opportunities).]

## Appendices

### A. Methodology

[Data model tables referenced, join logic for complex metrics, materialized view names, and BI tool configuration details.]

### B. Supporting Data

[Raw SQL queries used for accuracy validation, stakeholder requirements gathered in interviews, prior dashboard versions deprecated by this one.]
