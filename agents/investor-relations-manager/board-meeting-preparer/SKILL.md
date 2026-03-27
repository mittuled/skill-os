---
name: board-meeting-preparer
description: >
  This skill prepares board meeting materials and logistics. Use when asked to
  organize a board meeting, prepare board decks, or coordinate board
  communications. Also consider when a board meeting is approaching without
  preparation. Suggest when the user has scheduled a board meeting but not
  started materials preparation.
department: finance
agent: investor-relations-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../board-materials-coordinator/SKILL.md
  - ../monthly-investor-update/SKILL.md
---

# board-meeting-preparer

## Agent: Investor Relations Manager

L2 investor relations manager (1x) responsible for investor updates, board materials, cap table management, fundraising process, and data room.

Department ethos: [ideal-finance.md](../../../departments/finance/ideal-finance.md)

## Skill Description

Prepares board meeting materials, coordinates logistics, and ensures all pre-meeting deliverables are complete so board meetings run efficiently with informed directors.

## When to Use

- When a quarterly or special board meeting is approaching and materials need to be assembled and distributed to directors.
- When the CEO or CFO needs help organizing the board meeting agenda, collecting department updates, and preparing the board deck.
- When a material event (fundraising, acquisition, pivot) requires a special board session with focused preparation.

## Workflow

1. **Timeline and Agenda**: Establish the meeting date, confirm director availability, and draft the agenda with the CEO. Identify required materials for each agenda item. Set deadlines for material submissions from department leads. Deliverable: board meeting timeline with agenda and material deadlines.
2. **Material Collection**: Collect inputs from each department: financial package from CFO, product update from CPO, engineering update from CTO, go-to-market update from CBO. Chase overdue submissions. Deliverable: raw materials from all departments.
3. **Deck Assembly**: Assemble the board deck with consistent formatting: executive summary, KPI dashboard, financial review, department updates, strategic discussion topics, and consent items. Ensure data accuracy and narrative coherence. Deliverable: draft board deck.
4. **Pre-Read Distribution**: Distribute the board deck and supporting materials (financial statements, cap table, metrics dashboard) to directors at least 5 business days before the meeting. Include a cover note highlighting key discussion topics. Deliverable: distributed pre-read package.
5. **Meeting Logistics**: Confirm meeting logistics (video link, room booking, dial-in), prepare consent resolutions for routine items, and brief the CEO on anticipated questions or discussion points. Deliverable: logistics confirmation and CEO briefing notes.

## Anti-Patterns

- **Late material distribution**: Sending board materials less than 3 days before the meeting. *Why*: directors cannot prepare adequately, leading to surface-level discussion and deferred decisions that require follow-up meetings.
- **Data inconsistency across slides**: Presenting different numbers for the same metric in different sections of the board deck. *Why*: inconsistent data erodes board confidence in management's command of the business and triggers time-consuming reconciliation discussions.
- **No pre-meeting CEO briefing**: Sending the CEO into the board meeting without previewing likely questions or contentious topics. *Why*: unprepared responses to board concerns damage credibility and can lead to governance complications.

## Output

**On success**: Produces a complete board meeting package: agenda, board deck, financial statements, consent resolutions, and logistics confirmation. Delivered to directors 5+ business days before the meeting.

**On failure**: Report which materials are incomplete (e.g., missing department updates, unfinished financials), what partial package can be sent, and a revised timeline. Escalate to CFO if the meeting may need rescheduling.

## Related Skills

- [`board-materials-coordinator`](../board-materials-coordinator/SKILL.md) -- Coordinates the ongoing production of board materials that feed into meeting preparation.
- [`monthly-investor-update`](../monthly-investor-update/SKILL.md) -- Monthly updates provide the data and narrative foundation for quarterly board materials.
