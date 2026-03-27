---
name: roadmap-placer
description: >
  This skill places approved features and initiatives onto the product roadmap with timing,
  sequencing rationale, and dependency mapping. Use when asked to schedule a feature for a
  specific quarter, re-sequence roadmap items, or resolve conflicts between competing initiatives.
  Also consider when capacity changes or a new strategic priority forces roadmap reshuffling.
  Suggest when the user is about to commit engineering resources without confirming roadmap fit.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "place this on the roadmap"
  - "schedule this feature for next quarter"
  - "re-sequence the roadmap"
  - "where does this fit on the roadmap"
---

# roadmap-placer

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)

## Skill Description
Places approved features and initiatives on the product roadmap with timing, sequencing rationale, and dependency awareness.

## When to Use
- When a feature has been approved and needs a concrete roadmap slot with timing, dependencies, and capacity validation
- When a strategic shift, customer escalation, or capacity change requires re-sequencing existing roadmap items
- When multiple teams are requesting the same quarter and trade-off decisions need a documented rationale visible to all stakeholders

## Workflow
1. **Assess placement inputs**: Gather the initiative's priority score, estimated effort, team dependencies, and any hard deadlines (contractual, regulatory, event-driven). Review current roadmap utilisation for the target time horizon. Deliverable: placement brief listing initiative, priority, effort estimate, dependencies, and constraints.
2. **Identify candidate slots**: Map available capacity windows across the relevant teams for the next 2-4 quarters. Flag conflicts where the candidate initiative overlaps with already-committed work or shared dependencies. Deliverable: candidate slot options (2-3) with trade-off notes for each.
3. **Evaluate sequencing trade-offs**: For each candidate slot, assess downstream effects — what gets delayed, what unlocks, and how stakeholder commitments are affected. Score each option against strategic alignment, dependency risk, and team morale. Deliverable: trade-off matrix comparing slot options on 3-4 criteria.
4. **Place and document rationale**: Select the slot, record the "why" behind the placement decision (not just the "what"), and update the roadmap artefact. Link to the initiative brief, priority score, and any stakeholder agreements. Deliverable: updated roadmap entry with placement rationale, linked dependencies, and review date.
5. **Communicate placement**: Notify affected teams, stakeholders, and downstream consumers of the placement decision and any resulting schedule shifts. Deliverable: placement announcement with change summary and escalation path for objections.

## Anti-Patterns
- **Silent reshuffling**: Moving roadmap items without documenting the reason or notifying affected teams. *Why*: Undocumented changes erode trust in the roadmap as a planning tool and create misalignment between teams that only surfaces during delivery.
- **Date-first placement**: Assigning a ship date before validating capacity, dependencies, and effort estimates. *Why*: Date-driven placement produces commitments the team cannot keep, leading to crunch, quality cuts, or missed deadlines that damage credibility.
- **Perpetual "next quarter"**: Repeatedly deferring an initiative without explicitly deprioritising or cancelling it. *Why*: Zombie roadmap items consume planning energy every cycle and signal to stakeholders that the roadmap is aspirational fiction rather than a delivery plan.

## Output
**On success**: An updated roadmap entry containing the initiative name, assigned time slot, sequencing rationale, linked dependencies, effort estimate, and review date — formatted for the team's roadmap tool or as a markdown table row. Accompanied by a change summary distributed to affected stakeholders.

**On failure**: Report which inputs prevented placement (missing effort estimates, unresolved dependency conflicts, capacity data unavailable), which slot options were evaluated and why each was rejected, and recommend specific actions to unblock placement.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
