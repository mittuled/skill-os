# Fundraising Process Manager — Example Input

## Scenario

Meridian AI is running a Series A at a $15M target raise. The round has been in process for 14 weeks (of a typical 20-week Series A). Sequoia has signed a term sheet; a16z is in active diligence; three other firms are at earlier stages. One conversation has gone cold. The IR Manager needs a pipeline status report for the CEO before the weekly fundraising review.

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "round_type": "series_a",
  "target_raise_usd": 15000000,
  "weeks_elapsed": 14,
  "investors": [
    {
      "name": "Jane Wu",
      "firm": "Sequoia Capital",
      "stage": "term_sheet",
      "check_size_usd": 8000000,
      "last_contact": "2026-03-30",
      "days_since_contact": 1,
      "notes": "Term sheet received March 28. Exclusivity window closes April 10."
    },
    {
      "name": "David Park",
      "firm": "Andreessen Horowitz",
      "stage": "diligence",
      "check_size_usd": 5000000,
      "last_contact": "2026-03-28",
      "days_since_contact": 3,
      "notes": "Deep in diligence. Partner meeting scheduled April 5."
    },
    {
      "name": "Rachel Kim",
      "firm": "Founders Fund",
      "stage": "second_meeting",
      "check_size_usd": 4000000,
      "last_contact": "2026-03-25",
      "days_since_contact": 6,
      "notes": "Positive second meeting. Waiting on IC decision."
    },
    {
      "name": "Marcus Chen",
      "firm": "Benchmark",
      "stage": "first_meeting",
      "check_size_usd": 6000000,
      "last_contact": "2026-03-20",
      "days_since_contact": 11,
      "notes": "Introductory meeting held. Follow-up requested."
    },
    {
      "name": "Sarah Lee",
      "firm": "General Catalyst",
      "stage": "intro_requested",
      "check_size_usd": 0,
      "last_contact": "2026-03-10",
      "days_since_contact": 21,
      "notes": "Intro via portfolio founder. No response yet."
    },
    {
      "name": "Tom Walsh",
      "firm": "Battery Ventures",
      "stage": "passed",
      "check_size_usd": 0,
      "last_contact": "2026-03-15",
      "days_since_contact": 16,
      "notes": "Passed — not investing in AI workflow space right now."
    }
  ]
}
```
