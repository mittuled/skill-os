---
name: technical-expansion-identifier
description: >
  This skill identifies technical expansion opportunities based on account
  usage patterns and unmet technical needs. Use when asked to find upsell
  opportunities in enterprise accounts, analyze usage for expansion signals,
  or identify unmet technical needs. Also consider when renewal conversations
  approach. Suggest when the user manages enterprise accounts without
  systematic expansion identification.
department: customer-success
agent: technical-account-manager
version: 1.0.0
complexity: medium
related-skills: []
---

# technical-expansion-identifier

## Agent: Technical Account Manager

L2 technical account manager (1x) responsible for technical health monitoring of enterprise accounts and identifying expansion opportunities.

Department ethos: [ideal-customer-success.md](../../../../departments/customer-success/ideal-customer-success.md)

## Skill Description

Identifies technical expansion opportunities based on account usage patterns, integration potential, and unmet technical needs in enterprise accounts.

## When to Use

- When enterprise accounts show usage patterns that suggest readiness for expanded product adoption.
- When technical reviews reveal unmet needs that existing or upcoming product capabilities could address.
- When renewal conversations are approaching and expansion opportunities should be identified and qualified beforehand.

## Workflow

1. **Analyze Usage Patterns**: Review account-level usage data for expansion indicators: hitting API limits, increasing user counts, new use case exploration, and integration attempts. Deliverable: usage analysis with expansion indicators.
2. **Map Unmet Technical Needs**: Through technical conversations and support interactions, identify where the account has technical needs not yet addressed by their current product configuration. Deliverable: unmet needs inventory.
3. **Match to Product Capabilities**: Map identified needs and expansion indicators to available product features, higher tiers, add-ons, or upcoming capabilities. Deliverable: opportunity-to-product mapping.
4. **Qualify and Prioritize**: Assess each opportunity by account readiness, revenue potential, and implementation complexity. Prioritize opportunities and prepare handoff briefs for Account Management. Deliverable: qualified opportunity list with handoff briefs.

## Anti-Patterns

- **Selling from the TAM seat**: Directly pitching expansion to customers instead of qualifying and handing off to AM. *Why*: TAMs who sell lose the trusted technical advisor relationship that makes their insights valuable.
- **Technology-push expansion**: Recommending product capabilities the customer does not need because they are available. *Why*: unnecessary expansion erodes trust and creates shelfware that hurts renewal conversations.
- **Ignoring account health**: Pursuing expansion in accounts with unresolved technical issues. *Why*: asking for more spend while basic functionality is broken signals that the company values revenue over customer success.

## Output

**On success**: Produces a qualified expansion opportunity list with usage analysis, unmet needs mapping, product matching, and handoff briefs for Account Management. Delivered to AM and the CS Manager.

**On failure**: Report which accounts could not be analyzed (insufficient usage data, limited technical engagement), what partial opportunities were identified, and what engagement is needed for better data.

## Related Skills

- [`technical-health-monitor`](../technical-health-monitor/SKILL.md) -- Technical health must be stable before pursuing expansion.
- [`expansion-motion-designer-cs`](../../../customer-success/head-of-customer-success/expansion-motion-designer-cs/SKILL.md) -- The expansion motion framework that TAM opportunities feed into.
- [`tam-playbook-contributor`](../tam-playbook-contributor/SKILL.md) -- Expansion identification procedures documented in the TAM playbook.
