# Investor Pipeline Manager — Example Input

## Scenario

Meridian AI is 6 months away from a Series B and needs to start warming investor relationships now. The IR Manager is running the pipeline review for the CEO. They have 8 investors tracked at various relationship stages, targeting a $20M raise. Three investors are overdue for a touch, and the CEO needs to know which to prioritize this week.

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "target_raise_usd": 20000000,
  "fundraise_in_weeks": 26,
  "investors": [
    {
      "name": "Jane Wu",
      "firm": "Sequoia Capital",
      "stage": "invested",
      "check_size_usd": 8000000,
      "thesis_fit_score": 9,
      "check_size_fit_score": 9,
      "warmth_score": 10,
      "portfolio_value_score": 10,
      "days_since_contact": 35,
      "next_action": "Monthly investor update sent — schedule 1:1 for Q2 roadmap discussion",
      "notes": "Lead Series A investor. Pro-rata rights in Series B."
    },
    {
      "name": "David Park",
      "firm": "Andreessen Horowitz",
      "stage": "warm",
      "check_size_usd": 7000000,
      "thesis_fit_score": 9,
      "check_size_fit_score": 8,
      "warmth_score": 7,
      "portfolio_value_score": 8,
      "days_since_contact": 45,
      "next_action": "Send Q1 metrics update; gauge interest in leading Series B",
      "notes": "Lost Series A to Sequoia. Still interested. Partner meeting 3 months ago."
    },
    {
      "name": "Rachel Kim",
      "firm": "Founders Fund",
      "stage": "relationship_building",
      "check_size_usd": 5000000,
      "thesis_fit_score": 7,
      "check_size_fit_score": 7,
      "warmth_score": 6,
      "portfolio_value_score": 7,
      "days_since_contact": 60,
      "next_action": "Invite to product demo day in May",
      "notes": "Met at SaaStr. Good thesis fit. No prior relationship."
    },
    {
      "name": "Tom Walsh",
      "firm": "Battery Ventures",
      "stage": "first_contact",
      "check_size_usd": 5000000,
      "thesis_fit_score": 6,
      "check_size_fit_score": 7,
      "warmth_score": 4,
      "portfolio_value_score": 6,
      "days_since_contact": 25,
      "next_action": "Follow up on intro from Notion founder",
      "notes": "Cold intro 3 weeks ago. No response yet."
    },
    {
      "name": "Sarah Lee",
      "firm": "General Catalyst",
      "stage": "identified",
      "check_size_usd": 8000000,
      "thesis_fit_score": 8,
      "check_size_fit_score": 9,
      "warmth_score": 2,
      "portfolio_value_score": 8,
      "days_since_contact": 0,
      "next_action": "Identify warm intro path via shared portfolio company",
      "notes": "Top target for Series B. No relationship yet."
    }
  ]
}
```
