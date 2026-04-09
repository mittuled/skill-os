---
name: phase-scope-adjuster
description: >
  This skill adjusts product scope mid-phase in response to discoveries, capacity changes, or
  shifting priorities. Use when asked to cut scope, reprioritize within a phase, or respond to a
  new constraint without resetting the entire plan. Also consider when velocity data shows the
  current scope will not land on time. Suggest when the team is halfway through a phase and new
  information has materially changed what should ship.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "adjust phase scope"
  - "scope adjustment"
  - "phase scope change"
  - "resize phase scope"
  - "revise phase scope"
---

# phase-scope-adjuster

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Adjusts product scope mid-phase in response to discoveries, capacity changes, or shifting priorities while preserving the phase's core value commitment.

## When to Use
- When mid-phase discoveries (technical blockers, user research findings, competitive moves) invalidate part of the planned scope
- When team capacity drops unexpectedly (attrition, reassignment, illness) and the current scope cannot land on time
- When a stakeholder introduces a new priority that competes for the same phase's resources and requires an explicit trade-off decision

## Workflow
1. **Diagnose the trigger**: Identify what changed -- new information, capacity loss, priority shift, or timeline compression. Quantify the impact (e.g., "lost 30% of engineering capacity for 3 sprints" or "user research invalidated assumption X"). Deliverable: one-paragraph change summary with quantified impact.
2. **Reassess the value stack**: Re-rank remaining scope items by their contribution to the phase's exit criteria and the initiative's success metrics. Separate must-haves (required for the phase to deliver value) from should-haves and nice-to-haves. Deliverable: updated priority stack with value justification per item.
3. **Model scope options**: Create 2-3 scope scenarios (e.g., "cut feature Y, keep Z" vs. "simplify feature Y, defer Z to next phase"). For each scenario, state what ships, what is deferred, and the impact on exit criteria and timeline. Deliverable: scope options table with trade-off analysis.
4. **Recommend and decide**: Present options to the decision-maker (typically the product lead or initiative owner) with a clear recommendation. State which option best preserves the phase's core value given the constraint. Deliverable: decision record documenting the chosen option and rationale.
5. **Update downstream artifacts**: Revise the phase plan, milestone definitions, backlog, and any stakeholder communications to reflect the new scope. Flag deferred items for the next phase's intake. Deliverable: updated phase plan and backlog with deferred items tagged.

## Anti-Patterns
- **Silent scope creep in reverse**: Quietly dropping items from the backlog without communicating to stakeholders. *Why*: Undisclosed cuts erode trust and surface as surprises at phase review, when recovery options are gone.
- **Across-the-board trimming**: Reducing every feature by 20% instead of making hard cuts. *Why*: Uniform trimming produces a mediocre version of everything rather than a complete version of the most valuable items; users get half-baked experiences.
- **Scope adjustment without root cause**: Cutting scope to meet a deadline without understanding why the plan was wrong. *Why*: The same estimation or scoping error repeats in the next phase; the team is perpetually behind.
- **Deferral without a landing zone**: Moving items to "next phase" without confirming that phase has capacity or that the items still matter. *Why*: The deferred backlog becomes a graveyard of stale items that clutter future planning.

## Output
**On success**: A scope adjustment package containing the change summary, updated priority stack, scope options with trade-off analysis, decision record, and revised phase plan -- formatted for stakeholder review and backlog tool updates.

**On failure**: Report which trade-offs could not be resolved (conflicting stakeholder priorities, insufficient data to rank options, unclear exit criteria), what was attempted, and recommend specific escalation paths or data gathering to unblock the decision.

## Related Skills
- (none yet -- cross-references added in Phase 1.6)
