---
name: privacy-policy-generator
description: >
  This skill generates comprehensive privacy policies by detecting data collection
  practices from product analysis and mapping them to regulatory disclosure
  requirements. Use when launching a new product, app, or website that collects
  user data. Also consider when adding new data collection features or entering
  new jurisdictions. Suggest when product collects data but has no published
  privacy policy.
department: legal
agent: product-counsel
version: 1.0.0
complexity: complex
related-skills:
  - ../terms-of-service-drafter/SKILL.md
  - ../../../legal/security-compliance-programme-manager/compliance-auditor/SKILL.md
  - ../../../legal/corporate-counsel/contract-review-orchestrator/SKILL.md
triggers:
  - "generate privacy policy"
  - "privacy policy needed"
  - "update privacy policy"
  - "data collection disclosure"
---

# privacy-policy-generator

## Agent: Product Counsel

L2 product counsel (1x) responsible for legal review of business models, positioning, pricing, product compliance, and security audit oversight.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Generates comprehensive privacy policies by detecting data collection practices from product analysis and mapping them to regulatory disclosure requirements across GDPR, CCPA, CalOPPA, and ePrivacy frameworks.

## When to Use

- When launching a new product, application, or website that collects any form of user data and no privacy policy exists.
- When adding new data collection features (analytics, third-party integrations, tracking pixels) that expand the scope of existing data practices beyond what the current policy discloses.
- When expanding into a new jurisdiction (EU, California, Brazil, UK) where additional disclosure requirements apply that the current policy does not address.

## Workflow

1. **Scan Data Collection Points**: Scan the product, website, or application to detect all data collection points including forms, cookies, analytics scripts, third-party integrations, SDKs, APIs, and server-side logging. Use the data detection checklist (see [checklist.md](references/checklist.md)) to ensure no collection point is missed. Deliverable: complete inventory of data collection points with collection method and data flow.

2. **Categorize Data Types**: Categorize every data element collected into the data category taxonomy: personal identifiers, behavioral data, device information, location data, financial data, health data, biometric data, and children's data. Flag sensitive categories that trigger additional regulatory requirements. Deliverable: data categorization matrix mapping each collection point to data categories.

3. **Map Regulatory Requirements**: Map identified data practices to disclosure requirements under each applicable framework: GDPR Articles 13-14 (15 items), CCPA Section 1798.100 (12 items), CalOPPA (8 items), and ePrivacy Directive (6 items for cookies). Identify which requirements apply based on user geography and data types. Deliverable: regulatory mapping table showing each requirement, applicability, and corresponding data practice.

4. **Identify Processors and Third-Party Sharing**: Document all data processors, sub-processors, and third-party recipients. For each, record: entity name, processing purpose, data categories shared, legal basis for sharing, and whether data leaves the originating jurisdiction. Deliverable: third-party data sharing register.

5. **[GATE] Determine Retention and Legal Bases**: Establish data retention periods for each data category and confirm the legal basis for each processing activity (consent, legitimate interest, contractual necessity, legal obligation). Flag any processing activity lacking a defensible legal basis. Deliverable: retention schedule and legal basis register approved by product counsel.

6. **Generate Privacy Policy**: Generate the full privacy policy using the layered notice template (see [privacy-policy-template.md](assets/privacy-policy-template.md)). Populate all sections with product-specific data practices, regulatory disclosures, and third-party information. Annotate each section with the regulatory source requiring the disclosure. Deliverable: draft privacy policy with regulatory source annotations.

7. **Produce Layered Notice Output**: Produce the final policy document in two layers: a one-page summary table for quick reference and the full detailed policy. Verify every regulatory requirement from Step 3 has a corresponding disclosure. Flag any gaps for legal review. Deliverable: layered privacy policy document (summary + full) ready for legal sign-off and publication.

## Anti-Patterns

- **Template-only generation**: Producing a generic privacy policy from a template without actually scanning the product's data collection practices. *Why*: generic policies omit product-specific disclosures and create compliance gaps that regulators and privacy-savvy users will identify.

- **Single-jurisdiction drafting**: Writing the policy to satisfy only one regulatory framework (e.g., GDPR only) when the product serves users in multiple jurisdictions. *Why*: a GDPR-compliant policy may still violate CCPA or CalOPPA requirements; multi-jurisdiction mapping prevents enforcement actions from overlooked regulators.

- **Ignoring third-party data flows**: Listing first-party data collection without mapping third-party scripts, SDKs, and analytics tools that independently collect data. *Why*: third-party collection (e.g., Google Analytics, Facebook Pixel) is subject to the same disclosure requirements and is a leading cause of regulatory complaints.

- **Static publication**: Publishing the policy once without establishing a review trigger for new features, new integrations, or regulatory changes. *Why*: privacy policies must reflect current practices; stale policies create liability when actual practices diverge from published disclosures.

## Output

**On success**: Produces a layered privacy policy document containing a one-page summary table and a full detailed policy with all required disclosures, regulatory source annotations, third-party sharing register, and retention schedule. Delivered to product counsel for final review and to the engineering team for publication.

**On failure**: Report which data collection points could not be fully mapped (e.g., undocumented third-party scripts, unclear server-side logging), which regulatory requirements remain unaddressed, and what information is needed to complete the policy. Escalate to product counsel with a partial draft and gap list.

## Related Skills

- [`terms-of-service-drafter`](../terms-of-service-drafter/SKILL.md) -- Privacy policies and terms of service are co-published; data use disclosures in the privacy policy must align with rights granted in the ToS.
- [`compliance-auditor`](../../../legal/security-compliance-programme-manager/compliance-auditor/SKILL.md) -- Compliance audits assess whether published privacy policies match actual data practices.
- [`contract-review-orchestrator`](../../../legal/corporate-counsel/contract-review-orchestrator/SKILL.md) -- Vendor contracts must include data processing terms consistent with privacy policy commitments.
