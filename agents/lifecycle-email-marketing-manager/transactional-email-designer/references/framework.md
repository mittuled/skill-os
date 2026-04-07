# Framework: Transactional Email Designer

Defines design principles and standards for transactional emails that reinforce brand trust.

## Transactional Email Taxonomy

| Category | Examples | Priority | Secondary CTA Allowed |
|----------|---------|----------|----------------------|
| Authentication | Password reset, email verification, 2FA codes | Critical | No |
| Confirmation | Purchase receipt, subscription confirmation, booking | High | Yes (one) |
| Notification | Usage alert, team invite, comment mention | Medium | Yes (one) |
| Billing | Invoice, payment failure, plan change | High | No |
| System | Maintenance notice, security alert, data export ready | High | No |

## Design System Requirements

| Element | Specification |
|---------|--------------|
| Header | Brand logo (max 120px wide), no navigation links |
| Typography | System font stack for fast rendering; 16px body, 14px secondary |
| Colours | Brand primary for CTAs only; neutral palette for body; WCAG AA contrast |
| Layout | Single column, 600px max width, responsive |
| Footer | Company name, address (CAN-SPAM), unsubscribe link (marketing emails only), support link |
| Sender | Dedicated transactional subdomain (e.g., notify.company.com) |

## Deliverability Standards

| Requirement | Standard |
|-------------|---------|
| SPF | Configured for transactional sending domain |
| DKIM | 2048-bit key, aligned with From domain |
| DMARC | p=quarantine minimum on transactional subdomain |
| Sending domain | Separate from marketing email domain |
| Inbox placement | >99% for authentication and billing categories |
| Bounce handling | Hard bounces suppressed within 1 send; soft bounces retried 3x over 24h |

## Content Rules

1. **Essential information first**: the primary content (reset link, receipt total, alert detail) appears above the fold
2. **No marketing content in critical emails**: authentication and billing emails contain zero promotional content
3. **One secondary CTA maximum**: confirmation and notification emails may include one related action
4. **Plain text alternative**: every transactional email includes a readable plain-text version
5. **Accessible**: all images have alt text; links have descriptive text (not "click here")
