# Framework: Referral Engine Design

Defines the structural components and mechanics for building a viral referral program, grounded in k-factor growth theory, attribution science, and fraud prevention.

## Referral K-Factor Model

The viral coefficient (k-factor) determines whether a referral program drives exponential growth.

```
k = (invites sent per user) × (conversion rate per invite)

k > 1.0: Viral — each user generates more than 1 new user
k = 1.0: Steady-state — user base stable
k < 1.0: Decay — referral not self-sustaining (still valuable as a channel if CAC < LTV)
```

### K-Factor Optimization Levers

| Lever | Impact | How to Improve |
|-------|--------|---------------|
| Invite send rate | Direct multiplier on k | Reduce friction in share flow; 1-tap sharing |
| Invite send volume | Multiplier on reach | Prominent placement; re-engagement nudges |
| Invite click rate | Conversion stage 1 | Compelling invite copy; social proof in invite |
| Sign-up conversion | Conversion stage 2 | Optimized landing page with referral context |
| Activation rate | Conversion stage 3 | Activation-gated rewards align incentive with quality |
| Reward attractiveness | Multiplier on all stages | Test reward type and magnitude |

## Referral Program Architecture

### Program Design Decision Matrix

| Decision | One-Sided Reward | Two-Sided Reward |
|----------|-----------------|-----------------|
| When to use | Referrer motivation sufficient; product has high NPS | Both sides need incentive; lower organic NPS |
| Fraud risk | Lower (only 1 party benefits) | Higher (both parties motivated to game) |
| Cost per acquired user | Lower | Higher (2× reward) |
| Conversion rate effect | Moderate | Higher (referred user incentivized) |
| Example | "Give 20% off to a friend" (no referrer benefit) | "You get $20, friend gets $20" |

### Reward Type Selection

| Reward Type | Best For | Fraud Risk | Accounting Complexity |
|------------|----------|-----------|----------------------|
| Account credits | SaaS products | Medium | Low (liability on balance sheet) |
| Feature unlock / Premium | Product with premium tier | Low | Low |
| Cash (ACH/PayPal) | Consumer marketplaces | High | High (AML/KYC requirements) |
| Physical gift cards | E-commerce | Medium | Medium |
| Discount on next purchase | Transactional products | Low | Low |

### Qualification Trigger

Reward should only issue when the referred user completes a meaningful activation:

| Product Type | Qualification Event | Rationale |
|-------------|--------------------|-----------| 
| SaaS | Referred user completes onboarding + 1 core action | Ensures real engagement, not ghost signups |
| Marketplace | Referred user completes first transaction | Ensures real revenue, not browser signups |
| Consumer app | Referred user reaches activation milestone | Aligns reward with value exchange |
| E-commerce | Referred user places first order | Revenue-aligned; prevents fake account chains |

## Attribution Architecture

### Link Generation

```
Referral link structure:
https://app.example.com/signup?ref=<referral_code>[&utm_source=referral&utm_medium=direct]

referral_code: 8-character base62 (user_id encoded or random with DB lookup)
utm_source: "referral"
utm_medium: "email" | "sms" | "social" | "direct"
```

### Attribution Persistence

| Platform | Attribution Method | Persistence Duration |
|----------|------------------|---------------------|
| Web | First-party cookie + localStorage | 30 days |
| iOS | IDFV + SKAdNetwork (iOS 14.5+) | Constrained by SKAdNetwork limits |
| Android | Install referrer API | Session |
| Cross-device | Server-side probabilistic matching | 30 days |

### Attribution Priority

When multiple referral sources exist, apply this priority:

1. Direct referral link click (last-click, highest confidence)
2. Referral code entered manually during signup
3. Device fingerprint match (probabilistic, lower confidence)

## Fraud Detection Rules

### Rule Tiers

| Tier | Rule | Enforcement | Review |
|------|------|-------------|--------|
| Hard Block | Self-referral (same email, IP, or device as referrer) | Automatic reject | None |
| Hard Block | Velocity: > 10 referrals from 1 account in 24h | Automatic hold | Manual review queue |
| Hard Block | Device fingerprint cluster: > 3 accounts from same device | Automatic hold | Manual review queue |
| Soft Flag | IP cluster: > 5 accounts from same /24 subnet | Manual review flag | Review within 48h |
| Soft Flag | Referred user never logged in after activation | Flag for reward reversal audit | Monthly sweep |
| Soft Flag | Referred user churned within 7 days of activation | Audit for reward reversal | Monthly sweep |

### Fraud Review Queue

- Flagged referrals enter a review queue with pending reward status
- Manual reviewer approves or rejects within 48 hours
- On rejection: reward reversed (credits debited, gift card cancelled)
- Chronic abusers: account suspended from referral program

## Referral Conversion Funnel

| Stage | Metric | Benchmark (SaaS) |
|-------|--------|-----------------|
| Users who share at least 1 invite | Share rate | 5–15% of active users |
| Invites clicked / invites sent | Click rate | 20–40% |
| Signups / clicks | Sign-up conversion | 30–60% |
| Activations / signups | Activation rate | 40–70% |
| Rewards issued / activations | Reward qualification rate | 80–95% (if activation well-defined) |
| Net new users attributed / total new users | Referral share of acquisition | 10–30% at program maturity |
