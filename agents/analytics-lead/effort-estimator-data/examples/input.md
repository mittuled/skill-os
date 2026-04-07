# Scenario: Estimating Data Work for New Onboarding Funnel Feature

The product team is building a new onboarding funnel and needs an analytics effort estimate. Work includes instrumentation for 15 new onboarding events, a new dbt pipeline for funnel data, and a new conversion dashboard.

## Input Parameters

```json
{
  "initiative_name": "Onboarding Funnel Analytics",
  "complexity": "medium",
  "components": [
    {"name": "Onboarding event instrumentation", "type": "instrumentation", "size": "m"},
    {"name": "Funnel data pipeline (dbt)", "type": "pipeline", "size": "m"},
    {"name": "Onboarding conversion dashboard", "type": "dashboard", "size": "m"}
  ]
}
```
