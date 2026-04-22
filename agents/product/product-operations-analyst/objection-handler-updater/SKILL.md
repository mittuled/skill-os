---
name: objection-handler-updater
description: >
  This skill updates the sales objection handler based on product changes and new competitive information.
  Use when a product release changes capabilities that affect how sales handles buyer objections.
  Also consider when sales reports new objections that are not covered in the current handler or when a competitor ships a feature that changes the competitive landscape.
  Suggest when a release ships with differentiation impact but the objection handler has not been reviewed.
department: product
agent: product-operations-analyst
version: 1.0.0
complexity: simple
related-skills:
  - adoption-tracker
  - cohort-selector
  - cs-onboarding-playbook
  - early-adopter-success-builder
  - feedback-loop-formaliser
  - internal-comms-broadcaster
  - iteration-prioritiser
  - revenue-impact-monitor
  - rollout-configurator-review
  - signal-synthesiser
  - support-ticket-triage
triggers:
  - "update objection handler"
  - "refresh objection handling"
  - "objection responses"
  - "update sales objections"
  - "objection library"
---

# objection-handler-updater

## Agent: Product Operations Analyst
L3 product operations analyst (multi-instance) responsible for rollout configuration, adoption tracking, revenue impact monitoring, support triage, and iteration prioritisation.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Updates the sales objection handler based on product changes and new competitive information.

## When to Use
- When a product release adds, changes, or removes capabilities that affect how sales responds to buyer objections
- When the sales team reports encountering new objections not covered in the current handler
- When a competitor launches a feature that shifts the competitive narrative and existing responses become stale
- When win/loss analysis reveals recurring objections that the handler does not adequately address

## Workflow
1. **Identify objection-relevant changes**: Review the release notes, competitive intelligence updates, and recent win/loss data. List every change that affects an existing objection response or creates a new objection category. Deliverable: change-to-objection mapping listing each product or market change and the objections it affects.
2. **Draft updated responses**: For each affected objection, write or revise the handler response. Include the objection statement, the recommended response, proof points (metrics, case studies, technical details), and any caveats the sales rep should be aware of. Deliverable: updated objection handler entries ready for sales review.
3. **Review with sales and product**: Share the draft updates with sales leadership and the product manager. Validate that responses are accurate, the tone matches the sales motion, and proof points are current. Deliverable: reviewed and approved handler entries with sign-off.

## Anti-Patterns
- **Updating responses without sales input**: Writing objection handlers from a product perspective without validating with the people who deliver them. *Why*: Product-accurate responses that do not match the sales conversation flow get ignored in live calls.
- **Leaving deprecated responses in the handler**: Adding new responses without removing or marking outdated ones. *Why*: Sales reps who accidentally use an outdated response lose credibility with buyers and may misrepresent current capabilities.
- **Generic responses that avoid specifics**: Writing vague responses like "our product is the best in class" instead of providing concrete differentiators. *Why*: Buyers see through generic claims — specific proof points (metrics, architecture details, customer references) are what overcome objections.

## Output
**On success**: Updated objection handler entries covering new and revised responses with proof points, reviewed and approved by sales leadership — ready for distribution to the sales team.
**On failure**: Report which objections could not be updated (e.g., proof points not yet available for a new feature, competitive information unverified), what partial updates were made, and recommend a timeline for completing the remaining entries.

## Related Skills
- [`adoption-tracker`](../adoption-tracker/SKILL.md) — sibling skill under the same agent — combine with adoption-tracker for end-to-end coverage
- [`cohort-selector`](../cohort-selector/SKILL.md) — sibling skill under the same agent — combine with cohort-selector for end-to-end coverage
- [`cs-onboarding-playbook`](../cs-onboarding-playbook/SKILL.md) — sibling skill under the same agent — combine with cs-onboarding-playbook for end-to-end coverage
- [`early-adopter-success-builder`](../early-adopter-success-builder/SKILL.md) — sibling skill under the same agent — combine with early-adopter-success-builder for end-to-end coverage
- [`feedback-loop-formaliser`](../feedback-loop-formaliser/SKILL.md) — sibling skill under the same agent — combine with feedback-loop-formaliser for end-to-end coverage
- [`internal-comms-broadcaster`](../internal-comms-broadcaster/SKILL.md) — sibling skill under the same agent — combine with internal-comms-broadcaster for end-to-end coverage
- [`iteration-prioritiser`](../iteration-prioritiser/SKILL.md) — sibling skill under the same agent — combine with iteration-prioritiser for end-to-end coverage
- [`revenue-impact-monitor`](../revenue-impact-monitor/SKILL.md) — sibling skill under the same agent — combine with revenue-impact-monitor for end-to-end coverage
- [`rollout-configurator-review`](../rollout-configurator-review/SKILL.md) — sibling skill under the same agent — combine with rollout-configurator-review for end-to-end coverage
- [`signal-synthesiser`](../signal-synthesiser/SKILL.md) — sibling skill under the same agent — combine with signal-synthesiser for end-to-end coverage
- [`support-ticket-triage`](../support-ticket-triage/SKILL.md) — sibling skill under the same agent — combine with support-ticket-triage for end-to-end coverage
