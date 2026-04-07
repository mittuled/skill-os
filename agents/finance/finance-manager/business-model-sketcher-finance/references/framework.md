# Framework: business-model-sketcher-finance

Defines the analytical framework for stress-testing a business model's financial sustainability across revenue quality, cost structure, working capital, and scenario analysis.

## Business Model Decomposition Canvas

### Revenue Quality Assessment

| Dimension | Questions to Answer | Strong Signal | Weak Signal |
|-----------|-------------------|---------------|-------------|
| Recurrence | What percentage of revenue is subscription or contracted? | >80% ARR | <40% ARR; heavy one-time fees |
| Predictability | Can revenue be forecast within ±10% at 3 months out? | Consistent NRR >100%, low churn | High churn, lumpy bookings |
| Defensibility | What switching costs protect revenue? | Multi-year contracts, data lock-in, workflow integration | Month-to-month; multiple substitutes |
| Concentration | What is the top-customer revenue percentage? | Top 10 customers < 30% of revenue | Any single customer >15% |
| Expansion potential | Can customers spend more over time? | Usage-based or seat expansion; land-and-expand motion | Fixed price; no expansion motion |

### Cost Structure Analysis

| Cost Layer | Description | Operating Leverage Indicator |
|-----------|-------------|------------------------------|
| Gross margin | Revenue minus direct COGS (hosting, CS, support) | SaaS benchmark: 70–85% gross margin |
| Sales & Marketing efficiency | S&M as % of revenue; CAC payback | Best-in-class: CAC payback < 12 months |
| R&D investment | R&D as % of revenue; headcount productivity | 15–25% of revenue at growth stage |
| G&A leverage | G&A as % of revenue (should decline with scale) | Best-in-class: G&A < 10% at scale |
| Contribution margin | Revenue minus fully loaded variable costs | Must be positive per unit for the model to scale |

### Operating Leverage Analysis

```
At what ARR does the company reach operating breakeven?

Breakeven ARR = Fixed Costs / Gross Margin %

Example:
Fixed costs = $10M/year
Gross margin = 75%
Breakeven ARR = $10M / 0.75 = $13.3M ARR
```

Track quarterly progress toward operating leverage inflection.

## Stress Test Scenarios

| Scenario | Revenue Assumption | Cost Assumption | Purpose |
|---------|-------------------|-----------------|---------|
| Base Case | Current forecast | Current trajectory | Baseline planning |
| Downside 1: Revenue miss | −20% ARR vs. forecast | No cost adjustment | Tests burn rate sensitivity |
| Downside 2: Cost inflation | No change | +15% across OpEx | Tests operating leverage |
| Downside 3: Churn acceleration | +3pp gross churn | No cost adjustment | Tests retention-driven revenue sensitivity |
| Severe Downside: Combined | −20% revenue + +10% costs | Combination | Worst-case runway |
| Recovery: Cost-out response | −20% revenue | −20% OpEx (hiring freeze, cuts) | Tests management's ability to extend runway |

For each scenario, calculate:
- **Break-even MRR**: Minimum MRR to cover all costs
- **Runway extension**: How many months the model survives without additional capital
- **Path to cash-flow positivity**: Revenue required at current cost structure

## Working Capital Dynamics

| Factor | Impact on Cash | Action if Negative |
|--------|---------------|-------------------|
| Annual vs. monthly billing mix | Annual upfront billing improves cash; monthly creates collection lag | Incentivize annual plans with discounts |
| Days Sales Outstanding (DSO) | High DSO delays cash receipt from recognized revenue | Tighten payment terms; pursue collections |
| Vendor payment terms | Longer terms preserve cash | Negotiate net-60 or net-90 for large vendors |
| Deferred revenue | Increases as bookings grow; a cash buffer | Track deferred revenue as a cash runway metric |

Working capital position = Cash collected − Cash paid out (not revenue recognized − expenses accrued)

## Viability Verdicts

| Verdict | Criteria | Implication |
|---------|---------|-------------|
| VIABLE | Gross margin > 60%; positive path to operating leverage within 36 months; downside scenarios result in runway > 18 months | Proceed with current model; optimize the variables |
| CONDITIONALLY VIABLE | Gross margin 40–60%; operating leverage achievable but requires specific assumptions; downside runway < 12 months | Identify 2–3 model improvements needed before scaling; set milestones |
| NOT VIABLE | Gross margin < 40% with no structural path to improvement; model cannot reach operating breakeven at any realistic ARR | Rethink the fundamental cost structure or pricing before scaling; present alternatives |
