# Framework: Pricing Strategy Development

Reference framework for developing pricing strategy using established pricing research methodologies.

## Pricing Strategy Objectives

| Objective | When to Use | Implication |
|-----------|------------|-------------|
| Market penetration | New market entry, land-and-expand model | Price below market to maximise adoption; accept lower initial margins |
| Revenue maximisation | Established product with proven value | Price at top of WTP range; optimise for ACV over volume |
| Margin optimisation | Mature product, cost pressures | Restructure pricing to improve unit economics without losing deals |
| Competitive parity | Commoditising market, price-sensitive buyers | Match market pricing; compete on value-adds and service |

## Value Metric Selection

The value metric is the unit buyers perceive as the measure of value:

| Metric Type | Examples | Best For | Risk |
|-------------|---------|----------|------|
| Per-seat | Monthly per user | Collaboration tools, team-based products | Discourages adoption; users share accounts |
| Usage-based | Per API call, per GB, per transaction | Infrastructure, data, volume-driven products | Revenue unpredictability; buyer budget anxiety |
| Outcome-based | Per closed deal, per successful hire | High-value, measurable outcomes | Hard to meter; buyer disputes attribution |
| Flat-rate | Monthly/annual subscription | Simple products, SMB market | Does not scale with value; limits expansion revenue |
| Hybrid | Base platform fee + usage/seat component | Enterprise products with variable workloads | Complexity in pricing page and sales conversations |

### Value Metric Evaluation Criteria
1. **Scales with buyer success**: As the buyer gets more value, they naturally pay more
2. **Easy to understand**: A buyer can explain the pricing model in one sentence
3. **Predictable for the buyer**: The buyer can forecast their spend with reasonable accuracy
4. **Measurable**: The metric can be tracked and billed without disputes

## Willingness-to-Pay Research Methods

| Method | Sample Size | Complexity | Output |
|--------|------------|------------|--------|
| Van Westendorp (Price Sensitivity Meter) | 30-100 respondents | Low | Acceptable price range with optimal price point |
| Gabor-Granger | 100-300 respondents | Medium | Demand curve at specific price points |
| Conjoint analysis | 200-500 respondents | High | Trade-off preferences across features, price, and brand |
| Competitive benchmark | N/A (desk research) | Low | Market price range for comparable products |
| Customer interviews (qualitative) | 10-20 interviews | Low | Directional WTP signals and value perception themes |

### Van Westendorp Questions
1. At what price would this be **so cheap** you would doubt its quality?
2. At what price is this a **bargain** — a great buy for the money?
3. At what price is this **getting expensive** — you would think carefully before buying?
4. At what price is this **too expensive** — you would not consider it?

## Pricing Architecture Template

| Element | Description |
|---------|-------------|
| Number of tiers | Typically 3-4 (Good-Better-Best model) |
| Value metric | The unit buyers pay for (seats, usage, etc.) |
| Billing frequency | Monthly, annual (with discount), multi-year |
| Tier differentiation | Each tier serves a distinct buyer segment with clear upgrade triggers |
| Add-ons | Capabilities sold outside core tiers to address specific needs |
| Enterprise/custom | High-end tier with custom pricing, negotiated via sales |

## Competitive Pricing Positioning

| Stance | Price Relative to Market | Justification Required |
|--------|------------------------|----------------------|
| Premium (>20% above) | Superior product, proven ROI, strong brand | Clear differentiation evidence; customer success stories |
| Parity (within 20%) | Comparable product, compete on other dimensions | Feature and service comparison showing equivalence |
| Penetration (<20% below) | New entrant, land-and-expand, market share priority | Path to price increase once value is proven; expansion revenue model |

## Revenue Modelling Checklist

- [ ] Price points defined for each tier
- [ ] Expected deal volume per tier (conservative, base, optimistic)
- [ ] Average contract value calculated per tier
- [ ] Annual churn assumption per tier
- [ ] Expansion revenue assumption (upsell + cross-sell)
- [ ] Discount impact modelled (average discount rate from sales)
- [ ] Break-even analysis at each price point
- [ ] Sensitivity analysis: revenue impact of +/- 10% price change
