# Scenario: Synthesising Research on Developer Tool Buying Behaviour

The research lead has gathered findings from three sources: 12 customer interviews, a 150-person developer survey, and a Gartner report on DevOps platforms. They need a synthesis to inform the Q3 product strategy.

## Input Parameters

```json
{
  "research_question": "How do engineering teams evaluate and buy developer productivity tools?",
  "synthesis_date": "2026-03-31",
  "sources": [
    {
      "type": "customer_interviews",
      "sample_size": 12,
      "confidence": "high",
      "findings": [
        "Engineers drive tool evaluation; procurement gets involved only after technical approval",
        "Free trial is mandatory — no team will purchase without hands-on evaluation",
        "Integration with existing GitHub/GitLab workflow is a hard requirement"
      ]
    },
    {
      "type": "survey",
      "sample_size": 150,
      "confidence": "medium",
      "findings": [
        "67% of respondents cite 'easy onboarding' as top evaluation criterion",
        "Price is ranked 4th, below features, integrations, and support quality",
        "42% of teams evaluate 2-3 tools before purchasing"
      ]
    },
    {
      "type": "analyst_report",
      "sample_size": null,
      "confidence": "medium",
      "findings": [
        "PLG motions dominate developer tool adoption in companies under 500 engineers",
        "Enterprise deals (1000+ engineers) require security documentation and legal review"
      ]
    }
  ],
  "strategic_implications": [
    "PLG is the right primary GTM motion for our target segment",
    "Free trial quality directly determines win rate — invest in trial experience",
    "GitHub/GitLab integration completeness is a hard gate for most evaluations"
  ],
  "open_questions": [
    "What is the typical trial-to-paid conversion timeline?",
    "Which features drive the 'aha moment' during trial?"
  ],
  "recommended_actions": [
    "Invest in trial onboarding — reduce time to first value below 10 minutes",
    "Prioritise GitHub Actions integration on the roadmap",
    "Build a self-serve pricing page with clear trial CTA"
  ]
}
```
