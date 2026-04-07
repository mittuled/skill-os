# Secondary Transaction Coordinator — Example Input

## Scenario

Marcus Reed (angel investor) has found a secondary buyer for his 800,000 preferred shares at $3.50/share ($2.8M total). He notified the company 12 days ago. The ROFR window is currently open — Sequoia Capital has ROFR rights and has not yet indicated whether they will exercise. The IR Manager needs to track the transaction status and prepare the next steps.

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "transaction_type": "investor_to_investor",
  "seller_name": "Marcus Reed",
  "buyer_name": "Tiger Global Secondary",
  "share_class": "Preferred Seed",
  "shares": 800000,
  "price_per_share": 3.50,
  "status": "rofr_window_open",
  "days_elapsed": 12,
  "rofr_holders": ["Sequoia Capital"],
  "notes": "Sequoia has 18 days remaining in ROFR window. Price represents 1.75x the seed round valuation."
}
```
