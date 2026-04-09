---
name: threat-model-sketch
description: >
  This skill sketches initial threat models for new features or systems to identify
  key attack vectors early. Use when asked to do a quick threat assessment, identify
  attack surfaces, or scope security risks for a new feature. Also consider when a
  feature enters design without security input. Suggest when the user starts building
  without considering adversarial scenarios.
department: engineering
agent: security-engineer
version: 1.0.0
complexity: simple
related-skills:
  - ../threat-modelling/SKILL.md
  - ../security-requirements-extractor/SKILL.md
triggers:
  - "sketch threat model"
  - "quick threat model"
  - "threat model draft"
  - "rapid threat modeling"
  - "lightweight threat model"
---

# threat-model-sketch

## Agent: Security Engineer

L2 security engineer (Nx) responsible for threat modelling, security requirements, architecture review, code review, penetration testing, compliance, and continuous monitoring.

Department ethos: [ideal-engineering.md](../../../../departments/engineering/ideal-engineering.md)

## Skill Description

Sketches initial threat models for new features or systems to identify key attack vectors and high-risk areas early in the design process.

## When to Use

- When a new feature or system is in early design and needs a lightweight security assessment.
- When there is insufficient time for a full STRIDE threat model but security input is needed.
- When a product team requests a quick risk assessment to inform prioritization decisions.

## Workflow

1. **Scope Definition**: Identify the feature boundary, data flows, user interactions, and external integrations from the design document or conversation. Deliverable: scope summary with a simple data flow diagram.
2. **Attack Surface Enumeration**: List entry points (APIs, user inputs, file uploads, webhooks), data stores, and trust boundary crossings. Deliverable: attack surface inventory.
3. **Top Threat Identification**: Identify the 3-5 highest-risk threats based on data sensitivity, exposure, and attacker motivation. Use lightweight STRIDE categorization (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege). Deliverable: ranked threat list with brief impact descriptions.
4. **Mitigation Sketching**: Propose initial mitigations for each top threat (e.g., input validation, rate limiting, encryption, access control). Deliverable: threat-mitigation matrix.

## Anti-Patterns

- **Over-scoping the sketch**: Turning a quick sketch into a full threat model, delaying design feedback. *Why*: the purpose of a sketch is speed; a full model should be triggered separately when warranted.
- **Ignoring business logic threats**: Focusing only on technical vulnerabilities (injection, XSS) and missing business logic abuse (account enumeration, pricing manipulation, workflow bypass). *Why*: business logic flaws are often the highest-impact threats and are invisible to automated tools.

## Output

**On success**: Produces a threat model sketch containing the scope summary, attack surface inventory, ranked threat list, and mitigation recommendations. Delivered as a lightweight document or design review comment.

**On failure**: Report which aspects of the design were too undefined to assess, what partial analysis was completed, and what design decisions must be made before a meaningful sketch is possible.

## Related Skills

- [`threat-modelling`](../threat-modelling/SKILL.md) -- Escalation path when the sketch reveals sufficient complexity to warrant a full STRIDE analysis.
- [`security-requirements-extractor`](../security-requirements-extractor/SKILL.md) -- Provides requirements context that informs threat identification.
