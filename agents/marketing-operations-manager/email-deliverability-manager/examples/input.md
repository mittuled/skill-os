# Email Deliverability Manager — Example Input

## Scenario

Meridian AI is seeing inbox placement drop before a major product launch campaign. The Marketing Ops Manager needs to score deliverability health across their primary sending domain (mail.meridianai.com) before sending a 12,000-contact campaign. SPF and DKIM are configured but DMARC is not yet set. Bounce rates are acceptable but the domain was only warmed up 3 weeks ago.

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "sending_domain": "mail.meridianai.com",
  "spf_configured": true,
  "dkim_configured": true,
  "dmarc_configured": false,
  "hard_bounce_rate": 0.018,
  "unsubscribe_rate": 0.004,
  "spam_complaint_rate": 0.0008,
  "open_rate": 0.24,
  "click_rate": 0.025,
  "warmup_complete": false,
  "consistent_send_volume": true,
  "double_optin_used": true,
  "inactive_contacts_suppressed": false
}
```
