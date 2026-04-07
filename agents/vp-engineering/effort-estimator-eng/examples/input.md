# Scenario: Estimating Effort for Multi-Tenant Feature

VP Engineering needs to size the multi-tenancy feature before committing to a delivery date.

## Input Parameters

```json
{
  "project_name": "Multi-Tenant Architecture",
  "team_velocity_points_per_sprint": 35,
  "risk_level": "high",
  "work_streams": [
    {"name": "Tenant isolation in data layer", "complexity": "complex", "base_points": 20, "notes": "Schema partitioning, row-level security"},
    {"name": "Tenant-scoped authentication", "complexity": "medium", "base_points": 10},
    {"name": "Tenant admin UI", "complexity": "medium", "base_points": 8},
    {"name": "Billing per-tenant integration", "complexity": "complex", "base_points": 15, "notes": "Depends on Stripe billing API"}
  ],
  "assumptions": [
    "Team velocity: 35 points/sprint",
    "External Stripe API integration adds unknown delay — high risk buffer applied",
    "Estimates exclude QA and documentation time"
  ]
}
```
