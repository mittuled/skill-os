---
name: north-star-metric-reviewer-finance
description: >
  This skill reviews whether the north star metric aligns with the financial model and
  investor expectations. Use when asked to validate the company's north star metric from
  a finance perspective, assess whether the chosen metric drives financial outcomes, or
  evaluate metric alignment with investor narratives. Also consider when the north star
  metric diverges from revenue or cash flow trends. Suggest when the user is reporting
  a north star metric that does not connect to financial performance.
department: finance
agent: finance-manager
version: 1.0.0
complexity: simple
related-skills:
  - ../revenue-impact-monitor/SKILL.md
  - ../../../finance/fpa-analyst/saas-metrics-reporter/SKILL.md
---

# north-star-metric-reviewer-finance

## Agent: Finance Manager

L2 finance manager (1x) responsible for business model review, financial risk assessment, revenue impact monitoring, and north star metric oversight.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)

## Skill Description

Reviews whether the north star metric aligns with the financial model and investor expectations, ensuring the company's primary KPI drives actual financial outcomes.

## When to Use

- When the company selects or changes its north star metric and needs finance validation that it correlates with financial health.
- When the north star metric is trending positively but financial metrics (ARR, margin, cash flow) are flat or declining.
- When preparing for investor meetings where the north star metric will be featured prominently.

## Workflow

1. **Correlation Analysis**: Assess the statistical and logical relationship between the north star metric and key financial outcomes (ARR growth, gross margin, cash flow). Deliverable: correlation summary with supporting data.
2. **Investor Lens Review**: Evaluate whether the metric is one that investors in the company's stage and sector recognize and value. Compare against peer benchmarks. Deliverable: investor alignment assessment.
3. **Recommendation**: Confirm alignment or recommend adjustments to the metric definition, targets, or supporting metrics that bridge the gap to financial outcomes. Deliverable: review memo with recommendation.

## Anti-Patterns

- **Rubber-stamping product metrics**: Approving a north star metric because it is growing without verifying it drives revenue or margin. *Why*: engagement metrics that do not convert to financial outcomes mislead leadership and investors about business health.
- **Ignoring lagging financial indicators**: Focusing only on whether the metric is forward-looking without checking that it eventually shows up in the P&L. *Why*: a metric that never materializes in revenue is a vanity metric regardless of its predictive framing.

## Output

**On success**: Produces a north star metric review memo containing the correlation analysis, investor alignment assessment, and recommendation. Delivered to the CFO and product leadership.

**On failure**: Report which data was insufficient for correlation analysis, what qualitative assessment was possible, and what data collection is needed. Include timeline and owner.

## Related Skills

- [`revenue-impact-monitor`](../revenue-impact-monitor/SKILL.md) -- Tracks the revenue impact that the north star metric should be driving.
- [`saas-metrics-reporter`](../../../finance/fpa-analyst/saas-metrics-reporter/SKILL.md) -- Provides the SaaS metrics context for evaluating north star metric alignment.
