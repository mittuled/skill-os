---
name: notification-pipeline-builder
description: >
  This skill builds notification pipelines for user engagement and retention.
  Use when asked to set up email notifications, push notifications, or in-app
  messaging. Also consider when retention metrics show drop-off that
  notifications could address. Suggest when the user has no automated
  re-engagement system.
department: data-growth
agent: growth-engineer
version: 1.0.0
complexity: medium
related-skills:
  - ../onboarding-engineer/SKILL.md
  - ../growth-loop-activator/SKILL.md
  - ../referral-engine-builder/SKILL.md
---

# notification-pipeline-builder

## Agent: Growth Engineer

L2 growth engineer (Nx) responsible for growth instrumentation, metrics dashboards, funnel analysis, and growth loop activation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

Builds notification pipelines across email, push, and in-app channels to drive user engagement, retention, and re-activation through event-triggered and scheduled communications.

## When to Use

- When the product needs automated notifications to drive engagement (activity digests, milestone celebrations, social triggers) or retention (inactivity nudges, feature announcements).
- When a growth loop requires re-engagement notifications to close the loop (referral invites, content notifications).
- When onboarding flows need drip sequences to guide new users through activation milestones.

## Workflow

1. **Channel and Trigger Design**: Define notification channels (email, push, in-app, SMS), trigger events (user actions, time-based, system events), and targeting rules (user segments, frequency caps, quiet hours). Deliverable: notification architecture document.
2. **Pipeline Infrastructure**: Build the notification pipeline: event ingestion, trigger evaluation, template rendering, channel delivery, and delivery tracking. Integrate with email provider (SendGrid, Postmark), push service (FCM, APNs), and in-app messaging. Deliverable: working notification pipeline.
3. **Template System**: Build a template system supporting dynamic content, personalization variables, and A/B test variants. Ensure templates render correctly across email clients and devices. Deliverable: template system with base templates.
4. **Preference and Compliance**: Implement user notification preferences, unsubscribe handling, frequency capping, and compliance requirements (CAN-SPAM, GDPR consent). Deliverable: preference management system.
5. **Monitoring and Optimization**: Instrument delivery metrics (sent, delivered, opened, clicked, converted) and build a notification performance dashboard. Set up alerts for delivery failures and unusual unsubscribe rates. Deliverable: notification analytics dashboard.

## Anti-Patterns

- **Notifications without frequency caps**: Sending unlimited notifications without per-user rate limiting. *Why*: notification fatigue drives unsubscribes and app deletions, permanently losing the re-engagement channel.
- **Batch-only notifications**: Building only scheduled batch sends without event-triggered real-time notifications. *Why*: event-triggered notifications (e.g., "someone liked your post") have dramatically higher engagement than scheduled digests.
- **No unsubscribe path**: Launching notifications without proper unsubscribe handling. *Why*: beyond being illegal under CAN-SPAM, missing unsubscribe increases spam complaints which damages sender reputation and deliverability.

## Output

**On success**: Produces a working notification pipeline with channel integrations, template system, preference management, and analytics dashboard. Delivered to the Growth Lead with performance metrics.

**On failure**: Report which channels or integrations could not be completed (e.g., push certificate issues, email domain verification), what partial pipeline is functional, and what dependencies remain. Escalate to Growth Lead.

## Related Skills

- [`onboarding-engineer`](../onboarding-engineer/SKILL.md) -- Onboarding flows use notification pipelines for drip sequences.
- [`growth-loop-activator`](../growth-loop-activator/SKILL.md) -- Growth loops rely on notifications to close the re-engagement stage.
