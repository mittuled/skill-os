---
name: expansion-motion-sales
description: >
  This skill executes expansion sales motions to grow revenue within existing
  accounts. Use when asked to plan upsells, cross-sells, or seat expansions.
  Also consider when usage data signals expansion readiness.
  Suggest when an account hits utilization thresholds without an expansion plan.
department: sales
agent: account-executive
version: 1.0.0
complexity: medium
related-skills:
  - ../sales-signal-collector/SKILL.md
  - ../sales-signal-synthesizer/SKILL.md
  - ../../vp-sales/opportunity-framer-sales/SKILL.md
triggers:
  - "plan an upsell"
  - "expand this account"
  - "find cross-sell opportunities"
  - "grow revenue in existing accounts"
---

# expansion-motion-sales

## Agent: Account Executive

L3 account executive (Nx) responsible for sales signal synthesis, signal collection, and expansion sales motions.

Department ethos: [ideal-sales.md](../../../departments/sales/ideal-sales.md)

## Skill Description

Executes expansion sales motions to grow ACV within existing accounts through upsells, cross-sells, and seat expansions timed to usage signals and contract milestones.

## When to Use

- When an existing account hits usage thresholds that indicate readiness for a tier upgrade or seat expansion.
- When contract renewal is approaching and there is an opportunity to expand scope alongside the renewal.
- When a new product capability or module unlocks cross-sell potential into an account's adjacent teams.

## Workflow

1. **Expansion Signal Review**: Review account health data, usage metrics, support ticket trends, and champion engagement level. Identify the expansion trigger: usage ceiling, new department request, or product fit for an adjacent use case. Deliverable: expansion opportunity brief with trigger evidence.
2. **Stakeholder Mapping**: Map the account's organizational structure to identify new buyers, influencers, and potential champions for the expansion. Determine whether the economic buyer from the original deal is still the decision-maker or if a new budget holder is required. Deliverable: updated stakeholder map with expansion-specific roles.
3. **Value Case Construction**: Build the expansion value case using the account's own data: ROI from current usage, time saved, cost avoided, or revenue generated. Frame the expansion as extending proven value to new teams or use cases. Deliverable: account-specific expansion value case.
4. **Proposal and Negotiation**: Present the expansion proposal tied to the value case. Negotiate terms aligned to the existing contract structure (co-term, multi-year, volume discount). Use mutual action plan to drive timeline. Deliverable: expansion proposal with commercial terms. [GATE]
5. **Handoff to CS**: Document the expansion scope, new stakeholders, onboarding requirements, and success criteria. Hand off to Customer Success for implementation planning. Deliverable: expansion handoff document.

## Anti-Patterns

- **Expansion without value proof**: Pitching expansion before demonstrating ROI on the existing deployment. *Why*: asking for more spend before proving current value signals to the buyer that you prioritize revenue over their success.
- **Ignoring the champion**: Running the expansion motion through procurement or a new contact without engaging the original champion. *Why*: the champion has internal credibility and context; bypassing them risks losing your internal advocate and deal momentum.
- **Treating expansion as a new sale**: Running full discovery and qualification as if the account is a net-new prospect. *Why*: the account already has context and trust built; a redundant discovery process wastes their time and signals you do not know your own customer.

## Output

**On success**: Produces an expansion opportunity brief, stakeholder map, value case, proposal with commercial terms, and CS handoff document. Delivered as a closed-won expansion with updated ACV.

**On failure**: Report what blocked the expansion (e.g., budget freeze, low usage, champion departure), what was attempted, and recommended re-engagement timing and strategy.

## Related Skills

- [`sales-signal-collector`](../sales-signal-collector/SKILL.md) -- Provides the raw signals that indicate expansion readiness.
- [`sales-signal-synthesizer`](../sales-signal-synthesizer/SKILL.md) -- Synthesizes signals into actionable expansion insights.
- [`opportunity-framer-sales`](../../vp-sales/opportunity-framer-sales/SKILL.md) -- Provides the original opportunity frame that the expansion builds upon.
