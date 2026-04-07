# Framework: Adoption Tracking

## Core Model

Adoption tracking measures whether users are progressing from access to habitual use across defined milestones, with signal-based intervention when variance exceeds thresholds.

## Adoption Funnel

| Stage | Definition | Metric Type |
|-------|-----------|-------------|
| Activated | User completed first meaningful action | Binary (yes/no per user) |
| Engaged | User performed the action 3+ times in 30 days | Frequency count |
| Retained | User returned in weeks 2–4 after activation | Cohort retention rate |
| Habitual | User performs target action weekly for 4+ weeks | Active habit rate |

## Metric Selection Hierarchy

1. **Primary metric**: The single number that best reflects feature adoption (e.g., % of eligible users who activated within 14 days)
2. **Supporting metrics**: 2-4 indicators that explain primary metric movement (e.g., time-to-first-action, completion rate per step)
3. **Guardrail metrics**: Metrics that must not degrade (e.g., core workflow engagement, NPS, error rate)

Never report supporting metrics as primary — they explain, not decide.

## Variance Thresholds

| Variance vs Target | Status | Action Required |
|--------------------|--------|-----------------|
| Within 5% | Green | No action — continue monitoring |
| 5–15% below | Amber | Investigate; escalate if trend continues for 2+ cycles |
| >15% below | Red | Immediate diagnosis; recommend intervention |
| >10% above | Blue | Document cause; assess whether target was too conservative |

## Cohort Segmentation Rules

Always segment by:
- **Plan tier**: Free / Pro / Enterprise behave differently
- **Activation cohort**: Users who joined in the same week/month
- **Geography**: Regional differences affect adoption curves

Never aggregate when segments show >20% variance between them.

## Reporting Cadence

| Launch Phase | Cadence | Audience |
|---|---|---|
| Days 1–7 | Daily | Product + Engineering |
| Weeks 2–4 | Weekly | Product + CS + Stakeholders |
| Month 2+ | Bi-weekly or milestone-based | Leadership + Product |

## Trend Interpretation Rules

- 3 consecutive amber readings = escalate to red protocol
- Rising trend even while below target = hold intervention, monitor
- Declining trend even while above target = investigate before it drops further
- Flat trend after amber = intervention needed; organic recovery is not occurring
