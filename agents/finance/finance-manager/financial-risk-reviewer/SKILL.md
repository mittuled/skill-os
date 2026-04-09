---
name: financial-risk-reviewer
description: >
  This skill identifies and assesses financial risks including concentration risk, burn
  rate, and covenant compliance. Use when asked to evaluate financial risk exposure,
  assess runway sustainability, or review risk factors for board reporting. Also consider
  when the company takes on new debt, enters a new market, or experiences rapid growth
  that may mask underlying risks. Suggest when the user is scaling spend without a risk
  assessment.
department: finance
agent: finance-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../business-model-sketcher-finance/SKILL.md
  - ../../../finance/fpa-analyst/rolling-forecast-updater/SKILL.md
triggers:
  - "review financial risks"
  - "financial risk assessment"
  - "assess financial risk"
  - "identify financial risks"
  - "financial risk review"
---

# financial-risk-reviewer

## Agent: Finance Manager

L2 finance manager (1x) responsible for business model review, financial risk assessment, revenue impact monitoring, and north star metric oversight.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)

## Skill Description

Identifies and assesses financial risks including concentration risk, burn rate trajectory, covenant compliance, and FX exposure to ensure leadership has a clear view of financial vulnerabilities.

## When to Use

- When preparing for a board meeting or investor update that requires a current risk assessment.
- When the company's burn rate, customer concentration, or revenue mix has shifted materially since the last review.
- When entering new financial commitments (debt facility, multi-year contracts, new market entry) that alter the risk profile.

## Workflow

1. **Risk Identification**: Scan across risk categories -- concentration (customer, channel, geography), liquidity (burn rate, runway), market (FX, interest rate), operational (vendor dependency, key-person), and compliance (covenant, regulatory). Deliverable: risk inventory with category tags.
2. **Quantitative Assessment**: For each identified risk, quantify the potential financial impact and probability. Calculate revenue at risk from top-customer concentration, months of runway under current and stressed burn rates, and covenant headroom. Deliverable: risk register with impact/probability scoring.
3. **Trend Analysis**: Compare current risk levels against prior periods to identify deteriorating or improving trends. Flag any metric that has moved more than one standard deviation in the wrong direction. Deliverable: risk trend dashboard with period-over-period comparison.
4. **Mitigation Mapping**: For each high and critical risk, document existing mitigations and identify gaps. Propose specific actions with owners, timelines, and cost estimates. Deliverable: mitigation plan with gap analysis.
5. **Executive Summary**: Produce a concise risk summary for board or leadership consumption. Lead with the top 3 risks, their trajectory, and the mitigation status. Deliverable: financial risk memo with executive summary.

## Anti-Patterns

- **Boiling the ocean**: Cataloguing every conceivable risk without prioritizing by materiality. *Why*: an undifferentiated risk list produces analysis fatigue and prevents leadership from focusing on what matters.
- **Lagging indicators only**: Assessing risk based solely on historical data without incorporating forward-looking signals (pipeline changes, market shifts, upcoming renewals). *Why*: financial risks materialize before they appear in the financials; early warning requires leading indicators.
- **Risk without mitigation**: Identifying risks without proposing actionable mitigations. *Why*: risk identification without a response plan creates anxiety rather than enabling informed decision-making.

## Output

**On success**: Produces a financial risk memo containing the risk register, trend dashboard, mitigation plan, and executive summary. Delivered to the CFO and board financial pack.

**On failure**: Report which risk categories could not be assessed (e.g., missing customer-level revenue data for concentration analysis), what partial assessment was completed, and what data collection is required. Include specific owners for each gap.

## Related Skills

- [`business-model-sketcher-finance`](../business-model-sketcher-finance/SKILL.md) -- Provides the business model context that informs risk identification.
- [`rolling-forecast-updater`](../../../finance/fpa-analyst/rolling-forecast-updater/SKILL.md) -- Supplies the forward-looking financial data that feeds trend analysis.
