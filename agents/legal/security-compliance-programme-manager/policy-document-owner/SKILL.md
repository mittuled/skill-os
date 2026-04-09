---
name: policy-document-owner
description: >
  This skill owns and maintains security and compliance policy documents. Use when
  asked to draft a security policy, update existing policies for regulatory changes,
  or conduct the annual policy review cycle. Also consider when a new compliance
  framework requires additional policies. Suggest when the user is operating without
  documented security policies.
department: legal
agent: security-compliance-programme-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../compliance-framework-implementer/SKILL.md
  - ../audit-programme-manager/SKILL.md
triggers:
  - "own policy document"
  - "manage security policy"
  - "policy document review"
  - "update policy docs"
  - "security policy owner"
---

# policy-document-owner

## Agent: Security & Compliance Programme Manager

L2 security and compliance programme manager (1x) responsible for SOC 2, security awareness training, disaster recovery, GDPR/CCPA compliance, and penetration test programme management.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)

## Skill Description

Owns and maintains the security and compliance policy library by drafting new policies, conducting annual reviews, managing version control, and ensuring policies reflect current practices and regulatory requirements.

## When to Use

- When the annual policy review cycle arrives and policies need to be reviewed for currency and accuracy.
- When a new compliance framework or regulation requires policies that do not yet exist.
- When an audit finding identifies a policy gap or a policy that does not reflect actual practice.

## Workflow

1. **Policy Inventory**: Maintain a complete inventory of all security and compliance policies with metadata: owner, last review date, next review date, applicable frameworks, and approval status. Deliverable: policy inventory with review schedule.
2. **Drafting or Revision**: Draft new policies or revise existing ones. Ensure each policy covers purpose, scope, roles and responsibilities, requirements, exceptions process, and enforcement. Write in clear language accessible to the intended audience. Deliverable: draft policy document.
3. **Stakeholder Review**: Route the draft to relevant stakeholders (engineering, legal, HR, executive leadership) for accuracy and feasibility review. Incorporate feedback. Deliverable: stakeholder-reviewed policy.
4. **Approval and Publication**: Obtain formal approval from the designated authority (CISO, CEO, or board). Publish the policy with version number, effective date, and acknowledgement tracking. Archive the previous version. Deliverable: approved and published policy.

## Anti-Patterns

- **Aspirational policies**: Writing policies that describe an ideal state rather than current enforceable practice. *Why*: policies that do not reflect reality create audit findings when auditors test compliance; policies must be achievable and enforced.
- **Copy-paste from templates**: Adopting policy templates verbatim without customizing for the organization's size, technology, and risk profile. *Why*: generic policies miss organization-specific risks and include controls that are irrelevant or infeasible, reducing credibility with auditors.
- **No acknowledgement tracking**: Publishing policies without tracking whether employees have read and acknowledged them. *Why*: unacknowledged policies are difficult to enforce; compliance frameworks require evidence that employees are aware of applicable policies.

## Output

**On success**: Produces a maintained policy library with current policies, review schedule, version history, and acknowledgement tracking. Delivered on an ongoing basis with annual review cycle.

**On failure**: Report which policies are overdue for review, which gaps exist in the policy library, and recommended prioritization for remediation. Escalate to leadership if policy gaps create audit risk.

## Related Skills

- [`compliance-framework-implementer`](../compliance-framework-implementer/SKILL.md) -- Frameworks define the policies required; this skill produces and maintains them.
- [`audit-programme-manager`](../audit-programme-manager/SKILL.md) -- Auditors review policies as part of control testing; current policies reduce audit findings.
