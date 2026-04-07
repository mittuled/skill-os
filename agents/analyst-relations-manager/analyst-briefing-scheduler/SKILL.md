---
name: analyst-briefing-scheduler
description: >
  Schedules and prepares analyst briefings that shape how Gartner, Forrester, and peers perceive and position the company.
  Use when a major product launch, strategy shift, or evaluation cycle requires communicating with analysts before market release.
  Also consider when a new analyst covers the category and needs an introductory briefing.
  Suggest when quarterly briefing cadences are overdue or the company has not briefed a Tier 1 analyst in 90+ days.
department: marketing
agent: analyst-relations-manager
version: 1.0.0
complexity: medium
related-skills: []
---

# analyst-briefing-scheduler

## Agent: Analyst Relations Manager

L2 analyst relations manager responsible for analyst briefings, inquiry responses, Magic Quadrant strategy, and peer review platform management.

Department ethos: [ideal-marketing.md](../../../departments/marketing/ideal-marketing.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Schedules and prepares analyst briefings with Gartner, Forrester, and other relevant firms, ensuring every interaction advances the company's positioning in analyst research and evaluations.

## When to Use

- A major product launch, acquisition, or strategy shift needs communicating to analysts before it hits the market.
- An analyst evaluation cycle is approaching and the company must update its narrative and proof points.
- A new analyst covers the category and needs an introductory briefing to build the relationship.
- Quarterly or semi-annual briefing cadences are due to maintain ongoing analyst relationships.

## Workflow

1. Identify the briefing objective and type (introductory, strategy, product, evaluation, or emergency) using the briefing type table in [`references/framework.md`](references/framework.md). Map the objective to the specific analysts who influence the category based on their tier assignment.
2. Coordinate scheduling with analyst firms through their booking systems per the firm-specific methods in [`references/framework.md`](references/framework.md). Propose multiple time slots and confirm attendees from the company side. Maintain briefing frequency cadence per analyst tier.
3. Research the analyst's recent publications, stated positions, and known biases using the Step 1 research protocol in [`references/framework.md`](references/framework.md). Complete the Analyst Profile section of [`assets/analyst-briefing-brief-template.md`](assets/analyst-briefing-brief-template.md).
4. Draft the briefing deck using the deck construction section in [`references/framework.md`](references/framework.md). Complete the Key Messages and Customer Proof Points sections of the briefing brief template. Limit to 12 slides; every claim must have a source.
5. Prepare the internal speakers using the speaker preparation timeline in [`references/framework.md`](references/framework.md). Deliver the completed [`assets/analyst-briefing-brief-template.md`](assets/analyst-briefing-brief-template.md) 5 days before the briefing. Conduct dry run for all Tier 1 evaluation briefings.
6. Confirm logistics: video platform, dial-in details, NDA status, and materials to share before or after the briefing. Complete Section 8 of the briefing brief.
7. Conduct the briefing: lead with the narrative, support with data and customer evidence, leave time for analyst questions, and record all follow-up commitments in the Anticipated Questions section.
8. Send a follow-up within 48 hours per the post-briefing protocol in [`references/framework.md`](references/framework.md): thank-you note, any promised materials, and a summary of key discussion points. Update the AR tracker with all fields from the tracker record section.

## Anti-Patterns

- **Treating briefings as product demos instead of strategic conversations.** *Why*: Analysts evaluate market positioning and strategy, not feature checklists; demo-heavy briefings waste the opportunity to shape perception.
- **Scheduling briefings reactively only before evaluations.** *Why*: Analysts form opinions continuously; companies that only engage during evaluation cycles appear transactional and miss opportunities to influence ongoing research.
- **Sending unprepared speakers who contradict each other.** *Why*: Inconsistent messaging signals strategic confusion and erodes analyst confidence in the company's execution ability.
- **Skipping follow-up on commitments made during the briefing.** *Why*: Analysts track whether companies deliver on promises; broken follow-ups damage credibility for future interactions.

## Output

**Success artifacts:**
- Briefing schedule with analyst names, dates, and objectives
- Tailored briefing decks per analyst with key messages and proof points
- Speaker prep documents with analyst background and likely questions
- Post-briefing follow-up emails with committed materials delivered

**Failure reporting:**
- Flag scheduling conflicts or analyst cancellations within 24 hours
- Escalate situations where internal speakers are unavailable for high-priority briefings to marketing leadership

## Related Skills

- [`analyst-inquiry-responder`](../analyst-inquiry-responder/SKILL.md) — Briefings generate follow-up inquiries; use this skill to respond to analyst requests arising from briefing discussions.
- [`analyst-report-monitor`](../analyst-report-monitor/SKILL.md) — Reports published by briefed analysts require monitoring to assess whether briefings influenced the published narrative.
- [`magic-quadrant-strategy`](../magic-quadrant-strategy/SKILL.md) — Evaluation briefings are a critical component of the Magic Quadrant submission process managed by this skill.
