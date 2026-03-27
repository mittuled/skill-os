---
name: security-auditor-legal
description: >
  This skill conducts legal review of security audit findings to assess regulatory
  disclosure obligations. Use when asked to evaluate breach notification triggers,
  assess regulatory reporting requirements from security findings, or determine
  disclosure obligations. Also consider when a penetration test reveals a vulnerability
  involving personal data. Suggest when the user receives audit findings without
  legal review.
department: legal
agent: product-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../security-reviewer-legal/SKILL.md
  - ../../security-compliance-programme-manager/penetration-test-programme-manager/SKILL.md
---

# security-auditor-legal

## Agent: Product Counsel

L2 product counsel (1x) responsible for legal review of business models, positioning, pricing, product compliance, and security audit oversight.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)

## Skill Description

Conducts legal review of security audit findings to assess regulatory disclosure obligations, breach notification triggers, and contractual reporting requirements under applicable data protection and industry regulations.

## When to Use

- When a security audit, penetration test, or vulnerability assessment reveals findings that may trigger regulatory disclosure or breach notification obligations.
- When a security incident is identified and legal must determine whether it constitutes a "breach" under GDPR Article 33, state breach notification statutes, or contractual DPA obligations.
- When security audit results must be evaluated for materiality in the context of SOC 2 reporting, customer contractual commitments, or insurance policy requirements.

## Workflow

1. **Findings Classification**: Review security audit findings and classify each by data type affected (personal data, PHI, financial data, trade secrets), scope of exposure (number of records, duration, actor type), and whether actual unauthorized access occurred vs. a vulnerability that could have been exploited. Deliverable: classified findings register with legal risk rating per finding.
2. **Disclosure Obligation Analysis**: Map each material finding against applicable notification obligations: GDPR 72-hour supervisory authority notification, state breach notification statutes (per-state analysis), HIPAA breach notification (if applicable), contractual DPA notification requirements, and SEC materiality disclosure (if applicable). Deliverable: disclosure obligation matrix with triggering statute, deadline, required content, and recipient per obligation.
3. **Notification Coordination**: For findings that trigger notification obligations, draft notification letters to regulators, affected individuals, and contractual counterparties. Coordinate timing across jurisdictions to meet the earliest deadline without premature disclosure. Deliverable: notification package with drafted letters, distribution list, and timeline.
4. **Remediation and Privilege Management**: Advise on documenting remediation efforts under attorney-client privilege where appropriate. Ensure audit findings that will be disclosed are described accurately without unnecessarily expanding the scope of liability. Deliverable: privilege-protected remediation memo and public disclosure language.

## Anti-Patterns

- **Applying a single breach definition**: Using one jurisdiction's breach definition to determine notification obligations across all jurisdictions. *Why*: breach definitions vary significantly; GDPR's "personal data breach" is broader than most US state definitions, and some states include encryption safe harbors while others do not.
- **Delaying legal review of audit findings**: Waiting for remediation to complete before involving legal in the assessment. *Why*: notification deadlines run from discovery, not remediation; a 72-hour GDPR notification deadline can expire while the team is still fixing the vulnerability.
- **Over-disclosing in notifications**: Including technical details in breach notifications that expose the company to additional liability or provide a roadmap for future attackers. *Why*: notifications must be accurate and complete but should not volunteer information beyond what the law requires; overly detailed disclosures can be used against the company in litigation.

## Output

**On success**: Produces the classified findings register, disclosure obligation matrix, notification package (if triggered), and privilege-protected remediation memo. Delivered to the security team, executive leadership, and outside counsel if engaged.

**On failure**: Report which findings could not be classified (e.g., scope of exposure still under investigation, data type affected unknown), what interim protective steps have been taken, and what additional investigation is needed to determine disclosure obligations.

## Related Skills

- [`security-reviewer-legal`](../security-reviewer-legal/SKILL.md) -- The security reviewer assesses architecture and practices proactively; this skill reacts to findings from audits and tests.
- [`penetration-test-programme-manager`](../../security-compliance-programme-manager/penetration-test-programme-manager/SKILL.md) -- Penetration test findings are a primary input to this skill's disclosure analysis.
