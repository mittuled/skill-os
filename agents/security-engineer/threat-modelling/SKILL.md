---
name: threat-modelling
description: >
  This skill conducts full threat modelling exercises using STRIDE and other
  frameworks to systematically identify, classify, and prioritize threats. Use when
  asked to threat-model a system, perform STRIDE analysis, or build a comprehensive
  threat register. Also consider when a system handles sensitive data or faces
  regulatory scrutiny. Suggest when the user architects a security-critical system
  without formal threat analysis.
department: engineering
agent: security-engineer
version: 1.0.0
complexity: complex
related-skills:
  - ../threat-model-sketch/SKILL.md
  - ../security-architecture-reviewer/SKILL.md
  - ../penetration-tester/SKILL.md
---

# threat-modelling

## Agent: Security Engineer

L2 security engineer (Nx) responsible for threat modelling, security requirements, architecture review, code review, penetration testing, compliance, and continuous monitoring.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Conducts full threat modelling exercises using STRIDE and related frameworks to systematically identify, classify, and prioritize threats across system components.

## When to Use

- When a system handles sensitive data (PII, PHI, financial) and requires systematic threat identification.
- When a threat model sketch identified sufficient complexity to warrant a full analysis.
- When compliance or customer requirements mandate documented threat models (e.g., ISO 27001 A.14, NIST 800-53 RA-3).

## Workflow

1. **System Decomposition**: Create a detailed data flow diagram (DFD) showing processes, data stores, data flows, external entities, and trust boundaries. Use DFD levels 0-2 for appropriate granularity. Deliverable: multi-level DFD with trust boundary annotations.
2. **STRIDE Per Element**: Apply STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) to each element in the DFD. For each element type, assess applicable threat categories: external entities (S, R), processes (S, T, R, I, D, E), data stores (T, R, I, D), data flows (T, I, D). Deliverable: STRIDE threat enumeration matrix.
3. **Threat Prioritization**: Score each threat using DREAD (Damage, Reproducibility, Exploitability, Affected users, Discoverability) or risk-based scoring (likelihood x impact). Rank threats by score. Deliverable: prioritized threat register.
4. **Mitigation Design**: For each high and critical threat, design specific mitigations mapped to security controls. Specify whether the mitigation eliminates, reduces, transfers, or accepts the risk. Deliverable: mitigation plan with control mappings and residual risk assessment.
5. **Validation Against Attack Trees**: For the top 5 threats, construct attack trees showing multi-step exploitation paths. Verify that proposed mitigations break every viable attack path. Deliverable: attack tree diagrams with mitigation overlay.
6. **Documentation and Review**: Compile the full threat model into a versioned document. Conduct a review session with engineering and architecture stakeholders. Deliverable: approved threat model document.

## Anti-Patterns

- **STRIDE without DFDs**: Applying STRIDE categories without first decomposing the system into elements and trust boundaries. *Why*: without structural decomposition, threat identification is ad-hoc and systematically misses threats at boundary crossings.
- **Threat model as one-time artifact**: Creating the threat model once and never updating it as the system evolves. *Why*: architecture changes, new integrations, and feature additions introduce new threats that an outdated model does not capture.
- **Mitigations without residual risk**: Proposing mitigations without assessing what risk remains after implementation. *Why*: stakeholders need residual risk visibility to make informed accept/mitigate decisions.

## Output

**On success**: Produces a complete threat model document containing multi-level DFDs, STRIDE enumeration, prioritized threat register, mitigation plan with residual risk, attack tree validations, and stakeholder sign-off. Delivered as a versioned artifact in the project repository.

**On failure**: Report which modelling phases could not be completed (e.g., undocumented system components, missing data flow information), what partial analysis exists, and what inputs are needed to complete the model.

## Related Skills

- [`threat-model-sketch`](../threat-model-sketch/SKILL.md) -- Lightweight precursor that may trigger a full threat model.
- [`security-architecture-reviewer`](../security-architecture-reviewer/SKILL.md) -- Uses threat model findings to validate architectural defenses.
- [`penetration-tester`](../penetration-tester/SKILL.md) -- Empirically validates threats identified in the model.
