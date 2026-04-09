---
name: investor-comms-drafter
description: >
  This skill drafts investor communications including updates, announcements, and
  ad hoc correspondence. Use when asked to write an investor update, draft a funding
  announcement, or compose investor correspondence. Also consider when a material
  event occurs that investors should know about. Suggest when the user is communicating
  with investors without a consistent format or cadence.
department: finance
agent: investor-relations-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../monthly-investor-update/SKILL.md
  - ../board-materials-coordinator/SKILL.md
  - ../investor-pipeline-manager/SKILL.md
---

# investor-comms-drafter

## Agent: Investor Relations Manager

L2 investor relations manager (1x) responsible for investor updates, board materials, cap table management, fundraising process, and data room.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)

## Skill Description

Drafts investor communications including monthly updates, milestone announcements, asks for help, and ad hoc correspondence to maintain strong investor relationships and consistent information flow.

## When to Use

- When the monthly or quarterly investor update cycle arrives and the update needs to be drafted.
- When a material event occurs (key hire, product launch, partnership, pivot) that warrants proactive investor communication.
- When an investor requests specific information and a formal response needs to be prepared.

## Workflow

1. **Content Gathering**: Collect inputs from across the company: key metrics, product milestones, team changes, financial highlights, and asks (introductions, hiring referrals, advice). Deliverable: content brief with raw inputs from each department.
2. **Narrative Drafting**: Write the communication in the established format and tone. Lead with the most important update. Include metrics with context (direction, why it changed). Keep the ask section specific and actionable. Deliverable: draft communication.
3. **Review Cycle**: Route the draft to the CEO for tone and strategic alignment. Incorporate feedback. Verify all numbers against source data. Deliverable: approved final draft.
4. **Distribution**: Send via the established channel (email, investor portal). Track opens and replies. Follow up on specific asks within one week. Deliverable: sent communication with engagement tracking.

## Anti-Patterns

- **Metrics without context**: Reporting numbers without explaining what drove them or what they mean for the business trajectory. *Why*: investors need narrative context to interpret metrics; raw numbers without explanation invite incorrect assumptions.
- **Only good news**: Omitting challenges or misses from investor updates. *Why*: investors expect transparency; sugarcoating erodes trust and prevents investors from helping where they could add value.
- **Irregular cadence**: Sending updates only when there is good news to share. *Why*: inconsistent communication signals that bad months are being hidden; a regular cadence builds trust regardless of content.

## Output

**On success**: Produces a polished investor communication in the established format with verified metrics, strategic context, and specific asks. Delivered per the communication cadence.

**On failure**: Report which inputs could not be gathered, which sections are incomplete, and the recommended timeline for completing the communication. Escalate to CEO if the delay exceeds the standard cadence.

## Related Skills

- [`monthly-investor-update`](../monthly-investor-update/SKILL.md) -- The monthly update is the most frequent communication this skill produces.
- [`board-materials-coordinator`](../board-materials-coordinator/SKILL.md) -- Board materials share content with investor communications and must be consistent.
