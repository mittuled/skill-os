# Revenue Funnel Analyst — Example Input

## Scenario

The VP of Sales flagged that win rates have dropped over the last 2 quarters with no obvious cause. The RevOps team is running a full funnel analysis for Q1 2026 to identify where deals are stalling. Volume is up (more MQLs than last year) but closed-won deals haven't grown proportionally.

## Input JSON

```json
{
  "analysis_period": "Q1 2026",
  "total_pipeline_volume": 485,
  "stages": [
    {
      "name": "mql_to_sql",
      "conversion_rate_pct": 22,
      "avg_days_in_stage": 4,
      "volume_in": 485,
      "volume_out": 107,
      "segment_notes": "Conversion healthy; inbound leads quality improved after ICP refresh"
    },
    {
      "name": "sql_to_opportunity",
      "conversion_rate_pct": 48,
      "avg_days_in_stage": 9,
      "volume_in": 107,
      "volume_out": 51,
      "segment_notes": "Below benchmark — SDR-sourced opps converting at 38%, AE-sourced at 61%"
    },
    {
      "name": "opportunity_to_proposal",
      "conversion_rate_pct": 62,
      "avg_days_in_stage": 16,
      "volume_in": 51,
      "volume_out": 32,
      "segment_notes": "Slight slowdown vs. prior quarter; legal review adding 3-4 days"
    },
    {
      "name": "proposal_to_closed_won",
      "conversion_rate_pct": 16,
      "avg_days_in_stage": 28,
      "volume_in": 32,
      "volume_out": 5,
      "segment_notes": "Critical drop — competitive loss rate spiked; pricing objections increased vs. prior quarter"
    }
  ],
  "recommendations": {
    "sql_to_opportunity": "Improve SDR discovery call training; review disqualification criteria — SDRs may be advancing weak opps to meet pipeline targets",
    "proposal_to_closed_won": "Conduct win/loss analysis on Q1 losses; review competitive objection handling in sales playbook; consider pricing review for mid-market segment"
  }
}
```
