# Framework: Pricing Finaliser — Growth Mechanics Review

Defines the analytical framework for evaluating whether final pricing structure supports growth mechanics across activation, conversion, and expansion.

## Pricing Review Dimensions

### 1. Pre-Activation Friction Check

Identify all monetization touchpoints that appear before the activation moment:

| Touchpoint | Position in Funnel | Friction Level | Recommendation |
|------------|-------------------|---------------|----------------|
| Credit card required at signup | Pre-activation | High | Remove or defer to post-activation |
| Feature gate blocks aha moment | Pre-activation | Critical | Gate after activation, not before |
| Trial time limit expires pre-activation | Pre-activation | High | Extend trial or anchor to activation completion |
| Metered limit hit pre-activation | Pre-activation | Medium | Raise limit to cover activation journey |

**Rule**: No hard monetization touchpoint should appear before a user has completed the activation moment.

### 2. Conversion Rate Modeling

Use industry benchmarks as calibration anchors:

| Model | Benchmark Conversion Rate | Notes |
|-------|--------------------------|-------|
| Freemium (free-to-paid) | 2–5% | SaaS industry average |
| Free trial (opt-in, no CC) | 15–25% trial-to-paid | Varies by product complexity |
| Free trial (credit card required) | 40–60% trial-to-paid | Higher intent, lower trial volume |
| PLG (product-led, self-serve) | 3–8% free-to-paid | Depends on activation rate |

For each tier boundary, estimate: `conversion_rate × price_point × eligible_users = expected_MRR_impact`.

### 3. Expansion Mechanic Assessment

| Mechanic | NRR Impact | Signal |
|----------|-----------|--------|
| Seat-based pricing | High expansion potential | Team adoption triggers upgrades |
| Usage-based metering | Variable, up to 150%+ NRR | Power users expand naturally |
| Feature tier gating | Moderate | Requires feature desire to expand |
| Flat pricing | Low expansion | No natural trigger; relies on upsell motions |

**Target**: NRR > 100% requires at least one natural expansion trigger in the pricing structure.

### 4. Approval Decision Matrix

| Finding | Verdict |
|---------|---------|
| No pre-activation gates, conversion model meets target, expansion mechanic present | Approve |
| Minor pre-activation friction, conversion model within 20% of target | Approve with conditions |
| Hard gate before activation moment OR conversion model misses target by >20% | Reject |
| No expansion mechanic and product targets NRR > 100% | Approve with conditions (expansion redesign required) |
