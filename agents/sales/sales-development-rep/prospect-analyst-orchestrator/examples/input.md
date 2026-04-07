# Prospect Analyst Orchestrator — Example Input

## Scenario

An SDR team has just received a new territory assignment for Series B/C SaaS companies in the data infrastructure space. The prospect-analyst-orchestrator is aggregating outputs from company-researcher, lead-qualifier, and decision-maker-mapper for 4 priority accounts to produce a ranked intelligence report.

## Input JSON

```json
{
  "territory_name": "Series B/C Data Infrastructure — North America",
  "prospects": [
    {
      "name": "DataSync Labs",
      "research_confidence_pct": 85,
      "qualification_score": 8.5,
      "accessibility_score": 8,
      "days_since_last_contact": 999,
      "recommended_sequence": "tier_1_immediate_outbound",
      "entry_point_contact": "CTO — warm intro available via mutual LinkedIn connection"
    },
    {
      "name": "PipelineIO",
      "research_confidence_pct": 70,
      "qualification_score": 7.2,
      "accessibility_score": 6,
      "days_since_last_contact": 999,
      "recommended_sequence": "tier_2_campaign_wave",
      "entry_point_contact": "VP Engineering — identified via LinkedIn"
    },
    {
      "name": "StreamBase Inc.",
      "research_confidence_pct": 60,
      "qualification_score": 5.0,
      "accessibility_score": 4,
      "days_since_last_contact": 999,
      "recommended_sequence": "nurture_sequence",
      "entry_point_contact": "Director of Engineering — no direct intro available"
    },
    {
      "name": "Orbis Data",
      "research_confidence_pct": 90,
      "qualification_score": 7.8,
      "accessibility_score": 7,
      "days_since_last_contact": 30,
      "recommended_sequence": "cooling_off_hold",
      "entry_point_contact": "VP Product — in cooling-off period"
    }
  ]
}
```
