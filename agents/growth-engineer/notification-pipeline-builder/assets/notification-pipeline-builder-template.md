# Notification Pipeline Specification

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Engineer name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | notification-pipeline-builder |
| Product | [Product name] |
| Growth Lead | [Name] |

## Executive Summary

[2-3 sentences describing the notification pipeline scope, channels implemented, and the primary retention or engagement outcome targeted.
GUIDANCE: Lead with the business metric impact. Example: "This notification pipeline implements email, push, and in-app messaging across 6 trigger flows targeting a 15% improvement in 7-day retention. The highest-impact notification is the Day 3 activation nudge (currently 0% of inactive users are re-engaged; benchmark for event-triggered notifications is 8–12% re-activation rate)."]

## Channel and Trigger Architecture

[Complete list of notification triggers, channels, and targeting rules.

GUIDANCE:
- Good: Specify the exact trigger event, channel, segment, and frequency cap for each notification
- Bad: "Email users who haven't logged in"]

| Notification ID | Name | Trigger | Channel | Segment | Frequency Cap |
|----------------|------|---------|---------|---------|--------------|
| N001 | [e.g., Day 3 activation nudge] | [User has not completed activation after 3 days] | [Email + Push] | [Signed up but not activated] | [Once per user] |
| N002 | [e.g., Referral reward earned] | [referral_qualified event fires] | [Email + In-app] | [Referrer] | [Once per referral] |
| N003 | [e.g., Weekly activity digest] | [Cron: Monday 9am user local time] | [Email] | [Active users in past 30 days] | [Max 1/week] |

## Pipeline Infrastructure

[Technical components of the notification pipeline.

GUIDANCE:
- Good: Specify event ingestion method, trigger evaluation engine, and delivery integrations with latency targets
- Bad: "We will use SendGrid and FCM"]

| Component | Technology | Configuration | Latency Target |
|-----------|-----------|--------------|---------------|
| Event ingestion | [e.g., SQS FIFO queue from app events] | [Max retention: 4 days; DLQ after 3 retries] | |
| Trigger evaluation | [e.g., Lambda function or scheduled job] | [Runs every 5 min for time-based; real-time for event-based] | [< 30s for event-based] |
| Email delivery | [e.g., SendGrid / Postmark] | [Dedicated IP; DKIM/SPF configured] | [< 2 min delivery] |
| Push delivery | [e.g., FCM + APNs via service] | [Silent push for background sync; visible for engagement] | [< 30s delivery] |
| In-app delivery | [e.g., Custom WebSocket / Intercom] | [Delivered when app is active] | [Real-time] |

## Frequency Capping and Quiet Hours

[Global and per-channel frequency rules.

GUIDANCE:
- Good: Specify exact caps as rolling window rules that apply before any notification is dispatched
- Bad: "Don't send too many notifications"]

| Rule | Scope | Limit | Window | Enforcement |
|------|-------|-------|--------|------------|
| Global cap | All channels | [Max 3 notifications] | [Per 24 hours per user] | Pre-dispatch check |
| Email marketing cap | Email only | [Max 1 marketing email] | [Per 24 hours per user] | Pre-dispatch check |
| Re-engagement cap | Re-engagement notifications | [Max 1 sequence] | [Per 30 days per user] | Campaign-level dedup |
| Quiet hours | All marketing channels | [No delivery] | [22:00–08:00 user local time] | Timezone-aware scheduler |

## Template System

[Template architecture and dynamic variable usage.

GUIDANCE:
- Good: List each base template with its variables and the A/B test variants planned at launch
- Bad: "Email templates will be designed"]

| Template ID | Name | Channel | Dynamic Variables | A/B Test Planned |
|------------|------|---------|------------------|-----------------|
| T001 | [e.g., Activation nudge email] | Email | [`{{first_name}}`, `{{activation_step_remaining}}`, `{{days_since_signup}}`] | [Subject line: "Complete setup" vs. "You're almost there"] |
| T002 | [e.g., Referral reward push] | Push | [`{{referrer_name}}`, `{{reward_amount}}`] | [Copy variant A vs. B] |

## Preference and Compliance

[User preference management and regulatory compliance.

GUIDANCE:
- Good: Specify which notification types users can opt out of, how opt-outs are honored, and which notifications are transactional (non-optional)
- Bad: "We will have an unsubscribe link"]

### Preference Categories

| Category | User-Controllable? | Default | Transactional? |
|----------|-------------------|---------|---------------|
| [Marketing emails] | Yes — opt-out | Opted in (with consent) | No |
| [Weekly digest] | Yes — opt-out | Opted in | No |
| [Referral notifications] | Yes — opt-out | Opted in | No |
| [Security alerts] | No | Always on | Yes |
| [Account billing] | No | Always on | Yes |

### Compliance Checklist

- [ ] CAN-SPAM: Physical address and one-click unsubscribe in all marketing emails
- [ ] GDPR: Consent captured at signup; unsubscribe honored within 10 business days
- [ ] SMS (if applicable): TCPA consent form with clear disclosure; STOP keyword handling
- [ ] Unsubscribe processing: Global unsubscribe suppresses all marketing within [X seconds/minutes]

## Performance Monitoring

[Metrics and alerting for the notification pipeline.

GUIDANCE:
- Good: Include specific alert thresholds that trigger investigation or mitigation
- Bad: "We will monitor delivery rates"]

| Metric | Target | Warning Alert | Critical Alert |
|--------|--------|--------------|----------------|
| Email delivery rate | [≥ 98%] | [< 97%] | [< 95%] |
| Email open rate | [≥ 20%] | [< 15%] | [< 10%] |
| Unsubscribe rate | [< 0.3%] | [> 0.4%] | [> 0.5% — pause sends] |
| Spam complaint rate | [< 0.05%] | [> 0.06%] | [> 0.08% — pause sends immediately] |
| Push delivery rate | [≥ 95%] | [< 90%] | [< 85%] |
| Pipeline processing lag | [< 30s for real-time] | [> 60s] | [> 5 min] |

## Recommendations

[Prioritized recommendations for pipeline launch and optimization.

GUIDANCE: Focus on deliverability risks, compliance gaps, and highest-ROI notification opportunities.]

- **P1**: [Critical launch blocker or compliance gap]
- **P2**: [Important optimization for engagement rate within first 30 days]
- **P3**: [Long-term channel expansion or personalization enhancement]

## Appendices

### A. Methodology

[Infrastructure stack, integration decisions, and compliance review notes.]

### B. Notification Performance Benchmarks by Industry

[Industry benchmarks used to calibrate performance targets for this product's category.]

| Channel | Industry | Open Rate | CTR | Unsubscribe Rate |
|---------|----------|-----------|-----|-----------------|
| Email | [SaaS B2B] | [22%] | [4%] | [0.2%] |
| Push | [Consumer app] | [7%] | [3%] | [1% opt-out] |
