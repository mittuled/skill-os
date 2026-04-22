---
name: cohort-selector
description: >
  This skill selects the user cohort for a controlled rollout based on risk profile and representativeness.
  Use when a feature is ready for rollout and the team needs to define which users receive it first.
  Also consider when a rollout plan lacks a clear cohort definition or when past rollouts hit unexpected segments.
  Suggest when a launch is being planned and no cohort selection criteria have been discussed.
department: product
agent: product-operations-analyst
version: 1.0.0
complexity: medium
related-skills:
  - objection-handler-updater
  - early-adopter-success-builder
  - iteration-prioritiser
triggers:
  - "select cohort"
  - "choose cohort"
  - "cohort selection"
  - "define cohort"
  - "user cohort"
---

# cohort-selector

## Agent: Product Operations Analyst
L3 product operations analyst (multi-instance) responsible for rollout configuration, adoption tracking, revenue impact monitoring, support triage, and iteration prioritisation.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Selects the user cohort for a controlled rollout based on risk profile and representativeness.

## When to Use
- When a feature is approved for staged rollout and the team needs to decide which users get it first
- When the product manager asks for a cohort recommendation that balances risk with signal quality
- When a previous rollout failed because the initial cohort was unrepresentative and masked issues
- When a rollout plan is under review and cohort criteria have not been explicitly defined

## Workflow
1. **Review the rollout objectives**: Gather the feature brief, success metrics, and any known risk factors (performance sensitivity, billing impact, integration dependencies). Identify what the rollout needs to prove. Deliverable: one-paragraph rollout objective summary with key risks listed.
2. **Define cohort dimensions**: Identify the segmentation axes relevant to this rollout — plan tier, company size, geography, usage intensity, tenure, or platform. Prioritise dimensions that correlate with the identified risks. Deliverable: ranked list of segmentation dimensions with rationale for each.
3. **Assess representativeness**: Verify the candidate cohort reflects the broader user base across critical dimensions. Check that no high-risk segment (e.g., enterprise accounts, high-MRR customers) is over- or under-represented unless deliberately excluded. Deliverable: representativeness check showing cohort composition vs. population composition.
4. **Score risk exposure**: Evaluate the blast radius if the feature fails for the selected cohort. Consider revenue at risk, contractual SLA exposure, and reputational impact. Assign a risk tier (low/medium/high). Deliverable: risk exposure assessment with tier assignment and mitigation notes.
5. **Propose the cohort**: Recommend the final cohort with selection criteria, expected size, and rollout percentage. Include exclusion criteria and the rationale for each exclusion. Deliverable: cohort specification document with inclusion/exclusion rules, expected volume, and risk tier.
6. **Document rollback triggers**: Define the metrics or events that would trigger pausing or rolling back the cohort expansion. Deliverable: rollback trigger list appended to the cohort specification.

## Anti-Patterns
- **Selecting the easiest cohort instead of the most informative**: Choosing low-risk, low-usage users because they are safe, even though they produce no meaningful adoption signal. *Why*: The purpose of a staged rollout is to learn — a cohort that cannot generate actionable signal wastes the rollout phase.
- **Skipping representativeness checks**: Assuming any subset of users is "good enough" without verifying it reflects the broader population. *Why*: Unrepresentative cohorts produce misleading adoption and performance data, leading to false confidence before general availability.
- **Including high-risk accounts without explicit sign-off**: Adding enterprise or high-MRR customers to an early cohort without product and customer success approval. *Why*: Revenue concentration means a single bad experience can have outsized business impact and erode trust with strategic accounts.

## Output
**On success**: A cohort specification document containing selection criteria (inclusion and exclusion rules), expected cohort size and percentage, representativeness validation, risk tier with mitigation notes, and rollback triggers — ready for handoff to the rollout configurator.
**On failure**: Report which data was unavailable (e.g., missing segmentation data, no baseline population stats), what partial analysis was completed, and recommend steps to unblock (e.g., "request user segmentation export from data engineering").

## Related Skills
- [`objection-handler-updater`](../objection-handler-updater/SKILL.md) — sibling skill under the same agent — combine with objection-handler-updater for end-to-end coverage
- [`early-adopter-success-builder`](../early-adopter-success-builder/SKILL.md) — sibling skill under the same agent — combine with early-adopter-success-builder for end-to-end coverage
- [`iteration-prioritiser`](../iteration-prioritiser/SKILL.md) — sibling skill under the same agent — combine with iteration-prioritiser for end-to-end coverage
