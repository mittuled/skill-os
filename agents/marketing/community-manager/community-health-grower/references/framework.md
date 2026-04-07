# Framework: community-health-grower

Defines the measurement model, metric thresholds, and intervention playbook for sustaining community health.

## Health Dimension Model

| Dimension | Primary Metric | Secondary Metrics | Measurement Source |
|-----------|---------------|-------------------|-------------------|
| Activity | Monthly Active Members (MAM) | Posts/member, DAU/MAU ratio | Platform analytics |
| Retention | 30-day cohort retention | 90-day return rate, churn rate | Cohort analysis export |
| Sentiment | Net Sentiment Score (NSS) | Positive/neutral/negative ratio, complaint velocity | Conversation analysis |
| Content Quality | Contribution ratio | Unanswered questions %, avg response time | Platform moderation tools |
| Growth | New member activation rate | Onboarding completion %, first-post rate | Onboarding funnel data |

## Health Scorecard Thresholds

| Metric | Danger (Red) | Caution (Yellow) | Healthy (Green) | Leading (Blue) |
|--------|-------------|-----------------|-----------------|----------------|
| MAM / Total Members | < 10% | 10–20% | 20–40% | > 40% |
| 30-day cohort retention | < 20% | 20–35% | 35–55% | > 55% |
| Net Sentiment Score | < 30 | 30–50 | 50–70 | > 70 |
| Avg response time (hrs) | > 48 | 24–48 | 4–24 | < 4 |
| Contribution ratio (% who post) | < 5% | 5–10% | 10–20% | > 20% |
| New member activation (first post %) | < 10% | 10–25% | 25–50% | > 50% |

## Contribution Funnel Stages

| Stage | Definition | Typical % of Community | Intervention if Low |
|-------|-----------|------------------------|---------------------|
| Lurker | Joined, no posts | 60–70% | Welcome sequence, low-friction prompts |
| Observer | Reads regularly, no posts | 15–20% | Direct reply invitations, question threads |
| Commenter | Replies to others | 8–12% | Recognition, featured comment spotlights |
| Contributor | Posts original content | 3–6% | Writing incentives, editorial support |
| Advocate | Recruits others, runs events | 1–2% | Ambassador programme, exclusive access |

## Intervention Playbook

| Health Problem | Diagnosis Signal | Intervention | Expected Timeline |
|----------------|-----------------|-------------|------------------|
| Activity decline | MAM drop > 15% MoM | Weekly prompt threads, challenge series | 4–6 weeks |
| Retention cliff | < 20% 30-day cohort | Welcome DM sequence, onboarding buddy | 6–8 weeks |
| Sentiment drop | NSS below 40 | Moderation review, community listening session | 2–3 weeks |
| Content drought | < 1 post/active member/week | Content seed programme, expert AMA series | 3–4 weeks |
| High response time | Avg > 24 hrs | Moderation coverage schedule, community champions | 1–2 weeks |

## Measurement Cadence

| Report Type | Frequency | Audience | Key Metrics |
|-------------|-----------|----------|-------------|
| Health pulse | Weekly | Community team | DAU, sentiment flags, unanswered questions |
| Cohort retention | Monthly | Community + marketing | 30/60/90-day cohort curves |
| Intervention review | Bi-weekly | Community team | Metric delta vs. pre-intervention baseline |
| Executive summary | Quarterly | Leadership | MAM, NSS, retention, growth trend |
