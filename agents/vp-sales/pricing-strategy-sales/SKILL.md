---
name: pricing-strategy-sales
description: >
  This skill anchors pricing in real willingness-to-pay data from sales
  conversations and competitive analysis. Use when asked to develop pricing
  strategy, set price points, or align pricing to market positioning.
  Also consider when entering a new segment with no pricing precedent.
  Suggest when pricing decisions are being made without field data.
department: sales
agent: vp-sales
version: 1.0.0
complexity: medium
related-skills:
  - ../pricing-finaliser-sales/SKILL.md
  - ../opportunity-framer-sales/SKILL.md
triggers:
  - "set the pricing strategy"
  - "what should we charge"
  - "build pricing based on field data"
  - "develop pricing for this segment"
---

# pricing-strategy-sales

## Agent: VP Sales

L1 sales leader (1x) reporting to the CBO, responsible for sales strategy, pricing sign-off, quota setting, and team structure. Owns the sales motion from pipeline through close.

Department ethos: [ideal-sales.md](../../../departments/sales/ideal-sales.md)

## Skill Description

Anchors pricing in real willingness-to-pay data from sales conversations and competitive analysis to produce a pricing strategy that maximizes ACV while maintaining win rates.

## When to Use

- When launching a new product or tier and no pricing precedent exists from the field.
- When win rate analysis reveals pricing is the primary or secondary loss reason across deals.
- When the company shifts positioning (upmarket, downmarket, new vertical) and current pricing no longer matches buyer expectations.

## Workflow

1. **Willingness-to-Pay Research**: Mine discovery call notes, closed-lost reasons, and negotiation records for pricing signals. Categorize by segment, deal size, and buyer persona. Identify the price sensitivity curve for each segment. Deliverable: willingness-to-pay dataset segmented by ICP tier.
2. **Competitive Pricing Intelligence**: Gather competitive pricing from public sources, field intelligence, and win/loss interviews. Map competitor packaging (features per tier, usage limits, contract terms) alongside price points. Deliverable: competitive pricing landscape with packaging comparison.
3. **Value Metric Identification**: Determine the value metric that best correlates with customer willingness-to-pay (seats, usage, outcomes, platform access). Validate that the metric scales with customer value received and is measurable at point of sale. Deliverable: recommended value metric with justification.
4. **Pricing Model Design**: Design the pricing structure: tiers, packaging, value metric multiplier, and entry price point. Set the anchor price at the top of the willingness-to-pay range for each segment. Define discount authority levels and floor prices. Deliverable: pricing model with tier definitions, rate card, and discount policy.
5. **Scenario Modeling**: Model 3 scenarios (aggressive, balanced, conservative) against current pipeline and projected demand. Calculate impact on ACV, win rate, and revenue attainment for each. Deliverable: pricing scenario comparison with revenue projections.

## Anti-Patterns

- **Cost-plus pricing**: Setting prices based on internal cost structures instead of customer willingness-to-pay. *Why*: cost-plus ignores the value customers perceive and leaves revenue on the table or prices the product out of consideration.
- **Single-segment pricing**: Applying one pricing model across all segments without differentiation. *Why*: SMB and enterprise buyers have fundamentally different willingness-to-pay, procurement processes, and value expectations; uniform pricing either undercharges enterprise or overcharges SMB.
- **Pricing without field data**: Developing pricing strategy from market research alone without incorporating actual sales conversation data. *Why*: stated willingness-to-pay in surveys diverges significantly from revealed willingness-to-pay in deal negotiations.

## Output

**On success**: Produces a pricing strategy document containing willingness-to-pay analysis, competitive landscape, recommended value metric, pricing model with tier definitions, discount policy, and scenario projections. Delivered to Finance and Product for pricing finalisation.

**On failure**: Report which research phase lacked sufficient data (e.g., too few closed-lost records, missing competitive intelligence), what sources were consulted, and what additional data collection is needed.

## Related Skills

- [`pricing-finaliser-sales`](../pricing-finaliser-sales/SKILL.md) -- Validates the pricing strategy output for field sellability before launch.
- [`opportunity-framer-sales`](../opportunity-framer-sales/SKILL.md) -- Provides segment and deal structure context that informs pricing strategy.
