# Cohort Selector — Example Input

## Scenario

An SDR team is launching a Q2 outbound campaign targeting mid-market SaaS companies in the HR tech space. The team has 4 SDRs with capacity for 80 accounts. Intent data shows 12 companies recently searched for "workforce analytics" and "HRIS migration." One account was closed-lost 45 days ago.

## Input JSON

```json
{
  "campaign_name": "Q2 Mid-Market HR Tech — Workforce Analytics",
  "prospects": [
    {
      "name": "Lattice HR",
      "icp_scores": {
        "firmographic_fit": 9,
        "technographic_fit": 8,
        "intent_score": 9,
        "behavioral_indicators": 7
      },
      "intent_signals": ["searched workforce analytics x3", "job posting: HR Data Analyst"],
      "days_since_last_contact": 999,
      "assigned_sdr": "Alex Chen"
    },
    {
      "name": "Rippling",
      "icp_scores": {
        "firmographic_fit": 7,
        "technographic_fit": 9,
        "intent_score": 6,
        "behavioral_indicators": 5
      },
      "intent_signals": ["product review on G2", "attended competitor webinar"],
      "days_since_last_contact": 999,
      "assigned_sdr": "Maria Santos"
    },
    {
      "name": "HiBob",
      "icp_scores": {
        "firmographic_fit": 6,
        "technographic_fit": 5,
        "intent_score": 4,
        "behavioral_indicators": 3
      },
      "intent_signals": [],
      "days_since_last_contact": 999,
      "assigned_sdr": "Jordan Lee"
    },
    {
      "name": "Personio GmbH",
      "icp_scores": {
        "firmographic_fit": 8,
        "technographic_fit": 7,
        "intent_score": 8,
        "behavioral_indicators": 6
      },
      "intent_signals": ["searched HRIS migration", "hired 3 HR ops roles"],
      "days_since_last_contact": 45,
      "assigned_sdr": "Alex Chen"
    }
  ]
}
```
