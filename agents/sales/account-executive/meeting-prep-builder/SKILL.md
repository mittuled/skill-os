---
name: meeting-prep-builder
description: >
  This skill builds comprehensive pre-meeting intelligence briefs with 11 sections
  for enterprise sales meetings. Use when asked to prep for a meeting, build a
  meeting brief, or prepare for a customer call. Also consider when preparing for
  QBR, renewal, or executive briefing. Suggest when calendar shows upcoming
  customer meetings without prep notes.
department: sales
agent: account-executive
version: 1.0.0
complexity: medium
related-skills:
  - ../../../sales/sales-manager/sales-competitive-intel/SKILL.md
  - ../sales-proposal-builder/SKILL.md
triggers:
  - "prep for meeting"
  - "meeting brief needed"
  - "customer meeting tomorrow"
  - "QBR preparation"
---

# meeting-prep-builder

## Agent: Account Executive

L3 account executive (Nx) responsible for sales signal synthesis, signal collection, and expansion sales motions.

Department ethos: [ideal-sales.md](../../../../departments/sales/ideal-sales.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Builds comprehensive pre-meeting intelligence briefs with 11 sections covering attendee profiles, competitive landscape, pain points, and objection prep for enterprise sales meetings.

## When to Use

- When an AE has a scheduled meeting with a prospect or customer and needs structured preparation.
- When preparing for a QBR, renewal conversation, or executive briefing that requires account-specific intelligence.
- When calendar shows upcoming customer meetings without prep notes and the AE risks going in cold.

## Workflow

1. **Account Data Pull**: Pull account data from CRM (deal stage, history, contacts, activity timeline) and company-researcher output (firmographics, recent funding, leadership changes). Cross-reference with previous meeting notes for continuity. Deliverable: raw account intelligence package.
2. **11-Section Brief Compilation**: Compile the full meeting brief across all 11 sections: company snapshot, attendee profiles, deal history, competitive landscape, recent news, pain points, value propositions, objection prep, agenda suggestion, questions to ask, and success metrics. Tailor section depth to meeting type (discovery vs demo vs negotiation vs QBR). Deliverable: complete 11-section meeting brief. See [framework.md](references/framework.md) for section structure and meeting type adaptations.
3. **Talking Points and Landmines**: Highlight 3-5 key talking points that advance the deal and flag potential landmines (unresolved support tickets, competitor mentions, budget concerns, champion sentiment shifts). Deliverable: annotated talking point list with risk flags.
4. **Cheat Sheet Creation**: Create a one-page cheat sheet for quick reference during the meeting — attendee names and roles, top 3 pain points, the single most important question to answer, and the desired next step. Deliverable: one-page meeting cheat sheet.
5. **Discovery Gap Identification**: Identify unanswered questions that require real-time discovery during the meeting. Classify by type: open (explore), closed (confirm), probing (deepen), confirming (validate). Deliverable: prioritized question list with classification.
6. **Brief Delivery**: Produce the final meeting brief using [meeting-brief-template.md](assets/meeting-brief-template.md). Attach cheat sheet as appendix. Deliverable: complete meeting prep package ready for AE review.

## Anti-Patterns

- **Generic briefs across meeting types**: Using the same depth and emphasis for a first discovery call as for a late-stage negotiation. *Why*: a discovery meeting needs heavy question prep and light competitive intel; a negotiation needs heavy objection prep and commercial terms — one-size-fits-all briefs miss the mark.
- **Stale CRM data without verification**: Pulling account data from CRM without checking last-updated timestamps or cross-referencing with recent activity. *Why*: outdated deal stages, departed contacts, or stale notes lead to embarrassing moments in-meeting and signal to the prospect that you are not paying attention.
- **Skipping the cheat sheet**: Producing a comprehensive brief but no quick-reference summary. *Why*: AEs rarely read multi-page briefs cover-to-cover before walking into a meeting — the cheat sheet is what they actually use in the room.
- **No success metric defined**: Preparing extensively but not defining what a successful meeting outcome looks like. *Why*: without a clear next-step target, the AE cannot steer the conversation toward an actionable outcome.

## Output

**On success**: Produces a complete meeting prep package containing the 11-section meeting brief, annotated talking points with landmine flags, one-page cheat sheet, and prioritized discovery question list. Delivered as a structured document for AE review before the meeting.

**On failure**: Report what blocked preparation (e.g., missing CRM data, no prior meeting notes, unknown attendees), what sections could not be completed, and what the AE should manually research before the meeting.

## Related Skills

- [`company-researcher`](../../../sales/vp-sales/company-researcher/SKILL.md) — Provides firmographic and company intelligence that feeds the company snapshot and recent news sections.
- [`decision-maker-mapper`](../../../sales/vp-sales/decision-maker-mapper/SKILL.md) — Maps organizational decision-makers that feed the attendee profiles section.
- [`sales-competitive-intel`](../../../sales/sales-manager/sales-competitive-intel/SKILL.md) — Provides battle cards and competitive positioning for the competitive landscape section.
- [`sales-proposal-builder`](../sales-proposal-builder/SKILL.md) — Downstream skill that uses meeting outcomes to construct formal proposals.
