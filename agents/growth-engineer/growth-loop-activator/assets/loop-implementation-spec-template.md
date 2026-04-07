# Growth Loop Implementation Spec

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Engineer name] |
| Loop Name | [e.g., Referral Loop v1, Content Sharing Loop] |
| Loop Type | [Viral / Content / Paid reinvestment / Product-led] |
| Design Reference | [Link to growth lead's loop design doc] |
| Version | [1.0] |
| Status | [Draft / Engineering Review / Approved] |
| Skill | growth-loop-activator |

## Loop Architecture Overview

```
[Trigger] → [Distribution] → [Landing] → [Signup] → [Activation] → (loops back)
```

Example:
```
User completes project → Share button → Deeplink to project preview → Referred signup → Activates first project → (share button reappears)
```

| Loop Node | Description | Technical Component |
|-----------|-------------|-------------------|
| Trigger | [When and how the sharing prompt appears] | [UI component or backend event] |
| Distribution | [How the invite/share reaches new users] | [Email / In-app deeplink / SMS / Social share] |
| Landing | [What the referred user sees when they arrive] | [Landing page / Personalized preview] |
| Signup | [How the referred user is attributed to the referrer] | [Attribution link / Referral code] |
| Activation | [What the referred user must do to close the loop] | [Activation event from instrumentation spec] |
| Reward | [What the referrer receives when referred user activates] | [Credit / Feature unlock / Cash / None] |

## Technical Architecture

### Referral Code / Link System

| Parameter | Design |
|-----------|--------|
| Code format | [e.g., 8-character alphanumeric: `REF-XXXXXXXX`] |
| Code generation | [Server-generated on user request / Pre-generated at signup] |
| Code storage | [Database table: `referral_codes`] |
| Link format | [e.g., `https://app.example.com/join?ref=REF-XXXXXXXX`] |
| Deeplink support | [Yes — iOS/Android deeplinking configured / No] |
| Link expiry | [Never / 30 days / 90 days] |

### Attribution Tracking

| Parameter | Design |
|-----------|--------|
| Attribution method | [First-touch / Last-touch / Link-based] |
| Attribution window | [30 days] |
| Cross-device attribution | [Yes — cookie + fingerprint / No — link-only] |
| Attribution storage | [Column: `referred_by_user_id` on `users` table] |
| UTM parameters | [utm_source=referral, utm_medium=invite, utm_campaign=[referrer_id]] |

### Reward Mechanics

| Scenario | Reward | Trigger Condition | Timing |
|----------|--------|------------------|--------|
| Referrer (when referred user activates) | [e.g., $10 credit / 1 month Pro] | [Referred user reaches activation event] | [Immediate / Next billing cycle] |
| Referred user (signup reward) | [e.g., 30-day extended trial / 20% discount] | [Referral code applied at signup] | [Immediate on signup] |
| Milestone reward | [e.g., $50 credit for 5 successful referrals] | [5th referred activation] | [Immediate] |

### Fraud Prevention Rules

| Rule | Implementation |
|------|---------------|
| Self-referral prevention | [Block if referring user_id = new user_id; check email domain match] |
| Duplicate account detection | [Block if same email or device fingerprint exists in `users`] |
| Reward cap | [Max $200 total rewards per user per month] |
| Minimum account age to share | [Account must be ≥ 7 days old to generate referral code] |
| Minimum referred user quality | [Referred user must complete activation event; exclude bot traffic (email verification required)] |

## Loop Event Instrumentation

[Every node in the loop must be tracked. See instrumentation-implementer-growth for implementation details.]

| Event Name | Trigger | Required Properties | Node |
|-----------|---------|--------------------|----|
| referral_prompt_shown | [Trigger prompt displayed to user] | user_id, prompt_location, referral_code | Trigger |
| referral_link_shared | [User clicks share / copies link] | user_id, referral_code, share_method (copy/email/social) | Distribution |
| referral_link_clicked | [Referred user clicks the link] | referral_code, referrer_user_id, utm_source | Landing |
| referred_signup_completed | [Referred user creates account] | referred_user_id, referrer_user_id, referral_code, attribution_method | Signup |
| referred_user_activated | [Referred user hits activation event] | referred_user_id, referrer_user_id, days_to_activate | Activation |
| referral_reward_granted | [Reward attributed to referrer] | referrer_user_id, reward_type, reward_value, trigger_event | Reward |

## End-to-End Test Plan

[Execute in staging before production deployment.]

| Test Scenario | Steps | Expected Outcome |
|--------------|-------|-----------------|
| Happy path — full loop | 1. User A generates referral link. 2. User B clicks link, signs up, activates. 3. User A receives reward. | All 6 loop events fire; User A reward attributed correctly. |
| Self-referral prevention | User A applies their own referral code. | Signup blocked or reward not granted; fraud event logged. |
| Duplicate account prevention | User with existing email clicks referral link and re-registers. | Duplicate blocked; existing account detected. |
| Expired link | User clicks referral link after expiry date. | Graceful error page; no attribution created. |
| Cross-device attribution | User B clicks link on mobile, signs up on desktop. | Attribution preserved via fingerprint/cookie fallback. |

## Cycle Time Optimization

Target cycle time: [N days from trigger to referred user activation]

| Node | Current Duration | Target Duration | Optimization Lever |
|------|----------------|----------------|-------------------|
| Trigger → Share | [N hours] | [N hours] | [Reduce steps to share; add one-click share] |
| Share → Click | [N days] | [N days] | [Email subject line, send time optimization] |
| Click → Signup | [N hours] | [N hours] | [Landing page clarity; reduce form fields] |
| Signup → Activation | [N days] | [N days] | [Onboarding optimization; activation prompts] |

## Launch Checklist

- [ ] Referral code generation and storage tested
- [ ] Deeplinks verified on iOS and Android
- [ ] Attribution tracking verified end-to-end
- [ ] Fraud prevention rules tested (all 4 scenarios)
- [ ] Reward logic verified (referrer and referred user)
- [ ] All 6 loop events firing and verified in staging
- [ ] Email delivery configured and tested
- [ ] Landing page live and personalized for referred users
- [ ] Growth loop dashboard view live
- [ ] Analytics Lead has approved instrumentation
