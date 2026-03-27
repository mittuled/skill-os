---
name: business-model-sketcher-finance
description: >
  This skill reviews and stress-tests the business model from a financial sustainability
  perspective. Use when asked to evaluate revenue model viability, assess business model
  risks, or validate that a proposed model supports the company's financial targets.
  Also consider when product teams propose new monetization strategies without finance
  input. Suggest when the user is committing to a business model without financial
  stress-testing.
department: finance
agent: finance-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../../cfo-vp-finance/unit-econ-viability-gate/SKILL.md
  - ../financial-risk-reviewer/SKILL.md
---

# business-model-sketcher-finance

## Agent: Finance Manager

L2 finance manager (1x) responsible for business model review, financial risk assessment, revenue impact monitoring, and north star metric oversight.

Department ethos: [ideal-finance.md](../../../departments/finance/ideal-finance.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Reviews and stress-tests the business model from a financial sustainability perspective, validating that revenue streams, cost structure, and margin profile support long-term viability.

## When to Use

- When a new business model or monetization strategy is proposed and needs financial validation before commitment.
- When the company is considering a pivot and needs to understand the financial implications of the new model.
- When quarterly business reviews reveal that the current model's margin structure is degrading and needs reassessment.

## Workflow

1. **Model Decomposition**: Break the business model into revenue streams, cost drivers, and margin layers. Identify the key assumptions behind each (pricing power, volume growth, COGS scalability). Deliverable: business model canvas with financial annotations.
2. **Revenue Sustainability Check**: Assess whether each revenue stream is recurring, predictable, and defensible. Evaluate concentration risk (customer, channel, geography) and expansion potential (upsell, cross-sell, usage growth). Deliverable: revenue quality scorecard.
3. **Cost Structure Analysis**: Map fixed vs. variable costs and identify the contribution margin at current and projected scale. Model the path to operating leverage -- at what revenue level does the model generate positive operating margin. Deliverable: cost structure breakdown with operating leverage analysis.
4. **Stress Test Execution**: Run scenarios for revenue contraction (-20%), cost inflation (+15%), and churn acceleration (+3pp). Identify the break-even point and minimum viable revenue for each scenario. Deliverable: stress test results with break-even thresholds.
5. **Recommendation Synthesis**: Summarize findings with a viability verdict (VIABLE, CONDITIONALLY VIABLE, NOT VIABLE) and specific recommendations for strengthening the model. Deliverable: business model review memo with action items.

## Anti-Patterns

- **Revenue-only focus**: Evaluating the revenue side without equal scrutiny of cost scalability and margin structure. *Why*: a business model that grows revenue but cannot achieve operating leverage will consume cash indefinitely.
- **Ignoring working capital dynamics**: Assessing profitability without modelling the cash conversion cycle (billing terms, collection lag, vendor payment timing). *Why*: a model can be profitable on paper but cash-negative in practice if working capital requirements grow faster than revenue.
- **Confusing gross margin with contribution margin**: Using gross margin as the sole profitability indicator without accounting for variable sales and marketing costs per customer. *Why*: gross margin overstates unit profitability for models with high customer acquisition costs.

## Output

**On success**: Produces a business model review memo containing the revenue quality scorecard, cost structure analysis, stress test results, and viability verdict with recommendations. Delivered to the CFO and product leadership.

**On failure**: Report which model components could not be assessed (e.g., COGS data unavailable for new product line), what partial analysis was completed, and what data must be gathered to complete the review. Include owners and deadlines.

## Related Skills

- [`unit-econ-viability-gate`](../../cfo-vp-finance/unit-econ-viability-gate/SKILL.md) -- Provides the CFO-level gate decision that follows this financial review.
- [`financial-risk-reviewer`](../financial-risk-reviewer/SKILL.md) -- Assesses the risk dimensions that complement this sustainability analysis.
