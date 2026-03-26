---
name: backlog-groomer
description: >
  This skill refines, estimates, and re-prioritises backlog items so upcoming sprints contain only sprint-ready stories. Use when a sprint boundary approaches and the top of the backlog contains unrefined items. Also consider when acceptance criteria are missing, stale stories accumulate, or estimation confidence is low. Suggest when engineering flags ambiguity in upcoming work or when sprint velocity variance exceeds 20%.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills:
  - backlog-populator
  - sprint-planner
  - story-writer
  - dependency-mapper-review
---

# backlog-groomer

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)

## Skill Description
The backlog groomer refines the product backlog by ensuring every story within the sprint horizon has clear acceptance criteria, a story-point estimate agreed upon by the delivery team, and a RICE-informed priority rank. It transforms vague requests into actionable, estimable units of work that engineering can confidently pull into a sprint.

## When to Use
- The next sprint planning session is within two business days and the top N stories lack acceptance criteria or estimates.
- Stakeholders have added raw feature requests that need decomposition into user stories.
- Sprint velocity variance over the last three sprints exceeds 20%, signalling estimation drift.
- Engineering raises repeated clarification questions on stories already in the backlog.
- A reprioritisation event occurs (customer escalation, strategic pivot, dependency shift).

## Workflow
1. Pull the current backlog ranked by RICE score or existing priority order.
2. Identify stories in the sprint horizon (typically top 1.5x sprint capacity) that lack acceptance criteria, estimates, or an assigned epic.
3. For each unrefined story, draft or tighten acceptance criteria using the Given/When/Then format.
4. Facilitate asynchronous or synchronous estimation with the delivery team; record story-point consensus.
5. Flag stories with unclear scope or external dependencies and route them to `dependency-mapper-review` or `scope-boundary-setter`.
6. Remove or archive stories that have been inactive for more than two sprints and lack stakeholder sponsorship.
7. Re-rank the refined backlog segment using RICE (Reach, Impact, Confidence, Effort) inputs.
8. Publish the groomed backlog snapshot and notify the sprint planner that stories are sprint-ready.

## Anti-Patterns
- **Grooming without engineering input.** Estimates set unilaterally by product lack delivery-team buy-in and inflate velocity variance. *Why: estimation accuracy depends on the people who will do the work.*
- **Refining too far ahead.** Grooming stories more than two sprints out wastes effort on items likely to change. *Why: requirements evolve; premature refinement creates rework.*
- **Skipping acceptance criteria.** Pushing stories to "ready" without Given/When/Then leads to mid-sprint scope debates. *Why: ambiguity surfaces during development as blocked tickets.*
- **Treating grooming as a status meeting.** Spending session time on updates instead of refinement starves the backlog of sprint-ready stories. *Why: grooming is a preparation activity, not a reporting ceremony.*

## Output

**Success:**
- A groomed backlog segment where every story in the sprint horizon has acceptance criteria, a story-point estimate, and a RICE-informed rank.
- A clear "ready" / "not ready" flag per story, with blockers documented for any "not ready" items.

**Failure:**
- Stories enter sprint planning without estimates or acceptance criteria, causing mid-sprint renegotiation.
- The groomed segment is returned with unresolved dependency flags that were not escalated.

## Related Skills
- `backlog-populator` -- sources and creates the raw stories this skill refines.
- `sprint-planner` -- consumes the groomed backlog to build the sprint plan.
- `story-writer` -- authors the user stories that grooming polishes.
- `dependency-mapper-review` -- receives dependency flags surfaced during grooming.
