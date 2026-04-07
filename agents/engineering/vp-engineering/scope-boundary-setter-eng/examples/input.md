# Scenario: Setting Scope Boundaries for Notification System Overhaul

The notification system is being rebuilt. Midway through planning, two additional requests arrived from product and design. VP Engineering must lock scope boundaries and evaluate the change requests.

## Input Parameters

```json
{
  "project_name": "Notification System Overhaul v2",
  "in_scope": [
    "Replace legacy pub/sub library with Kafka-based event bus",
    "Email and in-app notification delivery",
    "Notification preferences UI (basic on/off per category)",
    "Delivery status tracking (sent/delivered/read)"
  ],
  "out_of_scope": [
    "SMS and push notification channels",
    "AI-based notification scheduling optimization",
    "Multi-language notification templates",
    "Analytics dashboard for notification performance"
  ],
  "change_requests": [
    {
      "id": "CHANGE-001",
      "description": "Add Slack notification channel for internal operational alerts",
      "size": "medium",
      "impact_assessed": true,
      "requester_approved": false,
      "requester": "VP Product"
    },
    {
      "id": "CHANGE-002",
      "description": "Fix broken unsubscribe link in current email templates (pre-existing bug)",
      "size": "minor",
      "impact_assessed": true,
      "requester_approved": true,
      "requester": "Legal"
    }
  ]
}
```
