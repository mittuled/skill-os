---
name: compliance-framework-implementer
description: >
  This skill implements security and compliance frameworks (SOC 2, ISO 27001, HIPAA,
  PCI DSS) by mapping requirements to controls and operationalizing them. Use when
  asked to adopt a new compliance framework, map controls across frameworks, or
  implement specific compliance requirements. Also consider when a customer contract
  requires a new certification. Suggest when the user is pursuing certification
  without a structured implementation plan.
department: legal
agent: security-compliance-programme-manager
version: 1.0.0
complexity: complex
related-skills:
  - ../audit-programme-manager/SKILL.md
  - ../policy-document-owner/SKILL.md
---

# compliance-framework-implementer

## Agent: Security & Compliance Programme Manager

L2 security and compliance programme manager (1x) responsible for SOC 2, security awareness training, disaster recovery, GDPR/CCPA compliance, and penetration test programme management.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)

## Skill Description

Implements security and compliance frameworks by mapping framework requirements to organizational controls, identifying gaps, designing remediation plans, and operationalizing controls to achieve and maintain certification readiness.

## When to Use

- When the company decides to pursue a new compliance certification (SOC 2, ISO 27001, HIPAA, PCI DSS) and needs a structured implementation plan.
- When a customer or partner contract requires demonstrating compliance with a specific framework.
- When an existing framework requires updates due to new standard versions or changed organizational scope.

## Workflow

1. **Framework Scoping**: Define the scope of the framework implementation: which systems, processes, and data are in scope. Select applicable trust service criteria, control objectives, or requirement categories. Deliverable: framework scope document.
2. **Control Mapping**: Map framework requirements to existing organizational controls. Identify where existing controls satisfy requirements, where controls exist but need enhancement, and where new controls are needed. Cross-reference with other frameworks to leverage shared controls. Deliverable: control mapping matrix with gap analysis.
3. **Gap Remediation Planning**: For each gap, design the control implementation: technical controls (tooling, configurations), administrative controls (policies, procedures), and physical controls (access restrictions). Estimate effort, assign owners, and set timelines. Deliverable: remediation plan with owner assignments.
4. **Control Implementation**: Execute the remediation plan. Build technical controls, draft policies, configure monitoring, and establish evidence collection processes. Validate each control works as designed. Deliverable: implemented controls with validation evidence.
5. **Evidence Framework**: Design the ongoing evidence collection process: what evidence each control produces, how it is collected (automated vs. manual), where it is stored, and how often it is reviewed. Deliverable: evidence collection framework.
6. **Certification Readiness Review**: Conduct a pre-certification internal audit against the full framework. Identify any remaining gaps or weak controls. Remediate before engaging the external auditor. Deliverable: certification readiness report.

## Anti-Patterns

- **Framework-per-framework implementation**: Implementing each framework independently without mapping shared controls. *Why*: most security frameworks share 60-80% of their controls; duplicating effort wastes resources and creates inconsistent control implementations.
- **Policy-only compliance**: Writing policies to satisfy framework requirements without implementing operational controls. *Why*: policies without operational backing are discovered during audit testing; auditors verify that controls operate, not just that policies exist.
- **Ignoring scope creep**: Allowing the framework scope to expand without reassessing the control set and timeline. *Why*: scope changes invalidate the control mapping; uncontrolled scope growth delays certification and increases cost.
- **Manual evidence collection**: Relying on manual processes to collect control evidence rather than automating where possible. *Why*: manual evidence collection is error-prone, time-consuming, and does not scale as the number of controls and frameworks grows.

## Output

**On success**: Produces a framework scope document, control mapping matrix, remediation plan, implemented controls, evidence framework, and certification readiness report. Delivered per the implementation timeline.

**On failure**: Report which controls could not be implemented, what gaps remain, what the impact is on certification readiness, and recommended timeline adjustments. Escalate to leadership if resource constraints prevent implementation.

## Related Skills

- [`audit-programme-manager`](../audit-programme-manager/SKILL.md) -- Audits validate the controls that framework implementation produces.
- [`policy-document-owner`](../policy-document-owner/SKILL.md) -- Policies are a required component of every compliance framework implementation.
