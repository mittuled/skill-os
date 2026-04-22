---
name: milestone-definer
description: >
  This skill defines product milestones with clear success criteria and target dates for a delivery
  phase or initiative. Use when asked to break a roadmap item into checkpoints, set phase gates, or
  define what "done" looks like at each stage. Also consider when a project is running without visible
  progress markers and stakeholders are losing confidence. Suggest when the team is about to start
  execution on a multi-sprint initiative without intermediate checkpoints.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills:
  - market-sizer
  - backlog-populator
  - risk-register-builder
triggers:
  - "define milestones"
  - "set milestones"
  - "milestone planning"
  - "project milestones"
  - "milestone definition"
---

# milestone-definer

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Defines product milestones with clear success criteria and target dates that give teams and stakeholders shared visibility into delivery progress.

## When to Use
- When a new initiative or delivery phase needs intermediate checkpoints before work begins
- When stakeholders are asking "are we on track?" and there are no defined milestones to answer against
- When a project has drifted past its original timeline and needs re-baselining with realistic, scoped milestones

## Workflow
1. **Inventory the deliverables**: Review the PRD, initiative brief, or phase plan to extract the full set of deliverables and dependencies. Identify which items are on the critical path. Deliverable: ordered list of deliverables with dependency annotations.
2. **Cluster into milestones**: Group deliverables into 3-6 milestones that each represent a meaningful, demonstrable increment of value. Each milestone must be independently verifiable -- avoid milestones that only make sense in combination. Deliverable: milestone list with scope summary per milestone.
3. **Define success criteria**: Write 2-4 binary (pass/fail) success criteria per milestone. Each criterion must be observable without subjective judgment -- prefer "API returns results in under 200ms" over "API is fast enough." Deliverable: success criteria table appended to each milestone.
4. **Assign target dates**: Work backward from the phase deadline or forward from sprint capacity estimates. Build in buffer for the highest-risk milestone (typically the one with the most external dependencies). Deliverable: milestone timeline with target dates and owners.
5. **Validate with engineering and design**: Walk the milestone plan through the delivery team. Confirm that scope clusters are technically coherent and that dates account for known risks. Deliverable: validated milestone plan or revision notes.

## Anti-Patterns
- **Milestone as task list**: Defining milestones that are individual tasks ("write API endpoint") rather than demonstrable increments of value. *Why*: Task-level milestones create false progress signals and prevent stakeholders from evaluating whether the product is actually converging on user value.
- **Vague success criteria**: Writing criteria like "feature works well" or "design is polished." *Why*: Subjective criteria make milestone reviews performative rather than diagnostic; teams pass milestones that should have been flagged.
- **Back-loaded risk**: Placing the hardest integration or most uncertain work in the final milestone. *Why*: Late discovery of blockers eliminates recovery time and forces scope cuts under pressure rather than by design.
- **Too many milestones**: Defining 10+ milestones for a single phase. *Why*: Overhead of milestone reviews exceeds their diagnostic value, and the team spends more time reporting than building.

## Output
**On success**: A milestone plan containing 3-6 milestones, each with scope summary, 2-4 binary success criteria, target date, and owner -- formatted as a table or structured document suitable for embedding in a project tracker or initiative brief.

**On failure**: Report which milestones could not be fully defined (unclear deliverables, unresolved dependencies, missing capacity estimates), what was attempted, and recommend specific conversations or decisions needed to unblock the plan.

## Related Skills
- [`market-sizer`](../market-sizer/SKILL.md) — sibling skill under the same agent — combine with market-sizer for end-to-end coverage
- [`backlog-populator`](../backlog-populator/SKILL.md) — sibling skill under the same agent — combine with backlog-populator for end-to-end coverage
- [`risk-register-builder`](../risk-register-builder/SKILL.md) — sibling skill under the same agent — combine with risk-register-builder for end-to-end coverage
