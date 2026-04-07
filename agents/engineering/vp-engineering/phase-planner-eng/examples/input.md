# Scenario: Phase Plan for Search Feature Rebuild

A 4-engineer team is rebuilding the search infrastructure. The VP Engineering needs a phase plan from the approved spec.

## Input Parameters

```json
{
  "project_name": "Search Infrastructure Rebuild",
  "team_capacity_points_per_sprint": 40,
  "phases": [
    {
      "name": "Phase 1 — Index Architecture",
      "entry_criteria": "Architecture ADR approved by VP Engineering",
      "exit_criteria": "New index serving read traffic in staging with <200ms p95 latency",
      "tasks": [
        {"name": "Design Elasticsearch cluster topology", "points": 5, "critical_path": true},
        {"name": "Provision staging index", "points": 8, "critical_path": true},
        {"name": "Implement indexing pipeline", "points": 13, "critical_path": true},
        {"name": "Write index health monitoring", "points": 5},
        {"name": "Load test to 3x expected query volume", "points": 8, "critical_path": true}
      ],
      "risks": ["Elasticsearch version compatibility with existing query DSL"]
    },
    {
      "name": "Phase 2 — Query Layer Migration",
      "entry_criteria": "Phase 1 exit criteria met; staging performance validated",
      "exit_criteria": "100% of query traffic routing to new index in production with zero regression",
      "tasks": [
        {"name": "Migrate query service to new client", "points": 8, "critical_path": true},
        {"name": "Implement dual-read shadow mode", "points": 5, "critical_path": true},
        {"name": "Validate result parity between old and new index", "points": 8, "critical_path": true},
        {"name": "Cutover traffic with feature flag", "points": 3, "critical_path": true},
        {"name": "Decommission old index", "points": 3}
      ],
      "risks": ["Result parity gaps may require index re-configuration"]
    }
  ]
}
```
