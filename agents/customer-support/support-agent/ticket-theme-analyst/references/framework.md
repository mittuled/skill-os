# Framework: Ticket Theme Analysis

Defines the methodology for identifying recurring support ticket themes and translating them into actionable product and documentation signals.

## Analysis Architecture

### Data Requirements

| Field | Required | Purpose |
|-------|----------|---------|
| Ticket ID | Yes | Deduplication |
| Creation timestamp | Yes | Period filtering and trend analysis |
| Category / Product area | Yes | Primary clustering dimension |
| Severity / Priority | Yes | Impact weighting |
| Resolution type | Yes | Signal classification (agent-resolved vs. escalated) |
| Customer tier | Yes | Impact scoring |
| Resolution time | Yes | Effort measurement |
| Tags | Recommended | Secondary clustering |
| Customer verbatim | Recommended | Qualitative signal extraction |

**Minimum sample size**: 50 tickets per analysis period. Below this threshold, report with a confidence caveat rather than drawing conclusions.

### Clustering Methodology

| Pass | Grouping Dimension | Output |
|------|--------------------|--------|
| 1 — Primary | Product area + issue type | Coarse theme clusters |
| 2 — Secondary | Root cause (bug / docs gap / UX confusion / missing feature) | Refined theme clusters |
| 3 — Merge | Semantic similarity of customer verbatim | Final theme list with merged duplicates |

### Theme Ranking Formula

**Theme Score** = (Ticket Count × 1.0) + (Enterprise Ticket Count × 2.0) + (Escalation Count × 1.5) + (Average Resolution Time in hours × 0.1)

Higher scores indicate themes with more customer impact and operational cost.

## Signal Classification

| Signal Type | Indicators | Recommended Owner |
|-------------|-----------|-------------------|
| Product Bug | Reproducible error, workaround needed, escalated to engineering | Engineering backlog |
| Documentation Gap | "I couldn't find how to…", help article cited but unhelpful, agent resolved by pointing to docs | Support + Content |
| UX Confusion | "I didn't know where to…", repeated questions about feature location | Product / Design |
| Missing Feature | "Can I…?" that the answer is "No", competitor comparison, feature request | Product backlog |
| Onboarding Friction | New customers, first 30 days, configuration or setup questions | Implementation + CS |

## Reporting Cadence

| Report Type | Frequency | Audience | Ticket Volume Threshold |
|-------------|-----------|----------|------------------------|
| Weekly snapshot | Weekly | Support Manager | ≥ 20 tickets |
| Monthly theme report | Monthly | Product, CS, Support | ≥ 100 tickets |
| Quarterly deep-dive | Quarterly | Leadership, Product roadmap | All tickets in period |
| Spike alert | On trigger | Support Manager, Product | >2× baseline volume in 48h |
