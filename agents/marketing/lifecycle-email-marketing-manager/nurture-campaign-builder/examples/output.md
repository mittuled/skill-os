# Nurture Sequence Plan: Enterprise Data Platform — Data Engineering Leaders

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026-03-29 |
| Author | Lifecycle Email Marketing Manager |
| Version | 1.0 |
| Status | Draft |
| Skill | nurture-campaign-builder |

## Executive Summary

Seven-email nurture sequence targeting VP/Director of Data Engineering at mid-market companies who downloaded the Modern Data Stack whitepaper. Designed to advance leads from problem awareness through solution evaluation to demo request, targeting a 10% MQL-to-SQL conversion rate (up from 5.1% baseline).

## Target Segment

| Attribute | Value |
|-----------|-------|
| Segment | Mid-market Data Engineering Leaders |
| Title | VP/Director of Data Engineering |
| Company Size | 200-2,000 employees |
| Entry Trigger | Downloaded "Modern Data Stack Architecture 2024" whitepaper |
| Monthly Volume | ~150 leads |
| Baseline MQL-to-SQL | 5.1% |
| Target MQL-to-SQL | 10% |

## Buyer Journey Map

| Stage | Key Question | Common Objection | Content Response | Exit Signal |
|-------|-------------|-----------------|-----------------|-------------|
| Awareness | Is my current data stack actually holding us back? | "Our ETL works fine" | Blog: "5 Signs Your ETL Pipeline Is Holding You Back" | Clicks on consideration content |
| Consideration | What would a modern data stack look like for us? | "Migration is too risky" | Webinar: "From Batch to Streaming: A Migration Playbook" | Downloads comparison guide |
| Decision | Which vendor fits our requirements and budget? | "How do I justify the cost?" | Case study + ROI calculator | Requests demo or starts trial |

## Email Sequence

| # | Trigger | Timing | Subject Line | CTA | Asset |
|---|---------|--------|-------------|-----|-------|
| 1 | Whitepaper download | Immediate | Thanks for downloading — here's what we see next | Read the whitepaper companion blog | Blog: 5 Signs Your ETL Pipeline Is Holding You Back |
| 2 | Time-based | Day 4 | The hidden cost of batch processing | Watch the 30-min playbook | Webinar: From Batch to Streaming |
| 3 | Time-based | Day 9 | How teams like yours are making the switch | See the comparison | Comparison guide: DataPlatform vs. Fivetran vs. Airbyte |
| 4 | Opened email 3 | Day 13 | Acme Corp cut data latency by 80% — here's how | Read the case study | Case study: Acme Corp |
| 5 | Time-based | Day 18 | What would your ROI look like? | Calculate your savings | ROI calculator |
| 6 | Time-based | Day 24 | Try it yourself — free sandbox, no commitment | Start your sandbox | 14-day free sandbox |
| 7 | No demo request by Day 30 | Day 30 | One question before we part ways | Reply with your biggest data challenge | Plain text, personal tone |

## Branch Logic

| Signal | Condition | Action |
|--------|-----------|--------|
| High engagement | Opens + clicks on 3 consecutive emails | Accelerate: skip to email 5 (ROI calculator); alert sales for parallel outreach |
| Pricing page visit | Visits /pricing on website | Skip to email 6 (sandbox); flag as high-intent for sales |
| Zero engagement | No opens on emails 1-3 | Move to re-engagement track: single plain-text email from a person, not the brand |
| Partial engagement | Opens but no clicks for 3 emails | Switch to shorter, curiosity-driven subject lines with single-link format |
| Demo request | Books demo at any point | Exit nurture immediately; hand to sales with full engagement history |

## Recommendations

1. **P1**: Integrate email engagement data with the lead scoring model so nurture clicks contribute to SQL threshold.
2. **P1**: Set up attribution tracking from each email CTA through to demo request and closed-won revenue.
3. **P2**: A/B test email 1 subject line in the first month (current vs. a curiosity-gap variant) to establish a performance baseline.
4. **P2**: Create a parallel nurture track for technical ICs (data engineers) who download the same whitepaper — their content needs differ from leadership.
5. **P3**: After 90 days of data, review branch logic thresholds and adjust the "high engagement" definition based on actual conversion patterns.
