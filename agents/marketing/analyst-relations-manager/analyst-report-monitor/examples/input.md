# Scenario: Monitoring a New Gartner Market Guide for Platform Engineering Tools

Gartner published a new Market Guide covering Platform Engineering Tools. The AR manager monitors the report to extract mentions, assess positioning, and route competitive intelligence to the appropriate teams.

## Input Parameters

```json
{
  "report_title": "Market Guide for Platform Engineering Tools 2026",
  "analyst_firm": "Gartner",
  "publication_date": "2026-03-28",
  "mentions": [
    {
      "mention_type": "challenger",
      "sentiment": "positive",
      "excerpt": "Acme Platform is gaining traction in mid-market enterprises due to its rapid deployment model and strong integration ecosystem. Customers cite time-to-value as a key differentiator."
    },
    {
      "mention_type": "competitive_reference",
      "sentiment": "neutral",
      "excerpt": "Larger incumbents such as Competitor A and Competitor B continue to dominate the enterprise segment, though newer entrants are challenging on developer experience and deployment speed."
    },
    {
      "mention_type": "not_mentioned",
      "sentiment": "neutral",
      "excerpt": "The report does not include Acme Platform in the Representative Vendors list despite the company's market presence."
    }
  ]
}
```
