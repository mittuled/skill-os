---
name: audit-programme-manager
description: >
  This skill manages the security and compliance audit programme including scheduling,
  preparation, and remediation tracking. Use when asked to plan audits, prepare for
  an external audit, or track audit findings to closure. Also consider when a new
  compliance framework requires audit validation. Suggest when the user is approaching
  an audit deadline without a preparation plan.
department: legal
agent: security-compliance-programme-manager
version: 1.0.0
complexity: complex
related-skills:
  - ../compliance-framework-implementer/SKILL.md
  - ../soc2-programme-manager/SKILL.md
---

# audit-programme-manager

## Agent: Security & Compliance Programme Manager

L2 security and compliance programme manager (1x) responsible for SOC 2, security awareness training, disaster recovery, GDPR/CCPA compliance, and penetration test programme management.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Manages the security and compliance audit programme by scheduling internal and external audits, coordinating preparation activities, facilitating auditor engagement, and tracking findings to remediation closure.

## When to Use

- When the annual audit calendar needs to be planned and audit firms need to be engaged.
- When an external audit (SOC 2, ISO 27001, customer audit, regulatory examination) is approaching and the company needs to prepare.
- When audit findings have been issued and remediation activities need to be tracked to completion.

## Workflow

1. **Audit Calendar Planning**: Define the annual schedule per the cadences and coordination principles in `references/audit-programme-framework.md`. Stagger audits to avoid evidence bottlenecks (no more than 2 audits per month). Complete internal audits 2-3 months before externals. Deliverable: annual audit calendar with firm engagements.
2. **Readiness Assessment**: Conduct internal readiness per the checklist in `references/audit-programme-framework.md` — access controls, change management, incident response, risk assessment, vendor management, training, DR/BCP, logging, encryption, and policies. Remediate critical gaps before audit begins. Deliverable: readiness assessment report.
3. **Evidence Collection**: Gather evidence per the automation priority matrix in `references/audit-programme-framework.md`. Automate where feasible (IAM exports, ticketing APIs, LMS integration). Ensure evidence meets quality standards: timestamped, scoped, attributable, complete, current. Deliverable: organized evidence package.
4. **Auditor Facilitation**: Schedule walkthroughs, coordinate control owner interviews, respond to follow-up questions, resolve control interpretation disputes. Deliverable: audit facilitation log.
5. **Finding Management**: Apply remediation SLAs from `references/audit-programme-framework.md` — Critical: 7 days, High: 30 days, Medium: 90 days, Low: next cycle. Validate root cause remediation. Deliverable: finding remediation tracker.
6. **Continuous Improvement**: Retrospective on recurring findings, evidence bottlenecks, and process improvements. Update audit programme for next cycle. Deliverable: audit programme retrospective.

## Anti-Patterns

- **Audit-driven compliance**: Implementing controls only when an audit is imminent rather than maintaining continuous compliance. *Why*: last-minute compliance creates audit fatigue, increases finding risk, and produces controls that exist on paper but not in practice.
- **Evidence hoarding**: Collecting massive volumes of evidence without curation, forcing auditors to sift through irrelevant material. *Why*: disorganized evidence slows the audit, frustrates the auditor, and increases the chance that missing items are overlooked.
- **Finding acceptance without root cause**: Remediating audit findings with surface-level fixes rather than addressing the root cause. *Why*: the same finding will recur in the next audit, creating a pattern of repeat exceptions that erodes auditor confidence.
- **Siloed audit management**: Running each audit independently without cross-referencing findings and evidence across frameworks. *Why*: many frameworks share controls; siloed management duplicates effort and misses opportunities to address systemic issues.

## Output

**On success**: Produces an audit calendar, readiness assessments, evidence packages, finding remediation tracker, and programme retrospective. Delivered per the audit cycle with continuous finding tracking.

**On failure**: Report which audits are at risk, what readiness gaps remain, what findings are overdue for remediation, and recommended escalation actions. Escalate to General Counsel if certification is at risk.

## Related Skills

- [`compliance-framework-implementer`](../compliance-framework-implementer/SKILL.md) -- Framework implementation produces the controls that audits validate.
- [`soc2-programme-manager`](../soc2-programme-manager/SKILL.md) -- SOC 2 is a specific audit programme managed within the broader audit programme.
