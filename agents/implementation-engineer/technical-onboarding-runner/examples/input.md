# Scenario: Technical Onboarding — Acme Corp Week 3 Status Update

Acme Corp is a mid-market customer (150 seats) implementing the platform after signing a 12-month enterprise contract. The implementation engineer is tracking progress heading into week 3 of a 5-week implementation timeline. Go-live is targeted for April 18.

## Input Parameters

```json
{
  "customer_name": "Acme Corp",
  "engineer": "Implementation Engineer — Jordan Lee",
  "go_live_date": "2026-04-18",
  "phase_statuses": {
    "environment_setup": "complete",
    "integration_configuration": "blocked",
    "data_migration": "pending",
    "acceptance_testing": "pending",
    "training": "pending",
    "go_live": "pending"
  },
  "issues": {
    "integration_configuration": "Acme's Salesforce admin has not provided API credentials. Integration cannot be configured until credentials are received. Follow-up sent 2026-03-28 — no response yet."
  }
}
```
