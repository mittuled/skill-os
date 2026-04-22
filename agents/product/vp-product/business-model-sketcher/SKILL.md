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
related-skills:
  - assumption-mapper
  - competitive-response-monitor
  - goal-framer
  - prd-assembler
  - design-partner-programme-builder
  - gate-12-evaluator
  - idea-critic
  - launch-coordinator
  - moat-analyzer
  - mvp-definer
  - north-star-metric-reviewer
  - opportunity-framer
  - packaging-designer
  - pitch-narrator
  - pricing-v1-setter
  - product-feedback-ingestion
  - sla-definer
triggers:
  - "sketch business model"
  - "business model"
  - "draft business model"
  - "business model canvas"
  - "model the business"
---

# business-model-sketcher

## Agent: VP Product
L1 product leader responsible for opportunity framing, MVP definition, PRD assembly, go-live coordination, and post-launch monitoring. Owns the product strategy and roadmap from idea through GA.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

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
- [`assumption-mapper`](../assumption-mapper/SKILL.md) — sibling skill under the same agent — combine with assumption-mapper for end-to-end coverage
- [`competitive-response-monitor`](../competitive-response-monitor/SKILL.md) — sibling skill under the same agent — combine with competitive-response-monitor for end-to-end coverage
- [`goal-framer`](../goal-framer/SKILL.md) — sibling skill under the same agent — combine with goal-framer for end-to-end coverage
- [`prd-assembler`](../prd-assembler/SKILL.md) — sibling skill under the same agent — combine with prd-assembler for end-to-end coverage
- [`design-partner-programme-builder`](../design-partner-programme-builder/SKILL.md) — sibling skill under the same agent — combine with design-partner-programme-builder for end-to-end coverage
- [`gate-12-evaluator`](../gate-12-evaluator/SKILL.md) — sibling skill under the same agent — combine with gate-12-evaluator for end-to-end coverage
- [`idea-critic`](../idea-critic/SKILL.md) — sibling skill under the same agent — combine with idea-critic for end-to-end coverage
- [`launch-coordinator`](../launch-coordinator/SKILL.md) — sibling skill under the same agent — combine with launch-coordinator for end-to-end coverage
- [`moat-analyzer`](../moat-analyzer/SKILL.md) — sibling skill under the same agent — combine with moat-analyzer for end-to-end coverage
- [`mvp-definer`](../mvp-definer/SKILL.md) — sibling skill under the same agent — combine with mvp-definer for end-to-end coverage
- [`north-star-metric-reviewer`](../north-star-metric-reviewer/SKILL.md) — sibling skill under the same agent — combine with north-star-metric-reviewer for end-to-end coverage
- [`opportunity-framer`](../opportunity-framer/SKILL.md) — sibling skill under the same agent — combine with opportunity-framer for end-to-end coverage
- [`packaging-designer`](../packaging-designer/SKILL.md) — sibling skill under the same agent — combine with packaging-designer for end-to-end coverage
- [`pitch-narrator`](../pitch-narrator/SKILL.md) — sibling skill under the same agent — combine with pitch-narrator for end-to-end coverage
- [`pricing-v1-setter`](../pricing-v1-setter/SKILL.md) — sibling skill under the same agent — combine with pricing-v1-setter for end-to-end coverage
- [`product-feedback-ingestion`](../product-feedback-ingestion/SKILL.md) — sibling skill under the same agent — combine with product-feedback-ingestion for end-to-end coverage
- [`sla-definer`](../sla-definer/SKILL.md) — sibling skill under the same agent — combine with sla-definer for end-to-end coverage
