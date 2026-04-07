# Framework: Pricing Strategy Growth

Defines the methodology for designing freemium tiers, trial mechanics, and expansion triggers that optimize acquisition velocity, activation rates, and net revenue retention.

## Freemium Design Principles

### The Activation Gate Rule
The free tier must allow users to reach the activation moment (aha moment) without payment. If the activation event requires a paid feature, the free-to-paid conversion will be driven by sales pressure rather than experienced value — producing poor conversion quality and high churn after payment.

**Test**: Can a free user complete the activation event defined by `activation-signal-definer`? If no → move the paywall.

### Free Tier Generosity Tradeoff

| Free Tier Constraint | Effect on Acquisition | Effect on Conversion | Net Growth Impact |
|--------------------|----------------------|--------------------|--------------------|
| Very generous (full feature access, usage caps only) | High — low signup friction | Low — no natural upgrade trigger | Often negative; users stay free indefinitely |
| Moderate (core features free, advanced gated) | Medium | Medium | Usually optimal |
| Restrictive (limited to preview/trial only) | Low — high friction | High among those who sign up | Negative at scale; small audience converts well |

**Optimal zone**: Free tier covers 80% of casual use case; paid tier covers the remaining 20% that power users need.

### Usage Limit vs. Feature Gate Decision

| Mechanism | Best For | Risk |
|-----------|---------|------|
| Usage limits (seats, API calls, storage) | Scaling products where cost grows with usage | Users hit limits at bad times and churn instead of upgrading |
| Feature gates (advanced features locked) | Products where advanced features clearly signal intent to pay | Users may not discover gated features; low upgrade awareness |
| Time-limited trial | Products where value is apparent quickly | Users don't convert if trial is too short; false urgency if too long |

## Trial Parameter Design

| Trial Length | Conversion Signal | Recommended For |
|-------------|-----------------|----------------|
| 7 days | Fast-to-value products (productivity tools, communication) | If aha moment achievable in < 1 day |
| 14 days | Standard SaaS | Most workflow products |
| 30 days | Complex products requiring configuration | Enterprise tools, data platforms |
| > 30 days | Avoid | Creates procrastination; use 30-day + manual extension instead |

**Credit card at signup**:
- With CC: +30–50% trial-to-paid conversion (opt-in bias), −60–80% trial volume
- Without CC: Higher volume, more unqualified leads; requires better engagement to convert
- **Recommendation**: No CC for consumer/PLG; consider CC for enterprise/high-ACV where unqualified leads are expensive.

## Expansion Trigger Design

Expansion triggers should fire at **value milestones**, not arbitrary limits:

| Expansion Trigger Type | Example | Conversion Quality |
|----------------------|---------|------------------|
| Seat limit (collaboration) | "Add more teammates — upgrade to Team plan" | High — natural workflow need |
| Usage milestone | "You've analyzed 100 reports — upgrade for unlimited" | Medium — depends on value clarity |
| Feature discovery | User attempts a premium feature → upgrade prompt | High — user expressed intent |
| Time-in-product | "You've been using X for 90 days — save 20% by upgrading" | Low — time does not signal intent |

## Competitive Pricing Analysis Template

Benchmark 3–5 competitors on:
1. Free tier feature set and usage limits
2. Paid tier entry price and included seats/usage
3. Trial length and CC requirement
4. Expansion pricing mechanics (seat-based, usage-based, tier-based)
5. Net revenue retention implication (does pricing incentivize staying and growing?)

## Conversion Economics Model

```
Free-to-Paid Conversion Rate under Tier Configuration:

Baseline: Industry median for product category (SaaS PLG: 2–8%)
Adjustments:
  + Generous free tier with clear value limit: +1–3pp
  + Frictionless upgrade flow (one-click): +0.5–1pp
  + Strong activation before paywall: +2–4pp
  - Credit card at signup: −2–4pp (volume-adjusted)
  - Aggressive feature gating before activation: −3–5pp

Net Revenue Retention target: ≥ 100% (expansion > contraction + churn)
NRR formula: (MRR_start + Expansion − Contraction − Churn) / MRR_start × 100
```
