---
name: gdpr-ccpa-compliance-manager
description: >
  This skill manages GDPR and CCPA compliance including data mapping, consent
  management, and data subject request processes. Use when asked to build a
  privacy programme, implement DSR workflows, or assess GDPR/CCPA readiness.
  Also consider when expanding into EU markets or processing California
  residents' data. Suggest when the user collects personal data without a
  privacy compliance framework.
department: legal
agent: security-compliance-programme-manager
version: 1.0.0
complexity: complex
related-skills:
  - ../soc2-programme-manager/SKILL.md
  - ../../corporate-counsel/compliance-scanner/SKILL.md
---

# gdpr-ccpa-compliance-manager

## Agent: Security & Compliance Programme Manager

L2 security and compliance programme manager (1x) responsible for SOC 2, security awareness training, disaster recovery, GDPR/CCPA compliance, and penetration test programme management.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)

## Skill Description

Manages the end-to-end GDPR and CCPA compliance programme including data mapping, lawful basis documentation, consent management, data subject request workflows, data processing agreements, and cross-border transfer mechanisms.

## When to Use

- When the company processes personal data of EU residents (GDPR) or California residents (CCPA/CPRA) and needs a structured compliance programme.
- When a new product feature, data integration, or vendor relationship introduces personal data processing activities that require privacy impact assessment.
- When a data subject exercises their rights (access, deletion, portability, opt-out of sale) and the company must respond within statutory deadlines.

## Workflow

1. **Data Mapping and Inventory**: Map all processing activities per the ROPA template in `references/privacy-compliance-framework.md`. Document data categories, data subjects, purposes, lawful basis (GDPR Article 6), retention periods, storage locations, third-party recipients, international transfers, and security measures per GDPR Article 30. Deliverable: Records of Processing Activities (ROPA).
2. **Lawful Basis and Consent Management**: Establish lawful basis per activity using the GDPR vs. CCPA comparison in `references/privacy-compliance-framework.md`. For GDPR consent: verify freely given, specific, informed, unambiguous. For CCPA: implement opt-out of sale/sharing, opt-in for under-16. Deliverable: lawful basis register and consent management specifications.
3. **Data Subject Request Workflow**: Build DSR workflows per the intake-verification-processing-response lifecycle in `references/privacy-compliance-framework.md`. Cover each right: access (Art. 15, CCPA right to know), deletion (Art. 17, CCPA right to delete), portability (Art. 20), rectification (Art. 16), restriction (Art. 18), opt-out (CCPA). Enforce SLAs: 30 days GDPR, 45 days CCPA. Deliverable: DSR workflow documentation.
4. **Data Processing Agreements**: Ensure all processors and subprocessors have executed DPAs compliant with GDPR Article 28 containing required clauses: processing instructions, confidentiality, security measures, subprocessor controls, data breach notification, audit rights, and data return/deletion obligations. Deliverable: DPA tracker with execution status per vendor and gap list for non-compliant agreements.
5. **Cross-Border Transfer Mechanisms**: Assess all international data transfers and implement appropriate transfer mechanisms: Standard Contractual Clauses (SCCs), adequacy decisions, binding corporate rules, or derogations. Conduct Transfer Impact Assessments (TIAs) where required. Deliverable: transfer mechanism register with TIA documentation per transfer.
6. **Privacy Impact Assessment Process**: Establish a DPIA process for high-risk processing activities (large-scale profiling, systematic monitoring, sensitive data processing). Define triggers, assessment methodology, and mitigation requirements. Deliverable: DPIA template and process documentation.
7. **Ongoing Monitoring and Reporting**: Establish privacy metrics (DSR response times, consent rates, DPA coverage), quarterly compliance reporting, and regulatory monitoring for privacy law developments (new state laws, EU guidance, enforcement actions). Deliverable: privacy compliance dashboard and quarterly report template.

## Anti-Patterns

- **Treating GDPR and CCPA as identical**: Applying GDPR compliance measures wholesale to CCPA without addressing CCPA-specific requirements (right to opt out of sale, financial incentive disclosures, authorized agent requests). *Why*: the two frameworks have different rights, definitions, and exemptions; a GDPR-only approach creates CCPA gaps and vice versa.
- **Cookie consent as the entire privacy programme**: Equating privacy compliance with implementing a cookie banner while ignoring data mapping, DPAs, DSR workflows, and cross-border transfers. *Why*: cookie consent is one component of a much broader compliance obligation; enforcement actions target systematic failures, not cookie banners.
- **Delegating DSR processing entirely to engineering**: Treating data subject requests as a pure technical exercise without legal review of exemptions, identity verification, and response adequacy. *Why*: DSR responses involve legal judgment (e.g., whether an exemption applies, whether third-party data must be redacted); incorrect responses create regulatory exposure.
- **Ignoring processor chain obligations**: Maintaining DPAs with direct vendors while failing to audit or contractually bind subprocessors further down the chain. *Why*: GDPR holds the controller responsible for the entire processing chain; an uncontrolled subprocessor creates liability regardless of direct vendor compliance.

## Output

**On success**: Produces the complete privacy compliance programme containing ROPA, lawful basis register, consent management specifications, DSR workflow documentation, DPA tracker, transfer mechanism register, DPIA process documentation, privacy dashboard, and quarterly report template. Delivered to the DPO (or equivalent), legal leadership, and engineering.

**On failure**: Report which compliance components could not be completed (e.g., incomplete data mapping due to undocumented systems, unsigned DPAs with critical vendors, unresolved cross-border transfer mechanisms), what interim measures are in place, and what actions are needed with estimated timelines.

## Related Skills

- [`soc2-programme-manager`](../soc2-programme-manager/SKILL.md) -- SOC 2 privacy criteria overlap with GDPR/CCPA requirements; coordinating both programmes reduces duplicate effort.
- [`compliance-scanner`](../../corporate-counsel/compliance-scanner/SKILL.md) -- The compliance scanner identifies which privacy regulations apply; this skill implements the compliance programme for GDPR and CCPA specifically.
