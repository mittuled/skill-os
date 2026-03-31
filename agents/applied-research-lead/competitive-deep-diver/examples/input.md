# Scenario: Deep Dive on a Competitor After They Announced a Major Product Expansion

A direct competitor announced a major platform expansion into our core market. The applied research lead is conducting a deep dive to understand the threat level and inform the product team's response.

## Input Parameters

```json
{
  "competitor_name": "RivalCo",
  "analysis_date": "2026-03-31",
  "next_review_date": "2026-06-30",
  "dimensions": {
    "overall_threat_level": "high",
    "product_capabilities": {
      "core_features": ["CI/CD pipeline", "code review", "deployment automation"],
      "gaps_vs_us": ["AI-assisted review", "multi-cloud support", "SOC 2 certification"],
      "recent_launches": ["New GitHub integration (March 2026)", "VS Code extension (Feb 2026)"]
    },
    "pricing_model": {
      "model_type": "per_seat",
      "entry_price": 15,
      "enterprise_price": "custom",
      "is_cheaper_than_us": true,
      "notes": "30% cheaper at entry tier; enterprise pricing unknown"
    },
    "go_to_market": {
      "primary_channel": "PLG + inside sales",
      "icp": "SMB and mid-market engineering teams 5-200 engineers",
      "geographic_focus": "US and EU"
    },
    "market_positioning": {
      "positioning_statement": "The fastest CI/CD platform for growing teams",
      "differentiators": ["Speed claims", "Simple onboarding", "Price"]
    },
    "strengths": ["Lower price point", "Faster onboarding", "Strong GitHub ecosystem integration"],
    "weaknesses": ["No AI features", "No SOC 2", "Limited enterprise support SLAs"],
    "win_conditions": ["Deals where AI review is valued", "Enterprise compliance requirements", "Multi-cloud deployments"],
    "loss_conditions": ["Pure price competition", "SMB deals where SOC 2 is not required"],
    "strategic_moves": {
      "recent_launches": ["Platform expansion into code review — direct overlap with our core product"],
      "funding": "Series B ($40M, January 2026)"
    }
  }
}
```
