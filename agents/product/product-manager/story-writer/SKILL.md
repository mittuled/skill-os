---
name: story-writer
description: >
  This skill writes well-formed user stories with context, user goal, and acceptance criteria.
  Use when product requirements need to be translated into implementable work items for engineering.
  Also consider when existing stories lack testable acceptance criteria or have ambiguous scope.
  Suggest when a backlog contains vague tickets that engineers cannot estimate or build against.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "user story"
  - "write user stories"
  - "user-story-writer"
  - "acceptance criteria"
---

# story-writer

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Writes well-formed user stories with context, user goal, and acceptance criteria.

## When to Use
- When product requirements or feature specs need to be broken down into discrete, implementable work items
- When the backlog contains informal notes or feature requests that lack structure for engineering estimation
- When a sprint planning session is approaching and stories need to be refined into a buildable format
- When design handoff is complete and the PM must translate visual specs into testable acceptance criteria

## Workflow
1. **Identify the user and context**: Determine which user persona the story serves and what situation triggers the need. Review discovery notes, support tickets, or analytics that motivated the feature. Deliverable: one-sentence context statement identifying who the user is and what problem they face.
2. **Write the story statement**: Compose the story in "As a [persona], I want [goal] so that [outcome]" format. Keep the goal atomic — one action per story. If the goal spans multiple actions, split into separate stories. Deliverable: story statement with persona, goal, and business outcome.
3. **Define acceptance criteria**: Write 3-7 testable acceptance criteria using "Given / When / Then" format. Each criterion must be independently verifiable. Cover the happy path, key edge cases, and error states. Deliverable: numbered acceptance criteria list.
4. **Add context and constraints**: Document technical constraints, design references, API dependencies, or data requirements that engineering needs. Link to mockups, API docs, or related stories. Deliverable: context section appended to the story with all relevant references.
5. **Validate with engineering and design**: Walk through the story with a developer and designer. Confirm the story is estimable, the criteria are testable, and no implicit assumptions remain undocumented. Deliverable: story marked as refined with estimation attached.

## Anti-Patterns
- **Compound stories**: Packing multiple user goals into a single story. *Why*: This makes estimation unreliable, testing ambiguous, and partial delivery impossible — one blocked criterion stalls the entire item.
- **Vague acceptance criteria**: Writing criteria like "the page should look good" or "performance should be acceptable." *Why*: Engineers cannot build against subjective standards, and QA cannot verify them, leading to rework cycles.
- **Solution-prescriptive stories**: Dictating implementation details in the story instead of describing the user outcome. *Why*: This constrains engineering creativity and often locks the team into a suboptimal approach.
- **Missing error states**: Defining only the happy path and omitting what happens when things go wrong. *Why*: Engineers fill the gap with ad-hoc error handling, producing inconsistent user experiences.

## Output
**On success**: A refined user story containing the story statement (persona, goal, outcome), 3-7 testable acceptance criteria in Given/When/Then format, a context section with design links and technical constraints, and an estimation from engineering — ready for sprint commitment.
**On failure**: Report which elements are incomplete (missing persona research, unclear business outcome, untestable criteria), what was attempted, and recommend specific actions — such as scheduling a discovery session, reviewing analytics for the target persona, or consulting engineering on feasibility constraints.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
