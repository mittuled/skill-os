# Referral Engine Specification

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Engineer name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | referral-engine-builder |
| Product | [Product name] |
| Growth Lead | [Name] |

## Executive Summary

[2-3 sentences describing the referral program design, target k-factor, and estimated impact.
GUIDANCE: Lead with the growth metric impact. Example: "This referral engine implements a two-sided credit reward ($20 referrer / $20 referee on first purchase) targeting a k-factor of 0.35 — meaning each 100 users will acquire 35 additional users through referral. At current acquisition volume of 1,000 users/month, a successful referral channel would add ~350 incremental users monthly at an estimated CAC of $8 vs. the current paid acquisition CAC of $45."]

## Program Design

[Core referral program parameters.

GUIDANCE:
- Good: Specify reward type, amount, qualification trigger, reward cap, and expiry — all affect fraud risk and unit economics
- Bad: "Two-sided referral with credits"]

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Program type | [One-sided / Two-sided] | [Rationale based on NPS, product, fraud risk] |
| Referrer reward | [e.g., $20 account credit] | |
| Referee reward | [e.g., $20 account credit on first purchase] | |
| Qualification event | [e.g., Referred user completes first purchase ≥ $10 within 30 days] | [Prevents low-quality referrals] |
| Reward cap per user | [e.g., Max $500 in referral credits per account] | [Fraud containment] |
| Reward expiry | [e.g., Credits expire 12 months after issuance] | |
| Referral link expiry | [e.g., Link valid for 30 days after generation] | |

## Attribution System

[Link generation and attribution tracking design.

GUIDANCE:
- Good: Specify the link format, cross-device attribution method, and attribution window
- Bad: "We will track who referred who"]

| Component | Design | Notes |
|-----------|--------|-------|
| Link format | [e.g., `https://app.co/r/<code>?utm_source=referral`] | |
| Code generation | [e.g., 8-char base62, stored in referral_codes table] | |
| Web attribution | [e.g., First-party cookie + localStorage, 30-day window] | |
| iOS attribution | [e.g., Branch.io / Custom IDFV lookup] | |
| Android attribution | [e.g., Play Install Referrer API] | |
| Cross-device | [e.g., Probabilistic fingerprint matching] | |
| Attribution priority | [1. Link click → 2. Manual code entry → 3. Device match] | |

## Reward Engine Design

[Reward processing logic including state machine and edge cases.

GUIDANCE:
- Good: Define each state in the reward lifecycle and the edge case handling (refunds, fraud reversals, account deletion)
- Bad: "The system will issue rewards when someone signs up"]

### Reward State Machine

```
PENDING → QUALIFIED → ISSUED → [REVERSED (fraud) | EXPIRED (unused)]
```

| State | Trigger | Action |
|-------|---------|--------|
| PENDING | Referred user signs up via referral link | Create reward record; no credit issued yet |
| QUALIFIED | Referred user completes qualification event | Issue credit to both parties; send notification |
| REVERSED | Fraud flag confirmed by review queue | Debit credit from account; notify user if policy allows |
| EXPIRED | Credit unused beyond expiry window | Mark expired; exclude from balance |

### Edge Cases

| Edge Case | Handling |
|-----------|---------|
| Referred user requests refund on qualifying purchase | [e.g., Reverse reward if refund within 30 days] |
| Referred user account deleted before reward issued | [e.g., Cancel pending reward] |
| Referrer account suspended | [e.g., Cancel all pending rewards; freeze issued rewards for review] |
| Same user referred by multiple people | [e.g., First-click attribution wins] |

## Fraud Detection Rules

[Specific fraud rules implemented at launch.

GUIDANCE:
- Good: List each rule with exact threshold and enforcement action (hard block vs. flag for review)
- Bad: "We will add fraud detection"]

| Rule | Threshold | Action |
|------|-----------|--------|
| Self-referral | Same email, IP, or device ID | Hard block: reject referral link |
| Velocity | > [N] referrals from 1 account in 24h | Auto-hold: send to review queue |
| Device cluster | > [N] accounts from same device fingerprint | Auto-hold: send to review queue |
| IP cluster | > [N] accounts from same /24 subnet | Flag for manual review |
| Fast churn | Referred user churns within [N] days of activation | Monthly audit for reward reversal |

## Analytics Dashboard Requirements

[Metrics and funnel stages the dashboard must display.

GUIDANCE:
- Good: Specify each metric, its definition, and the time granularity needed
- Bad: "Show referral stats"]

| Metric | Definition | Granularity |
|--------|-----------|-------------|
| Referral links generated | Count of unique referral link generations | Daily |
| Invites sent | Links clicked / emailed / shared (by channel) | Daily |
| Referral sign-ups | New signups via referral link | Daily |
| Referral activations | Referred users who completed qualification event | Daily |
| Rewards issued | Total credit value issued | Daily / Monthly |
| Program ROI | (Revenue from referred users - Reward cost) / Reward cost | Monthly |
| Fraud rate | Rewards reversed / Rewards issued | Weekly |
| K-factor | (Invites sent per active user) × (activation rate per invite) | Weekly |

## Recommendations

[Prioritized recommendations for launch and post-launch optimization.

GUIDANCE: Focus on fraud risks, reward economics, and k-factor improvement levers.]

- **P1**: [Critical risk or blocker to launch]
- **P2**: [Important optimization for first 30 days post-launch]
- **P3**: [Long-term program enhancement]

## Appendices

### A. Unit Economics

[CAC calculation for referral channel at current conversion assumptions.]

| Input | Value |
|-------|-------|
| Average reward cost per referred user (both sides) | [$X] |
| Estimated referral activation rate | [Y%] |
| Blended CAC via referral | [$Z = reward cost / activation rate] |
| Current paid CAC | [$W] |
| CAC improvement | [W - Z = $savings per user] |

### B. Technical Dependencies

[External services, internal APIs, and infrastructure required by the referral engine.]

| Dependency | Purpose | Owner |
|-----------|---------|-------|
| [Deep linking SDK / custom] | Mobile attribution | [Team] |
| [Email/SMS provider] | Invite delivery | [Team] |
| [Payments / credits system] | Reward issuance | [Team] |
| [Fraud review queue] | Manual review interface | [Team] |
