# Scenario: Build Enterprise Implementation Playbook

The company has signed its first three enterprise customers (500+ seats each) and the ad-hoc implementation approach used for mid-market customers is not scaling. The Implementation Lead is creating the enterprise-tier implementation playbook to standardize the process for the implementation team.

## Input Parameters

```json
{
  "playbook_name": "Enterprise Implementation Playbook v1.0",
  "tier": "enterprise",
  "go_live_criteria": [
    "All acceptance criteria documented in requirements doc are passed and customer-signed",
    "100% of contracted integrations are live and data flow verified",
    "Executive sponsor has approved go-live in writing",
    "Support team has received handoff brief with customer context",
    "Hypercare monitoring plan is active"
  ],
  "templates": [
    "Executive kickoff deck",
    "Technical discovery questionnaire",
    "Requirements document template",
    "RACI matrix template",
    "Weekly status report template",
    "Acceptance testing checklist",
    "Go-live readiness checklist",
    "Hypercare incident log"
  ],
  "custom_phases": [
    {
      "label": "Security Review",
      "weeks": 1,
      "deliverables": ["Completed security questionnaire", "Penetration test results (if required)", "BAA signed"],
      "entry_criteria": "Discovery complete"
    }
  ]
}
```
