# Golden Path Definer — Example Input

## Scenario

Meridian AI's platform engineering team is auditing their golden paths. The team has grown to 12 engineers across 3 teams and is seeing divergent tooling choices. Deployment is well-defined but new service creation and observability are inconsistent. Security scanning has never been standardized.

## Input JSON

```json
{
  "team_name": "Meridian AI Platform Engineering",
  "domains": [
    {
      "domain": "new_service",
      "maturity": "draft",
      "existing_tools": ["GitHub template repo (partial)", "Docker Compose"],
      "notes": "Template exists but is 6 months out of date. No CI/CD or observability pre-wired."
    },
    {
      "domain": "deployment",
      "maturity": "enforced",
      "existing_tools": ["GitHub Actions", "ArgoCD", "Terraform"],
      "notes": "GitOps is enforced. All deployments go via ArgoCD. Blue/green available but not default."
    },
    {
      "domain": "observability",
      "maturity": "active",
      "existing_tools": ["Datadog APM", "Datadog Logs", "PagerDuty"],
      "notes": "Datadog is standard but not all services emit structured logs. Tracing is only 4 of 8 services."
    },
    {
      "domain": "database_access",
      "maturity": "active",
      "existing_tools": ["PostgreSQL", "Prisma ORM", "PgBouncer"],
      "notes": "Prisma is de facto standard. Read replica routing not consistently used."
    },
    {
      "domain": "security",
      "maturity": "not_started",
      "existing_tools": [],
      "notes": "No automated dependency scanning. Secret in code incidents occurred twice in Q1."
    }
  ]
}
```
