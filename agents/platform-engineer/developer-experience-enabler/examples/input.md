# Developer Experience Enabler — Example Input

## Scenario

Meridian AI hired 5 new engineers in Q1 and onboarding averaged 3 days to first commit. The platform team ran a DX retrospective after VP Engineering Sarah Chen's first month. Her feedback: build times are slow (15 min CI), docs are hard to find, and deploying to staging requires Slack-ing the platform team. Score the DX and identify the top improvements for Q2.

## Input JSON

```json
{
  "team_name": "Meridian AI Engineering",
  "team_size": 14,
  "scores": {
    "onboarding_speed": 5,
    "local_dev_parity": 7,
    "build_test_speed": 3,
    "deployment_self_service": 4,
    "docs_discoverability": 4,
    "tooling_satisfaction": 6
  },
  "notes": {
    "onboarding_speed": "Average 3 days to first commit in Q1. Target is 1 day.",
    "local_dev_parity": "Docker Compose covers 90% of services. One legacy service requires manual config.",
    "build_test_speed": "GitHub Actions CI takes 15 minutes. Flaky tests add another 5-10 min on reruns.",
    "deployment_self_service": "Staging deploys require @platform-team Slack message. No self-service.",
    "docs_discoverability": "Docs are in 3 places: Notion, Confluence (legacy), and GitHub wikis. Engineers can't find things.",
    "tooling_satisfaction": "Survey: 6.2/10 average. Main complaints: slow CI and scattered docs."
  },
  "pain_points": [
    "15-minute CI is killing PR iteration speed",
    "No self-service staging deploys — must ask platform team",
    "Can't find runbooks — in Notion but not indexed well",
    "Onboarding checklist is out of date (3 months old)",
    "Local Redis setup for development is undocumented"
  ]
}
```
