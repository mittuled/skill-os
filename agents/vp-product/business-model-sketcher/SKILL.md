---
name: business-model-sketcher
description: >
  This skill sketches the initial business model including revenue streams, cost structure, and unit economics.
  Use when a product opportunity has been validated and the team needs to understand how it will generate and capture value.
  Also consider when pricing discussions stall because no one has modeled the unit economics or cost structure.
  Suggest when an MVP is being scoped without any viability analysis or when leadership asks "how does this make money?"
department: product
agent: vp-product
version: 1.0.0
complexity: medium
related-skills: []
---

# business-model-sketcher

## Agent: VP Product
L1 product leader responsible for opportunity framing, MVP definition, PRD assembly, go-live coordination, and post-launch monitoring. Owns the product strategy and roadmap from idea through GA.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)

## Skill Description
Sketches the initial business model including revenue streams, cost structure, and unit economics.

## When to Use
- When a validated opportunity needs a viability layer before committing engineering resources to an MVP
- When the team is debating pricing strategy and needs a lightweight model of revenue streams, COGS, and contribution margin
- When presenting an initiative to leadership and the business case requires a first-pass unit economics sketch to justify investment

## Workflow
1. **Identify the value exchange**: Define what value the product delivers and what the user gives in return (money, data, attention, network effects). Map the primary and secondary revenue streams — e.g., subscription, usage-based, marketplace take-rate, upsell. Deliverable: value exchange diagram with revenue stream labels.
2. **Model unit economics**: Calculate the key per-unit metrics: CAC, LTV, gross margin, and payback period. Use analogues from comparable products or internal benchmarks where direct data is unavailable. State every assumption explicitly. Deliverable: unit economics table with formula, inputs, and output for each metric.
3. **Sketch the cost structure**: Break costs into variable (hosting, API calls, support per user) and fixed (engineering headcount, tooling). Estimate costs at three scale points: launch, 1K users, 10K users. Deliverable: cost structure table with variable/fixed split and scale projections.
4. **Test the margin threshold**: Compare contribution margin against company benchmarks. Identify the break-even point in users or revenue. Flag if the model requires unrealistic adoption to reach profitability. Deliverable: break-even analysis with sensitivity on the top 2 input variables.
5. **Document the business model sketch**: Assemble value exchange, unit economics, cost structure, and break-even analysis into a one-page sketch. Call out the top 3 viability risks and what would change the model. Deliverable: business model sketch document ready for finance review.

## Anti-Patterns
- **Revenue without cost awareness**: Projecting revenue growth without modeling the corresponding cost curve. *Why*: Gross margin can turn negative at scale if infrastructure or support costs grow faster than revenue, making the business model a trap.
- **Precision theater**: Building a 50-row spreadsheet with false precision when the inputs are guesses. *Why*: Creates an illusion of rigor that discourages healthy skepticism and delays real validation of pricing and willingness-to-pay.
- **Single-scenario planning**: Modeling only the optimistic case without stress-testing pessimistic or base scenarios. *Why*: Hides the conditions under which the model breaks, leaving leadership without the information needed to set risk appetite.

## Output
**On success**: A business model sketch containing the value exchange diagram, unit economics table (CAC, LTV, gross margin, payback), cost structure with scale projections, break-even analysis, and top viability risks — formatted as a one-pager suitable for leadership review and finance validation.
**On failure**: Report which model components could not be estimated (e.g., no pricing analogues, unknown infrastructure costs), what placeholder assumptions were used, and recommend specific data collection steps such as pricing surveys, competitive teardowns, or finance consultations to fill the gaps.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
