# Scenario: Staffing the GraphQL API Migration

A 4-engineer team needs to be allocated across 3 work streams for the GraphQL API migration project.

## Input Parameters

```json
{
  "project_name": "GraphQL API Migration",
  "engineers": [
    {"name": "Priya S.", "skills": ["graphql", "typescript", "postgres"], "current_allocation_pct": 10},
    {"name": "James L.", "skills": ["rest-api", "python", "postgres"], "current_allocation_pct": 20},
    {"name": "Sofia R.", "skills": ["graphql", "typescript", "react"], "current_allocation_pct": 0},
    {"name": "David K.", "skills": ["devops", "kubernetes", "ci-cd"], "current_allocation_pct": 30}
  ],
  "work_streams": [
    {"name": "Schema design and resolvers", "required_skills": ["graphql", "typescript"], "capacity_pct_needed": 60},
    {"name": "REST-to-GraphQL adapter layer", "required_skills": ["rest-api", "python"], "capacity_pct_needed": 50},
    {"name": "CI/CD pipeline for schema validation", "required_skills": ["devops", "ci-cd"], "capacity_pct_needed": 30}
  ]
}
```
