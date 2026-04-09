---
name: risk-register-maintainer
description: >
  This skill maintains the security and compliance risk register. Use when asked to
  assess a new risk, update risk ratings, or conduct a periodic risk review. Also
  consider when incidents, audit findings, or architectural changes introduce new
  risks. Suggest when the user is making security decisions without a current risk
  register.
department: legal
agent: security-compliance-programme-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../compliance-framework-implementer/SKILL.md
  - ../vendor-security-assessor/SKILL.md
triggers:
  - "maintain risk register"
  - "update risk register"
  - "risk register"
  - "track risks"
  - "risk log management"
---

# risk-register-maintainer

## Agent: Security & Compliance Programme Manager

L2 security and compliance programme manager (1x) responsible for SOC 2, security awareness training, disaster recovery, GDPR/CCPA compliance, and penetration test programme management.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)

## Skill Description

Maintains the security and compliance risk register by identifying, assessing, rating, and tracking risks with their mitigations to ensure informed risk-based decision-making across the organization.

## When to Use

- When the quarterly or annual risk review cycle arrives and the register needs to be updated.
- When a new risk is identified through incidents, audit findings, vulnerability disclosures, or architectural changes.
- When leadership needs a current view of the organization's risk posture to make investment or prioritization decisions.

## Workflow

1. **Risk Identification**: Gather new risks from multiple sources: security incidents, audit findings, vulnerability scans, threat intelligence, architectural reviews, and stakeholder interviews. Deduplicate against existing register entries. Deliverable: new risk candidates.
2. **Risk Assessment**: For each risk, assess likelihood and impact using the organization's risk rating methodology. Document the threat scenario, affected assets, existing controls, and residual risk after controls. Deliverable: assessed risk entries with ratings.
3. **Mitigation Planning**: For risks above the organization's risk appetite, define mitigation actions: additional controls, process changes, or risk transfer (insurance). Assign owners and deadlines. For accepted risks, document the acceptance rationale and approver. Deliverable: mitigation plan or risk acceptance record.
4. **Register Review**: Conduct periodic register reviews with stakeholders. Re-rate existing risks based on changed conditions. Close risks that are fully mitigated. Escalate risks that have worsened. Deliverable: updated risk register with review notes.

## Anti-Patterns

- **Static register**: Creating the risk register once and never updating it. *Why*: the threat landscape changes continuously; a stale register provides false confidence and fails to surface emerging risks.
- **Risk inflation**: Rating all risks as critical to ensure they get attention. *Why*: if everything is critical, nothing is; risk inflation destroys the register's value as a prioritization tool.
- **Mitigations without tracking**: Assigning mitigations without following up on implementation. *Why*: unimplemented mitigations leave risks at their pre-mitigation level while the register shows them as addressed.

## Output

**On success**: Produces a current risk register with assessed risks, mitigation plans, acceptance records, and review history. Delivered on an ongoing basis with quarterly reviews.

**On failure**: Report which risks could not be assessed (insufficient information, unclear asset ownership), what the current register coverage is, and recommended actions to close assessment gaps.

## Related Skills

- [`compliance-framework-implementer`](../compliance-framework-implementer/SKILL.md) -- Compliance frameworks require risk assessment; the register is a mandatory artifact.
- [`vendor-security-assessor`](../vendor-security-assessor/SKILL.md) -- Vendor assessments identify third-party risks that belong in the risk register.
