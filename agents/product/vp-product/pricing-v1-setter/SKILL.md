---
name: pricing-v1-setter
description: >
  This skill sets the initial pricing model, price points, and monetization
  mechanics for a product's first commercial release. Use when a product is
  transitioning from beta or free trial to paid GA. Also consider when pivoting
  from one monetization model to another (e.g., flat-rate to usage-based).
  Suggest when design partners ask about future pricing or when finance requests
  revenue projections for board materials.
department: product
agent: vp-product
version: 1.0.0
complexity: complex
related-skills: []
triggers:
  - "set v1 pricing"
  - "initial pricing"
  - "pricing v1"
  - "first pricing"
  - "launch pricing"
---

# pricing-v1-setter

## Agent: VP Product
L1 product leader responsible for opportunity framing, MVP definition, PRD assembly, go-live coordination, and post-launch monitoring. Owns the product strategy and roadmap from idea through GA.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Sets the initial pricing for the product's first commercial release.

## When to Use
- When a product is moving from beta, design-partner phase, or free trial to its first paid release
- When Finance or the board requires a revenue model for fundraising or planning cycles
- When competitive positioning demands a deliberate pricing stance (premium, penetration, freemium)
- When the sales team needs published pricing to close pipeline that has been waiting on commercial terms

## Workflow
1. **Establish pricing objectives**: Clarify whether V1 pricing optimizes for land-and-expand, revenue maximization, market-share capture, or signaling. Deliverable: pricing objectives memo.
2. **Analyse value metrics**: Identify the unit of value the customer receives (seats, API calls, records processed, outcomes delivered) and validate that the metric scales with perceived value. Deliverable: value metric analysis.
3. **Research willingness-to-pay**: Gather data from design-partner interviews, Van Westendorp surveys, conjoint analysis, or competitive benchmarking to establish price sensitivity bands. Deliverable: WTP research summary.
4. **Select the pricing model**: Choose the monetization architecture — subscription, usage-based, hybrid, per-seat, or outcome-based — and justify against the value metric and buyer procurement norms. Deliverable: pricing model decision document.
5. **Set price points**: Define the specific dollar amounts per tier or unit, including any free tier limits, commit discounts, and annual-vs-monthly differentials. Deliverable: price card draft. [GATE]
6. **Model unit economics**: Calculate gross margin, CAC payback, and LTV under the proposed pricing using conservative, base, and optimistic adoption scenarios. Deliverable: unit economics model.
7. **Stress-test with GTM stakeholders**: Walk Sales, CS, and Finance through the price card to surface objections around deal mechanics, discounting authority, and billing complexity. Deliverable: stakeholder sign-off or revision log.
8. **Define discounting guardrails**: Set maximum discount thresholds, approval chains, and conditions under which non-standard pricing is permitted (e.g., design-partner carryover, multi-year commits). Deliverable: discounting policy.
9. **Document and enable**: Publish the final pricing in an internal pricing bible and create enablement materials for Sales, including objection-handling scripts and competitive price comparisons. Deliverable: pricing bible and enablement deck.
10. **Plan the pricing review cadence**: Schedule a 90-day post-launch pricing review and define the metrics (conversion rate, ARPU, discount frequency) that would trigger a pricing adjustment. Deliverable: pricing review calendar entry with trigger thresholds.

## Anti-Patterns
- **Cost-plus pricing**: Setting price as a markup on infrastructure cost rather than on customer value. *Why*: Cost-plus ignores willingness-to-pay and leaves money on the table or prices out value-sensitive segments.
- **Copying the competitor**: Adopting a competitor's exact price points without understanding their cost structure, packaging, or strategic intent. *Why*: Your value proposition and cost basis differ; borrowed prices create margin or positioning traps.
- **Premature complexity**: Launching with a multi-tier, usage-metered model when the product has a narrow ICP and limited usage data. *Why*: Complex pricing confuses early buyers and burdens engineering with metering infrastructure before product-market fit is confirmed.
- **Anchor-free pricing**: Publishing prices without a visible anchor (e.g., annual list price) that makes the actual price feel like a deal. *Why*: Buyers evaluate price relative to a reference point; without one, every price feels arbitrary.
- **Skipping discounting guardrails**: Launching pricing without defined discount limits. *Why*: Sales will create ad-hoc discounts that erode margin and set precedents that are painful to walk back.
- **Set-and-forget**: Treating V1 pricing as permanent. *Why*: Early pricing is a hypothesis; failing to revisit it with real data locks in mistakes.

## Output
**On success**: A pricing bible containing the monetization model, price card, value metric rationale, unit economics model, discounting policy, and enablement materials — approved by Product, Finance, and Sales leadership.
**On failure**: Report which step blocked (e.g., insufficient WTP data, stakeholder disagreement on model), what alternatives were evaluated, the best available fallback (e.g., time-limited beta pricing extended), and the data needed to unblock a final decision.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
