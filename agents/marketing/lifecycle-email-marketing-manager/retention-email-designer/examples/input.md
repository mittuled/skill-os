# Scenario: Retention Sequence for Analytics Platform

Design a churn-prevention email sequence for a B2B analytics platform seeing increased churn in the mid-market segment.

## Context

- **Product**: InsightHub — embedded analytics platform for SaaS companies
- **Segment**: Mid-market (50-500 employees), $30K-$80K ACV
- **Monthly at-risk cohort**: ~45 accounts showing declining usage signals
- **Current monthly churn rate**: 3.2% (target: sub-2%)
- **Revenue at risk**: ~$180K MRR across at-risk cohort

## Observed Churn Signals

1. Dashboard view frequency drops from 5+/week to <2/week for 14 consecutive days
2. No new dashboard or report created in 30+ days (previously creating 2+/month)
3. Admin user has not logged in for 21+ days
4. Data export volume spikes (3x normal in a 7-day window)
5. Support CSAT score below 3 on most recent interaction

## Segment Tiers

- **Enterprise** ($80K+ ACV): 12 accounts — immediate CS escalation
- **Growth** ($30K-$80K ACV): 25 accounts — automated sequence + CS alert
- **Starter** ($10K-$30K ACV): 8 accounts — fully automated sequence
