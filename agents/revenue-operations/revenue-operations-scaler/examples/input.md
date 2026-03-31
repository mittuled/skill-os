# Revenue Operations Scaler — Example Input

## Scenario

A SaaS company just closed a Series B and expects pipeline volume to grow 3x over the next 12 months. The RevOps team is auditing current processes to identify what will break under higher volume. The sales team is growing from 8 to 25 reps and onboarding volume is surging.

## Input JSON

```json
{
  "audit_period": "Q2 2026 Planning",
  "bottlenecks": [
    {
      "name": "Manual closed-won handoff to Customer Success",
      "type": "handoff_failures",
      "impact_category": "customer_experience",
      "volume_at_current": 15,
      "volume_projected": 50,
      "proposed_solution": "Configure CRM automation: Closed Won → create onboarding task in CS system → notify assigned CSM",
      "estimated_effort_days": 3
    },
    {
      "name": "Manual deal data entry from email negotiations",
      "type": "manual_data_entry",
      "impact_category": "team_productivity_loss",
      "volume_at_current": 50,
      "volume_projected": 150,
      "proposed_solution": "Deploy email-to-CRM parsing automation; train reps on deal update hygiene",
      "estimated_effort_days": 5
    },
    {
      "name": "Weekly revenue report takes 4 hours to build manually",
      "type": "slow_reporting",
      "impact_category": "reporting_latency",
      "volume_at_current": 1,
      "volume_projected": 3,
      "proposed_solution": "Build automated HubSpot dashboard synced to Google Data Studio; eliminate manual report",
      "estimated_effort_days": 7
    },
    {
      "name": "Territory assignment done manually as reps join",
      "type": "territory_overflow",
      "impact_category": "team_productivity_loss",
      "volume_at_current": 8,
      "volume_projected": 25,
      "proposed_solution": "Configure CRM round-robin and territory rules; automate new rep onboarding workflow",
      "estimated_effort_days": 4
    }
  ]
}
```
