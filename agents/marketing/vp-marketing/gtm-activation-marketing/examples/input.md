# Scenario: Product Feature Launch — AI Reporting Module

A B2B SaaS company is launching a major new AI-powered reporting module. Launch date is in 5 days. VP Marketing needs to validate all channel activation assets are ready before giving the go-live order. The campaign spans paid search, paid social, email, and sales enablement.

## Input Parameters

```json
{
  "campaign_name": "AI Reporting Module Launch — Q2 2026",
  "launch_date": "2026-04-05",
  "activation_sequence": ["email", "sales_enablement", "paid_search", "paid_social"],
  "channels": [
    {
      "channel": "paid_search",
      "assets_ready": ["landing_page", "ad_creatives", "utm_tracking"],
      "owner": "paid_media_manager"
    },
    {
      "channel": "paid_social",
      "assets_ready": ["ad_creatives", "landing_page", "utm_tracking", "pixel_firing"],
      "owner": "social_media_manager"
    },
    {
      "channel": "email",
      "assets_ready": ["email_sequence", "unsubscribe_link", "utm_tracking"],
      "owner": "email_marketing_manager"
    },
    {
      "channel": "sales_enablement",
      "assets_ready": ["sales_deck", "one_pager"],
      "owner": "product_marketing_manager"
    }
  ]
}
```
