# Transactional Email Template Library: CollabSpace

## Metadata

| Field | Value |
|-------|-------|
| Date | 2026-03-29 |
| Author | Lifecycle Email Marketing Manager |
| Version | 1.0 |
| Status | Draft |
| Skill | transactional-email-designer |

## Executive Summary

Ten-template transactional email library for CollabSpace migrating from plain-text emails on a shared domain to branded, responsive HTML templates on a dedicated transactional subdomain (notify.collabspace.com). Expected to resolve the 8% spam placement issue and establish brand consistency at the highest-open-rate touchpoints.

## Template Inventory

| Template | Category | Trigger | Priority | Secondary CTA |
|----------|----------|---------|----------|--------------|
| Email verification | Authentication | New signup | Critical | No |
| Password reset | Authentication | User request | Critical | No |
| Team invitation | Notification | Admin invites member | High | No |
| Comment mention | Notification | @mention in comment | Medium | Yes — view thread |
| File shared | Notification | File shared with user | Medium | Yes — open file |
| Subscription confirmation | Confirmation | Plan selected | High | Yes — explore features |
| Payment receipt | Billing | Successful charge | High | No |
| Payment failure | Billing | Charge failed | Critical | No |
| Plan change confirmation | Billing | Upgrade or downgrade | High | No |
| Data export ready | System | Export job completed | Medium | No |

## Template Specifications

### Email Verification
- **Subject**: Verify your CollabSpace email
- **Preheader**: One click to get started — this link expires in 24 hours
- **Primary content**: Verification button with link, expiry notice (24h), and plain-text URL fallback
- **Secondary CTA**: None
- **Design note**: Minimal — logo, button, support link. No marketing content.

### Password Reset
- **Subject**: Reset your CollabSpace password
- **Preheader**: This link expires in 1 hour — if you didn't request this, ignore this email
- **Primary content**: Reset button, expiry notice (1h), security notice, plain-text URL fallback
- **Secondary CTA**: None
- **Design note**: Include "If you didn't request this" security reassurance above the fold.

### Team Invitation
- **Subject**: [Inviter name] invited you to [workspace name] on CollabSpace
- **Preheader**: Join your team and start collaborating
- **Primary content**: Inviter name and avatar, workspace name, accept button
- **Secondary CTA**: None
- **Design note**: Personalise with inviter's name and workspace context to increase accept rate.

### Comment Mention
- **Subject**: [Name] mentioned you in [project name]
- **Preheader**: "[First 60 chars of comment...]"
- **Primary content**: Comment preview with author avatar, project context
- **Secondary CTA**: View full thread
- **Design note**: Show enough comment context to be useful without requiring a click for casual reading.

### File Shared
- **Subject**: [Name] shared "[filename]" with you
- **Preheader**: Open in CollabSpace to view or download
- **Primary content**: File name, type icon, sharer name, file size
- **Secondary CTA**: Open file
- **Design note**: Include file type icon for quick visual recognition.

### Subscription Confirmation
- **Subject**: Welcome to CollabSpace [Plan name]
- **Preheader**: Your subscription is active — here's what's included
- **Primary content**: Plan name, price, billing cycle, next billing date, included features summary
- **Secondary CTA**: Explore your plan features
- **Design note**: This is the one transactional email where a secondary CTA to explore features is appropriate.

### Payment Receipt
- **Subject**: Your CollabSpace receipt — [amount]
- **Preheader**: Payment received for [billing period]
- **Primary content**: Amount, date, plan, billing period, payment method (last 4 digits), invoice link
- **Secondary CTA**: None

### Payment Failure
- **Subject**: Action needed: CollabSpace payment failed
- **Preheader**: Update your payment method to keep your workspace active
- **Primary content**: Failed amount, reason (if available), update payment button, grace period deadline
- **Secondary CTA**: None
- **Design note**: Urgency without alarm. State the deadline clearly and provide a direct link to billing settings.

### Plan Change Confirmation
- **Subject**: Your CollabSpace plan has been updated to [new plan]
- **Preheader**: Changes take effect immediately — here's what changed
- **Primary content**: Previous plan, new plan, what changed (features added/removed), new price, next billing date
- **Secondary CTA**: None

### Data Export Ready
- **Subject**: Your CollabSpace data export is ready
- **Preheader**: Download available for 7 days
- **Primary content**: Export type, file size, download link, expiry date (7 days)
- **Secondary CTA**: None

## Sender Configuration

| Setting | Value |
|---------|-------|
| Sending domain | notify.collabspace.com (NEW — dedicated transactional subdomain) |
| SPF | `v=spf1 include:_spf.emailprovider.com -all` |
| DKIM selector | `transactional._domainkey.notify.collabspace.com` (2048-bit) |
| DMARC | `v=DMARC1; p=quarantine; rua=mailto:dmarc@collabspace.com` |
| From address | CollabSpace <noreply@notify.collabspace.com> |
| Reply-to | support@collabspace.com (for actionable emails) |

## Rendering Test Plan

| Client | Platform | Priority |
|--------|----------|----------|
| Gmail (web) | Desktop | Critical |
| Gmail (app) | iOS, Android | Critical |
| Outlook 365 | Desktop | High |
| Apple Mail | macOS, iOS | High |
| Yahoo Mail | Web | Medium |
| Samsung Mail | Android | Medium |

## Recommendations

1. **P1**: Migrate transactional sends to notify.collabspace.com immediately to isolate from marketing domain reputation. This should resolve the 8% spam placement issue.
2. **P1**: Deploy SPF, DKIM, and DMARC on the new subdomain before sending the first email.
3. **P2**: Implement responsive HTML templates with the single-column, 600px layout. Test across the 6 clients listed above.
4. **P2**: Add BIMI record with CollabSpace logo to display brand icon in Gmail inbox.
5. **P3**: Set up weekly deliverability monitoring dashboard tracking inbox placement rate per template type.
