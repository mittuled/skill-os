---
name: nda-generator
description: >
  This skill generates Non-Disclosure Agreements in 4 variants (mutual, one-way,
  employee, consultant) with plain English annotations explaining each clause's
  purpose. Use when any party requests an NDA before sharing confidential information.
  Also consider when standard NDA template needs customization for specific deal
  context. Suggest when business development or partnership discussions begin.
department: legal
agent: corporate-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../../../legal/corporate-counsel/contract-review-orchestrator/SKILL.md
  - ../../../legal/corporate-counsel/missing-protections-finder/SKILL.md
  - ../../../legal/product-counsel/terms-of-service-generator/SKILL.md
triggers:
  - "NDA"
  - "generate NDA"
  - "non-disclosure agreement"
  - "draft NDA"
---

# nda-generator

## Agent: Corporate Counsel

L2 corporate counsel (1x) responsible for compliance scanning, risk registers, third-party ToS review, entity formation, bylaws, equity issuance, and agreement generation.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Generates Non-Disclosure Agreements in four variants with plain English annotations, producing contracts that are both legally enforceable and understandable by non-lawyers.

## When to Use

- When any internal team requests an NDA before sharing confidential information with an external party.
- When an existing NDA template needs customization for a specific deal, jurisdiction, or relationship type.
- When business development, partnership, or vendor discussions begin and no NDA is in place.
- When onboarding a new employee or contractor who will access confidential information.

## Workflow

1. **Variant Selection**: Determine the appropriate NDA variant based on the relationship and information flow. Mutual: both parties share confidential information (partnerships, joint ventures). One-way disclosing: company shares information, counterparty receives (vendor evaluations, investor pitches). One-way receiving: counterparty shares, company receives (acquisition targets, inbound technology). Employee/Consultant: individual bound to company confidentiality. Deliverable: selected variant with rationale.

2. **Parameter Gathering**: Collect all required parameters: full legal names of parties, effective date, confidentiality term (typically 2-5 years), jurisdiction (governing law and venue), specific carve-outs or exclusions (e.g., information already known, independently developed, publicly available), any deal-specific additions (non-solicitation, non-compete during term, residuals clause). Deliverable: completed parameter sheet.

3. **NDA Generation**: Generate the NDA using the selected variant template from the [NDA template](assets/nda-template.md) and the [clause framework](references/framework.md). Populate all placeholders with gathered parameters. Include all standard clauses: definition of confidential information, exclusions, obligations of receiving party, term and termination, return/destruction of materials, remedies (including injunctive relief), and miscellaneous provisions. Deliverable: complete NDA draft.

4. **Plain-English Annotation**: Add a plain-English annotation after each substantive clause explaining its purpose, practical effect, and why it matters. Follow the legal department's ethos of plain language over legal jargon. Annotations should help non-lawyers understand what they are agreeing to without needing legal counsel for basic comprehension. Deliverable: annotated NDA.

5. **[GATE] Review and Finalization**: Present the annotated NDA for review. Verify all parameters are correctly populated, all variant-specific sections are included (and inapplicable sections removed), jurisdiction-specific requirements are met, and the document is ready for signature. Deliverable: final NDA document ready for counterparty delivery.

## Anti-Patterns

- **One-size-fits-all NDA**: Using a mutual NDA when information flow is one-directional. *Why*: mutual NDAs impose obligations on both parties — if the company is only disclosing, a mutual NDA unnecessarily restricts the company's use of information it did not receive.

- **Overly broad confidential information definition**: Defining confidential information as "everything disclosed" without meaningful boundaries. *Why*: overbroad definitions are harder to enforce, may be struck down by courts, and create compliance burden for the receiving party that breeds resentment and non-compliance.

- **Missing jurisdiction-specific requirements**: Using US-style NDAs for UK or EU counterparties without adapting to local law. *Why*: enforceability varies by jurisdiction — non-compete provisions in NDAs may be void in California, and GDPR may impose additional requirements on how confidential personal data is handled.

- **Skipping annotations for "simple" NDAs**: Omitting plain-English explanations because the NDA is "standard." *Why*: every NDA is standard to a lawyer and foreign to the business person signing it — annotations prevent misunderstandings that lead to inadvertent breaches.

## Output

**On success**: Produces a complete, annotated NDA in the selected variant with all parameters populated, plain-English annotations for each clause, and jurisdiction-appropriate provisions. Delivered using the [NDA template](assets/nda-template.md).

**On failure**: Report which parameters could not be determined (e.g., counterparty legal name unknown, jurisdiction unclear), what partial draft was produced, and what information must be gathered to complete the NDA.

## Related Skills

- [`contract-review-orchestrator`](../../../legal/corporate-counsel/contract-review-orchestrator/SKILL.md) — Reviews counterparty-provided NDAs when company paper is not used.
- [`missing-protections-finder`](../../../legal/corporate-counsel/missing-protections-finder/SKILL.md) — Validates generated NDA against the NDA protection checklist.
- [`terms-of-service-generator`](../../../legal/product-counsel/terms-of-service-generator/SKILL.md) — Parallel document generation skill for product-facing legal documents.
