---
name: security-requirements-extractor
description: >
  This skill extracts security and compliance requirements from product and business
  specifications. Use when asked to derive security requirements, identify compliance
  obligations, or translate business needs into security controls. Also consider when
  a PRD lacks security considerations. Suggest when the user starts design without
  security requirements.
department: engineering
agent: security-engineer
version: 1.0.0
complexity: simple
related-skills:
  - ../threat-model-sketch/SKILL.md
  - ../security-architecture-reviewer/SKILL.md
---

# security-requirements-extractor

## Agent: Security Engineer

L2 security engineer (Nx) responsible for threat modelling, security requirements, architecture review, code review, penetration testing, compliance, and continuous monitoring.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Extracts security and compliance requirements from product and business specifications, translating them into actionable engineering constraints.

## When to Use

- When a new product requirement document (PRD) or feature specification is created and needs security requirements.
- When entering a regulated market that introduces new compliance obligations.
- When a security incident reveals missing requirements that should have been captured upfront.

## Workflow

1. **Specification Review**: Read the product specification, identify data types handled (PII, PHI, financial, credentials), user roles, and integration points. Deliverable: data classification and scope summary.
2. **Regulatory Mapping**: Identify applicable regulations and standards based on data types, geographies, and industries (GDPR for EU PII, HIPAA for PHI, PCI-DSS for payment data, SOX for financial reporting). Deliverable: regulatory applicability matrix.
3. **Requirement Derivation**: Translate regulatory obligations and security best practices into specific, testable engineering requirements (e.g., "All PII must be encrypted at rest using AES-256", "Session tokens must expire after 30 minutes of inactivity"). Deliverable: security requirements list with traceability to source regulations.
4. **Handoff**: Deliver requirements to the architecture and development teams for incorporation into the design. Deliverable: requirements document integrated into the project backlog.

## Anti-Patterns

- **Generic requirement lists**: Copying standard security checklists without tailoring to the specific product context. *Why*: generic requirements miss product-specific risks and create noise that teams learn to ignore.
- **Requirements without testability**: Writing vague requirements like "the system must be secure" without measurable criteria. *Why*: untestable requirements cannot be verified and provide no engineering guidance.

## Output

**On success**: Produces a security requirements document containing data classification, regulatory applicability matrix, and testable requirements with traceability. Delivered to the project backlog and architecture team.

**On failure**: Report which specifications lacked sufficient detail for requirement extraction, what assumptions were made, and what clarifications are needed from product stakeholders.

## Related Skills

- [`threat-model-sketch`](../threat-model-sketch/SKILL.md) -- Uses extracted requirements to inform initial threat identification.
- [`security-architecture-reviewer`](../security-architecture-reviewer/SKILL.md) -- Validates that architecture satisfies these requirements.
