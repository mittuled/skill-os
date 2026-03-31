# Scenario: Phase 1 Retrospective for API Gateway Migration

Phase 1 of the API Gateway Migration completed. The team delivered 78 of 90 planned story points. VP Engineering facilitates the inter-phase retrospective before Phase 2 begins.

## Input Parameters

```json
{
  "phase_name": "Phase 1 — API Gateway Core Migration",
  "velocity_planned": 90,
  "velocity_actual": 78,
  "findings": [
    {
      "type": "went_well",
      "category": "technical",
      "description": "Zero-downtime cutover using feature flags worked perfectly — no customer impact",
      "impact": "high"
    },
    {
      "type": "went_well",
      "category": "process",
      "description": "Daily async standups kept the distributed team aligned without meeting overhead",
      "impact": "medium"
    },
    {
      "type": "needs_improvement",
      "category": "process",
      "description": "Dependency on Auth team's API contract was not confirmed until Sprint 2, blocking 12 points of work",
      "impact": "high",
      "suggested_action": "Identify all external dependencies in kickoff week and get contracts signed before Phase 2 starts",
      "owner": "Tech Lead",
      "deadline": "2026-04-07",
      "success_metric": "Zero dependency surprises after Phase 2 Sprint 1"
    },
    {
      "type": "needs_improvement",
      "category": "communication",
      "description": "Stakeholders were not updated when scope changed mid-phase, causing confusion in the all-hands",
      "impact": "high",
      "suggested_action": "VP Engineering to send scope change notification within 24h of any change approval",
      "owner": "VP Engineering",
      "deadline": "2026-04-01",
      "success_metric": "No stakeholder surprise notifications in Phase 2"
    },
    {
      "type": "needs_improvement",
      "category": "tooling",
      "description": "CI pipeline build time increased from 8 to 22 minutes after adding gateway tests",
      "impact": "medium",
      "suggested_action": "Optimize test parallelization and cache build artifacts",
      "owner": "DevOps Engineer",
      "deadline": "2026-04-14",
      "success_metric": "CI build time back under 10 minutes by Phase 2 Sprint 2"
    }
  ]
}
```
