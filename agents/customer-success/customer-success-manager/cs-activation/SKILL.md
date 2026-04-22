---
name: cs-activation
description: >
  This skill activates new customers through structured onboarding to reach the
  first value milestone. Use when asked to onboard a new customer, drive initial
  adoption, or ensure time-to-value. Also consider when a customer has signed
  but not started using the product. Suggest when the user closes deals without
  handing off to a structured activation process.
department: customer-success
agent: customer-success-manager
version: 1.0.0
complexity: medium
related-skills:
  - cs-onboarding-playbook-cs
  - early-adopter-success-builder-cs
  - cs-signal-extractor
triggers:
  - "activate customer success"
  - "cs activation"
  - "onboard new customer"
  - "customer activation plan"
  - "kickoff CS engagement"
---

# cs-activation

## Agent: Customer Success Manager

L3 customer success manager (Nx) responsible for signal extraction, feedback synthesis, early adopter success, and customer activation.

Department ethos: [ideal-customer-success.md](../../../../departments/customer-success/ideal-customer-success.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Activates new customers through structured onboarding to reach the first value milestone within the defined time-to-value target.

## When to Use

- When a new customer has signed and needs to be guided through onboarding to first value.
- When a signed customer has not engaged with the product after the expected activation window.
- When an existing customer is expanding to a new use case and needs re-activation support.

## Workflow

1. **Kickoff Meeting**: Conduct the kickoff meeting following the onboarding playbook. Confirm customer goals, success criteria, key stakeholders, and timeline. Deliverable: kickoff notes with agreed success criteria.
2. **Configuration Support**: Guide the customer through product configuration, integration setup, and initial data import. Remove technical blockers. Deliverable: configured product environment.
3. **Drive First Use Case**: Work with the customer to execute their first complete use case end-to-end. Ensure they experience the value the product was sold on. Deliverable: completed first use case with customer confirmation.
4. **Verify Value Achievement**: Confirm the customer has reached the first value milestone as defined in kickoff. Collect feedback on the onboarding experience. Deliverable: value milestone confirmation with customer feedback.
5. **Transition to Steady State**: Hand off from activation mode to ongoing CS engagement. Brief the customer on available resources, support channels, and next milestones. Deliverable: steady-state transition with documented next steps.

## Anti-Patterns

- **Passive activation**: Sending welcome emails and waiting for the customer to figure it out. *Why*: customers who are left to self-activate have lower adoption rates and higher early churn.
- **Feature-focused activation**: Teaching the customer every feature instead of focusing on the specific use case that motivated their purchase. *Why*: overwhelming new customers with features delays value realization and increases confusion.
- **Activation without measurement**: Completing onboarding steps without verifying the customer actually achieved value. *Why*: checked boxes are not the same as customer success; activation must be measured by outcomes, not activities.

## Output

**On success**: Produces a completed activation record with kickoff notes, configuration confirmation, first use case completion, value milestone verification, and steady-state transition plan. Delivered to the CS Manager.

**On failure**: Report where activation stalled (configuration blocker, engagement drop-off, unresolved technical issue), what interventions were attempted, and recommended next steps or escalation.

## Related Skills

- [`cs-onboarding-playbook-cs`](../../../customer-success/head-of-customer-success/cs-onboarding-playbook-cs/SKILL.md) -- The onboarding playbook that activation follows.
- [`early-adopter-success-builder-cs`](../early-adopter-success-builder-cs/SKILL.md) -- Early adopter activation requires additional interventions.
- [`cs-signal-extractor`](../cs-signal-extractor/SKILL.md) -- Activation conversations generate signals for product and market insight.
