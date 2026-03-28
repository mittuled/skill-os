---
name: follow-up-sequence-builder
description: >
  This skill designs contextual follow-up sequences for 5 common sales scenarios
  with optimized cadence and messaging. Use when a prospect has engaged but not
  converted (opened email, attended webinar, downloaded content, had initial call,
  went silent). Also consider when deal stage requires re-engagement after no-show
  or ghosting. Suggest when pipeline review reveals stalled opportunities.
department: sales
agent: sales-development-rep
version: 1.0.0
complexity: medium
related-skills:
  - ../cold-outreach-builder/SKILL.md
  - ../decision-maker-mapper/SKILL.md
  - ../cohort-selector-sales/SKILL.md
  - ../../account-executive/sales-signal-collector/SKILL.md
triggers:
  - "follow up sequence needed"
  - "prospect went silent"
  - "re-engagement campaign"
  - "post-demo follow up"
---

# follow-up-sequence-builder

## Agent: Sales Development Rep

L3 sales development representative (Nx) responsible for outbound prospecting, follow-up execution, and pipeline re-engagement at target accounts.

Department ethos: [ideal-sales.md](../../../departments/sales/ideal-sales.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Designs contextual follow-up sequences for five common sales scenarios with optimized cadence, channel mix, and value-add messaging to re-engage prospects who have shown interest but not converted.

## When to Use

- When a prospect has engaged with outreach (opened emails, attended a webinar, downloaded content, or had an initial call) but has not taken the next step toward a meeting or deal progression.
- When a prospect goes silent after a demo, meeting, or proposal and needs a structured re-engagement sequence with escalating value rather than repeated "checking in" messages.
- When pipeline review surfaces stalled opportunities where the prospect showed genuine interest but the deal has not advanced in 2+ weeks.

## Workflow

1. **Scenario Classification**: Classify the follow-up scenario based on the prospect's last meaningful engagement: post-demo, post-content (downloaded resource or attended webinar), post-meeting (had a call but no next step), re-engagement (went silent after active conversation), or event follow-up (met at conference or event). Reference [framework.md](references/framework.md) for scenario definitions and cadence matrices. Deliverable: classified scenario with engagement history summary.

2. **Tone and Urgency Calibration**: Select tone and urgency level based on engagement depth and recency. Post-demo gets warm, confident tone with moderate urgency. Post-content gets educational, low-pressure tone. Post-meeting gets direct, action-oriented tone. Re-engagement gets curious, zero-pressure tone. Event follow-up gets warm, personal tone. Deliverable: tone and urgency settings with rationale.

3. **Sequence Construction**: Build a 3-5 touch sequence where each touch adds new value rather than restating the previous message. Structure the arc: Touch 1 (acknowledge + new value), Touch 2 (different angle + social proof), Touch 3 (address likely objection), Touch 4 (final value offer or escalation), optional Touch 5 (graceful close). Each touch must answer the prospect's implicit question: "Why should I respond now?" Deliverable: sequenced touchpoints with message drafts.

4. **Cadence Matrix Application**: Apply the scenario-specific cadence from [framework.md](references/framework.md) to determine days between touches and channel rotation. Post-demo: Day 0/1/3/7/14. Post-content: Day 0/3/7. Post-meeting: Day 0/2/5/10. Re-engagement: Day 0/7/21/45. Event follow-up: Day 0/1/3/7. Adjust for prospect seniority and deal size. Deliverable: cadence calendar with channel assignments per touch.

5. **Exit Criteria Definition**: Define when to stop following up and either archive the prospect, downgrade to a nurture track, or escalate to the AE for a different approach. Set explicit thresholds: maximum touches without response, time elapsed since last engagement, and signals that indicate the prospect has churned (job change, competitor announcement). Deliverable: exit criteria with escalation path.

6. **[GATE] Sequence Compilation**: Compile the complete follow-up sequence using [follow-up-sequence-template.md](assets/follow-up-sequence-template.md). Review with the assigned AE before deployment, especially for post-demo and re-engagement scenarios where deal context is critical. Deliverable: completed follow-up sequence document.

## Anti-Patterns

- **"Just checking in" syndrome**: Sending follow-ups that add no new value and rely on the prospect's goodwill to respond. *Why*: every message without new value trains the prospect to ignore you — each empty follow-up makes the next one less likely to get a response.

- **Identical cadence for all scenarios**: Using the same timing and touch count whether following up after a demo or re-engaging a cold prospect. *Why*: a post-demo prospect expects quick follow-up (Day 0-1) while a re-engagement prospect needs wider spacing (Day 7-21) to avoid feeling harassed — mismatched cadence signals you are on autopilot.

- **Escalating pressure instead of value**: Increasing urgency ("I have not heard back", "time is running out") without providing new information or resources. *Why*: artificial urgency without new value creates resentment — the prospect did not respond because they lacked a reason to, not because they forgot.

- **Skipping the exit**: Following up indefinitely without a defined stopping point. *Why*: unbounded sequences damage domain reputation, consume SDR time on dead leads, and make the company look desperate — a clean exit preserves the relationship for future re-engagement.

## Output

**On success**: Produces a completed follow-up sequence document following [follow-up-sequence-template.md](assets/follow-up-sequence-template.md) containing scenario classification, engagement history, sequenced touchpoints with message drafts, cadence calendar, exit criteria, and escalation path. Delivered to the SDR or AE for execution.

**On failure**: Report what prevented sequence creation (e.g., insufficient engagement history to classify the scenario, unclear deal stage, no CRM data on prior interactions), what was partially completed, and recommended next steps such as requesting engagement history from the AE or defaulting to the re-engagement scenario as a safe fallback.

## Related Skills

- [`cold-outreach-builder`](../cold-outreach-builder/SKILL.md) — Produces the initial cold sequences that follow-up sequences extend when prospects engage but do not convert.
- [`decision-maker-mapper`](../decision-maker-mapper/SKILL.md) — Informs follow-up strategy when the stall is caused by single-threaded engagement and additional stakeholders need to be contacted.
- [`cohort-selector-sales`](../cohort-selector-sales/SKILL.md) — Receives prospects who exit follow-up sequences without converting for potential re-inclusion in future cohorts.
- [`sales-signal-collector`](../../account-executive/sales-signal-collector/SKILL.md) — Provides engagement signals that determine the correct follow-up scenario and inform personalization.
