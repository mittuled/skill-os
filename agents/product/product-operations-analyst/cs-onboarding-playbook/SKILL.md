---
name: cs-onboarding-playbook
description: >
  This skill reviews and contributes to the customer success onboarding playbook from a product perspective.
  Use when the CS team is drafting or updating an onboarding playbook and needs product input on flows and milestones.
  Also consider when onboarding completion rates drop or when a major product change affects the onboarding journey.
  Suggest when a new feature ships that changes the first-run experience but the onboarding playbook has not been updated.
department: product
agent: product-operations-analyst
version: 1.0.0
complexity: medium
related-skills:
  - objection-handler-updater
  - early-adopter-success-builder
  - iteration-prioritiser
triggers:
  - "cs onboarding playbook"
  - "customer success playbook"
  - "onboarding playbook"
  - "cs playbook"
  - "customer onboarding guide"
---

# cs-onboarding-playbook

## Agent: Product Operations Analyst
L3 product operations analyst (multi-instance) responsible for rollout configuration, adoption tracking, revenue impact monitoring, support triage, and iteration prioritisation.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Reviews and contributes to the customer success onboarding playbook from a product perspective.

## When to Use
- When the customer success team is creating or revising an onboarding playbook and requests product operations input
- When onboarding completion rates decline and the team suspects the playbook is out of sync with the current product
- When a significant product change (new flow, removed feature, changed UI) invalidates steps in the existing playbook
- When new customer segments are being onboarded and the playbook needs segment-specific guidance

## Workflow
1. **Audit the current playbook**: Read the existing onboarding playbook end-to-end. Map each step to the current product state — identify steps that reference deprecated features, outdated screenshots, or flows that have changed. Deliverable: audit log listing each playbook step with a status of current, outdated, or missing.
2. **Identify product-driven milestones**: Define the activation milestones that matter from a product perspective — first value moment, key integration completion, feature discovery checkpoints. Cross-reference with adoption metrics to confirm these milestones correlate with retention. Deliverable: milestone list with metric backing for each.
3. **Draft product contributions**: Write or revise playbook sections that require product expertise — setup flows, configuration guidance, feature walkthroughs, and troubleshooting paths. Use the current product state as source of truth. Deliverable: drafted playbook sections ready for CS review.
4. **Add segment-specific branches**: Where onboarding differs by customer segment (plan tier, use case, industry), add conditional paths in the playbook. Flag where the product itself should adapt vs. where the playbook compensates for product gaps. Deliverable: branching logic added to the playbook with segment labels.
5. **Review with CS and product**: Walk through the updated playbook with customer success leads and the product manager. Validate that product milestones align with CS touchpoints and that nothing is missing. Deliverable: reviewed playbook with sign-off notes or revision requests.

## Anti-Patterns
- **Writing the playbook in isolation from CS**: Drafting product sections without understanding CS workflows and touchpoints. *Why*: The playbook is a CS-owned artifact — product contributions that ignore CS context create friction and get overridden.
- **Assuming the product is self-explanatory**: Skipping setup guidance or configuration steps because "the UI is intuitive." *Why*: What feels obvious to the product team is often confusing to new users, especially in enterprise contexts with complex configurations.
- **Static playbook without update triggers**: Contributing once and never revisiting. *Why*: Products change continuously — a playbook that is not updated with each significant release drifts into inaccuracy and erodes CS trust in the document.

## Output
**On success**: Updated onboarding playbook sections covering product-driven milestones, setup flows, segment-specific branches, and troubleshooting paths — reviewed and approved by both CS and product stakeholders.
**On failure**: Report which playbook sections could not be updated (e.g., product flow is mid-redesign, metrics unavailable for milestone validation), what partial contributions were made, and recommend a timeline for revisiting once blockers clear.

## Related Skills
- [`objection-handler-updater`](../objection-handler-updater/SKILL.md) — sibling skill under the same agent — combine with objection-handler-updater for end-to-end coverage
- [`early-adopter-success-builder`](../early-adopter-success-builder/SKILL.md) — sibling skill under the same agent — combine with early-adopter-success-builder for end-to-end coverage
- [`iteration-prioritiser`](../iteration-prioritiser/SKILL.md) — sibling skill under the same agent — combine with iteration-prioritiser for end-to-end coverage
