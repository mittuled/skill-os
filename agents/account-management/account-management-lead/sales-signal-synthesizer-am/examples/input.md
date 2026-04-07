# Scenario: Q1 Portfolio Review — Identifying Systemic Churn and Expansion Trends

The AM lead is preparing for the Q1 portfolio review. Four account managers have submitted their signals for the week. The lead wants to synthesise portfolio-level trends before the leadership briefing on Friday.

## Input Parameters

```json
{
  "signals": [
    {
      "account_name": "NovaCorp",
      "signal_type": "churn_risk",
      "indicators": ["nps_below_6", "usage_decline_over_20pct", "support_escalations_open"],
      "source_interaction": "Weekly check-in call",
      "confidence": "confirmed"
    },
    {
      "account_name": "BlueWave Inc",
      "signal_type": "expansion_opportunity",
      "indicators": ["usage_above_80pct", "headcount_growth", "champion_engaged"],
      "source_interaction": "QBR",
      "confidence": "confirmed"
    },
    {
      "account_name": "Orbis Systems",
      "signal_type": "competitive_threat",
      "indicators": ["competitor_evaluation", "executive_sponsor_change"],
      "source_interaction": "Renewal discussion",
      "confidence": "inferred"
    },
    {
      "account_name": "BlueWave Inc",
      "signal_type": "product_feedback",
      "indicators": ["feature_request_submitted", "budget_cycle_open"],
      "source_interaction": "Product feedback session",
      "confidence": "confirmed"
    }
  ]
}
```
