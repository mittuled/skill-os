# Framework: Paywall Implementation

Defines the entitlement model, gate placement rules, and conversion optimization approach for freemium and trial paywalls.

## Paywall Type Selection

| Paywall Type | How It Works | Best For | Freemium-to-Paid Benchmark |
|-------------|-------------|---------|---------------------------|
| Feature gate (hard) | Specific features require paid plan | Discrete high-value features | 2–5% conversion |
| Usage metering (soft gate) | Free tier allows N uses; upgrade to expand | Unlimited usage as core value | 3–7% conversion |
| Time-limited trial | Full access for N days; credit card required post-trial | High-complexity tools needing evaluation | 40–60% trial-to-paid |
| Opt-in trial (no CC) | Full access for N days; opt-in to pay | Products where CC friction kills trial volume | 15–25% trial-to-paid |
| Reverse trial | Pro plan by default; auto-downgrade at trial end | Products where free tier underrepresents value | 10–20% conversion |

## Entitlement Matrix Structure

Define the entitlement matrix before any gate implementation:

| Feature | Free | Pro | Enterprise |
|---------|------|-----|-----------|
| [Core feature 1] | Full access | Full access | Full access |
| [Activation feature] | Full access | Full access | Full access |
| [Expansion feature] | Limited (N uses) | Unlimited | Unlimited |
| [Power feature] | Blocked | Available | Available |
| [Admin/team feature] | Blocked | Blocked | Available |

**Rule**: The activation moment feature must never be gated. At least one feature per paid tier must create genuine desire beyond the free tier.

## Gate Placement Rules

1. **Never gate the activation moment**: The feature or action that constitutes the activation signal must be freely accessible.
2. **Gate after demonstrated value**: Introduce the first gate after the user has completed the activation moment at least once.
3. **Soft gate before hard gate**: Show a usage limit warning (soft gate) before blocking access entirely (hard gate). This converts users who were not yet aware they needed more.
4. **Contextual timing**: Display upgrade prompts when the user is trying to do something they want to do — not on page load or idle.

## Paywall Performance Benchmarks

| Metric | Weak | Average | Strong |
|--------|------|---------|--------|
| Paywall impression-to-click rate | <3% | 3–8% | >8% |
| Upgrade page-to-payment-start | <20% | 20–45% | >45% |
| Payment-start-to-completion | <60% | 60–80% | >80% |
| Overall free-to-paid (freemium) | <2% | 2–5% | >5% |

## A/B Test Hierarchy for Paywall Optimization

Test in this order (highest expected impact first):
1. Gate placement position in the funnel (before vs. after activation)
2. Upgrade prompt copy (feature-benefit framing vs. social proof vs. urgency)
3. Pricing display (monthly vs. annual billing default; price anchoring)
4. CTA button text and colour
5. Plan comparison table format
