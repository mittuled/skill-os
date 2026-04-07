# Retention Email Sequence Plan: InsightHub Analytics Platform

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026-03-29 |
| Author | Lifecycle Email Marketing Manager |
| Version | 1.0 |
| Status | Draft |
| Skill | retention-email-designer |

## Executive Summary

Retention sequence targeting 45 mid-market InsightHub accounts showing declining usage, representing ~$180K MRR at risk. Five-email sequence across three intervention tiers with escalation to CS for enterprise accounts. Target: recover 25% of at-risk accounts to healthy engagement within 30 days.

## Churn Risk Signals

| Signal | Data Source | Threshold | Severity | False Positive Rate |
|--------|-----------|-----------|----------|-------------------|
| Dashboard view decline | Product analytics | <2 views/week for 14 days (baseline: 5+/week) | Medium | ~15% (seasonal dips) |
| Content creation stall | Product analytics | 0 new dashboards in 30 days (baseline: 2+/month) | High | ~8% |
| Admin absence | Auth logs | No admin login for 21+ days | High | ~5% |
| Data export spike | API logs | 3x normal export volume in 7 days | Critical | ~20% (legitimate migrations) |
| Low support CSAT | Support platform | CSAT < 3 on most recent ticket | High | ~10% |

**Entry rule**: Account enters the sequence when 2+ signals fire within a 14-day window (reduces false positives from single-signal triggering).

## Segment Definitions

| Segment | Account Value | At-Risk Count | Intervention Tier | Sequence |
|---------|--------------|--------------|-------------------|----------|
| Enterprise | $80K+ ACV | 12 | Tier 3 — CS rescue | Email 1 only, then immediate CS handoff |
| Growth | $30K-$80K ACV | 25 | Tier 2 — Re-engage | Full 5-email sequence + CS alert at email 3 |
| Starter | $10K-$30K ACV | 8 | Tier 1 — Nudge | Full 5-email automated sequence |

## Email Sequence

### Email 1: Value Reminder
- **Trigger**: Account enters at-risk cohort (2+ signals confirmed)
- **Subject**: Your team queried 12,400 records last month — here's what's trending
- **Approach**: Personalised usage summary with specific metrics from their account. Lead with value delivered, not absence.
- **CTA**: View your latest insights
- **Recovery signal**: 3+ dashboard views in 7 days after send

### Email 2: Feature Discovery
- **Trigger**: 5 days after Email 1, no recovery signal
- **Subject**: 3 things other analytics teams are building this quarter
- **Approach**: Showcase features or use cases the account has not tried. Use anonymised peer examples from similar-sized companies.
- **CTA**: Try embedded dashboards
- **Recovery signal**: Any new dashboard or report created

### Email 3: Peer Success Story
- **Trigger**: 10 days after Email 1, no recovery signal
- **Subject**: How [similar company] increased product adoption 40% with embedded analytics
- **Approach**: Case study featuring a company in the same industry/size band. Focus on business outcomes, not features.
- **CTA**: See the full story
- **Recovery signal**: Engagement with case study + return to product within 48h
- **Escalation**: For Growth tier, alert CS with account context and engagement history

### Email 4: Direct Outreach
- **Trigger**: 17 days after Email 1, no recovery signal
- **Subject**: Quick question about your analytics setup
- **Approach**: Plain-text email from a named person (CS manager or product lead). Ask one specific, open-ended question about their use case. No marketing formatting.
- **CTA**: Reply to this email
- **Recovery signal**: Reply received (route to CS for follow-up)

### Email 5: Final Value Check
- **Trigger**: 25 days after Email 1, no recovery signal
- **Subject**: Want to make sure InsightHub is still working for you
- **Approach**: Acknowledge they may be reconsidering. Offer a 30-minute optimisation session with a solutions engineer at no cost. No discount.
- **CTA**: Book a free optimisation session
- **Recovery signal**: Session booked or renewed engagement
- **Post-sequence**: If no recovery after 30 days, move to win-back hold list (re-engage in 60 days with product update email)

## Recovery Metrics

| Metric | Definition | Target | Measurement Window |
|--------|-----------|--------|-------------------|
| Recovery rate | % of at-risk accounts returning to healthy engagement | 25% | 30 days from first email |
| Time to recovery | Median days from first email to recovery signal | < 14 days | Per cohort |
| Revenue saved | MRR of recovered accounts | $45K/month | Monthly |
| False positive rate | % of accounts that re-engaged without intervention (control) | Benchmark via 10% holdout | 30 days |

## Recommendations

1. **P1**: Implement the 2-signal entry rule to reduce false positives before launch. Single-signal triggering will annoy healthy users and erode email trust.
2. **P1**: Set up a 10% holdout control group for the first 90 days to measure true incremental recovery vs. natural re-engagement.
3. **P2**: Connect the data export spike signal to an immediate CS alert for enterprise accounts — this signal often precedes migration to a competitor.
4. **P2**: Personalise Email 1 with actual account metrics pulled from the product analytics API (query count, dashboard views, team members active).
5. **P3**: After 90 days of data, build a predictive churn model to replace rule-based signal detection with a probability score.
