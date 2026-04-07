# Growth Pricing Brief

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Lead name] |
| Product | [Product name] |
| Stage | [Pre-launch / Existing product — pricing revision] |
| Version | [1.0] |
| Status | [Draft / Review / Approved] |
| Skill | pricing-strategy-growth |

## Executive Summary

[2-3 sentences: recommended pricing model type, free tier or trial approach, and the expected free-to-paid conversion rate from the growth model.

GUIDANCE: Example: "Recommended pricing is a freemium model with a 5-seat team limit on the free tier, converting to a $99/mo starter plan. At an estimated 4% free-to-paid conversion rate and $250 CAC, the model achieves 2.8:1 LTV:CAC at month 12. The activation moment (create first shared workspace) is reachable on the free tier."]

## Growth Model Inputs

| Growth Model Assumption | Current Value | Pricing Impact |
|------------------------|--------------|----------------|
| Free-to-paid conversion rate | [X%] | [Directly set by free tier generosity] |
| Trial-to-paid conversion rate | [X%] | [Set by trial length and access level] |
| Time-to-conversion | [N days] | [Shorter with trial friction, longer with freemium] |
| Expansion revenue (NRR) | [XXX%] | [Set by expansion trigger design] |
| Viral coefficient (k) | [0.XX] | [Impacted by free tier sharability] |

## Proposed Pricing Structure

### Free Tier

| Parameter | Proposed Value | Rationale |
|-----------|--------------|-----------|
| Core feature access | [Full / Limited to X] | [Users must reach activation moment for free] |
| Usage limit | [e.g., 3 projects / 1,000 events / 5 seats] | [Limit where value is clear but expansion value is visible] |
| Collaboration limit | [e.g., 1 user / 5 users] | [Team plans require upgrade] |
| Data retention | [e.g., 30 days] | [Historical access drives upgrade] |
| Excluded features | [List premium features excluded] | [Wedge features that drive paid upgrade] |
| Time limit | [Unlimited / 14-day trial period] | [Freemium = unlimited; trial = time-boxed] |

**Free tier philosophy**: Users must reach the activation moment ([event_name]) without upgrading. The upgrade trigger appears only when the user has experienced value and hit a natural ceiling.

### Starter Plan — [$XX/month or $XX/user/month]

| Parameter | Value |
|-----------|-------|
| Price | [$XX/mo billed monthly / $XX/mo billed annually] |
| Usage limit | [Expanded limit from free] |
| Seats | [Up to N seats / unlimited] |
| Key differentiating features | [Feature 1, Feature 2] |
| Target persona | [Describe — e.g., individual or small team] |

### Pro Plan — [$XX/month]

| Parameter | Value |
|-----------|-------|
| Price | [$XX/mo billed monthly / $XX/mo billed annually] |
| Usage limit | [Higher or unlimited] |
| Seats | [Unlimited] |
| Key differentiating features | [Feature 1, Feature 2, Feature 3] |
| Target persona | [Describe — e.g., growing team, advanced use case] |

## Conversion Economics Model

### Scenario Analysis

| Scenario | Free Tier Generosity | Trial Length | Free-to-Paid CVR | Monthly Volume | Monthly Revenue |
|----------|--------------------|--------------|-----------------|-----------------------|----------------|
| Conservative | [High] | [N/A] | [2%] | [N free users] | [$N ARR-equiv] |
| **Base Case** | **[Medium]** | **[N/A]** | **[4%]** | **[N free users]** | **[$N ARR-equiv]** |
| Optimistic | [Low] | [N/A] | [7%] | [N free users] | [$N ARR-equiv] |

### LTV:CAC by Scenario

| Scenario | CAC | LTV (24mo) | LTV:CAC | Payback (mo) |
|----------|-----|-----------|---------|-------------|
| Conservative | [$X,XXX] | [$X,XXX] | [X:1] | [N] |
| **Base Case** | **[$X,XXX]** | **[$X,XXX]** | **[X:1]** | **[N]** |
| Optimistic | [$X,XXX] | [$X,XXX] | [X:1] | [N] |

## Expansion Trigger Design

| Expansion Trigger | Plan Boundary | Growth Rationale | Expected Upgrade Rate |
|------------------|--------------|-----------------|----------------------|
| [Seat count limit] | [Free → Starter at 5 seats] | [Teams naturally grow beyond solo use] | [X% of free users per month] |
| [Usage volume limit] | [Starter → Pro at N events] | [High-engagement users hit limit naturally] | [X% of Starter users per month] |
| [Feature unlock] | [Pro feature needed for workflow] | [Power users require advanced feature] | [X% of Starter users per month] |

## Competitive Benchmarks

| Competitor | Free Tier | Entry Paid Plan | Notes |
|------------|-----------|----------------|-------|
| [Competitor A] | [Description] | [$XX/mo] | [Key differentiator vs. our proposal] |
| [Competitor B] | [Description] | [$XX/mo] | [Key differentiator vs. our proposal] |
| [Competitor C] | [Description] | [$XX/mo] | [Key differentiator vs. our proposal] |

**Our differentiation**: [1-2 sentences on how the proposed pricing is differentiated.]

## Recommended Pricing Tests

| Test | Hypothesis | Primary Metric | Timeline |
|------|-----------|---------------|----------|
| [Free tier seat limit: 3 vs. 5 vs. 10] | [Higher limit → higher activation → higher revenue] | [Free-to-paid CVR] | [4 weeks] |
| [Trial length: 14 days vs. 30 days] | [Longer trial → lower urgency → lower conversion] | [Trial CVR] | [6 weeks] |
| [Annual discount: 20% vs. 30%] | [Higher discount → more annual prepay → better cash flow] | [Annual plan take rate] | [4 weeks] |
