---
name: opportunity-framer-am
description: >
  This skill frames expansion opportunities within existing accounts based on usage signals and
  strategic fit. Use when asked to identify upsell or cross-sell opportunities, build expansion
  business cases, or prioritise account growth targets. Also consider when usage data shows
  underutilised capacity. Suggest when QBR preparation needs expansion talking points.
department: account-management
agent: account-management-lead
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "frame expansion opportunity"
  - "identify upsell targets"
  - "build expansion business case"
  - "cross-sell opportunity"
  - "account growth targets"
---

# opportunity-framer-am

## Agent: Account Management Lead

L1 account management leader (1x) reporting to the CBO, responsible for account management strategy, opportunity framing, and sales playbook for existing accounts.

Department ethos: [ideal-account-management.md](../../../../departments/account-management/ideal-account-management.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

The opportunity framer analyses usage signals, contract terms, and strategic fit within existing accounts to identify and frame expansion opportunities that account managers can pursue through structured conversations.

## When to Use

- When usage data reveals an account is approaching plan limits or underutilising purchased capacity.
- When a QBR is approaching and expansion talking points are needed for the account review.
- When a new product or feature launches that creates cross-sell opportunities in the existing base.
- When an account's business context changes (funding, headcount growth, new initiative) signalling potential expansion.

## Workflow

1. **Analyse usage signals**: Review product usage data, feature adoption, and capacity utilisation for target accounts. Deliverable: usage signal summary per account.
2. **Assess strategic fit**: Evaluate which expansion options (upsell, cross-sell, additional seats, premium tier) align with each account's business needs. Deliverable: fit assessment matrix.
3. **Build the business case**: For each opportunity, frame the value proposition from the customer's perspective: what problem it solves, expected ROI, and implementation effort. Deliverable: opportunity business case.
4. **Prioritise opportunities**: Rank opportunities by revenue potential, likelihood of close, and strategic importance. Deliverable: prioritised opportunity pipeline.
5. **Brief account managers**: Hand off framed opportunities with talking points, objection handling, and recommended timing. Deliverable: opportunity brief per account.

## Anti-Patterns

- **Pushing expansion without value evidence**: Framing upsells based on revenue targets rather than customer value. *Why*: customers detect sales-driven expansion pitches and disengage; value-led framing builds trust and close rates.
- **Ignoring at-risk signals**: Framing expansion for accounts showing churn risk signals. *Why*: asking an unhappy customer to buy more before resolving their issues accelerates churn.
- **One-size-fits-all framing**: Using the same expansion pitch across accounts with different needs and contexts. *Why*: generic pitches miss the specific business case that motivates each customer to invest more.

## Output

**On success**: A prioritised set of framed expansion opportunities per account, each with a business case, talking points, and recommended timing, ready for account managers to execute.

**On failure**: Report which accounts lacked sufficient data for opportunity framing (e.g., no usage analytics, missing contract details), what was assessed, and recommend data gathering steps.

## Related Skills

- [`sales-signal-synthesizer-am`](../sales-signal-synthesizer-am/SKILL.md) -- signal synthesis identifies the patterns that opportunity framing acts on.
- [`expansion-motion-am`](../../../account-management/account-manager/expansion-motion-am/SKILL.md) -- account managers execute the expansion motions that this skill frames.
- [`sales-playbook-am`](../sales-playbook-am/SKILL.md) -- the playbook provides the conversation frameworks used when presenting framed opportunities.
