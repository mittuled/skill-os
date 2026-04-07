# Competitor Mapper — Example Input

## Scenario

Meridian AI's PMM is mapping the competitive landscape before Q2 planning. Meridian AI offers an AI-powered compliance automation platform targeting VP/Director Compliance at fintech and healthcare companies (51-500 employees). Sales has reported losing deals to two names repeatedly — Vanta and Drata — and a new entrant, ComplyAI, is appearing in RFPs. The PMM needs a structured map to inform positioning refresh and battle card updates.

## Input JSON

```json
{
  "company_name": "Meridian AI",
  "our_product": {
    "name": "Meridian Compliance Platform",
    "segment": "SMB fintech/healthcare (51-500 employees)",
    "value_prop": "AI-native continuous compliance monitoring with automated evidence collection",
    "differentiators": ["ai_native_evidence_collection", "healthcare_specific_frameworks", "slack_native_alerts", "sub_24hr_onboarding"]
  },
  "competitors": [
    {
      "name": "Vanta",
      "tier": "direct",
      "segment": "SMB-midmarket SaaS",
      "pricing_model": "per_employee",
      "estimated_arpu_usd": 12000,
      "funding_stage": "Series C",
      "strengths": ["brand_awareness", "integrations", "soc2_automation"],
      "weaknesses": ["no_healthcare_frameworks", "slow_onboarding", "limited_ai"],
      "scores": {
        "target_segment_overlap": 8,
        "feature_parity": 7,
        "pricing_proximity": 7,
        "go_to_market_similarity": 8,
        "brand_strength": 9
      },
      "intel_sources": ["g2_reviews", "sales_loss_notes", "pricing_page"]
    },
    {
      "name": "Drata",
      "tier": "direct",
      "segment": "SMB-midmarket SaaS",
      "pricing_model": "per_employee",
      "estimated_arpu_usd": 15000,
      "funding_stage": "Series B",
      "strengths": ["automation_depth", "audit_readiness_dashboard", "integrations"],
      "weaknesses": ["expensive", "complex_setup", "no_slack_native"],
      "scores": {
        "target_segment_overlap": 8,
        "feature_parity": 8,
        "pricing_proximity": 6,
        "go_to_market_similarity": 7,
        "brand_strength": 8
      },
      "intel_sources": ["g2_reviews", "sales_loss_notes", "linkedin_ads"]
    },
    {
      "name": "ComplyAI",
      "tier": "emerging",
      "segment": "SMB AI-first companies",
      "pricing_model": "flat_rate",
      "estimated_arpu_usd": 6000,
      "funding_stage": "Seed",
      "strengths": ["ai_native", "low_price", "fast_setup"],
      "weaknesses": ["limited_frameworks", "no_enterprise_support", "small_team"],
      "scores": {
        "target_segment_overlap": 6,
        "feature_parity": 5,
        "pricing_proximity": 8,
        "go_to_market_similarity": 7,
        "brand_strength": 3
      },
      "intel_sources": ["techcrunch", "producthunt", "rfp_appearances"]
    },
    {
      "name": "Spreadsheets + Consultants",
      "tier": "indirect",
      "segment": "all_segments",
      "pricing_model": "project_based",
      "estimated_arpu_usd": 25000,
      "funding_stage": "n/a",
      "strengths": ["familiar", "flexible", "no_new_vendor"],
      "weaknesses": ["manual", "error_prone", "no_continuous_monitoring"],
      "scores": {
        "target_segment_overlap": 7,
        "feature_parity": 2,
        "pricing_proximity": 4,
        "go_to_market_similarity": 2,
        "brand_strength": 4
      },
      "intel_sources": ["win_loss_interviews", "discovery_calls"]
    }
  ]
}
```
