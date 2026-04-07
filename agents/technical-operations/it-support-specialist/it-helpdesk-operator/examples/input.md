# IT Helpdesk Operator — Example Input

## Scenario

Monday morning at Meridian AI. The IT Support Specialist opens the ticket queue to find 5 new tickets that came in over the weekend and this morning. The queue includes a password lockout, a laptop hardware issue, a software install request, a connectivity problem affecting the whole engineering team, and a data recovery request.

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "tickets": [
    {
      "ticket_id": "INC-041",
      "requester": "Marcus Webb (Senior Engineer)",
      "category": "connectivity",
      "description": "VPN is down for the entire engineering team since 7am. Nobody can connect to AWS dev environment. Production is not affected.",
      "impact": "high",
      "affects_multiple_users": true,
      "status": "open"
    },
    {
      "ticket_id": "INC-042",
      "requester": "Diana Torres (Head of Design)",
      "category": "password_reset",
      "description": "Locked out of my Google account after failed MFA device replacement. Can't access Notion, Figma, or email.",
      "impact": "high",
      "affects_multiple_users": false,
      "status": "open"
    },
    {
      "ticket_id": "INC-043",
      "requester": "Kevin Park (Operations)",
      "category": "hardware_issue",
      "description": "My MacBook Pro won't boot — just shows a flashing folder icon. Started this morning.",
      "impact": "medium",
      "affects_multiple_users": false,
      "status": "open"
    },
    {
      "ticket_id": "INC-044",
      "requester": "New Hire 2 (Sales)",
      "category": "software_install",
      "description": "Need Salesforce installed and configured on my laptop. Also requesting Outreach access.",
      "impact": "medium",
      "affects_multiple_users": false,
      "status": "open"
    },
    {
      "ticket_id": "INC-045",
      "requester": "Jordan Lee (CPO)",
      "category": "data_recovery",
      "description": "Accidentally deleted a Notion page with Q2 product roadmap. Deleted yesterday afternoon.",
      "impact": "medium",
      "affects_multiple_users": false,
      "status": "open"
    }
  ]
}
```
