# Revenue Funnel Analysis Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [RevOps analyst name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | revenue-funnel-analyst |
| Analysis Period | [YYYY-MM-DD to YYYY-MM-DD] |
| Data Source | [CRM name + extraction date] |

## Executive Summary

[2-3 sentences covering: overall funnel health, the primary bottleneck, and the highest-priority recommendation. Example: "The Q3 2025 funnel analysis covering 412 MQLs shows a healthy MQL-to-SQL conversion of 68% but a critical SQO-to-Closed-Won drop to 12% (benchmark: 25%). The primary bottleneck is mid-market deals stalling in legal review for an average of 47 days. The highest-impact action is a standardised MSA template to reduce legal cycle time."]

## Funnel Snapshot

[Overall conversion rates and volume for the analysis period.

GUIDANCE: Compare each rate against the benchmark from the framework. Highlight rates outside benchmark in bold.]

| Stage Transition | Volume In | Volume Out | Conversion Rate | Benchmark | Variance |
|-----------------|-----------|-----------|-----------------|-----------|----------|
| MQL → SAL | [N] | [N] | [%] | 60-75% | [+/- %] |
| SAL → SQL | [N] | [N] | [%] | 40-60% | [+/- %] |
| SQL → SQO | [N] | [N] | [%] | 50-70% | [+/- %] |
| SQO → Closed-Won | [N] | [N] | [%] | 20-35% | [+/- %] |
| **MQL → Closed-Won** | **[N]** | **[N]** | **[%]** | **5-15%** | **[+/- %]** |

## Velocity Analysis

[Average time in each stage.

GUIDANCE: Flag stages exceeding the benchmark with the count of deals affected and the revenue at risk.]

| Stage | Avg Days | Benchmark | Deals > Benchmark | Revenue at Risk |
|-------|----------|-----------|-------------------|-----------------|
| MQL → SQL | [days] | 5-14 days | [N] | [$ ARR] |
| SQL → SQO | [days] | 7-21 days | [N] | [$ ARR] |
| SQO → Closed-Won | [days] | 14-60 days | [N] | [$ ARR] |

## Segmented Analysis

[Conversion and velocity broken down by the highest-signal dimensions.

GUIDANCE:
- Good: Show the 2-3 dimensions with the most variance (e.g., "Enterprise SQO→Won = 18% vs. SMB = 32% — 14-point gap")
- Bad: Reporting only aggregate totals
- Format: One table per dimension showing conversion and velocity comparison]

### By Deal Size

| Segment | MQL→SQL | SQL→SQO | SQO→Won | Avg Cycle (days) |
|---------|---------|---------|---------|------------------|
| SMB (< $10k ARR) | [%] | [%] | [%] | [days] |
| Mid-Market ($10k-$100k ARR) | [%] | [%] | [%] | [days] |
| Enterprise (> $100k ARR) | [%] | [%] | [%] | [days] |

### By Lead Source

| Source | Volume | MQL→Won | Notes |
|--------|--------|---------|-------|
| [Channel] | [N] | [%] | [Observation] |

## Bottleneck Analysis

[Detailed breakdown of stages with below-benchmark conversion or velocity.

GUIDANCE:
- For each bottleneck, state the severity (using the framework severity classification), the root cause hypothesis, supporting evidence, and proposed fix.
- Format: One subsection per bottleneck, ranked by severity]

### Bottleneck 1: [Stage transition] — [Severity: Normal/Watch/Warning/Critical]

| Field | Value |
|-------|-------|
| Conversion Rate | [%] vs. [benchmark]% benchmark |
| Gap | [- %pts] |
| Revenue at Risk | [$ ARR stuck in or lost at this stage] |
| Root Cause Hypothesis | [e.g., Legal review cycle > 45 days on Enterprise deals] |
| Supporting Evidence | [e.g., 78% of Enterprise SQO→Lost deals cite "timing" as lost reason; median legal stage = 47 days] |
| Proposed Fix | [e.g., Standardise MSA template; pre-negotiate DPA with top 20 prospects] |
| Proposed Owner | [Team] |

## Recommendations

[Prioritised, actionable improvements with expected funnel impact.

GUIDANCE: Quantify the expected impact where possible (e.g., "If SQO→Won improves from 12% to 20%, that is [N] additional closed deals at current volume, or $[X] ARR").

| Priority | Recommendation | Owner | Expected Impact | Deadline |
|----------|---------------|-------|----------------|----------|
| P1 | [Specific action] | [Team] | [Impact estimate] | [Date] |
]

## Appendices

### A. Methodology

[CRM query logic, deal inclusion/exclusion criteria, how stage timestamps were calculated, and any data quality issues encountered.]

### B. Trend Comparison

[Current period conversion rates vs. previous 2 periods to show direction of change.]

| Stage | 2 Periods Ago | Previous Period | Current Period | Trend |
|-------|--------------|-----------------|----------------|-------|
| MQL → SQL | [%] | [%] | [%] | [↑ / ↓ / →] |
| SQO → Won | [%] | [%] | [%] | [↑ / ↓ / →] |
