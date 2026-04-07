# Decision Maker Mapper — Example Input

## Scenario

An AE flagged single-threaded deal risk on an enterprise opportunity at Acme Corp ($280K ACV). All conversation has been with one Director of IT who is technically positive but has no budget authority. The deal has been stalled at Stage 3 for 3 weeks.

## Input JSON

```json
{
  "account_name": "Acme Corp",
  "deal_stage": "Stage 3 — Technical Evaluation",
  "stakeholders": [
    {
      "name": "James Reyes",
      "title": "Director of IT",
      "role": "technical_buyer",
      "influence_score": 4,
      "sentiment": "positive",
      "background": "15 years at Acme; technical champion for all infrastructure decisions",
      "recommended_approach": "Leverage as internal guide to map budget process; request intro to VP IT"
    },
    {
      "name": "Patricia Wells",
      "title": "VP of Finance",
      "role": "economic_buyer",
      "influence_score": 5,
      "sentiment": "unknown",
      "background": "Joined Acme 8 months ago from Deloitte; tightened budget approval thresholds to $50K",
      "recommended_approach": "Request executive sponsor intro through James; lead with ROI and payback period"
    },
    {
      "name": "Derek Huang",
      "title": "Head of Procurement",
      "role": "gatekeeper",
      "influence_score": 3,
      "sentiment": "neutral",
      "background": "Controls all vendor agreements above $25K; prefers established vendors",
      "recommended_approach": "Provide case studies from Fortune 500 references early; request security questionnaire upfront"
    },
    {
      "name": "Sandra Torres",
      "title": "VP of Engineering",
      "role": "blocker",
      "influence_score": 4,
      "sentiment": "negative",
      "background": "Prefers build-over-buy; previously championed an internal solution that was deprioritized",
      "recommended_approach": "Avoid direct engagement until champion is strengthened; use economic buyer to frame strategic importance"
    }
  ]
}
```
