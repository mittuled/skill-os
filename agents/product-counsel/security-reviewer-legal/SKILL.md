---
name: security-reviewer-legal
description: >
  This skill reviews security architecture and practices for legal and regulatory
  compliance. Use when asked to assess whether security controls meet legal
  requirements, review data protection measures for regulatory adequacy, or
  evaluate encryption and access controls against compliance standards. Also
  consider when designing security architecture for regulated data. Suggest when
  the user builds security controls without considering legal requirements.
department: legal
agent: product-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../security-auditor-legal/SKILL.md
  - ../../security-compliance-programme-manager/soc2-programme-manager/SKILL.md
---

# security-reviewer-legal

## Agent: Product Counsel

L2 product counsel (1x) responsible for legal review of business models, positioning, pricing, product compliance, and security audit oversight.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)

## Skill Description

Reviews security architecture, data protection practices, and access controls for compliance with legal and regulatory requirements including GDPR technical measures, SOC 2 criteria, and contractual security obligations.

## When to Use

- When a new system architecture is designed that will process personal data, financial data, or protected health information and must meet "appropriate technical measures" standards under GDPR Article 32 or equivalent regulations.
- When customer contracts or enterprise sales require specific security representations (encryption standards, access controls, data residency) that must be verified against actual implementation.
- When the security team proposes architecture changes and needs legal confirmation that the proposed controls satisfy regulatory and contractual obligations.

## Workflow

1. **Requirements Mapping**: Compile all legal and contractual security requirements applicable to the system under review. Sources include GDPR Article 32 (appropriate technical and organizational measures), SOC 2 Trust Services Criteria, customer DPA security schedules, cyber insurance policy requirements, and industry standards (PCI-DSS, HIPAA Security Rule). Deliverable: security requirements register mapping each requirement to its legal source.
2. **Architecture Assessment**: Review the security architecture against the requirements register. Assess encryption (at rest, in transit, key management), access controls (RBAC, MFA, least privilege), data residency and cross-border transfer mechanisms (SCCs, adequacy decisions), logging and monitoring, incident response capabilities, and vendor security (subprocessor obligations). Deliverable: compliance gap analysis mapping each requirement to current implementation status.
3. **Contractual Representation Verification**: Verify that security representations made in customer contracts, DPAs, and marketing materials are accurate and defensible based on actual security posture. Flag any representations that overstate current capabilities. Deliverable: representation accuracy report with flagged items.
4. **Recommendation and Roadmap**: Provide a compliant/non-compliant assessment with specific remediation requirements for gaps. Prioritize by regulatory exposure and contractual breach risk. Deliverable: security compliance review memo with remediation roadmap.

## Anti-Patterns

- **Reviewing security in legal terms only**: Assessing compliance documentation without understanding the actual technical implementation. *Why*: a policy that requires encryption is meaningless if the implementation uses deprecated algorithms or stores keys alongside encrypted data; legal review must engage with technical reality.
- **One-size-fits-all security requirements**: Applying the same security standard to all data types regardless of sensitivity classification. *Why*: GDPR requires "appropriate" measures proportional to risk; over-engineering security for low-sensitivity data wastes resources while under-engineering for high-sensitivity data creates liability.
- **Ignoring subprocessor security**: Reviewing the company's own security controls without assessing whether subprocessors meet equivalent standards. *Why*: the company remains liable for subprocessor security under GDPR Article 28; a compliant primary system with a non-compliant subprocessor creates an unmitigated legal exposure.

## Output

**On success**: Produces the security compliance review memo containing the requirements register, gap analysis, representation accuracy report, and remediation roadmap. Delivered to the security team, product counsel records, and relevant customer-facing teams.

**On failure**: Report which security areas could not be assessed (e.g., undocumented architecture, vendor security posture unknown), what partial assessment is available, and what technical documentation or access is needed to complete the review.

## Related Skills

- [`security-auditor-legal`](../security-auditor-legal/SKILL.md) -- The auditor handles reactive review of security findings; this skill provides proactive architectural review.
- [`soc2-programme-manager`](../../security-compliance-programme-manager/soc2-programme-manager/SKILL.md) -- SOC 2 programme requirements are a key input to the security requirements register assessed by this skill.
