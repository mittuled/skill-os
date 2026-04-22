---
name: training-material-creator-cs
description: >
  This skill creates training materials for the CS team on product features,
  processes, and customer communication. Use when asked to build CS training
  content, onboard new CSMs, or update product knowledge materials. Also
  consider when product changes are not reflected in CS training. Suggest when
  the user launches features without CS team enablement.
department: customer-success
agent: head-of-customer-success
version: 1.0.0
complexity: medium
related-skills:
  - support-runbook-builder-cs
  - cs-release-readiness
  - cs-onboarding-playbook-cs
triggers:
  - "create training materials"
  - "cs training content"
  - "build training docs"
  - "training material cs"
  - "onboarding training cs"
---

# training-material-creator-cs

## Agent: Head of Customer Success

L1 customer success leader reporting to the CBO (1x) responsible for CS strategy, SLA design, playbook creation, expansion motion, and training materials.

Department ethos: [ideal-customer-success.md](../../../../departments/customer-success/ideal-customer-success.md)

## Skill Description

Creates training materials for the CS team covering product features, internal processes, and customer communication best practices.

## When to Use

- When new CSMs are joining the team and need onboarding materials.
- When a product release introduces features the CS team needs to understand before customer conversations.
- When CS team performance reviews reveal knowledge gaps in product or process areas.

## Workflow

1. **Identify Training Needs**: Gather input from CS managers, performance reviews, and product release notes. Prioritize topics by impact on customer outcomes. Deliverable: training needs assessment.
2. **Design Training Modules**: Structure content into digestible modules: product feature guides, process walkthroughs, customer communication frameworks, and scenario-based exercises. Deliverable: training module outlines.
3. **Create Content**: Write training materials in clear, practical language. Include examples, screenshots, and practice scenarios. Deliverable: complete training materials per module.
4. **Review with SMEs**: Have product managers and senior CSMs review materials for accuracy and completeness. Deliverable: reviewed and approved training materials.
5. **Deliver and Assess**: Distribute materials to the CS team. Include knowledge checks or quizzes to verify comprehension. Deliverable: delivered training with assessment results.

## Anti-Patterns

- **Feature documentation as training**: Copying product documentation verbatim instead of framing features in customer-value terms. *Why*: CSMs need to explain features in terms of customer outcomes, not technical specifications.
- **One-time training dumps**: Delivering all training in a single session without reinforcement or follow-up. *Why*: information retention drops sharply without spaced repetition; training must be ongoing.
- **Training without practice**: Providing information without scenario-based exercises. *Why*: knowledge without practice does not transfer to real customer conversations.

## Output

**On success**: Produces training materials containing product guides, process documentation, communication frameworks, and assessment exercises. Delivered to the CS team with knowledge check results.

**On failure**: Report which training modules could not be completed (missing product information, unavailable SMEs), what was created, and what inputs are needed.

## Related Skills

- [`support-runbook-builder-cs`](../support-runbook-builder-cs/SKILL.md) -- Runbooks are a key training reference for scenario handling.
- [`cs-release-readiness`](../../../customer-success/cs-manager/cs-release-readiness/SKILL.md) -- Release readiness includes training as a prerequisite.
- [`cs-onboarding-playbook-cs`](../cs-onboarding-playbook-cs/SKILL.md) -- CSMs must be trained on the onboarding playbook they execute.
