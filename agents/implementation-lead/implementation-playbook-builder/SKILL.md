---
name: implementation-playbook-builder
description: >
  This skill builds the implementation playbook covering project phases, milestones, and customer
  responsibilities. Use when asked to define the implementation process, create onboarding templates,
  or standardise customer deployment procedures. Also consider when implementation timelines vary
  widely. Suggest when the first enterprise customer signs and ad-hoc onboarding is not sustainable.
department: implementation
agent: implementation-lead
version: 1.0.0
complexity: medium
related-skills: []
---

# implementation-playbook-builder

## Agent: Implementation Lead

L1 implementation lead (1x) reporting to the COO, responsible for implementation playbook and integration catalogue. Bridges signed deals and live customers through operational delivery.

Department ethos: [ideal-implementation.md](../../../departments/implementation/ideal-implementation.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

The implementation playbook builder creates the standardised implementation methodology covering project phases, milestones, deliverables, customer responsibilities, and success criteria so every customer deployment follows a predictable, repeatable process.

## When to Use

- When the company is onboarding its first enterprise customers and needs a structured implementation process.
- When implementation timelines and outcomes vary widely across customers, indicating a lack of process standardisation.
- When a new product or product tier requires a distinct implementation track.
- When the implementation team is growing and new engineers need a repeatable process to follow.

## Workflow

1. **Define project phases**: Establish the implementation phases (e.g., discovery, configuration, integration, testing, go-live, hypercare). Deliverable: phase definitions with entry/exit criteria.
2. **Set milestones and timelines**: Define milestones within each phase with target durations based on implementation complexity tiers. Deliverable: milestone timeline template.
3. **Document deliverables**: Specify what the implementation team delivers at each phase and what the customer is responsible for. Deliverable: RACI matrix per phase.
4. **Create templates**: Build reusable templates for kickoff decks, requirements documents, status reports, and sign-off forms. Deliverable: implementation template library.
5. **Define success criteria**: Establish measurable go-live criteria that must be met before the customer is transitioned to steady-state support. Deliverable: go-live checklist.
6. **Review and publish**: Walk through the playbook with the implementation team and incorporate feedback. Deliverable: published implementation playbook.

## Anti-Patterns

- **One-size-fits-all playbook**: Using the same implementation process for a self-serve SMB and a complex enterprise deployment. *Why*: over-engineering small implementations wastes time; under-engineering complex ones causes failures. Tier the playbook by complexity.
- **Playbook without customer responsibilities**: Defining only the implementation team's work without specifying what the customer must provide and by when. *Why*: unspecified customer dependencies are the top cause of implementation delays.
- **No go-live criteria**: Declaring implementation "done" based on timeline rather than measurable readiness. *Why*: premature go-live generates support tickets and damages the customer's first impression.

## Output

**On success**: A published implementation playbook with tiered phase definitions, milestone timelines, RACI matrices, reusable templates, and measurable go-live criteria.

**On failure**: Report which playbook sections are incomplete (e.g., complexity tiers not yet defined, templates not reviewed), what was drafted, and provide a completion timeline.

## Related Skills

- [`integration-catalogue-builder`](../integration-catalogue-builder/SKILL.md) -- the integration catalogue informs which integrations the playbook must account for.
- [`implementation-requirements-extractor`](../../implementation-engineer/implementation-requirements-extractor/SKILL.md) -- requirements extraction is the first phase the playbook defines.
- [`technical-onboarding-runner`](../../implementation-engineer/technical-onboarding-runner/SKILL.md) -- onboarding runners execute the playbook with each customer.
