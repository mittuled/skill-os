---
name: pricing-finaliser-finance
description: >
  This skill provides finance sign-off on final pricing to confirm margin and revenue
  model viability. Use when asked to approve a pricing change, validate that new pricing
  preserves target margins, or sign off on a pricing proposal before launch. Also consider
  when pricing decisions are being made without finance input. Suggest when the user is
  about to ship a pricing change without margin validation.
department: finance
agent: cfo-vp-finance
version: 1.0.0
complexity: medium
related-skills:
  - ../../fpa-analyst/pricing-review-runner/SKILL.md
  - ../unit-econ-viability-gate/SKILL.md
---

# pricing-finaliser-finance

## Agent: CFO / VP Finance

L1 CFO and VP Finance (1x) reporting to the COO, responsible for unit economics, financial modelling, pricing sign-off, and pitch narration for financial audiences.

Department ethos: [ideal-finance.md](../../../departments/finance/ideal-finance.md)

## Skill Description

Provides the CFO-level finance sign-off on final pricing to confirm that margins, revenue model assumptions, and unit economics remain viable under the proposed structure.

## When to Use

- When a new pricing structure, tier change, or discount policy is ready for final approval before go-live.
- When the product or sales team proposes pricing that deviates from the approved financial model.
- When entering a new market segment or geography where pricing must be validated against local cost structures and competitive dynamics.

## Workflow

1. **Pricing Proposal Review**: Receive the pricing proposal including proposed price points, packaging, discount guardrails, and expected volume mix. Deliverable: documented pricing proposal with completeness checklist.
2. **Margin Impact Analysis**: Model the gross margin and contribution margin impact at the proposed price points. Compare against current margins and board-approved targets. Deliverable: margin impact analysis with variance to plan.
3. **Revenue Model Reconciliation**: Validate that the proposed pricing is consistent with the financial model's revenue assumptions. Reforecast ARR, MRR, and ACV under the new pricing. Deliverable: updated revenue forecast with delta to current plan.
4. **Downside Scenario Modelling**: Model the impact of adverse scenarios -- lower-than-expected adoption of premium tiers, higher discount utilization, competitive price pressure. Deliverable: downside scenario analysis with floor pricing thresholds.
5. **Sign-Off Decision**: Issue APPROVED, APPROVED WITH CONDITIONS, or REJECTED with specific rationale. For conditional approvals, define the conditions (e.g., minimum deal size, discount caps, sunset dates). Deliverable: pricing sign-off memo with conditions.

## Anti-Patterns

- **Approving without volume mix assumptions**: Signing off on pricing without modelling the expected mix across tiers or segments. *Why*: attractive headline pricing can destroy margins if the actual mix skews toward low-margin tiers.
- **Ignoring second-order effects**: Evaluating pricing in isolation without considering impact on existing customer base (downgrades, churn) or sales compensation (sandbagging, deal acceleration). *Why*: pricing changes ripple through the entire revenue system.
- **Rubber-stamping under time pressure**: Approving pricing to meet a launch deadline without completing the margin analysis. *Why*: pricing mistakes compound over every future deal; a one-week delay costs far less than a year of margin erosion.

## Output

**On success**: Produces a pricing sign-off memo containing the margin impact analysis, revenue model reconciliation, downside scenarios, and an APPROVED/CONDITIONAL/REJECTED decision with conditions. Delivered to the pricing committee and archived for audit.

**On failure**: Report which analyses could not be completed (e.g., missing COGS data for new product line), what partial assessment was done, and what information is needed to complete the sign-off. Include a clear timeline and owner for each gap.

## Related Skills

- [`pricing-review-runner`](../../fpa-analyst/pricing-review-runner/SKILL.md) -- Conducts periodic pricing reviews that feed into this final sign-off decision.
- [`unit-econ-viability-gate`](../unit-econ-viability-gate/SKILL.md) -- Validates the broader unit economics that pricing must support.
