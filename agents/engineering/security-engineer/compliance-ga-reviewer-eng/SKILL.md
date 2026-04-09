---
name: compliance-ga-reviewer-eng
description: >
  This skill reviews engineering deliverables for compliance with security and
  regulatory requirements at general availability. Use when asked to sign off on a
  GA release, audit compliance controls, or verify regulatory readiness. Also consider
  when a product ships to regulated markets. Suggest when the user prepares a GA
  release without a compliance checkpoint.
department: engineering
agent: security-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../security-compliance-enabler/SKILL.md
  - ../security-requirements-extractor/SKILL.md
triggers:
  - "review compliance for GA"
  - "GA compliance check"
  - "compliance review"
  - "pre-GA compliance audit"
  - "GA readiness compliance"
---

# compliance-ga-reviewer-eng

## Agent: Security Engineer

L2 security engineer (Nx) responsible for threat modelling, security requirements, architecture review, code review, penetration testing, compliance, and continuous monitoring.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Reviews engineering deliverables for compliance with security and regulatory requirements as a gate condition for general availability release.

## When to Use

- When a product or feature is approaching GA release and requires compliance sign-off.
- When regulatory requirements (SOC 2, GDPR, HIPAA, PCI-DSS) apply to the release scope.
- When a previous compliance review identified findings that require re-verification before launch.

## Workflow

1. **Scope Mapping**: Identify which compliance frameworks apply to the release (SOC 2 Type II, GDPR Article 32, HIPAA Security Rule, PCI-DSS). Map each requirement to the relevant engineering deliverable. Deliverable: compliance scope matrix.
2. **Control Verification**: Verify that each mapped control is implemented: encryption at rest and in transit, access control enforcement, audit logging, data retention policies, and incident response procedures. Deliverable: control verification checklist with evidence links.
3. **Gap Assessment**: Identify any controls that are missing, partially implemented, or not evidenced. Classify gaps by severity (blocker, major, minor). Deliverable: gap report with severity classifications.
4. **Remediation Tracking**: For each blocker or major gap, confirm a remediation plan exists with an owner and deadline. Deliverable: remediation tracker linked to the release timeline.
5. **Sign-Off Decision**: Issue a go/no-go compliance verdict with conditions. Deliverable: compliance sign-off document or rejection with required actions.

## Anti-Patterns

- **Checkbox compliance**: Marking controls as "done" without verifying evidence or testing effectiveness. *Why*: unverified controls create a false sense of security and will fail under audit scrutiny.
- **Late-stage review**: Running the compliance review days before GA instead of iteratively during development. *Why*: blocker-level gaps discovered late force either a delayed launch or a risky exception.
- **Scope creep avoidance**: Excluding in-scope data flows or third-party integrations to simplify the review. *Why*: auditors and regulators assess the full data path; gaps in scope become audit findings.

## Output

**On success**: Produces a compliance sign-off document containing the scope matrix, control verification evidence, gap assessment (if any), and the go/no-go verdict. Delivered to the release management process.

**On failure**: Report which controls could not be verified, the severity of gaps, and the minimum remediation required before re-review.

## Related Skills

- [`security-compliance-enabler`](../security-compliance-enabler/SKILL.md) -- Implements the controls this skill verifies.
- [`security-requirements-extractor`](../security-requirements-extractor/SKILL.md) -- Extracts the requirements this review validates against.
