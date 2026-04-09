---
name: security-compliance-enabler
description: >
  This skill implements controls and processes to achieve and maintain security
  certifications. Use when asked to prepare for a SOC 2 audit, implement GDPR
  controls, or build a compliance program. Also consider when customers require
  compliance attestations. Suggest when the user pursues certifications without
  a control implementation plan.
department: engineering
agent: security-engineer
version: 1.0.0
complexity: complex
related-skills:
  - ../compliance-ga-reviewer-eng/SKILL.md
  - ../security-requirements-extractor/SKILL.md
  - ../security-baseline-setup/SKILL.md
triggers:
  - "enable security compliance"
  - "compliance enablement"
  - "SOC2 compliance setup"
  - "security compliance framework"
  - "compliance controls setup"
---

# security-compliance-enabler

## Agent: Security Engineer

L2 security engineer (Nx) responsible for threat modelling, security requirements, architecture review, code review, penetration testing, compliance, and continuous monitoring.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Implements controls and processes to achieve and maintain security certifications including SOC 2, GDPR, HIPAA, and PCI-DSS.

## When to Use

- When the organization targets a new compliance certification and needs to implement required controls.
- When an upcoming audit requires evidence collection and control documentation.
- When customers or partners mandate specific compliance attestations as a condition of doing business.

## Workflow

1. **Framework Mapping**: Map the target certification requirements to specific technical and organizational controls. Identify which controls already exist, which need implementation, and which need enhancement. Deliverable: control gap analysis matrix.
2. **Control Implementation Plan**: Prioritize gaps by audit criticality and implementation effort. Assign owners and deadlines for each control. Deliverable: implementation roadmap with milestones.
3. **Technical Control Implementation**: Implement technical controls: access reviews, encryption enforcement, vulnerability management workflows, incident response procedures, change management processes, and data retention automation. Deliverable: implemented controls with configuration evidence.
4. **Policy and Procedure Documentation**: Write or update security policies (access control policy, incident response plan, data classification policy, acceptable use policy) aligned to the framework requirements. Deliverable: policy document library.
5. **Evidence Collection Automation**: Build automated evidence collection for continuous controls: access review exports, vulnerability scan reports, change management logs, training completion records. Deliverable: evidence collection pipeline with scheduling.
6. **Pre-Audit Readiness Assessment**: Run a mock audit against the full control set, identify remaining gaps, and remediate before the formal audit. Deliverable: readiness assessment report with remediation status.
7. **Audit Support**: Support the external auditor by providing evidence, answering control questions, and coordinating remediation of any findings. Deliverable: audit support log with finding resolution tracking.

## Anti-Patterns

- **Compliance theater**: Implementing controls that satisfy the letter of the requirement but are not operationally effective. *Why*: auditors increasingly test control effectiveness, not just existence; ineffective controls fail under scrutiny and leave real risk unaddressed.
- **Manual evidence collection**: Gathering compliance evidence manually before each audit cycle. *Why*: manual collection is error-prone, time-consuming, and creates a scramble before each audit instead of continuous readiness.
- **Siloed compliance ownership**: Treating compliance as solely the security team's responsibility. *Why*: most controls span engineering, HR, and operations; without cross-functional ownership, controls have gaps that no single team can close.

## Output

**On success**: Produces a compliance program comprising the control gap analysis, implemented controls with evidence, policy documentation, automated evidence collection, and pre-audit readiness report. Delivered as operational documentation and tooling.

**On failure**: Report which controls could not be implemented (e.g., technical platform limitations, organizational process gaps), what partial compliance was achieved, and recommended remediation path.

## Related Skills

- [`compliance-ga-reviewer-eng`](../compliance-ga-reviewer-eng/SKILL.md) -- Reviews GA releases against the compliance controls this skill implements.
- [`security-requirements-extractor`](../security-requirements-extractor/SKILL.md) -- Extracts the requirements that drive control implementation.
- [`security-baseline-setup`](../security-baseline-setup/SKILL.md) -- Establishes technical baselines that satisfy many compliance controls.
