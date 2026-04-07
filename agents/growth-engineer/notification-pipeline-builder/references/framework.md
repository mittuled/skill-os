# Framework: Notification Pipeline Architecture

Defines the structural components for building multi-channel notification pipelines covering trigger design, delivery infrastructure, template systems, preference management, and performance optimization.

## Notification Channel Characteristics

| Channel | Delivery Speed | Opt-out Risk | Best Use Case | Cost |
|---------|--------------|-------------|--------------|------|
| Email | Seconds–minutes | Low unsubscribe if relevant | Digests, transactional, drip sequences | Low |
| Push notification | Seconds | Medium uninstall risk if overused | Time-sensitive triggers, re-engagement | Low (infra only) |
| In-app message | Immediate (when app open) | Low (contextual) | Onboarding, feature announcements | Low |
| SMS | Seconds | High unsubscribe, high open rate | Critical transactional, OTP | High |
| Webhook / Slack | Seconds | N/A (developer notifications) | B2B alerts, integrations | Low |

## Trigger Classification

| Trigger Type | Examples | Latency Requirement |
|-------------|----------|---------------------|
| Real-time event-based | "Someone liked your post", payment failed, referral activated | < 30 seconds |
| Time-based after event | "You haven't logged in for 7 days" (T+7d) | Minutes (scheduled job) |
| Threshold-based | "You've used 80% of your storage quota" | < 5 minutes |
| Scheduled batch | Weekly activity digest, monthly report | Fixed schedule (cron) |
| System alert | Service downtime, security event | < 60 seconds |

## Pipeline Architecture

### Core Pipeline Stages

```
Event Source (app events, cron, external webhook)
         │
         ▼
Event Ingestion (message queue: SQS, Kafka, Pub/Sub)
         │
         ▼
Trigger Evaluation
  ├── Is user in target segment?
  ├── Frequency cap check (has user received N notifications in window X?)
  ├── Quiet hours check (is it within user's permitted notification window?)
  └── Preference check (has user opted out of this notification type?)
         │
         ▼
Template Rendering (personalization + A/B variant selection)
         │
         ▼
Channel Delivery (ESP / FCM+APNs / in-app)
         │
         ▼
Delivery Tracking (sent → delivered → opened → clicked → converted)
```

### Frequency Capping Rules

| Cap Type | Recommended Default | Configuration |
|----------|---------------------|--------------|
| Global cap | Max 3 notifications per user per day (all channels) | Per-user rolling window |
| Channel cap | Max 1 email per user per 24h for marketing | Per-channel rolling window |
| Campaign cap | Max 1 re-engagement sequence per user per 30d | Per-campaign lifetime cap |
| Notification type cap | Max 1 milestone celebration per user per event | Per-trigger deduplication |

**Quiet hours default**: Do not deliver marketing notifications between 22:00 and 08:00 in the user's local timezone.

## Template System Requirements

### Dynamic Content Variables

| Variable Category | Examples | Source |
|------------------|----------|--------|
| User identity | `{{first_name}}`, `{{account_tier}}` | User profile |
| Behavioral context | `{{days_since_last_login}}`, `{{items_in_cart}}` | Event properties |
| Product data | `{{feature_name}}`, `{{plan_limit}}` | Product catalog |
| Social proof | `{{connections_count}}`, `{{referral_reward}}` | Computed aggregates |
| Time context | `{{trial_days_remaining}}`, `{{renewal_date}}` | Subscription data |

### A/B Test Support in Templates

- Subject line variants (email): A/B test on subject line with % split per variant
- CTA copy variants: Test button text while keeping rest of template constant
- Layout variants: Test single vs. dual column for email templates
- Frequency variants: Test 1-day vs. 3-day re-engagement cadence

### Email Rendering Compatibility

- Test in: Gmail (web + mobile), Apple Mail, Outlook 2019/2021, Yahoo Mail
- Mobile-first design: > 60% of email opens are mobile
- Max width: 600px; responsive at 375px
- No background images as primary content (blocked by default in some clients)
- ALT text on all images

## Compliance Requirements

| Regulation | Requirement | Implementation |
|-----------|-------------|---------------|
| CAN-SPAM | Physical address in footer; one-click unsubscribe | Include in every marketing email template |
| GDPR | Explicit consent for marketing; right to withdraw | Consent captured at signup; unsubscribe honored within 10 business days |
| CASL (Canada) | Express consent before sending commercial messages | Canadian users require explicit opt-in checkbox |
| TCPA (SMS) | Written consent before commercial SMS | SMS opt-in form with clear disclosure |

### Unsubscribe Handling

```
Unsubscribe types:
1. Global unsubscribe (all marketing) → suppress from all non-transactional sends immediately
2. Category unsubscribe (e.g., "weekly digest only") → suppress from that category
3. SMS opt-out (STOP keyword) → suppress SMS within 30 seconds (carrier requirement)

Transactional notifications (receipts, security alerts, OTPs) are NOT subject to marketing unsubscribe.
```

## Delivery Performance Benchmarks

| Metric | Email (Marketing) | Push | In-App |
|--------|------------------|------|--------|
| Delivery rate | ≥ 98% | ≥ 95% | 100% (when app open) |
| Open rate (industry avg) | 20–25% | 5–10% | 70–90% |
| Click-through rate (industry avg) | 3–5% | 2–5% | 10–20% |
| Unsubscribe rate (alert threshold) | > 0.5% | > 1% (opt-out) | N/A |
| Spam complaint rate (alert threshold) | > 0.08% | N/A | N/A |

### Email Sender Reputation Requirements

- SPF, DKIM, and DMARC records configured on sending domain
- Dedicated sending IP warmed for > 30 days before high-volume sends
- Engagement rate above industry benchmarks (low engagement triggers spam filters)
- Bounce rate < 2% (remove bounced addresses from list immediately)
