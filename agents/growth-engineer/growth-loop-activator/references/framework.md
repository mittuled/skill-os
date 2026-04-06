# Framework: Growth Loop Activation

Defines the technical architecture for implementing referral, viral, and product-led growth loops with fraud prevention and full attribution tracking.

## Loop Architecture Components

Every growth loop requires five technical components:

| Component | Purpose | Key Design Decisions |
|-----------|---------|---------------------|
| Trigger | Surface the loop entry point at the right moment in the user journey | Placement (post-activation vs. post-value-delivery), prompt format (modal, banner, inline) |
| Referral link / invite system | Generate unique, trackable distribution artifacts | Deeplink for mobile, UTM-tagged URL for web, shortener for SMS |
| Attribution | Link referred users back to their referrer across sessions and devices | First-party cookie, deeplink callback, device fingerprint fallback |
| Reward engine | Process incentives for referrer and/or referee | Trigger (signup vs. activation vs. payment), reward type (credit, feature unlock, cash), fraud gate |
| Fraud prevention | Prevent reward gaming | Self-referral block, IP/device clustering, velocity limits, manual review queue |

## Trigger Placement Rules

| Trigger Moment | Rationale | Expected CTR Range |
|---------------|-----------|-------------------|
| Post-activation (immediately after aha moment) | Highest intent; user has just experienced value and is most likely to share | 5–15% |
| Post-value-delivery (after repeated activation) | Higher-quality referrals; user is confident in the product | 8–20% |
| During social / collaborative feature usage | Natural sharing context (e.g., "Invite teammates") | 10–30% |
| Post-purchase confirmation | High-intent buyer; can offer both-sides reward | 15–35% |
| Random / time-based | No value context; disruptive | 1–3% |

**Rule**: Trigger placement at post-activation produces the best balance of reach and referral quality.

## Viral Coefficient Targets

| Loop Mechanic | Minimum Viable k | Good k | Strong k |
|--------------|-----------------|--------|---------|
| Consumer referral (two-sided reward) | 0.15 | 0.30 | 0.50+ |
| B2B seat-based invite | 0.10 | 0.25 | 0.40+ |
| Content / UGC loop | 0.05 | 0.15 | 0.30+ |
| Product-embedded (collaboration feature) | 0.20 | 0.40 | 0.60+ |

If measured k is below minimum viable, the loop needs structural redesign before optimization.

## Attribution Technical Pattern

```
Referral flow:
1. Referrer clicks share → generate invite_id (UUID) and store referrer_id → invite_id mapping in DB
2. Invite URL: https://app.com/invite/[invite_id]?ref=[referrer_id]
3. Referred user lands → read invite_id and referrer_id from URL → store in localStorage + first-party cookie (7-day expiry)
4. Referred user signs up → read from localStorage → attach referrer_id and invite_id to signup event and user record
5. Referred user activates → referral_activation event fires with referrer_id from user record
6. Reward trigger: referral_reward_granted fires after qualifying event (e.g., activation or payment)
```

## Fraud Prevention Rules

Implement all four rules at launch (no partial fraud prevention):

| Rule | Implementation |
|------|---------------|
| Self-referral block | Compare referrer_id against signed-in user_id at signup; reject if match |
| Duplicate account detection | Check email + IP + device fingerprint at signup against existing referred accounts |
| Velocity cap | Max N reward grants per referrer per 30 days (set based on expected organic sharing rate × 3) |
| Manual review trigger | Flag accounts where referred users never log in after reward qualification |

## Cycle Time Optimization

Cycle time = days from trigger to referred user's activation. Reduce by:
1. Optimize invite delivery speed (push > email for time-sensitive referrals)
2. Reduce friction in the referral landing experience (pre-filled signup, referrer name visible)
3. Accelerate referred user onboarding (personalized onboarding referencing referrer)
