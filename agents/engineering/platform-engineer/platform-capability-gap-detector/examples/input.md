# Platform Capability Gap Detector — Example Input

## Scenario

Meridian AI's platform team is preparing for the Series A due diligence technical review. The CTO asked for a platform capability self-assessment to identify gaps before investors' technical team audits the infrastructure. The team has good CI/CD but observability is incomplete and there is no internal developer portal or feature flag service.

## Input JSON

```json
{
  "team_name": "Meridian AI Platform",
  "capabilities": [
    {
      "domain": "developer_onboarding",
      "present_capabilities": ["Local dev environment via Docker Compose", "README documentation", "Service template (partial)"],
      "notes": "Setup takes ~2 hours, not 30 min. Template is outdated."
    },
    {
      "domain": "ci_cd",
      "present_capabilities": ["Automated testing on PR (GitHub Actions)", "Automated deployment to staging", "Automated deployment to production with approval (ArgoCD)", "Rollback via ArgoCD"],
      "notes": "CI/CD is the most mature capability. Full GitOps implemented."
    },
    {
      "domain": "observability",
      "present_capabilities": ["Centralized logging (Datadog)", "Metrics and dashboards (Datadog)"],
      "notes": "No distributed tracing. Alerting exists but runbooks are incomplete."
    },
    {
      "domain": "infrastructure",
      "present_capabilities": ["All infrastructure in Terraform", "Environment provisioning is automated"],
      "notes": "No drift detection. Cost tagging is manual."
    },
    {
      "domain": "security_compliance",
      "present_capabilities": ["Access control and least privilege (AWS IAM)"],
      "notes": "No dependency scanning. No secret scanning in CI. Audit logging not centralized."
    },
    {
      "domain": "developer_self_service",
      "present_capabilities": [],
      "notes": "No internal portal, no service catalogue, no feature flags."
    }
  ]
}
```
