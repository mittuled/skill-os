---
name: vendor-security-assessor
description: >
  This skill assesses the security posture of third-party vendors before and during
  engagement. Use when asked to evaluate a vendor's security practices, review vendor
  certifications, or conduct a periodic vendor security review. Also consider when
  onboarding a new vendor that will access company data. Suggest when the user is
  granting a vendor access to systems without a security assessment.
department: legal
agent: security-compliance-programme-manager
version: 1.0.0
complexity: complex
related-skills:
  - ../risk-register-maintainer/SKILL.md
  - ../../../legal/product-counsel/data-processing-agreement-negotiator/SKILL.md
---

# vendor-security-assessor

## Agent: Security & Compliance Programme Manager

L2 security and compliance programme manager (1x) responsible for SOC 2, security awareness training, disaster recovery, GDPR/CCPA compliance, and penetration test programme management.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)

## Skill Description

Assesses the security posture of third-party vendors by reviewing certifications, evaluating security practices, identifying risks, and establishing ongoing monitoring to ensure vendors meet the organization's security requirements.

## When to Use

- When onboarding a new vendor that will access, process, or store company or customer data.
- When the annual vendor security review cycle requires re-assessment of existing vendors.
- When a vendor experiences a security incident and the company needs to evaluate its exposure and the vendor's response.

## Workflow

1. **Vendor Tiering**: Classify the vendor by risk tier based on data access (none, metadata, PII, sensitive PII), system access (none, read-only, read-write, admin), and business criticality (replaceable, important, critical). Assign assessment depth based on tier. Deliverable: vendor risk tier classification.
2. **Questionnaire and Documentation Review**: Send the security questionnaire appropriate to the vendor's tier. Review returned questionnaire, certifications (SOC 2, ISO 27001, HIPAA), penetration test summaries, and security policies. Deliverable: questionnaire review with initial findings.
3. **Gap Analysis**: Compare the vendor's security posture against the organization's vendor security requirements. Identify gaps in areas such as encryption, access controls, incident response, business continuity, and data handling. Deliverable: vendor security gap analysis.
4. **Risk Decision**: Based on the gap analysis, recommend one of: approve (meets requirements), approve with conditions (acceptable gaps with compensating controls or remediation timeline), or reject (unacceptable risk). Document the rationale. Deliverable: vendor security decision with rationale.
5. **Ongoing Monitoring**: For approved vendors, define the ongoing monitoring cadence: annual reassessment, certification renewal tracking, breach notification monitoring, and trigger-based reassessment (vendor incident, scope change). Deliverable: vendor monitoring plan.

## Anti-Patterns

- **Certification-only assessment**: Accepting a SOC 2 or ISO 27001 certificate as sufficient without reviewing scope, exceptions, or complementary user entity controls. *Why*: certifications cover specific scopes and may exclude the services the company uses; exceptions in the report may be material.
- **One-time assessment**: Assessing vendors only at onboarding without periodic reassessment. *Why*: vendor security posture changes over time; a vendor that was secure at onboarding may have degraded practices or experienced unreported incidents.
- **Same assessment for all vendors**: Applying the same assessment depth to a critical data processor and a low-risk SaaS tool. *Why*: tiered assessment allocates review effort proportionally to risk; over-assessing low-risk vendors wastes cycles while under-assessing high-risk vendors creates exposure.
- **Assessment without contractual backing**: Identifying security gaps without requiring contractual remediation commitments. *Why*: assessment findings without contractual enforcement are advisory only; the vendor has no obligation to remediate.

## Output

**On success**: Produces a vendor risk tier classification, questionnaire review, gap analysis, security decision, and monitoring plan. Delivered per the vendor onboarding or review timeline.

**On failure**: Report which vendors could not be assessed (non-responsive, insufficient documentation), what the risk exposure is from proceeding without assessment, and recommended alternatives (different vendor, reduced scope, or risk acceptance with executive sign-off).

## Related Skills

- [`risk-register-maintainer`](../risk-register-maintainer/SKILL.md) -- Vendor security gaps are recorded as third-party risks in the risk register.
- [`data-processing-agreement-negotiator`](../../../legal/product-counsel/data-processing-agreement-negotiator/SKILL.md) -- DPAs formalize the security requirements identified during vendor assessment.
