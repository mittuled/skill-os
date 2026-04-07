# Access Provisioning Manager — Example Input

## Scenario

Sarah Chen is joining Meridian AI as VP Engineering on April 14. IT needs to provision her access before her start date so she can hit the ground running. Her role requires senior engineer-level access plus admin access to the AWS production environment and GitHub org admin. Her manager is Alex Chen (CEO).

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "request_type": "onboarding",
  "employee_name": "Sarah Chen",
  "role": "senior_engineer",
  "department": "Engineering",
  "manager": "Alex Chen (CEO)",
  "date": "2026-04-14",
  "additional_systems": ["AWS (production)", "GitHub (org-admin)", "PagerDuty (admin)", "Rippling (HR read-only)"],
  "notes": "VP Engineering — also needs access to board materials folder in Google Drive (request from CEO)"
}
```
