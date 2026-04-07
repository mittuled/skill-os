# Campaign Analytics Reporter — Example Input

## Scenario

Meridian AI's Marketing Ops Manager is generating the weekly campaign report for the week of March 24-30, 2026. The team ran 4 active channels: LinkedIn Ads, Google Paid Search, HubSpot email nurture, and organic content. Weekly MQL target is 25 and pipeline target is $300K. LinkedIn is their primary demand gen channel.

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "report_period": "Week of March 24-30, 2026",
  "targets": {
    "mqls": 25,
    "pipeline_usd": 300000
  },
  "channels": [
    {
      "channel_name": "LinkedIn Ads",
      "channel_type": "paid_social",
      "spend_usd": 8400,
      "impressions": 145000,
      "clicks": 2175,
      "leads": 47,
      "mqls": 12,
      "sqls": 5,
      "pipeline_usd": 168000
    },
    {
      "channel_name": "Google Paid Search",
      "channel_type": "paid_search",
      "spend_usd": 3200,
      "impressions": 28000,
      "clicks": 1120,
      "leads": 28,
      "mqls": 9,
      "sqls": 3,
      "pipeline_usd": 72000
    },
    {
      "channel_name": "Email Nurture (HubSpot)",
      "channel_type": "email",
      "spend_usd": 420,
      "leads": 18,
      "mqls": 5,
      "sqls": 2,
      "pipeline_usd": 48000
    },
    {
      "channel_name": "Organic Content",
      "channel_type": "content",
      "spend_usd": 1800,
      "leads": 12,
      "mqls": 3,
      "sqls": 1,
      "pipeline_usd": 24000
    }
  ]
}
```
