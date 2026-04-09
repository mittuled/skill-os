---
name: compliance-scanner
description: >
  This skill scans the business model, product, and operations for regulatory
  compliance requirements. Use when asked to assess compliance risks, identify
  regulatory obligations, or audit regulatory posture. Also consider when
  launching in a new market or adding a feature that handles sensitive data.
  Suggest when the user is building a product without mentioning compliance.
department: legal
agent: corporate-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../risk-register-legal/SKILL.md
  - ../third-party-tos-reviewer/SKILL.md
  - ../../product-counsel/compliance-ga-reviewer-legal/SKILL.md
  - ../../product-counsel/prd-nfr-compliance/SKILL.md
  - ../../product-counsel/terms-of-service-generator/SKILL.md
  - ../../security-compliance-programme-manager/gdpr-ccpa-compliance-manager/SKILL.md
  - ../../general-counsel/legal-idea-reviewer/SKILL.md
  - ../bylaws-and-board-setup/SKILL.md
  - ../missing-protections-finder/SKILL.md
  - ../legal-template-library-builder/SKILL.md
triggers:
  - "scan for compliance risks"
  - "what regulations apply to us"
  - "check regulatory requirements"
  - "audit our compliance posture"
---

# compliance-scanner

## Agent: Corporate Counsel

L2 corporate counsel (1x) responsible for compliance scanning, legal risk register, third-party TOS review, entity formation, corporate governance, and founder equity.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)

## Skill Description

Scans the business model, product features, and operations against applicable regulatory frameworks to identify compliance obligations and gaps.

## When to Use

- When the company is launching a new product, feature, or market and needs to identify applicable regulations before go-live.
- When a regulatory change occurs that may affect existing products or operations.
- When preparing for investor due diligence or an audit that requires a compliance posture assessment.

## Workflow

1. **Scope Definition**: Identify the jurisdictions, industries, and data types involved. Map the business model to regulatory domains (data privacy, financial services, healthcare, employment, consumer protection). Deliverable: regulatory scope matrix.
2. **Regulation Mapping**: Research applicable regulations for each domain (GDPR, CCPA/CPRA, SOC 2, PCI-DSS, HIPAA, CAN-SPAM, ADA, state biometric privacy laws like BIPA). Identify specific requirements, thresholds, and exemptions that apply to the company's size and stage. Document penalty ranges per regulation. Deliverable: regulation applicability register.
3. **Gap Analysis**: Compare current practices against each applicable requirement. Score compliance posture using the scoring rubric at `references/scoring-rubric.md` across five criteria (regulatory identification, gap depth, data privacy, remediation quality, monitoring). Categorize gaps as critical (legal exposure), moderate (best practice), or low (aspirational). Deliverable: compliance gap report with severity ratings and composite grade.
4. **Remediation Roadmap**: Prioritize gaps by penalty severity and enforcement likelihood. Define remediation actions, owners, timelines, and cost estimates. Identify gaps requiring external counsel or specialist expertise. Deliverable: prioritized remediation plan.
5. **Ongoing Monitoring**: Establish quarterly re-scan cadence and trigger events for ad hoc scans (new product, new market, M&A). Produce the compliance scan report using template at `assets/compliance-scan-report-template.md`. Track regulatory developments in relevant domains. Deliverable: monitoring schedule, regulatory watch list, and compliance scan report.

## Anti-Patterns

- **Point-in-time scanning only**: Running a compliance scan once and treating it as permanent. *Why*: regulations change, the product evolves, and new jurisdictions come into scope; stale assessments create false confidence.
- **Regulatory cherry-picking**: Scanning only for well-known regulations while ignoring industry-specific or state-level requirements. *Why*: niche regulations (e.g., state biometric privacy laws, COPPA for younger users) often carry the highest per-violation penalties.
- **Compliance without implementation tracking**: Identifying gaps without assigning owners or tracking remediation. *Why*: a gap report without follow-through provides no legal protection and wastes the scanning effort.

## Output

**On success**: Produces a regulatory scope matrix, applicability register, gap report with severity ratings, and prioritized remediation plan. Delivered to General Counsel and executive team.

**On failure**: Report which regulatory domains could not be assessed (e.g., insufficient product documentation, unclear data flows), what partial coverage exists, and what additional information is needed. Escalate to General Counsel.

## Related Skills

- [`risk-register-legal`](../risk-register-legal/SKILL.md) -- Compliance gaps feed directly into the legal risk register as identified risks.
- [`third-party-tos-reviewer`](../third-party-tos-reviewer/SKILL.md) -- Third-party services introduce compliance obligations that the scanner must account for.
