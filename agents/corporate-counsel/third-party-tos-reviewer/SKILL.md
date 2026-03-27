---
name: third-party-tos-reviewer
description: >
  This skill reviews third-party terms of service and contracts for legal risk
  before execution. Use when asked to review a vendor contract, evaluate SaaS
  terms, or assess a partner agreement. Also consider when onboarding a new
  third-party tool or service. Suggest when the user is signing up for services
  without legal review.
department: legal
agent: corporate-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../risk-register-legal/SKILL.md
  - ../compliance-scanner/SKILL.md
---

# third-party-tos-reviewer

## Agent: Corporate Counsel

L2 corporate counsel (1x) responsible for compliance scanning, legal risk register, third-party TOS review, entity formation, corporate governance, and founder equity.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)

## Skill Description

Reviews third-party terms of service, vendor contracts, and partner agreements to identify legal risks, unfavorable clauses, and compliance implications before the company commits.

## When to Use

- When the company is evaluating a new vendor, SaaS tool, or service provider and needs to understand the legal implications of their terms.
- When a third-party contract includes data processing, IP licensing, or indemnification clauses that require legal analysis.
- When renewing an existing vendor agreement and terms have changed since the last review.

## Workflow

1. **Document Collection**: Obtain the complete terms of service, privacy policy, data processing agreement, and any supplemental terms. Identify the governing law and dispute resolution mechanism. Deliverable: complete document set with key metadata.
2. **Risk Clause Analysis**: Review for high-risk clauses: unlimited liability, broad IP assignment, unilateral modification rights, data ownership ambiguity, non-compete restrictions, and auto-renewal with penalty. Deliverable: annotated risk summary with clause references.
3. **Data and Compliance Review**: Assess data handling provisions against the company's privacy obligations (GDPR, CCPA). Verify sub-processor disclosure, data breach notification obligations, and data portability/deletion rights. Deliverable: data compliance assessment.
4. **Recommendation**: Provide a clear accept/reject/negotiate recommendation with specific redline requests for unacceptable clauses. Include fallback positions for negotiable terms. Deliverable: review memo with recommendation and redlines.
5. **Risk Register Update**: Log any accepted risks (clauses that could not be negotiated) in the legal risk register with mitigation notes. Deliverable: updated risk register entry.

## Anti-Patterns

- **Reviewing TOS after signing**: Conducting legal review after the team has already committed to the service. *Why*: post-signing review has no leverage; unfavorable terms are already binding and can only be mitigated, not negotiated.
- **Ignoring privacy policy and DPA**: Reviewing only the main TOS without examining the privacy policy and data processing agreement. *Why*: data handling obligations often live in separate documents, and missing them creates compliance gaps that regulators will find.
- **Binary accept/reject without alternatives**: Rejecting a vendor without suggesting alternatives or negotiation strategies. *Why*: the requesting team needs a path forward, not just a veto; legal should enable the business while managing risk.

## Output

**On success**: Produces an annotated risk summary, data compliance assessment, and recommendation memo with redlines. Delivered to the requesting team and filed in the legal review archive.

**On failure**: Report which documents were unavailable for review (e.g., vendor refused to share DPA), what partial assessment is possible, and whether proceeding without full review is acceptable. Escalate to General Counsel.

## Related Skills

- [`risk-register-legal`](../risk-register-legal/SKILL.md) -- Accepted risks from TOS reviews are logged in the legal risk register.
- [`compliance-scanner`](../compliance-scanner/SKILL.md) -- Compliance requirements inform which TOS clauses require scrutiny.
