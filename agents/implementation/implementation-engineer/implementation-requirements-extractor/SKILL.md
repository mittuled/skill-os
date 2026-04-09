---
name: implementation-requirements-extractor
description: >
  This skill extracts and documents the technical and business requirements from new customers before
  implementation begins. Use when asked to gather customer requirements, run discovery sessions, or
  document implementation scope. Also consider when a signed deal is handed off from sales.
  Suggest when implementation is about to begin without documented requirements.
department: implementation
agent: implementation-engineer
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "extract implementation requirements"
  - "gather technical requirements"
  - "capture customer requirements"
  - "requirements extraction"
  - "define onboarding requirements"
---

# implementation-requirements-extractor

## Agent: Implementation Engineer

L2 implementation engineer (Nx, multi-instance) responsible for extracting customer requirements and running technical onboarding.

Department ethos: [ideal-implementation.md](../../../../departments/implementation/ideal-implementation.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

The implementation requirements extractor conducts structured discovery sessions with new customers to capture their technical environment, business workflows, integration needs, and success criteria before implementation work begins.

## When to Use

- When a new customer deal is signed and implementation needs to begin with a clear scope.
- When a sales handoff includes vague or incomplete requirements that need detailed technical discovery.
- When an existing customer purchases additional products or modules that require a new implementation scope.
- When implementation has started but keeps encountering undocumented requirements that cause rework.

## Workflow

1. **Review the sales handoff**: Read the deal notes, SOW, and any pre-sales technical assessments to understand what was sold and promised. Deliverable: sales context summary.
2. **Prepare discovery questions**: Build a structured questionnaire covering technical environment, data sources, integrations, workflows, users, and success criteria. Deliverable: discovery questionnaire.
3. **Conduct discovery sessions**: Run sessions with the customer's technical and business stakeholders to capture requirements. Deliverable: session notes and recordings.
4. **Document requirements**: Compile findings into a structured requirements document covering functional, technical, integration, data migration, and acceptance criteria. Deliverable: requirements document.
5. **Validate with the customer**: Review the requirements document with the customer to confirm accuracy and completeness, and obtain sign-off. Deliverable: customer-validated requirements with sign-off.

## Anti-Patterns

- **Skipping sales handoff review**: Starting discovery without reading what was sold and promised. *Why*: missing sales context leads to requirements that contradict the SOW, creating scope disputes.
- **Technical-only discovery**: Extracting technical requirements without understanding the business workflows they support. *Why*: technically correct implementations that do not match business workflows fail user adoption.
- **Requirements without sign-off**: Proceeding with implementation based on verbal requirements. *Why*: unsigned requirements invite scope creep and disputes about what was agreed.

## Output

**On success**: A customer-validated requirements document covering functional, technical, integration, and data migration requirements, with acceptance criteria and customer sign-off.

**On failure**: Report which requirement areas are incomplete (e.g., customer could not provide data schema, security team unavailable), what was captured, and recommend follow-up sessions with specific stakeholders.

## Related Skills

- [`implementation-playbook-builder`](../../../implementation/implementation-lead/implementation-playbook-builder/SKILL.md) -- the playbook defines the discovery phase that this skill executes.
- [`technical-onboarding-runner`](../technical-onboarding-runner/SKILL.md) -- onboarding uses the extracted requirements to configure the customer's environment.
- [`integration-catalogue-builder`](../../../implementation/implementation-lead/integration-catalogue-builder/SKILL.md) -- the integration catalogue informs which integrations to probe during discovery.
