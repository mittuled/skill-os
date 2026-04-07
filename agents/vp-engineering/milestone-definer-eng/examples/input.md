# Scenario: Milestones for Mobile App Rebuild

A mobile engineering team is rebuilding the iOS app from scratch. VP Engineering needs to define milestones before the phase plan is finalized.

## Input Parameters

```json
{
  "project_name": "iOS App Rebuild v3",
  "milestones": [
    {
      "name": "Core Navigation Shell",
      "target_date": "2026-04-18",
      "responsible_team": "Mobile Team",
      "type": "delivery",
      "success_criteria": [
        "Tab bar navigation renders correctly on iOS 16+ with all 5 tabs",
        "Deep link routing resolves to correct screen for all 12 defined routes",
        "App launches to main screen in <2 seconds on iPhone 12"
      ],
      "dependencies": []
    },
    {
      "name": "Authentication Flow",
      "target_date": "2026-05-02",
      "responsible_team": "Mobile Team",
      "type": "delivery",
      "success_criteria": [
        "Email/password login returns authenticated session token",
        "Biometric login (Face ID / Touch ID) passes on supported devices",
        "Session refresh works without prompting re-login for 30-day sessions"
      ],
      "dependencies": ["Core Navigation Shell"]
    },
    {
      "name": "Beta TestFlight Release",
      "target_date": "2026-05-23",
      "responsible_team": "Mobile Team",
      "type": "gate",
      "success_criteria": [
        "App passes Apple TestFlight review",
        "Zero P0 crash bugs in first 48h of internal testing",
        "All core user flows (login, browse, checkout) functional end-to-end"
      ],
      "dependencies": ["Authentication Flow"]
    }
  ]
}
```
