# Sales Competitive Intel — Example Input

## Scenario

A Sales Manager at a workforce analytics SaaS has noticed win rate against competitor "Workday Analytics" dropping from 55% to 38% over the last quarter. The team needs an updated battle card and win/loss analysis to understand what changed.

## Input JSON

```json
{
  "product_name": "PeopleMetrics",
  "analysis_date": "2026-03-31",
  "competitors": [
    {
      "name": "Workday Analytics",
      "encounter_pct": 45,
      "win_rate_pct": 38,
      "overview": "Enterprise HCM suite with embedded analytics. Strong in HRIS-attached deals. Recent launch of Workday Prism Analytics strengthened their standalone analytics story.",
      "strengths": [
        "Deep HRIS integration — zero data migration for existing Workday customers",
        "Large enterprise trust and brand recognition",
        "Recent Prism Analytics launch closes gap on custom dashboards"
      ],
      "weaknesses": [
        "Prism Analytics requires expensive PS engagement to configure",
        "Workday implementation timelines are 6-12 months — slow time-to-value",
        "Weak on real-time workforce insights — batch data refresh only"
      ],
      "trap_questions": [
        "Are you already on Workday HCM?",
        "How important is having analytics inside your HR system of record?",
        "What's your IT team's bandwidth for a new analytics implementation?"
      ],
      "landmines": [
        "Do not discuss total implementation cost — Workday reps will respond with TCO arguments favoring their platform",
        "Avoid comparing feature lists — Workday has more features; win on speed and flexibility"
      ],
      "talk_tracks": [
        "When prospect is on Workday HCM: 'Our customers who run Workday tell us Prism Analytics takes 4-6 months to configure and requires SI involvement. PeopleMetrics connects to Workday in a day and delivers first insights in week 1.'",
        "When prospect likes Workday brand: 'Workday is a great system of record. PeopleMetrics is purpose-built for analytics — it's the difference between using Excel to run a presentation vs. PowerPoint.'"
      ],
      "proof_points": [
        "Deel replaced Workday Prism with PeopleMetrics — 14-day implementation vs. 6-month Prism rollout",
        "Rippling customer: 60% reduction in manual reporting hours vs. Workday embedded reports"
      ],
      "switching_costs": {
        "financial": 3,
        "operational": 4,
        "data_migration": 2,
        "relationship": 5,
        "opportunity_cost": 3
      },
      "we_win_when": [
        "Prospect is frustrated with Workday implementation timelines",
        "Decision is made by Analytics/Data team, not IT or HR IT",
        "Prospect is NOT already deep in the Workday ecosystem"
      ],
      "we_lose_when": [
        "IT insists on single-vendor strategy",
        "Procurement already has a Workday enterprise agreement",
        "Champion is the Workday admin who owns the existing relationship"
      ],
      "dangerous_stages": ["technical_evaluation", "negotiation"]
    }
  ]
}
```
