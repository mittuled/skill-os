# Scenario: Post-Launch Iteration Backlog Prioritization — Dashboard Redesign

Three weeks after launching the redesigned analytics dashboard, the product team has collected feedback from session recordings, customer support tickets, and an NPS survey. The Head of Design needs to prioritize the backlog of improvement items for the next sprint cycle.

## Input Parameters

```json
{
  "backlog_items": [
    {
      "id": "DX-001",
      "title": "Chart legend overlaps data on mobile viewport",
      "source": "Session recordings + 8 support tickets",
      "affected_surface": "Analytics dashboard — mobile",
      "scores": {
        "user_impact": 4,
        "business_value": 3,
        "design_effort": 4,
        "accessibility_severity": 2
      },
      "notes": "Affects ~35% of users who access on mobile devices"
    },
    {
      "id": "DX-002",
      "title": "Date range picker has no keyboard navigation support",
      "source": "Accessibility audit finding",
      "affected_surface": "Analytics dashboard — date filter",
      "scores": {
        "user_impact": 3,
        "business_value": 2,
        "design_effort": 3,
        "accessibility_severity": 5
      },
      "notes": "WCAG 2.1 AA violation — keyboard trap. Blocking for screen reader users."
    },
    {
      "id": "DX-003",
      "title": "Empty state for no-data charts uses developer placeholder text",
      "source": "NPS verbatims (5 mentions)",
      "affected_surface": "All chart components",
      "scores": {
        "user_impact": 2,
        "business_value": 2,
        "design_effort": 5,
        "accessibility_severity": 0
      },
      "notes": "Quick win — copy update only, no design change required"
    },
    {
      "id": "DX-004",
      "title": "Export button not discoverable — users cannot find CSV export",
      "source": "3 support tickets + sales call feedback",
      "affected_surface": "Analytics dashboard — toolbar",
      "scores": {
        "user_impact": 4,
        "business_value": 5,
        "design_effort": 3,
        "accessibility_severity": 0
      },
      "notes": "Cited in 2 deal blockers where prospect needed export for reporting workflow"
    }
  ]
}
```
