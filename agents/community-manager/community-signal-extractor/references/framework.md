# Framework: community-signal-extractor

Defines the signal taxonomy, source inventory model, severity classification, and routing protocols for extracting actionable signals from community conversations.

## Signal Taxonomy

| Category | Definition | Subcategories | Priority |
|----------|-----------|--------------|---------|
| Feature Request | Member asks for a capability that does not exist | Enhancement, New feature, Integration | High |
| Pain Point | Friction with existing product or experience | Bug, UX issue, Performance, Documentation gap | Critical |
| Use Case Discovery | Novel or unexpected way member uses product | Confirmed workaround, Creative application | High |
| Competitive Intelligence | Mentions of competitor products or comparisons | Feature comparison, Pricing comparison, Switching intent | High |
| Praise Signal | Positive sentiment about specific product area | Feature praise, Outcome celebration, Referral intent | Medium |
| Churn Indicator | Language suggesting disengagement or departure | Frustration, Unmet expectation, Cancellation intent | Critical |
| Content Gap | Member unable to find information they need | Missing docs, Outdated guide, Unclear error message | High |
| Community Health Signal | Signal about the community experience itself | Moderation issue, Onboarding friction, Response time complaint | Medium |

## Signal Severity Scale

| Severity | Definition | Response SLA |
|----------|-----------|-------------|
| P0 — Critical | Churn indicator or product-breaking bug reported by 3+ members | Same day routing to product/support |
| P1 — High | Pain point reported by 5+ unique members in 30 days, or competitive threat with switching intent | 48-hour routing |
| P2 — Medium | Feature request or use case discovered by 2–4 members | Weekly synthesis |
| P3 — Low | Single praise signal or isolated content gap | Monthly synthesis |

## Source Inventory Model

| Source Type | Signal Quality | Volume | Access Method | Update Frequency |
|------------|--------------|--------|--------------|-----------------|
| Community forums (public channels) | High | High | Platform export or manual review | Daily |
| Direct messages (with consent) | Very high | Low | Manual review with member consent | Weekly |
| Event Q&A and feedback forms | High | Medium | Event platform export | Per event |
| Social media mentions | Medium | Variable | Social listening tool | Daily |
| Support ticket tags | High | High | Helpdesk export | Weekly |
| User interview notes | Very high | Low | CRM or notes tool | Per interview |
| Survey open-text responses | High | Medium | Survey tool export | Per survey |

## Signal Extraction Workflow

### Tagging Protocol

Each extracted signal must include:

| Field | Values | Required? |
|-------|--------|----------|
| Category | From taxonomy above | Yes |
| Severity | P0–P3 | Yes |
| Source | Channel/forum/event name | Yes |
| Date | YYYY-MM-DD | Yes |
| Member ID | Anonymized or consented | Yes |
| Member Segment | Power user / new / churned / enterprise | Yes |
| Product Area | [Product-specific] | Yes |
| Frequency | Number of unique members raising same signal | Yes |
| Verbatim quote | Exact member language (1–2 sentences) | Yes |

### Clustering Method

1. Group signals with > 60% semantic overlap into a theme
2. Name theme after the underlying need, not the symptom
3. Quantify theme: count of unique members + severity distribution
4. Correlate with product events: releases, outages, pricing changes

## Signal Routing Matrix

| Signal Category | Primary Recipient | Secondary Recipient | Expected Action |
|----------------|------------------|---------------------|----------------|
| Feature Request | Product Manager | Engineering | Added to backlog with community vote count |
| Pain Point (bug) | Engineering | Support | Bug ticket opened |
| Pain Point (UX/docs) | Product Designer / Tech Writer | PM | Improvement ticket opened |
| Competitive Intel | PMM | Sales | Competitive brief updated |
| Churn Indicator | Customer Success | Product | At-risk member outreach |
| Content Gap | Technical Writer | DevRel | Documentation task created |
| Community Health | Community Manager | Community Lead | Health intervention triggered |

## Closing the Loop

After routing signals, close the loop with the community within:

| Action Taken | Community Communication |
|-------------|------------------------|
| Feature shipped | "You asked, we built" announcement with attribution |
| Bug fixed | Direct reply to original thread with resolution |
| Feature deferred | Transparent post explaining prioritization decision |
| Content updated | Reply to original thread with link to updated docs |

**Why this matters**: Communities where signals visibly lead to action generate 3–5x more signal volume than communities where feedback disappears.
