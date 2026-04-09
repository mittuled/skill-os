---
name: transactional-email-designer
description: Designs transactional emails that reinforce brand trust and drive secondary engagement at the highest-open-rate touchpoint.
department: marketing
agent: lifecycle-email-marketing-manager
version: 1.0.0
complexity: simple
related-skills: []
triggers:
  - "design transactional emails"
  - "build transactional email templates"
  - "order confirmation email"
  - "system notification email"
  - "transactional email audit"
---

# transactional-email-designer

## Agent

L2 lifecycle and email marketing manager responsible for onboarding sequences, nurture campaigns, retention emails, re-engagement, and transactional email design.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)

## Skill Description

Designs receipt, confirmation, and notification emails that reinforce brand identity while delivering essential information clearly and driving secondary engagement actions.

## When to Use

- A new product feature generates transactional events that need email notifications.
- Existing transactional emails are plain-text or off-brand and need design upgrades.
- Deliverability audits reveal transactional emails landing in spam or rendering poorly.
- The product team adds a new user action that triggers a confirmation or receipt.

## Workflow

1. Inventory all transactional email types: receipts, confirmations, password resets, usage alerts, and billing notifications. Map each to its trigger event.
2. Define the design system for transactional emails: brand-consistent header, typography, colour palette, and footer that distinguishes them from marketing emails.
3. Write copy for each template: lead with the essential information, keep it scannable, and include one secondary CTA where appropriate.
4. Build responsive HTML templates that render correctly across major email clients and devices.
5. Configure sender reputation settings: use a dedicated transactional subdomain and authenticate with SPF, DKIM, and DMARC.
6. Test each template across email clients using a rendering tool. Fix layout breaks before launch.
7. Deploy templates and monitor deliverability metrics: inbox placement, open rates, and bounce rates for the first week.

## Anti-Patterns

- **Stuffing transactional emails with marketing content.** *Why*: Overloading receipts with promotions violates user expectations, risks spam complaints, and can trigger CAN-SPAM issues.
- **Using the same sending domain for transactional and marketing emails.** *Why*: Marketing spam complaints drag down the domain reputation, causing critical transactional emails to land in spam.
- **Skipping responsive design testing.** *Why*: Transactional emails have the highest open rates; a broken layout on mobile wastes the most-seen brand touchpoint.

## Output

**Success artifacts:**
- Transactional email template library with responsive HTML
- Sender authentication configuration documentation
- Deliverability baseline report for each transactional email type

**Failure reporting:**
- Flag deliverability drops or rendering failures within 24 hours of deployment
- Escalate transactional emails landing in spam to the marketing lead immediately

## Related Skills

*No related skills defined yet.*
