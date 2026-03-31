# Scenario: Mid-Sprint Velocity Check for Platform Team

The platform team completed Sprint 22 delivering 38 of 52 planned story points. VP Engineering needs a velocity health assessment after two consecutive sprints where the team missed commitments. DORA metrics are available from the CI/CD dashboard.

## Input Parameters

```json
{
  "team_name": "Platform Team",
  "sprint_velocity_completed": 38,
  "sprint_velocity_planned": 52,
  "rolling_avg_velocity": 46,
  "dora_metrics": {
    "deployment_frequency_per_week": 2.5,
    "lead_time_to_change_hours": 18,
    "change_failure_rate_pct": 8,
    "mttr_hours": 3
  },
  "interventions": [],
  "sprint_number": 22,
  "context": "Two consecutive misses; team reports dependency blocks from external API team and unplanned incident load"
}
```
