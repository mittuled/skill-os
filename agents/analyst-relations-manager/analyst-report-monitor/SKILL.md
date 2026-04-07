---
name: analyst-report-monitor
description: >
  Monitors analyst publications for positioning shifts and competitive intelligence that should shape go-to-market strategy.
  Use when a major analyst firm publishes a new report, market guide, or evaluation in the company's category.
  Also consider when competitor coverage spikes or sales encounters prospects citing analyst research in active deals.
  Suggest when quarterly analyst landscape reviews are due or when no internal intelligence brief has been produced in the last 30 days.
department: marketing
agent: analyst-relations-manager
version: 1.0.0
complexity: medium
related-skills: []
---

# analyst-report-monitor

## Agent: Analyst Relations Manager

L2 analyst relations manager responsible for analyst briefings, inquiry responses, Magic Quadrant strategy, and peer review platform management.

Department ethos: [ideal-marketing.md](../../../departments/marketing/ideal-marketing.md)

## Skill Description

Monitors analyst reports for mentions, positioning changes, and competitive intelligence, transforming analyst research into actionable insights for marketing, sales, and product teams.

## When to Use

- A major analyst firm publishes a new report, market guide, or evaluation in the company's category.
- Competitors receive new analyst coverage that could shift buyer perceptions or influence active deals.
- Sales encounters prospects citing analyst research during the evaluation process and needs counter-positioning.
- Quarterly analyst landscape reviews are due to keep leadership informed of positioning trends.

## Workflow

1. Maintain a monitoring list of analyst firms tiered per the coverage model in [`references/framework.md`](references/framework.md). Configure alert keywords across company mentions, competitor mentions, and category definition keywords. Set review SLAs per firm tier.
2. Set up alerts for new publications using the keyword sets and alert channel configuration in [`references/framework.md`](references/framework.md). Confirm alert triggers for negative positioning and new evaluation cycle announcements.
3. Review each relevant publication within the SLA for its tier: extract company positioning, strengths, cautions, and competitor comparisons using the report evaluation criteria in [`references/framework.md`](references/framework.md). Complete the Company Positioning and Competitive Landscape sections of [`assets/analyst-report-tracking-template.md`](assets/analyst-report-tracking-template.md).
4. Categorise findings by impact using the alert configuration trigger types in [`references/framework.md`](references/framework.md): direct company mention, competitive positioning shift, market definition change, or emerging trend.
5. Draft an internal intelligence brief for each high-impact publication using [`assets/analyst-report-tracking-template.md`](assets/analyst-report-tracking-template.md). Include sales talking points from Section 7 and prioritised recommended actions.
6. Distribute briefs to the relevant teams per the audience column in the internal intelligence brief structure in [`references/framework.md`](references/framework.md). Activate the relevant response protocol for each finding type.
7. Update the competitive positioning tracker with all fields from the tracker schema in [`references/framework.md`](references/framework.md).
8. Compile a quarterly analyst landscape summary using the quarterly summary section structure in [`references/framework.md`](references/framework.md): publications reviewed, positioning trends, competitive shifts, and briefing priority recommendations.

## Anti-Patterns

- **Monitoring only reports that mention the company by name.** *Why*: The most important intelligence often comes from category definitions and competitor coverage that shapes buyer expectations before the company is even considered.
- **Distributing raw reports without an internal interpretation layer.** *Why*: Sales and product teams need actionable takeaways, not 40-page PDFs; uninterpreted reports go unread.
- **Reacting to negative coverage with defensiveness instead of strategy.** *Why*: Analyst criticism is feedback that should inform positioning adjustments and briefing priorities, not PR counter-attacks.
- **Treating monitoring as a passive activity instead of a competitive function.** *Why*: Timely intelligence enables proactive positioning shifts; delayed monitoring turns insights into stale news.

## Output

**Success artifacts:**
- Publication alert dashboard with categorised findings
- Internal intelligence briefs for high-impact publications
- Competitive positioning tracker updated with analyst perspective shifts
- Quarterly analyst landscape summary with trend analysis

**Failure reporting:**
- Flag negative company mentions or positioning downgrades within 24 hours of publication
- Escalate category redefinitions that could exclude the company to marketing and product leadership

## Related Skills

- [`analyst-briefing-scheduler`](../analyst-briefing-scheduler/SKILL.md) — Intelligence briefs from monitored reports determine which analysts need a corrective or follow-up briefing.
- [`magic-quadrant-strategy`](../magic-quadrant-strategy/SKILL.md) — New evaluation cycle announcements detected via monitoring trigger the full evaluation strategy workflow.
- [`analyst-inquiry-responder`](../analyst-inquiry-responder/SKILL.md) — Negative or inaccurate positioning discovered through monitoring may require a rapid inquiry response to correct the analyst's view.
