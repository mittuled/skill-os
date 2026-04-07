---
name: board-materials-coordinator
description: >
  This skill coordinates the preparation and distribution of board meeting materials.
  Use when asked to prepare the board deck, coordinate section owners for board materials,
  or manage the board meeting logistics. Also consider when a board meeting is scheduled
  without a preparation timeline. Suggest when the user has a board meeting within 3
  weeks and no preparation has started.
department: finance
agent: investor-relations-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../../../finance/fpa-analyst/board-financial-pack/SKILL.md
  - ../monthly-investor-update/SKILL.md
---

# board-materials-coordinator

## Agent: Investor Relations Manager

L2 investor relations manager (1x) responsible for investor updates, board materials, cap table management, fundraising process, and data room.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Coordinates the preparation and distribution of board meeting materials by managing the content calendar, collecting section inputs from department leads, and ensuring timely delivery to directors.

## When to Use

- When a board meeting is scheduled and materials preparation needs to begin (typically 3 weeks before the meeting).
- When the board requests ad-hoc materials (strategy deep-dives, M&A analysis, market reviews) outside the regular cadence.
- When the company is establishing its first board and needs to define the board pack structure and process.

## Workflow

1. **Agenda and Timeline Setting**: Confirm the board agenda with the CEO and board chair. Define the content sections, assign owners, and set internal deadlines (first draft 10 days before, final 3 days before). Deliverable: board prep timeline with section ownership.
2. **Content Collection**: Collect section drafts from each owner (CEO strategic update, CFO financials, CPO product update, CTO engineering update). Review for completeness, consistency, and appropriate level of detail. Deliverable: consolidated draft board deck.
3. **Quality Review**: Review the full deck for narrative coherence, data consistency across sections, and appropriate level of detail for board consumption. Ensure financials tie to the FP&A-approved numbers. Deliverable: reviewed and corrected board deck.
4. **Pre-Read Distribution**: Distribute final materials to board members at least 48 hours before the meeting (72 hours preferred). Include the agenda, deck, and any supplementary materials. Deliverable: distributed board package with read receipts.
5. **Post-Meeting Follow-Up**: Document board decisions, action items, and follow-up requests. Distribute minutes within 48 hours. Track action item completion. Deliverable: board minutes and action item tracker.

## Anti-Patterns

- **Last-minute distribution**: Sending board materials the night before or day of the meeting. *Why*: directors who cannot review materials in advance cannot provide informed guidance; the meeting becomes a presentation rather than a strategic discussion.
- **Inconsistent structure**: Changing the board deck structure and metrics every meeting. *Why*: directors track trends across meetings; inconsistent structure forces them to re-orient each time and prevents pattern recognition.
- **Missing the "so what"**: Presenting data without recommendations or decisions requested. *Why*: board meetings are expensive in terms of director attention; every slide should drive toward a decision, approval, or strategic input.

## Output

**On success**: Produces a complete board package including the deck, pre-read materials, and post-meeting minutes with action items. Delivered per the preparation timeline.

**On failure**: Report which sections are incomplete, what partial materials can be distributed, and whether the meeting should be rescheduled. Escalate to the CEO if material sections are missing.

## Related Skills

- [`board-financial-pack`](../../../finance/fpa-analyst/board-financial-pack/SKILL.md) -- Provides the financial section that is the core of the board materials.
- [`monthly-investor-update`](../monthly-investor-update/SKILL.md) -- Shares content themes but at a different depth and cadence.
