---
name: terms-of-service-drafter
description: >
  This skill drafts and maintains the terms of service and related user agreements.
  Use when asked to draft ToS, update terms for a product change, or review terms
  for legal adequacy. Also consider when the product's functionality changes in ways
  that make current terms inaccurate. Suggest when the user is launching new features
  not covered by existing terms.
department: legal
agent: product-counsel
version: 1.0.0
complexity: complex
related-skills:
  - ../content-moderation-advisor/SKILL.md
  - ../privacy-impact-assessor/SKILL.md
---

# terms-of-service-drafter

## Agent: Product Counsel

L2 product counsel (1x) responsible for legal review of business models, positioning, pricing, product compliance, and security audit oversight.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)

## Skill Description

Drafts and maintains the terms of service and related user agreements by translating product functionality, business model, and legal requirements into enforceable, user-comprehensible terms that protect the company while maintaining user trust.

## When to Use

- When the company is launching a new product or service that requires initial terms of service.
- When product changes (new features, pricing model changes, data practices changes) make existing terms inaccurate or insufficient.
- When entering a new jurisdiction that requires terms modifications (consumer protection, language requirements, mandatory clauses).

## Workflow

1. **Scope Definition**: Identify all product functionality, user interactions, data practices, and business model elements that the terms must cover. Map each element to the legal protections it requires (liability limitations, IP ownership, acceptable use, dispute resolution). Deliverable: terms scope matrix.
2. **Jurisdictional Requirements**: Identify mandatory terms and prohibited clauses by jurisdiction. Review consumer protection requirements (cooling-off periods, unfair terms regulations), data protection requirements, and sector-specific mandatory disclosures. Deliverable: jurisdictional requirements checklist.
3. **Drafting**: Draft the terms in clear, accessible language while maintaining legal enforceability. Structure sections logically: account terms, acceptable use, intellectual property, payment terms, liability, dispute resolution, termination, and modifications. Deliverable: draft terms of service.
4. **Internal Review**: Route the draft to product, engineering, and business stakeholders to verify accuracy of product descriptions, data practices, and commercial terms. Deliverable: stakeholder-reviewed draft.
5. **Enforceability Optimization**: Review clickwrap/browsewrap implementation for enforceability. Ensure the acceptance mechanism creates a binding agreement. Design the change notification process for existing users. Deliverable: acceptance mechanism specification and change notification plan.
6. **Publication and Versioning**: Publish the terms with proper versioning, effective date, and change summary. Archive previous versions. Implement the user notification process for material changes. Deliverable: published terms with version history. [GATE]

## Anti-Patterns

- **Copy-paste from competitors**: Adopting another company's terms without customization. *Why*: terms must reflect the specific product, business model, and jurisdictional exposure; borrowed terms may include inapplicable provisions and miss critical protections.
- **Legalese maximalism**: Drafting terms in dense legal language that no user can understand. *Why*: courts in many jurisdictions disfavour incomprehensible terms; clear language improves enforceability and user trust.
- **Set-and-forget terms**: Drafting terms once and never updating them as the product evolves. *Why*: outdated terms create gaps between what the terms permit and what the product does, reducing legal protection and potentially misleading users.
- **Silent updates**: Changing terms materially without notifying users or providing opt-out mechanisms. *Why*: silent changes may be unenforceable; many jurisdictions require affirmative consent for material changes.

## Output

**On success**: Produces published terms of service with jurisdictional compliance, acceptance mechanism specification, change notification plan, and version history. Delivered for launch and updated per product changes.

**On failure**: Report which product areas lack terms coverage, which jurisdictional requirements are unmet, and what the legal exposure is from operating under incomplete terms. Escalate to General Counsel.

## Related Skills

- [`content-moderation-advisor`](../content-moderation-advisor/SKILL.md) -- Content moderation policies must be consistent with the acceptable use provisions in the terms of service.
- [`privacy-impact-assessor`](../privacy-impact-assessor/SKILL.md) -- Privacy practices described in the terms must align with the privacy impact assessment findings.
