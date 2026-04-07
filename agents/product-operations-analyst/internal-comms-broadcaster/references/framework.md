# Framework: Internal Communications Broadcasting

## Core Model

Internal release communications translate product changes into audience-specific briefings that give each team exactly what they need to support, sell, or respond to the change — no more, no less.

## Audience Segmentation

| Audience | Primary Need | Communication Goal |
|----------|-------------|-------------------|
| Support | What changed, how to handle tickets | Reduce first-response errors |
| Sales | How to position, new objection handlers | Increase deal confidence |
| Customer Success | Impact on existing customers, upsell angles | Proactive outreach readiness |
| Marketing | Key messages, timing | Campaign and content alignment |
| Engineering | Technical summary, dependencies, known issues | Incident readiness |
| Leadership | Business impact, metrics to watch | Awareness + escalation readiness |

## Message Hierarchy

Each audience briefing follows this hierarchy:
1. **What changed** (the fact): Specific, jargon-free description of the change
2. **Why it matters to them** (the relevance): Impact on their day-to-day workflow or customer conversations
3. **What they need to do** (the action): Specific actions required, with deadlines
4. **Where to get help** (the resource): Links to docs, Slack channel, or contact

Never include all information for all audiences in a single message — segment always.

## Timing Framework

| Launch Phase | Comms Type | Timing |
|---|---|---|
| T-7 days | Preview / heads-up | Sales, CS: preview for account conversations |
| T-2 days | Final briefing | All customer-facing teams: full briefing with talking points |
| T-0 (launch) | Go-live announcement | All internal teams: confirmation it's live |
| T+3 days | Signal check | PM → Support + CS: first feedback from customers |
| T+14 days | Impact update | PM → Leadership: early metrics and adoption status |

## Channel Selection

| Channel | Best For | Avoid When |
|---------|---------|-----------|
| Slack announcement | Immediate awareness, short updates | Complex information requiring reference |
| Email briefing | Detailed audience-specific briefing | Urgent same-day actions required |
| Internal wiki / Notion | Reference documentation | Time-sensitive announcements |
| All-hands or team meeting | Major releases, company-wide impact | Minor updates, routine releases |
| Loom video | Demos of new UI flows, complex features | Text-only changes, minor fixes |

## Readiness Checklist Before Broadcasting

- [ ] Support team has read documentation and can answer top 5 expected questions
- [ ] Sales has updated objection handlers (if applicable)
- [ ] CS has list of affected accounts and can proactively reach out
- [ ] Internal docs are live and linked in the announcement
- [ ] Known issues or limitations are documented (never hide them)
- [ ] Slack channel or DRI named for incoming questions
