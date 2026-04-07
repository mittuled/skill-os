# Framework: Pricing Strategy Development

## Purpose

Provides the structured methodology for developing a pricing strategy grounded in field willingness-to-pay data, competitive intelligence, and value metric analysis.

## Willingness-to-Pay Research Method

### Data Sources (Priority Order)

1. **Closed-won deal data** -- Actual contract values, discount levels, negotiation records (highest signal)
2. **Closed-lost deal data** -- Loss reasons mentioning pricing, last quoted price vs. competitor price
3. **Discovery call notes** -- Budget indicators, stated budget ranges, pricing reactions
4. **Win/loss interviews** -- Buyer's stated price sensitivity and anchoring factors
5. **Market research** -- Published benchmarks, analyst reports (lowest signal; use to validate, not anchor)

### Segmentation Dimensions

Segment WTP data by these dimensions (minimum 10 data points per segment):

| Dimension | Why It Matters |
|-----------|---------------|
| Company size (employees) | Budget scales, procurement complexity differs |
| Industry vertical | WTP varies by industry margin structure |
| Use case | Primary vs. secondary use case affects perceived value |
| Current solution | Switching from a paid tool vs. manual process changes anchoring |
| Geography | Regional pricing expectations differ |

### Price Sensitivity Analysis

For each segment, calculate:
- **Van Westendorp indicators**: Too cheap, cheap, expensive, too expensive price points
- **Revealed WTP**: Median and interquartile range of actual selling prices
- **Price elasticity estimate**: Win rate change per 10% price increase/decrease

## Value Metric Selection Criteria

Evaluate candidate value metrics against these criteria:

| Criterion | Weight | What to Assess |
|-----------|--------|----------------|
| Value alignment | 30% | Does the metric scale with customer value received? More metric = more value? |
| Predictability | 25% | Can the customer predict their cost? Unpredictable metrics create budget anxiety |
| Measurability | 20% | Can the metric be measured at point of sale? Can the customer verify it? |
| Growth potential | 15% | Does the metric naturally grow as the customer succeeds, enabling NRR expansion? |
| Competitive norm | 10% | Does the metric match what buyers expect in this category? |

### Common Value Metrics by Model

| Metric Type | Best For | Risk |
|-------------|----------|------|
| Per seat (named user) | Collaboration tools, CRM | Discourages adoption; seat shelfware |
| Per active user | Usage-focused products | Revenue volatility if usage dips |
| Usage-based (API calls, records) | Infrastructure, data products | Unpredictable costs for buyer |
| Platform fee + usage | Enterprise platforms | Complexity; hard to quote quickly |
| Outcome-based | High-confidence ROI products | Requires measurement infrastructure |

## Pricing Model Design Principles

### Tier Architecture

1. **Entry tier** -- Priced at the low end of revealed WTP; optimized for conversion and time-to-value
2. **Core tier** -- Priced at the median WTP; captures the majority of revenue; includes all features most customers need
3. **Premium tier** -- Priced at the high end of WTP; includes advanced features that only 20% of customers need but are willing to pay significantly more for

### Anchor Pricing

Set the first price the buyer sees at the top of the WTP range (premium tier), then present lower tiers as accessible alternatives. Anchoring to the premium tier makes the core tier feel reasonable.

### Discount Policy Framework

| Level | Discount Range | Authority | Required Justification |
|-------|---------------|-----------|----------------------|
| Standard | 0-10% | AE | Annual commitment, standard negotiation |
| Escalated | 11-20% | Sales Manager | Multi-year, strategic account, competitive displacement |
| Executive | 21-30% | VP Sales | Written business case with LTV justification |
| Exception | 30%+ | CEO/CRO | Requires pricing committee review |

Floor price = variable cost + minimum margin. No deal closes below floor regardless of strategic justification.

## Scenario Modeling Method

Model three scenarios against current pipeline:

| Scenario | Price Position | Optimization Target |
|----------|---------------|-------------------|
| Aggressive | Top 25% of WTP range | Maximize ACV; accept lower win rate |
| Balanced | Median WTP | Optimize ACV x win rate product |
| Conservative | Bottom 25% of WTP range | Maximize win rate; accept lower ACV |

For each scenario, calculate:
- Projected ACV per segment
- Projected win rate (use historical elasticity data)
- Projected revenue = pipeline value x win rate x (new ACV / current ACV)
- Projected CAC payback period change
- Break-even analysis: at what win rate does the scenario produce equivalent revenue?
