---
name: terms-of-service-generator
description: >
  This skill generates GDPR/CCPA-compliant Terms of Service by analyzing a product's
  website, features, and data practices to produce a comprehensive, enforceable ToS.
  Use when launching a new product or service that needs Terms of Service. Also consider
  when existing ToS needs updating for new features, jurisdictions, or regulatory changes.
  Suggest when product launches without published terms.
department: legal
agent: product-counsel
version: 1.0.0
complexity: complex
related-skills:
  - ../../../legal/product-counsel/privacy-policy-generator/SKILL.md
  - ../../../legal/corporate-counsel/contract-review-orchestrator/SKILL.md
  - ../../../legal/corporate-counsel/compliance-scanner/SKILL.md
triggers:
  - "generate terms of service"
  - "ToS needed"
  - "update terms of service"
  - "product launch needs terms"
---

# terms-of-service-generator

## Agent: Product Counsel

L2 product counsel (1x) responsible for business model legal review, positioning review, pricing review, PRD compliance, security review, security audit, and compliance review for product launches.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Generates GDPR/CCPA-compliant Terms of Service by analyzing a product's features, data practices, and applicable jurisdictions to produce a comprehensive, enforceable ToS with plain-English annotations.

## When to Use

- When launching a new product or service that requires Terms of Service before going live.
- When existing Terms of Service need updating due to new features, expanded jurisdictions, or regulatory changes.
- When a product is live without published terms, creating legal exposure.
- When entering a new market (EU, California, etc.) that imposes additional disclosure requirements on existing terms.

## Workflow

1. **Product Analysis**: Scan the product website, app, or documentation to identify all features, data collection points, user interactions, payment flows, user-generated content mechanisms, and third-party integrations. Map each feature to its legal implications (e.g., file upload → content licensing, payment → refund policy, user profiles → data collection). Deliverable: product feature inventory with legal implication mapping.

2. **Jurisdiction and Regulation Mapping**: Determine all applicable jurisdictions based on where the company operates, where users are located, and where data is processed. Identify applicable regulations: GDPR (EU users), CCPA/CPRA (California users), CAN-SPAM (email communications), COPPA (users under 13), sector-specific regulations (HIPAA, PCI-DSS). Cross-reference against the [regulatory compliance checklist](references/checklist.md). Deliverable: jurisdiction map with applicable regulation list.

3. **Clause Set Selection**: Select the appropriate clause set based on product type: SaaS (subscription access to hosted software), Marketplace (platform connecting buyers and sellers), Social Platform (user-generated content and interactions), E-commerce (direct sale of goods or services), or Hybrid (combining multiple types). Merge clause sets if the product spans multiple types. Deliverable: selected clause set with product-type rationale.

4. **ToS Generation**: Generate the Terms of Service using the [ToS template](assets/terms-of-service-template.md) with all required sections: acceptance mechanism, definitions, account terms, user obligations and acceptable use, intellectual property rights, payment and billing (if applicable), data practices summary, limitation of liability, warranties and disclaimers, termination, dispute resolution, governing law, modification procedures, and contact information. Populate all [CUSTOMIZE] markers with product-specific content. Deliverable: complete ToS draft.

5. **GDPR Compliance Layer**: Apply GDPR Article 13/14 disclosure requirements. Verify the ToS includes or references: legal basis for processing, data controller identity, DPO contact (if applicable), data subject rights (access, rectification, erasure, portability, objection), cross-border transfer mechanisms, retention periods, and right to lodge a complaint with a supervisory authority. Add or modify clauses to meet each requirement. Deliverable: GDPR-annotated ToS.

6. **CCPA Compliance Layer**: Apply CCPA/CPRA consumer rights sections. Verify the ToS includes or references: categories of personal information collected, purposes of collection, consumer rights (know, delete, opt-out of sale, non-discrimination), "Do Not Sell My Personal Information" mechanism, financial incentive disclosures (if applicable), and verification process for consumer requests. Add or modify clauses to meet each requirement. Deliverable: CCPA-annotated ToS.

7. **[GATE] Finalization and Plain-English Sidebar**: Add a plain-English sidebar or annotation for each major section explaining what it means in practical terms. Review the complete document for internal consistency, completeness against the regulatory checklist, and enforceability. Verify that acceptance mechanism is legally binding (clickwrap preferred over browsewrap). Deliverable: final ToS document with plain-English sidebar, ready for legal review and publication.

## Anti-Patterns

- **Copy-pasting another company's ToS**: Using a competitor's or template service's ToS without adapting to the specific product. *Why*: ToS must reflect the actual product features and data practices — a SaaS ToS applied to a marketplace creates unenforceable clauses and misses platform-specific liability protections.

- **Burying critical terms**: Hiding limitation of liability, auto-renewal, or arbitration clauses deep in dense paragraphs. *Why*: courts increasingly scrutinize whether consumers had reasonable notice of material terms — buried terms may be found unconscionable, and regulators (FTC, EU consumer protection) actively target dark patterns in terms.

- **Ignoring browsewrap vs. clickwrap enforceability**: Relying on a footer link ("by using this site you agree") instead of affirmative consent. *Why*: browsewrap agreements have significantly lower enforceability than clickwrap — courts have repeatedly found that passive access does not constitute agreement, especially for material terms like arbitration.

- **Static ToS for evolving products**: Publishing ToS once and never updating as the product adds features, enters new markets, or changes data practices. *Why*: stale ToS creates gaps between what the product does and what the terms cover, exposing the company to regulatory action and limiting the enforceability of terms that do not reflect current practices.

- **Omitting modification notice requirements**: Reserving the right to change terms at any time without notice. *Why*: while many ToS include this clause, unilateral modification without reasonable notice may render changes unenforceable — GDPR and consumer protection laws increasingly require affirmative notification of material changes.

## Output

**On success**: Produces a complete, regulation-compliant Terms of Service with GDPR Article 13/14 disclosures, CCPA consumer rights sections, product-specific clauses, plain-English sidebar annotations, and a compliance coverage summary. Delivered using the [ToS template](assets/terms-of-service-template.md). Reference the [regulatory compliance checklist](references/checklist.md) for validation.

**On failure**: Report which product features could not be analyzed (e.g., payment flow undocumented, data practices unknown), which regulatory requirements could not be addressed (e.g., jurisdiction unclear), what partial ToS was produced, and what information must be gathered to complete the document.

## Related Skills

- [`privacy-policy-generator`](../../../legal/product-counsel/privacy-policy-generator/SKILL.md) — Companion document that must be generated alongside or referenced by the ToS for data practice disclosures.
- [`contract-review-orchestrator`](../../../legal/corporate-counsel/contract-review-orchestrator/SKILL.md) — Reviews third-party terms that the product may incorporate by reference.
- [`compliance-scanner`](../../../legal/corporate-counsel/compliance-scanner/SKILL.md) — Validates regulatory compliance of the generated ToS against applicable frameworks.
