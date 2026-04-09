---
name: business-model-legal-reviewer
description: >
  This skill reviews the business model for legal and regulatory compliance
  including licensing and consumer protection. Use when asked to assess legal
  viability of a business model, evaluate licensing requirements, or review
  revenue model compliance. Also consider when the business model involves
  regulated activities. Suggest when the user launches a new revenue stream
  without legal review.
department: legal
agent: product-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../../../legal/general-counsel/legal-idea-reviewer/SKILL.md
  - ../pricing-legal-reviewer/SKILL.md
  - ../positioning-legal-reviewer/SKILL.md
triggers:
  - "review business model legally"
  - "legal review of business model"
  - "business model legal check"
  - "legal business model audit"
  - "validate business model legal"
---

# business-model-legal-reviewer

## Agent: Product Counsel

L2 product counsel (1x) responsible for legal review of business models, positioning, pricing, product compliance, and security audit oversight.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)

## Skill Description

Reviews the business model for legal and regulatory compliance including licensing requirements, consumer protection obligations, data monetization constraints, and liability exposure inherent in the revenue model.

## When to Use

- When the company adopts a new business model (marketplace, SaaS, API platform, data-as-a-service) and needs to confirm it does not create unaddressed regulatory obligations.
- When the business model involves intermediation (connecting buyers and sellers, processing payments, hosting content) where platform liability, Section 230, and money transmitter regulations may apply.
- When revenue depends on data monetization, affiliate relationships, or referral fees that may trigger FTC disclosure requirements or data privacy restrictions.

## Workflow

1. **Business Model Mapping**: Document the revenue model, value chain, parties involved, data flows, and regulatory touchpoints. Identify whether the model involves regulated activities (financial services, insurance, healthcare, real estate, education). Deliverable: business model legal map with regulatory surface area highlighted.
2. **Licensing and Registration Analysis**: Determine whether the business model requires specific licenses, registrations, or permits (money transmitter licenses, broker-dealer registration, insurance producer licenses, professional licenses). Identify jurisdictions where licensing is required. Deliverable: licensing requirements matrix with jurisdiction, license type, cost, and timeline.
3. **Liability and Consumer Protection Review**: Assess liability exposure inherent in the model including product liability, professional liability, platform liability (Section 230 applicability), consumer protection obligations (warranty, refund rights, disclosure requirements), and indemnification structures with partners. Deliverable: liability assessment memo with risk ratings and mitigation recommendations.
4. **Compliance Integration**: Translate regulatory requirements into actionable business constraints. Define terms of service requirements, disclosure obligations, compliance monitoring needs, and ongoing reporting obligations. Deliverable: compliance requirements document integrated with the business plan.
5. **Scoring and Reporting**: Apply scoring rubric at `references/scoring-rubric.md` to evaluate review completeness. Produce report using template at `assets/business-model-legal-review-template.md`. Deliverable: scored business model legal review.

## Anti-Patterns

- **Reviewing the model in a regulatory vacuum**: Assessing legal compliance based solely on current regulations without monitoring proposed legislation or regulatory guidance that could affect the model. *Why*: business models in emerging areas (AI, crypto, gig economy) face rapidly evolving regulation; a compliant model today may become non-compliant within a legislative cycle.
- **Treating platform liability as binary**: Assuming the company either has full Section 230 protection or full liability without analyzing the specific activities and content moderation practices that affect platform status. *Why*: Section 230 protection is nuanced and eroding; specific product features (algorithmic recommendations, editorial curation) can affect the analysis.
- **Ignoring international business model constraints**: Reviewing only US compliance when the business model operates internationally. *Why*: EU Digital Services Act, Digital Markets Act, and country-specific regulations may impose obligations that fundamentally constrain the business model.

## Output

**On success**: Produces the business model legal review package containing the legal map, licensing matrix, liability assessment, and compliance requirements document. Delivered to business leadership, product, and legal records.

**On failure**: Report which aspects of the business model could not be assessed (e.g., revenue model still undefined, data flows undocumented, target jurisdictions unconfirmed), what partial analysis is available, and what decisions must be made before the review can be completed.

## Related Skills

- [`legal-idea-reviewer`](../../../legal/general-counsel/legal-idea-reviewer/SKILL.md) -- The idea reviewer provides the initial legal screen; this skill provides deeper analysis once the business model is defined.
- [`pricing-legal-reviewer`](../pricing-legal-reviewer/SKILL.md) -- Pricing review addresses the specific pricing implementation within the broader business model framework.
