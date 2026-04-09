---
name: fundraising-process-manager
description: >
  This skill manages the fundraising process including investor pipeline, diligence
  coordination, and term sheet negotiation support. Use when asked to run a fundraise,
  manage investor outreach, or coordinate due diligence. Also consider when the company
  is 6 months from needing capital and should begin fundraising preparation. Suggest
  when the user is approaching investors without a structured process.
department: finance
agent: investor-relations-manager
version: 1.0.0
complexity: complex
related-skills:
  - ../data-room-builder/SKILL.md
  - ../../../finance/cfo-vp-finance/pitch-narrator-finance/SKILL.md
  - ../cap-table-manager/SKILL.md
  - ../investor-pipeline-manager/SKILL.md
  - ../data-room-v1-builder/SKILL.md
  - ../due-diligence-coordinator/SKILL.md
  - ../data-room-manager/SKILL.md
  - ../secondary-market-manager/SKILL.md
triggers:
  - "manage fundraising process"
  - "run the fundraise"
  - "fundraising process"
  - "manage investor outreach"
  - "lead fundraising"
---

# fundraising-process-manager

## Agent: Investor Relations Manager

L2 investor relations manager (1x) responsible for investor updates, board materials, cap table management, fundraising process, and data room.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)

## Skill Description

Manages the end-to-end fundraising process including investor targeting, pipeline management, meeting coordination, diligence facilitation, and term sheet negotiation support to close the round efficiently.

## When to Use

- When the company decides to raise a funding round and needs to execute a structured fundraising process.
- When investor interest is inbound and needs to be channelled into a managed process rather than ad-hoc conversations.
- When the current round is stalling and the process needs to be reset or restructured.

## Workflow

1. **Process Design**: Define the fundraising timeline, target raise amount, valuation range, and investor profile (stage, sector, check size, value-add). Set milestones for each phase (preparation, outreach, meetings, diligence, close). Deliverable: fundraising process plan with timeline.
2. **Investor Targeting**: Build the target investor list with research on each firm's thesis, portfolio, recent investments, and partner assignments. Prioritize by fit and likelihood to lead. Identify warm introduction paths. Deliverable: tiered investor target list with introduction strategy.
3. **Pipeline Management**: Track every investor interaction in a CRM or tracker: outreach date, meeting stage, feedback received, next steps, and decision timeline. Maintain weekly pipeline reviews with the CEO. Deliverable: investor pipeline tracker with weekly status.
4. **Meeting Coordination**: Schedule and prepare for investor meetings. Brief the CEO on each investor's background, portfolio, and likely questions. Debrief after each meeting to capture feedback and adjust the pitch. Deliverable: meeting briefs and debrief notes.
5. **Diligence Coordination**: When an investor enters diligence, coordinate the data room access, schedule reference calls, and manage the diligence request list. Track response times and ensure no request goes unanswered for more than 48 hours. Deliverable: diligence tracker with response log.
6. **Term Sheet Management**: When term sheets arrive, compile a comparison matrix covering valuation, liquidation preferences, board composition, protective provisions, and other key terms. Support the CEO and counsel in negotiation. Deliverable: term sheet comparison matrix.
7. **Closing Coordination**: Coordinate signing and closing logistics with legal counsel, transfer agent, and banking. Ensure all closing conditions are met and funds are wired. Update the cap table. Deliverable: closing checklist with confirmation of fund receipt.

## Anti-Patterns

- **Sequential investor outreach**: Meeting investors one at a time rather than creating a compressed, parallel process. *Why*: sequential outreach kills competitive tension and gives investors unlimited time to wait; a compressed process with multiple conversations creates urgency.
- **No debrief loop**: Meeting investors without systematically capturing feedback and iterating the pitch. *Why*: the first 5 meetings are effectively practice rounds; without a debrief loop, the pitch does not improve and the best investors may be burned early.
- **Neglecting existing investors**: Focusing entirely on new investor outreach without keeping existing investors informed and engaged. *Why*: existing investors are the most likely to provide warm introductions and may want to participate; keeping them in the dark risks losing their support.
- **Sharing the data room too early**: Granting data room access before an investor has expressed serious interest and entered a structured diligence process. *Why*: premature data room access provides information without commitment and can leak competitive intelligence.

## Output

**On success**: Produces a closed funding round with signed documents, wired funds, updated cap table, and investor pipeline documentation. Delivered per the fundraising timeline.

**On failure**: Report the current pipeline status, which investors passed and why, what feedback patterns emerged, and recommended adjustments to the process, materials, or terms. Include a revised timeline or recommendation to pause.

## Related Skills

- [`data-room-builder`](../data-room-builder/SKILL.md) -- Builds the data room that supports investor diligence during the fundraise.
- [`pitch-narrator-finance`](../../../finance/cfo-vp-finance/pitch-narrator-finance/SKILL.md) -- Crafts the financial narrative used in investor meetings.
