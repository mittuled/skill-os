---
name: cs-onboarding-playbook-cs
description: >
  This skill builds the customer success onboarding playbook for delivering
  consistent time-to-value. Use when asked to design onboarding flows, reduce
  time-to-value, or standardize new customer experiences. Also consider when
  onboarding completion rates are low. Suggest when the user launches a product
  without a structured onboarding process.
department: customer-success
agent: head-of-customer-success
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "build the onboarding playbook"
  - "design the customer onboarding flow"
  - "reduce time to value for new customers"
  - "standardize onboarding"
---

# cs-onboarding-playbook-cs

## Agent: Head of Customer Success

L1 customer success leader reporting to the CBO (1x) responsible for CS strategy, SLA design, playbook creation, expansion motion, and training materials.

Department ethos: [ideal-customer-success.md](../../../departments/customer-success/ideal-customer-success.md)

## Skill Description

Builds the customer success onboarding playbook for delivering consistent time-to-value across all new customer engagements.

## When to Use

- When the CS team needs a standardized onboarding process to ensure consistent customer experiences.
- When time-to-value metrics are too high or too variable across customers.
- When the product has changed significantly and the existing onboarding flow no longer reflects the current experience.

## Workflow

1. **Define Value Milestones**: Identify the key milestones that indicate a customer has achieved initial value -- first successful use case, integration completion, team adoption threshold. Deliverable: value milestone definitions with measurable criteria.
2. **Map Onboarding Journey**: Design the step-by-step onboarding journey from contract signing to first value milestone. Include touchpoints, content delivery, and customer actions at each stage. Deliverable: onboarding journey map with timeline.
3. **Create Playbook Content**: Write the playbook sections: kickoff meeting agenda, configuration checklist, training schedule, success criteria per stage, and escalation triggers for stalled onboarding. Deliverable: complete onboarding playbook document.
4. **Define Handoff Protocols**: Specify how the customer transitions from sales to CS at onboarding start, and from onboarding to steady-state CS at completion. Deliverable: handoff checklists for both transitions.
5. **Establish Measurement**: Define onboarding metrics -- time-to-value, completion rate, stage drop-off rates, and customer satisfaction at onboarding end. Apply the scoring rubric at `references/scoring-rubric.md`. Deliverable: onboarding metrics framework.

## Anti-Patterns

- **One-size-fits-all onboarding**: Using the same onboarding flow for all customer segments regardless of size, complexity, or use case. *Why*: enterprise customers need hands-on configuration support while self-serve customers need automated guidance; mixing them wastes effort or under-serves.
- **Feature tour without value connection**: Walking customers through product features without connecting each feature to the customer's specific business outcomes. *Why*: customers churn when they see features but not value; onboarding must demonstrate ROI, not product capability.
- **Onboarding without exit criteria**: Running onboarding indefinitely without clear completion criteria. *Why*: undefined endpoints mean customers linger in onboarding, never transitioning to steady-state engagement where expansion happens.

## Output

**On success**: Produces a complete onboarding playbook containing journey map, playbook content, handoff protocols, and metrics framework. Delivered to the CS Manager and CS team for execution.

**On failure**: Report which playbook components could not be completed (unclear value milestones, undefined handoff process), what was drafted, and what product or sales inputs are needed.

## Related Skills

- [`cs-activation`](../../customer-success-manager/cs-activation/SKILL.md) -- Individual customer activation follows the onboarding playbook.
- [`sla-definer-cs`](../sla-definer-cs/SKILL.md) -- SLAs define the response time commitments during onboarding.
- [`training-material-creator-cs`](../training-material-creator-cs/SKILL.md) -- Training materials are a key component of the onboarding experience.
