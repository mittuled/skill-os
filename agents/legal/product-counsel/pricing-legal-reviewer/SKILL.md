---
name: pricing-legal-reviewer
description: >
  This skill reviews pricing strategy and practices for legal compliance including
  antitrust and consumer protection. Use when asked to vet pricing models for
  legal risk, assess bundling or tying arrangements, or review discount programs.
  Also consider when pricing varies by geography or customer segment. Suggest when
  the user sets pricing without considering legal constraints.
department: legal
agent: product-counsel
version: 1.0.0
complexity: simple
related-skills:
  - ../business-model-legal-reviewer/SKILL.md
  - ../positioning-legal-reviewer/SKILL.md
---

# pricing-legal-reviewer

## Agent: Product Counsel

L2 product counsel (1x) responsible for legal review of business models, positioning, pricing, product compliance, and security audit oversight.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)

## Skill Description

Reviews pricing strategy, discount programs, and billing practices for compliance with antitrust law, consumer protection statutes, and international pricing regulations.

## When to Use

- When the company introduces a new pricing model (usage-based, tiered, freemium-to-paid conversion) and needs to confirm it does not create antitrust or consumer protection exposure.
- When pricing varies by geography, customer segment, or volume in ways that could raise price discrimination concerns under the Robinson-Patman Act or equivalent international regulations.
- When promotional pricing, free trials, or automatic renewal terms are implemented and must comply with state auto-renewal laws and FTC guidelines.

## Workflow

1. **Pricing Structure Review**: Analyze the pricing model for antitrust concerns — predatory pricing assessment against market position, Robinson-Patman Act analysis for differential pricing, tying/bundling review for market power abuse, and price-fixing risk evaluation. For international pricing, assess EU competition law. Deliverable: antitrust risk assessment.
2. **Consumer Protection Compliance**: Review billing practices against California ARL Section 17602, FTC Negative Option Rule, EU Consumer Rights Directive, and Australian Consumer Law. Verify auto-renewal disclosures, free trial conversion flows (check for dark patterns), refund/cancellation policies, and currency conversion transparency. Deliverable: consumer protection checklist with pass/fail per item.
3. **Recommendation**: Apply scoring rubric at `references/scoring-rubric.md`. Provide compliant/modify/reject recommendation with specific changes. Produce memo using template at `assets/pricing-review-memo-template.md`. For modifications, include compliant alternative pricing structures. Deliverable: pricing review memo.

## Anti-Patterns

- **Reviewing price points without billing mechanics**: Assessing the price itself while ignoring how the customer is billed, renewed, and charged for overages. *Why*: most pricing litigation targets billing practices (dark patterns, hidden fees, auto-renewal traps), not the headline price.
- **Ignoring geographic pricing regulations**: Applying US-only analysis when the product is sold internationally. *Why*: EU consumer protection law, Australian Consumer Law, and other jurisdictions impose stricter requirements on pricing transparency, cooling-off periods, and refund rights.

## Output

**On success**: Produces a pricing review memo containing the antitrust risk assessment, consumer protection checklist, and recommendation with approved pricing terms. Delivered to the pricing team and legal records.

**On failure**: Report which pricing elements could not be assessed (e.g., competitor pricing data unavailable for predatory pricing analysis, international billing flow undocumented), what partial review was completed, and what information is needed.

## Related Skills

- [`business-model-legal-reviewer`](../business-model-legal-reviewer/SKILL.md) -- Business model review addresses the broader legal framework within which pricing operates.
- [`positioning-legal-reviewer`](../positioning-legal-reviewer/SKILL.md) -- Pricing claims in marketing materials require coordinated review of both pricing compliance and positioning accuracy.
