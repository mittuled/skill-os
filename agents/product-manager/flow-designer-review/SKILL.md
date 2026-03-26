---
name: flow-designer-review
description: >
  This skill reviews proposed user flows for completeness, usability, and alignment with product requirements.
  Use when a designer or engineer submits a user flow diagram and needs PM validation before implementation begins.
  Also consider when an existing flow is being refactored and the revised version needs to be checked against original
  requirements and newly discovered edge cases. Suggest when a feature is moving from design to engineering and no one
  has verified that the flow covers all user personas, error states, and integration touchpoints.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills: []
---

# flow-designer-review

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)

## Skill Description
Reviews proposed user flows for completeness, usability, and alignment with requirements, ensuring every path a user can take is intentional, handles errors gracefully, and maps back to accepted stories.

## When to Use
- When a designer submits a new user flow diagram (task flow, wireflow, or screen flow) for PM review
- When an existing flow has been revised after usability testing or stakeholder feedback and needs re-evaluation
- When engineering flags ambiguity in a flow during sprint planning and needs the PM to clarify intended behavior
- When a feature spans multiple user personas and each persona's path through the flow must be validated separately

## Workflow
1. **Gather context**: Collect the user stories, acceptance criteria, and persona definitions that the flow is meant to satisfy. Identify any prior usability research, competitive analysis, or customer feedback that informed the design. Deliverable: context package with linked stories and supporting research.
2. **Map flow coverage to requirements**: Walk through every step in the proposed flow and tag it to the acceptance criterion it satisfies. Identify criteria with no corresponding flow step (gaps) and flow steps with no corresponding criterion (scope creep). Deliverable: coverage matrix showing story-to-step mapping with gap and creep annotations.
3. **Trace each persona path**: For every persona the feature serves, trace the expected path through the flow from entry to completion. Verify the flow accommodates differences in persona goals, technical proficiency, and access level. Deliverable: persona path trace with notes on where the flow diverges per persona.
4. **Evaluate error and edge-case handling**: Identify every point where the user can fail, abandon, or encounter an unexpected state. Verify the flow defines what happens at each failure point -- error messages, recovery paths, and fallback states. Deliverable: edge-case inventory with handling status (covered / missing / partial).
5. **Assess flow coherence**: Check that navigation is consistent, terminology matches the product's existing patterns, and the number of steps is justified by the task complexity. Flag unnecessary steps that add friction without value. Deliverable: coherence notes with specific reduction or consolidation suggestions.
6. **Deliver the review verdict**: Summarize findings into an approve, revise, or rework recommendation. For revisions, list each required change with the specific acceptance criterion or usability principle it addresses. Deliverable: review memo with decision, required changes, and priority ranking of each change.

## Anti-Patterns
- **Reviewing the flow in isolation from requirements**: Evaluating usability and aesthetics without checking whether the flow actually satisfies the accepted stories. *Why*: A flow can feel intuitive yet miss critical functionality, and the gap only surfaces when engineering delivers a feature that does not match what customers were promised.
- **Ignoring error states**: Approving a happy-path-only flow because edge cases seem unlikely. *Why*: Users inevitably hit error states, and unhandled failures create support tickets, data corruption, or silent failures that erode trust faster than a missing feature.
- **Scope expansion during review**: Adding new requirements or features during the flow review instead of evaluating against the agreed scope. *Why*: Derails the sprint timeline, creates confusion about what was agreed upon, and forces the designer into an unplanned iteration cycle without updated stories.
- **Delegating the review entirely to design**: Assuming the designer has already validated requirements alignment because they wrote the flow. *Why*: Designers optimize for usability and visual coherence; the PM owns requirements alignment, and these are distinct evaluations that catch different categories of issues.

## Output
**On success**: A flow review memo containing the coverage matrix, persona path traces, edge-case inventory, coherence notes, and a clear verdict (approved / revisions required / rework needed) with prioritized change list referencing specific acceptance criteria.
**On failure**: Report which parts of the review could not be completed (missing persona definitions, unclear acceptance criteria, incomplete flow diagram), what was evaluated, and the specific artifacts or clarifications needed from the designer or stakeholder before the review can resume.

## Related Skills
- (none yet -- cross-references added in Phase 1.6)
