# North Star Metric Review Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Analytics Lead / name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | north-star-metric-reviewer-data |
| Review Period | [e.g., Q2 2026 — quarterly or ad-hoc] |
| Current North Star | [Metric name and formula] |

## Executive Summary

[2–3 sentences with the verdict and key supporting data.
GUIDANCE: State the retain/refine/replace recommendation first, then cite the top 1–2 data points that drove it. Example: "The north star metric 'Weekly Active Creators' retains a Pearson r of 0.76 with 90-day revenue and is targeted by 3 active experiments, supporting a retain decision. One instrumentation gap on Android (12% of users) reduces the measurability score and should be resolved this sprint."]

**Verdict**: [ Retain / Refine / Replace ]

**Overall Grade**: [ A+ / A / B / C / D / F ] — Composite Score: [ X.X / 10 ]

## Scoring Summary

[Scores per criterion with brief evidence note.

GUIDANCE:
- Good: "Correlation: 7.5 — Pearson r = 0.72 with revenue; n = 95 days; p = 0.003"
- Bad: "Correlation is good"
- Format: Table below]

| # | Criterion | Weight | Raw Score (0–10) | Weighted Score | Key Evidence |
|---|-----------|--------|-----------------|---------------|-------------|
| 1 | Revenue & Retention Correlation | 30% | [0–10] | [score × 0.30] | [Pearson r value, p-value, sample size] |
| 2 | Actionability | 25% | [0–10] | [score × 0.25] | [# experiments, % that moved metric] |
| 3 | Measurability | 20% | [0–10] | [score × 0.20] | [% platform coverage, data quality status] |
| 4 | Definition Clarity | 15% | [0–10] | [score × 0.15] | [# stakeholders surveyed, # aligned] |
| 5 | Business Model Fit | 10% | [0–10] | [score × 0.10] | [last business model change date] |
| **Total** | | **100%** | — | **[sum]** | |

## Correlation Analysis

[Results of the statistical correlation analysis between the north star and business outcomes.

GUIDANCE:
- Good: "Pearson r = 0.72 (p = 0.003) between weekly active creators and 90-day revenue over 95 days. Day-30 retention correlation: r = 0.68 (p = 0.007). Both exceed the 0.5 threshold."
- Bad: "Metric correlates with revenue"
- Include: Pearson r values, p-values, sample window, confounders identified]

| Outcome Metric | Pearson r | p-value | Sample (days) | Threshold Met? |
|---------------|-----------|---------|---------------|---------------|
| 90-day revenue | [r] | [p] | [n] | [Yes / No — threshold 0.5] |
| Day-30 retention | [r] | [p] | [n] | [Yes / No] |
| Day-7 retention | [r] | [p] | [n] | [Yes / No] |

**Confounders**: [List any external factors (seasonality, marketing campaigns, competitor events) that may inflate or suppress the correlation.]

## Actionability Assessment

[Evidence that product or growth levers demonstrably move the north star.

GUIDANCE:
- Good: "3 experiments in Q1 targeted the north star. 2 reached significance: Feature X (+4.2% lift, p=0.02) and Onboarding change Y (+2.8% lift, p=0.04). 1 was inconclusive."
- Bad: "Teams run experiments that affect this metric"
- Format: Table of experiments + documented levers]

| Experiment | Date | Target Lever | Result | North Star Movement |
|-----------|------|-------------|--------|---------------------|
| [Name] | [YYYY-MM-DD] | [Lever] | [Significant / Inconclusive / No-ship] | [+/- % or n/a] |

**Validated levers**: [List the 3 product/growth levers confirmed to move the metric with evidence.]

## Measurability Audit

[Instrumentation coverage and data quality status.

GUIDANCE:
- Good: "Web: 100% covered. iOS: 97% (1 edge case in background-refresh sessions). Android: 88% — missing in-app purchase events since v3.2. Data warehouse refresh SLA: 2 hours — met in 98.5% of windows last 30 days."
- Bad: "Data is mostly available"]

| Platform | Coverage | Known Gaps | Data Quality Issues (last 30 days) |
|---------|----------|-----------|-------------------------------------|
| Web | [%] | [None / description] | [None / count and type] |
| iOS | [%] | [None / description] | [None / count and type] |
| Android | [%] | [None / description] | [None / count and type] |
| Server | [%] | [None / description] | [None / count and type] |

**Data refresh SLA**: [Defined SLA] — [Met / Breached in X% of windows last 30 days]

## Definition Clarity Survey

[Stakeholder survey results.

GUIDANCE:
- Survey 3–5 stakeholders from PM, growth, and engineering
- Ask each to state the metric definition in their own words — do not prompt with the official definition
- Good: "5 stakeholders surveyed. 4 stated identical definition. 1 PM used a 7-day window instead of the official 14-day window — corrected during session."
- Bad: "Stakeholders understand the metric"]

| Stakeholder | Role | Stated Definition | Aligned? | Divergence |
|------------|------|------------------|----------|-----------|
| [Name] | [Role] | [Their definition] | [Yes/No] | [Description if no] |

## Recommendations

[Prioritized actions based on findings.

GUIDANCE:
- P1: Actions required before the next planning cycle to prevent misaligned decisions
- P2: Quality improvements that reduce measurement risk this quarter
- P3: Longer-term enhancements to improve sensitivity or coverage]

- **P1**: [Specific action — e.g., "Fix Android in-app purchase instrumentation gap to restore 100% platform coverage; assign to data-analyst; target: next sprint"]
- **P2**: [Specific action]
- **P3**: [Specific action]

## Appendices

### A. Methodology

[Correlation analysis method, data source, time window, and tools used. Note any adjustments for seasonality or outliers.]

### B. Survey Questions

[The exact questions asked in the definition clarity survey.]

### C. Historical North Star Trend

[Chart or table showing the north star metric trend over the past 6 months, annotated with product releases and experiments.]
