---
name: pricing-finaliser-sales
description: >
  This skill validates that final pricing is sellable based on field feedback
  and competitive positioning. Use when asked to sign off on pricing, review
  pricing before launch, or assess whether pricing changes will impact win rates.
  Also consider when field reps report consistent pricing objections.
  Suggest when pricing is being set without sales input.
department: sales
agent: vp-sales
version: 1.0.0
complexity: medium
related-skills:
  - ../pricing-strategy-sales/SKILL.md
  - ../../sales-manager/objection-handler-updater-sales/SKILL.md
triggers:
  - "finalize the pricing"
  - "is this pricing sellable"
  - "sign off on the price"
  - "validate pricing with sales"
---

# pricing-finaliser-sales

## Agent: VP Sales

L1 sales leader (1x) reporting to the CBO, responsible for sales strategy, pricing sign-off, quota setting, and team structure. Owns the sales motion from pipeline through close.

Department ethos: [ideal-sales.md](../../../departments/sales/ideal-sales.md)

## Skill Description

Validates that the final pricing is sellable based on field feedback, competitive positioning, and pipeline impact analysis before go-to-market launch.

## When to Use

- When pricing has been proposed by Product or Finance and requires sales sign-off before launch.
- When field reps report recurring pricing objections that suggest the current pricing is misaligned with buyer willingness-to-pay.
- When a competitive shift (new entrant, price cut, packaging change) threatens win rates at current pricing.

## Workflow

1. **Field Feedback Aggregation**: Collect pricing feedback from AEs and SEs including deal-level win/loss data, discount frequency, objection themes, and competitive pricing intelligence. Filter for the last 2 quarters of closed-won and closed-lost deals. Deliverable: pricing feedback summary with quantified objection frequency.
2. **Willingness-to-Pay Validation**: Compare proposed pricing against actual deal data: average selling price vs. list price, discount depth distribution, and deal velocity by price tier. Flag any tier where discount rates exceed 20% as a sellability risk. Deliverable: willingness-to-pay analysis with tier-level risk flags.
3. **Competitive Pricing Benchmark**: Map proposed pricing against the top 3 competitors' published and street pricing. Identify where the proposed pricing creates a positive spread (premium justified by value) vs. negative spread (premium without differentiation). Deliverable: competitive pricing benchmark with spread analysis.
4. **Pipeline Impact Assessment**: Model the impact of proposed pricing on current pipeline: deals at risk of stalling, deals that benefit from simplification, and net pipeline value change. Deliverable: pipeline impact model with deal-level exposure.
5. **Sign-Off Decision**: Issue a go/no-go/conditional recommendation. If conditional, specify required adjustments (tier restructuring, discount policy changes, bundling modifications). Deliverable: pricing sign-off memo with conditions if applicable. [GATE]

## Anti-Patterns

- **Rubber-stamping without data**: Approving pricing based on gut feel without reviewing field feedback or deal data. *Why*: pricing disconnected from field reality creates a gap between list price and street price that erodes margins and breeds discounting culture.
- **Blocking on perfection**: Refusing to sign off until pricing is "perfect" across every segment and deal type. *Why*: pricing is iterative; delaying launch waiting for perfection costs more in lost pipeline than imperfect pricing corrected in-market.
- **Ignoring competitive context**: Evaluating pricing in isolation without benchmarking against alternatives the buyer actually considers. *Why*: buyers anchor on competitive pricing whether sales does or not; unaddressed price gaps become silent deal-killers.

## Output

**On success**: Produces a pricing sign-off memo containing field feedback summary, willingness-to-pay analysis, competitive benchmark, pipeline impact model, and go/no-go recommendation with conditions. Delivered to Product and Finance stakeholders.

**On failure**: Report which validation step could not be completed (e.g., insufficient deal data, missing competitive intelligence), what was attempted, and what data is needed to unblock the decision.

## Related Skills

- [`pricing-strategy-sales`](../pricing-strategy-sales/SKILL.md) -- Provides the upstream pricing strategy that this skill validates for sellability.
- [`objection-handler-updater-sales`](../../sales-manager/objection-handler-updater-sales/SKILL.md) -- Consumes pricing objection patterns surfaced during validation.
