---
name: unit-economics-monitor
description: >
  This skill monitors unit economics metrics including CAC, LTV, payback period, and
  gross margin. Use when asked to track unit economics trends, report on CAC/LTV ratios,
  or flag when economics are deteriorating. Also consider when growth spending is
  accelerating without corresponding unit economics monitoring. Suggest when the user
  is scaling acquisition spend without tracking payback period.
department: finance
agent: fpa-analyst
version: 1.0.0
complexity: medium
related-skills:
  - ../../../finance/cfo-vp-finance/unit-econ-viability-gate/SKILL.md
  - ../saas-metrics-reporter/SKILL.md
---

# unit-economics-monitor

## Agent: FP&A Analyst

L2 FP&A analyst (1x) responsible for budgeting, forecasting, variance analysis, board reporting, fundraising models, and SaaS metrics.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)

## Skill Description

Monitors unit economics metrics including CAC, LTV, payback period, and gross margin on an ongoing basis, tracking trends and flagging deterioration before it becomes material.

## When to Use

- When the monthly reporting cycle requires an update to unit economics metrics.
- When CAC is rising, gross margin is declining, or payback period is lengthening and leadership needs a structured assessment.
- When the company is scaling acquisition channels and needs to track whether new channels maintain viable unit economics.

## Workflow

1. **CAC Calculation**: Calculate fully-loaded CAC by channel including sales compensation, marketing spend, sales tools, and allocated overhead. Break down by segment (SMB, mid-market, enterprise) and acquisition channel (inbound, outbound, partner). Deliverable: CAC report by channel and segment.
2. **LTV Calculation**: Calculate LTV using gross-margin-weighted revenue per customer divided by churn rate. Compare gross-margin LTV with contribution-margin LTV to show the true picture. Deliverable: LTV report with methodology documentation.
3. **Ratio and Payback Analysis**: Calculate LTV/CAC ratio and CAC payback period in months for each segment and channel. Compare against targets (e.g., LTV/CAC >3x, payback <18 months) and prior periods. Deliverable: ratio analysis with threshold comparison.
4. **Trend Monitoring**: Plot 6-12 month trends for each metric. Identify inflection points and assess whether changes are structural or transient. Calculate the rate of change to distinguish gradual drift from sudden shifts. Deliverable: trend dashboard with rate-of-change indicators.
5. **Alert and Recommendation**: Flag any metric that has breached a threshold or is trending toward breach within 2 months. Recommend specific actions (channel reallocation, pricing adjustment, churn intervention). Deliverable: unit economics alert memo with action items.

## Anti-Patterns

- **Blended CAC only**: Reporting a single company-wide CAC without breaking it down by channel and segment. *Why*: blended CAC masks channels where economics are unviable; you cannot optimize what you cannot decompose.
- **Static LTV assumptions**: Using a fixed churn rate from months ago rather than updating with current retention data. *Why*: LTV is only as accurate as the churn assumption; stale inputs produce misleading ratios.
- **Ignoring fully-loaded costs**: Excluding sales compensation, tools, or overhead from CAC to make the ratio look better. *Why*: understated CAC creates a false sense of economic health that collapses when scrutinized by investors or the board.

## Output

**On success**: Produces a unit economics report containing CAC by channel/segment, LTV calculations, ratio analysis, trend dashboard, and alert memo. Delivered monthly to the CFO and growth leadership.

**On failure**: Report which cost or revenue data is unavailable for accurate calculation (e.g., marketing spend not attributed by channel), what metrics can be calculated with available data, and what data collection processes must be implemented.

## Related Skills

- [`unit-econ-viability-gate`](../../../finance/cfo-vp-finance/unit-econ-viability-gate/SKILL.md) -- Uses this monitoring data as input for go/no-go gate decisions.
- [`saas-metrics-reporter`](../saas-metrics-reporter/SKILL.md) -- Provides the subscription metrics context that complements unit economics.
