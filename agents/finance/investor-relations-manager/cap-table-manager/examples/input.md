# Cap Table Manager — Example Input

## Scenario

Meridian AI is closing a $3M seed round led by Sequoia. The founders need to model how existing shareholders will be diluted before signing the term sheet. The company currently has 8,000,000 shares outstanding split between three founders and an early angel. Sequoia is investing $3M at a $15M pre-money valuation, which implies issuing 1,600,000 new shares.

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "shareholders": [
    {
      "name": "Alex Chen (CEO)",
      "share_class": "Common",
      "shares": 3200000
    },
    {
      "name": "Priya Nair (CTO)",
      "share_class": "Common",
      "shares": 2400000
    },
    {
      "name": "Jordan Lee (CPO)",
      "share_class": "Common",
      "shares": 1600000
    },
    {
      "name": "Marcus Reed (Angel)",
      "share_class": "Preferred Seed",
      "shares": 800000
    }
  ],
  "convertibles": [
    {
      "holder": "Y Combinator",
      "instrument": "SAFE",
      "principal": 125000,
      "valuation_cap": 8000000,
      "discount_rate": 0.20,
      "note": "Pre-money SAFE, converts at Series A"
    }
  ],
  "new_round": {
    "investor_name": "Sequoia Capital",
    "round_name": "Seed",
    "new_shares": 1600000,
    "investment_amount": 3000000,
    "pre_money_valuation": 15000000
  }
}
```
