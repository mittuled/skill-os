# Secondary Market Manager — Example Input

## Scenario

Meridian AI is 5 years old and several early employees are approaching option expiration. The company wants to run a $1.5M tender offer at $4.50/share to give early employees liquidity before a potential IPO in 2028. Four employees are eligible. Total potential proceeds exceed the budget, so a pro-rata reduction will be required.

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "programme_type": "tender_offer",
  "programme_date": "2026-05-01",
  "price_per_share": 4.50,
  "total_budget_usd": 1500000,
  "participants": [
    {
      "name": "Jordan Lee",
      "role": "Original CPO (departed)",
      "share_type": "iso",
      "shares_vested": 1600000,
      "shares_eligible": 400000,
      "years_at_company": 4,
      "notes": "Fully vested, departed 6 months ago. Options expire in 90 days."
    },
    {
      "name": "Marcus Webb",
      "role": "Senior Engineer (early hire)",
      "share_type": "iso",
      "shares_vested": 240000,
      "shares_eligible": 120000,
      "years_at_company": 4,
      "notes": "Still employed. Requesting partial liquidity."
    },
    {
      "name": "Diana Torres",
      "role": "Head of Design (early hire)",
      "share_type": "nso",
      "shares_vested": 160000,
      "shares_eligible": 80000,
      "years_at_company": 3,
      "notes": "Still employed. NSO grant from first option pool."
    },
    {
      "name": "Kevin Park",
      "role": "Operations Lead",
      "share_type": "iso",
      "shares_vested": 80000,
      "shares_eligible": 40000,
      "years_at_company": 2,
      "notes": "Still employed. Requesting liquidity for house purchase."
    }
  ]
}
```
