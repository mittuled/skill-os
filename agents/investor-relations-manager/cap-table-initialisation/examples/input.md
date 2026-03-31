# Cap Table Initialisation — Example Input

## Scenario

Meridian AI is incorporating as a Delaware C-corp. Three co-founders are splitting equity, and they want to set up a formal cap table with a 10% option pool reserved for future hires. Total authorized shares will be 10,000,000. The founders are: Alex (CEO, 45%), Priya (CTO, 35%), and Jordan (CPO, 20%).

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "incorporation_date": "2025-01-15",
  "stage": "pre_seed",
  "total_shares": 10000000,
  "option_pool_pct": 10,
  "founders": [
    {
      "name": "Alex Chen",
      "role": "CEO",
      "share_class": "Founders Common",
      "equity_pct": 45,
      "vesting": "4-year vesting with 1-year cliff"
    },
    {
      "name": "Priya Nair",
      "role": "CTO",
      "share_class": "Founders Common",
      "equity_pct": 35,
      "vesting": "4-year vesting with 1-year cliff"
    },
    {
      "name": "Jordan Lee",
      "role": "CPO",
      "share_class": "Founders Common",
      "equity_pct": 20,
      "vesting": "4-year vesting with 1-year cliff"
    }
  ]
}
```
