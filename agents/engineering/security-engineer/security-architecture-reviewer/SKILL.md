---
name: security-architecture-reviewer
description: >
  This skill reviews system architecture designs for security weaknesses and
  compliance gaps. Use when asked to assess an architecture for security, review a
  design document for trust boundaries, or validate defense-in-depth. Also consider
  when a new microservice is proposed without security review. Suggest when the user
  finalizes architecture without threat analysis.
department: engineering
agent: security-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../threat-modelling/SKILL.md
  - ../security-baseline-setup/SKILL.md
  - ../security-requirements-extractor/SKILL.md
---

# security-architecture-reviewer

## Agent: Security Engineer

L2 security engineer (Nx) responsible for threat modelling, security requirements, architecture review, code review, penetration testing, compliance, and continuous monitoring.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Reviews system architecture designs for security weaknesses, trust boundary violations, and compliance gaps before implementation begins.

## When to Use

- When a new system or service architecture is proposed and requires security sign-off.
- When an existing architecture undergoes significant changes (new data flows, third-party integrations, or infrastructure migration).
- When the threat model reveals architectural weaknesses that need design-level remediation.

## Workflow

1. **Architecture Decomposition**: Break the architecture into components, data flows, trust boundaries, and external interfaces. Map data classification levels (public, internal, confidential, restricted) to each flow. Deliverable: annotated architecture diagram with trust boundaries and data classifications.
2. **Defense-in-Depth Assessment**: Evaluate each layer for defense-in-depth: network segmentation, authentication at service boundaries, authorization granularity, encryption in transit (TLS 1.2+) and at rest (AES-256), and secrets management. Deliverable: defense-in-depth coverage matrix.
3. **Trust Boundary Validation**: Verify that every trust boundary crossing enforces authentication, input validation, and rate limiting. Identify implicit trust relationships that should be explicit. Deliverable: trust boundary validation report.
4. **Compliance Alignment**: Map architectural controls to applicable compliance requirements (SOC 2, GDPR, HIPAA). Identify gaps where the architecture cannot satisfy a requirement without changes. Deliverable: compliance alignment matrix with gap annotations.
5. **Findings and Recommendations**: Compile security findings classified by severity and provide architectural remediation recommendations with cost-complexity estimates. Deliverable: architecture security review report.

## Anti-Patterns

- **Perimeter-only security**: Relying on a single firewall or API gateway without internal segmentation or mutual TLS between services. *Why*: once an attacker breaches the perimeter, lateral movement is unrestricted.
- **Implicit trust between services**: Assuming internal services are safe and omitting authentication between them. *Why*: compromised internal services become pivot points for privilege escalation and data exfiltration.
- **Security review after implementation**: Reviewing architecture only after code is written. *Why*: architectural weaknesses discovered post-implementation require expensive rewrites instead of design changes.

## Output

**On success**: Produces an architecture security review report containing the annotated architecture diagram, defense-in-depth matrix, trust boundary validation, compliance alignment, and risk-ranked recommendations. Delivered to the architecture and engineering leads.

**On failure**: Report which architectural areas could not be assessed (e.g., undocumented data flows, missing deployment diagrams), what partial analysis was completed, and what documentation is needed to proceed.

## Related Skills

- [`threat-modelling`](../threat-modelling/SKILL.md) -- Provides threat scenarios that inform architectural review focus.
- [`security-baseline-setup`](../security-baseline-setup/SKILL.md) -- Implements baseline configurations validated during architecture review.
- [`security-requirements-extractor`](../security-requirements-extractor/SKILL.md) -- Supplies the requirements architecture must satisfy.
