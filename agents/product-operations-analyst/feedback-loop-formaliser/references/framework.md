# Framework: Feedback Loop Formalisation

## Core Model

A formalised feedback loop ensures every customer signal — regardless of entry channel — is captured, classified, routed to the right owner, and closed with a documented outcome. The loop has four stages: Capture → Classify → Route → Close.

## Signal Sources and Capture Methods

| Source | Signal Type | Capture Method | Cadence |
|--------|------------|----------------|---------|
| Support tickets | Bug reports, friction, missing features | Automated tagging in helpdesk | Continuous |
| NPS/CSAT surveys | Sentiment, effort score, open-text themes | Survey tool export | Weekly/Monthly |
| Sales calls | Objections, competitor mentions, feature gaps | CRM notes + call recordings | Per-deal |
| CS check-ins | Adoption blockers, success stories, churn risks | CS meeting notes | Bi-weekly |
| In-app feedback | Feature-specific friction | Microsurvey or feedback widget | On-trigger |
| Social / community | Public sentiment, feature requests | Community monitoring | Weekly |

## Classification Taxonomy

Every signal must be tagged with:
1. **Type**: Bug / UX Friction / Feature Request / Positive Signal / Churn Risk / Competitor Mention
2. **Severity**: Critical (blocks workflow) / High (significant friction) / Medium / Low
3. **Segment**: Plan tier, company size, or cohort this signal originates from
4. **Frequency**: Isolated (1 mention) / Recurring (2–4) / Systemic (5+)

Signal tagged as Systemic + Critical or Churn Risk escalates immediately to the product manager.

## Routing Rules

| Signal Type | Severity | Route To | SLA |
|-------------|---------|---------|-----|
| Bug | Critical | Engineering on-call + PM | Same day |
| Bug | High | Next sprint backlog | Within 1 week |
| Feature Request | Any | Product backlog (tagged) | Within 2 weeks review |
| Churn Risk | Any | CS + PM | Same business day |
| Positive Signal | Any | PMM + CS (for case study pipeline) | Weekly digest |
| Competitor Mention | Any | PMM | Weekly digest |

## Closure Requirements

A feedback item is closed when:
- Bug fix shipped and verified
- Feature added to roadmap with target quarter (or explicitly declined with rationale)
- Churn risk resolved or escalation documented
- Customer notified of outcome (for Systemic or high-severity items)

Never close an item by marking it "noted" without a documented action or explicit deferral decision.

## Loop Health Metrics

Track monthly to assess loop quality:
- **Capture rate**: % of feedback channels with active collection (target: 100%)
- **Classification lag**: Median hours from capture to classification (target: <24 hours)
- **Routing compliance**: % of items routed per SLA (target: >90%)
- **Closure rate**: % of items closed within 30 days (target: >80%)
- **Systemic signal-to-action rate**: % of Systemic signals that result in a backlog item (target: 100%)
