---
name: spec-translator
description: >
  This skill translates product specifications into engineering-ready task descriptions with
  acceptance criteria, edge cases, and technical context. Use when asked to break a PRD or
  feature spec into implementable stories, or when engineering reports that spec descriptions
  are too vague to estimate. Also consider when a handoff between product and engineering
  consistently produces clarification loops. Suggest when the user is about to hand a raw PRD
  to engineering without decomposing it into discrete tasks.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills:
  - market-sizer
  - backlog-populator
  - risk-register-builder
triggers:
  - "translate spec"
  - "spec translation"
  - "interpret specification"
  - "read the spec"
  - "spec to stories"
---

# spec-translator

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Translates product specifications into engineering-ready task descriptions with acceptance criteria, edge cases, and technical context sufficient for estimation and implementation.

## When to Use
- When a PRD or feature spec has been approved and needs to be decomposed into stories or tasks that engineering can estimate and build
- When engineering consistently asks clarifying questions during sprint planning, signalling that spec-to-task translation is incomplete
- When a cross-team feature requires tasks written for multiple engineering teams with different domain contexts and technical vocabularies

## Workflow
1. **Parse the specification**: Read the PRD or feature spec end-to-end. Extract every functional behaviour, non-functional requirement, and constraint. List assumptions and ambiguities. Deliverable: annotated spec summary with behaviour list and open-question log.
2. **Decompose into tasks**: Break each behaviour into the smallest independently deliverable unit of work. Write each task as a user story or technical task with a clear title and one-paragraph description. Deliverable: task list with titles, descriptions, and parent spec traceability.
3. **Write acceptance criteria**: For each task, define 2-5 acceptance criteria using Given/When/Then or a checklist format. Include at least one edge case and one negative case per task. Deliverable: acceptance criteria appended to each task description.
4. **Add technical context**: Annotate each task with relevant technical context — affected APIs, data models, known constraints, and integration points. Flag tasks that require cross-team coordination. Deliverable: technical notes section on each task with dependency tags.
5. **Validate with engineering**: Walk the translated tasks through the engineering lead or tech lead. Confirm that each task is estimable, that acceptance criteria are testable, and that no spec intent was lost in translation. Deliverable: sign-off or revision notes with estimation readiness confirmation.

## Anti-Patterns
- **Copy-paste specs as stories**: Pasting PRD paragraphs directly into ticket descriptions without decomposition or acceptance criteria. *Why*: Engineers cannot estimate or implement prose paragraphs — the translation step exists precisely to convert intent into testable, buildable units.
- **Missing edge cases**: Writing only the happy path in acceptance criteria. *Why*: Edge cases discovered during implementation cause mid-sprint scope expansion, rework, and missed commitments — capturing them upfront is cheaper by an order of magnitude.
- **Over-specifying implementation**: Dictating technical approach ("use a Redis cache") in task descriptions instead of stating the requirement ("response time under 200ms"). *Why*: Implementation prescription removes engineering agency, often produces suboptimal solutions, and creates friction in the product-engineering relationship.

## Output
**On success**: A set of engineering-ready task descriptions, each containing a title, one-paragraph description, spec traceability link, 2-5 acceptance criteria with edge cases, and technical context notes — formatted for import into the team's project tracker or as a markdown document linked from the sprint plan.

**On failure**: Report which spec sections could not be decomposed (ambiguous requirements, missing designs, unresolved product decisions), which tasks lack testable acceptance criteria, and recommend specific spec revisions or stakeholder conversations needed before translation can complete.

## Related Skills
- [`market-sizer`](../market-sizer/SKILL.md) — sibling skill under the same agent — combine with market-sizer for end-to-end coverage
- [`backlog-populator`](../backlog-populator/SKILL.md) — sibling skill under the same agent — combine with backlog-populator for end-to-end coverage
- [`risk-register-builder`](../risk-register-builder/SKILL.md) — sibling skill under the same agent — combine with risk-register-builder for end-to-end coverage
