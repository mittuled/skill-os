---
name: expansion-motion-am
description: >
  This skill executes expansion motions within assigned accounts including upsell, cross-sell, and
  multi-year renewal conversations. Use when asked to grow account revenue, negotiate renewals,
  or present expansion proposals. Also consider when a framed opportunity has been handed off.
  Suggest when an account's usage signals indicate readiness for a larger plan.
department: account-management
agent: account-manager
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "run expansion motion"
  - "execute account expansion"
  - "upsell motion AM"
  - "grow account ARR"
  - "expansion playbook AM"
---

# expansion-motion-am

## Agent: Account Manager

L2 account manager (Nx, multi-instance) responsible for collecting account signals and executing expansion motions.

Department ethos: [ideal-account-management.md](../../../../departments/account-management/ideal-account-management.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

The expansion motion executor runs the end-to-end expansion process for assigned accounts -- from presenting the framed opportunity through negotiation to close -- to grow revenue through upsells, cross-sells, and multi-year renewals.

## When to Use

- When an opportunity has been framed by the AM lead and handed off for execution.
- When an account's usage signals indicate they are approaching plan limits and would benefit from a larger tier.
- When a renewal conversation presents a natural opportunity to propose multi-year terms or additional products.
- When a customer proactively asks about additional capabilities or higher-tier features.

## Workflow

1. **Review the opportunity brief**: Understand the framed opportunity, business case, and recommended approach. Deliverable: internalised opportunity context.
2. **Prepare the proposal**: Build a tailored expansion proposal with pricing, implementation timeline, and expected value. Deliverable: expansion proposal document.
3. **Present to the customer**: Deliver the proposal in a value-led conversation tied to the customer's business outcomes. Deliverable: customer meeting with proposal presented.
4. **Handle objections**: Address customer concerns using the playbook objection-handling frameworks. Deliverable: objection responses documented.
5. **Negotiate and close**: Negotiate final terms, obtain customer commitment, and process the expansion order. Deliverable: signed expansion agreement.
6. **Hand off to implementation**: Brief the implementation or CS team on what was sold and any commitments made. Deliverable: implementation handoff document.

## Anti-Patterns

- **Leading with price instead of value**: Opening the expansion conversation with pricing rather than the business problem the expansion solves. *Why*: price-first conversations trigger procurement objections; value-first conversations create budget willingness.
- **Selling without customer success alignment**: Proposing expansion to a customer with open support issues or low satisfaction. *Why*: unhappy customers do not buy more; resolve issues first, then expand.
- **Vague commitments during negotiation**: Making verbal promises about features or timelines that are not in the contract. *Why*: unwritten commitments become disputed expectations that damage the relationship post-close.

## Output

**On success**: A signed expansion agreement with a completed implementation handoff document, the CRM updated with the new deal value, and the customer relationship strengthened.

**On failure**: Report why the expansion did not close (customer objection, budget constraints, timing), what was proposed, and recommend next steps (retry timing, alternative offer, relationship repair).

## Related Skills

- [`opportunity-framer-am`](../../../account-management/account-management-lead/opportunity-framer-am/SKILL.md) -- opportunity framing provides the business case that this skill executes.
- [`sales-signal-collector-am`](../sales-signal-collector-am/SKILL.md) -- signals collected during expansion conversations feed back into portfolio intelligence.
- [`sales-playbook-am`](../../../account-management/account-management-lead/sales-playbook-am/SKILL.md) -- the playbook provides the conversation frameworks used during expansion execution.
