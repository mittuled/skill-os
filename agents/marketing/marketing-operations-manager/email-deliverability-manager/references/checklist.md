# Email Deliverability Checklist

Reference checklist for maintaining inbox placement rates, managing sender reputation, and handling bounce and complaint hygiene.

---

## 1. DNS Authentication Setup

Complete before sending any commercial email from a domain.

- [ ] **SPF record** published in DNS (`TXT` record on sending domain)
  - Includes all authorised sending IPs and services (ESP, CRM, transactional)
  - Uses `-all` (hard fail) not `~all` (soft fail) for production domains
  - Record has fewer than 10 DNS lookups (SPF limit)
- [ ] **DKIM** configured for all sending domains
  - Key length ≥ 2048 bits
  - DKIM selector and public key published in DNS
  - Signed by ESP and verified with a tool (MXToolbox, mail-tester.com)
- [ ] **DMARC** policy published (`TXT` record on `_dmarc.<domain>`)
  - Policy at least `p=quarantine`; escalate to `p=reject` after monitoring period
  - `rua` address set to receive aggregate reports
  - `ruf` address set to receive forensic reports (if privacy-compliant)
  - DMARC report monitoring configured (Postmark, Valimail, or equivalent)
- [ ] **BIMI** record configured (optional, enhances inbox trust display)
  - Requires DMARC at `p=reject` and VMC certificate for major mailbox providers

---

## 2. Sending Infrastructure

- [ ] Dedicated sending IPs provisioned for marketing email (separate from transactional)
- [ ] IP warm-up plan completed before high-volume sends
  - Week 1: ≤500 emails/day to highest-engagement segment
  - Week 2: ≤2,000 emails/day
  - Week 3: ≤5,000 emails/day
  - Week 4+: Scale in 50% increments based on reputation metrics
- [ ] Separate subdomains for marketing and transactional (`mail.domain.com` vs `notify.domain.com`)
- [ ] List-Unsubscribe header (`List-Unsubscribe-Post`) enabled in ESP
- [ ] One-click unsubscribe functional and tested (required for Google/Yahoo bulk senders as of 2024)
- [ ] Physical mailing address included in footer (CAN-SPAM / CASL requirement)

---

## 3. List Hygiene

Run before every major send; run full audit quarterly.

### Pre-Send

- [ ] Remove hard bounces from prior sends (bounce rate target: <2%)
- [ ] Remove known spam traps (use hygiene service: ZeroBounce, NeverBounce, BriteVerify)
- [ ] Remove contacts who have not opened or clicked in 6+ months (sunset policy)
- [ ] Remove contacts with unsubscribe or complaint flag set
- [ ] Validate all newly imported addresses before first send
- [ ] De-duplicate list — remove duplicate email addresses

### Quarterly Audit

- [ ] Run full list through email validation service
- [ ] Identify and remove role-based addresses (`info@`, `admin@`, `sales@`) from marketing sends
- [ ] Review and action "soft bounce" accumulations (3+ soft bounces = treat as hard bounce)
- [ ] Review unengaged segment (no open/click in 90 days) — re-engagement campaign or sunset
- [ ] Confirm consent records are current and documented (GDPR / CASL)

---

## 4. Content and Template Checks

- [ ] Subject line: ≤60 characters; no ALL CAPS; no spam trigger words (free, urgent, click now)
- [ ] Preheader text set and relevant (≤90 characters)
- [ ] Plain-text version matches HTML content
- [ ] HTML:text ratio — no all-image emails; maintain ≥25% readable text
- [ ] All links functional and using tracked UTM parameters
- [ ] Unsubscribe link prominent and working in one click
- [ ] No link shorteners in email body (flagged by spam filters)
- [ ] Sender name and From address match brand (no `noreply@` for marketing sends)
- [ ] Images have ALT text
- [ ] Email renders correctly in top 5 clients: Gmail, Apple Mail, Outlook, mobile iOS, mobile Android

---

## 5. Sending Behaviour

- [ ] Send time-of-day matches audience timezone (B2B: Tue–Thu, 9–11am local time)
- [ ] Send volume consistent day-over-day (avoid sudden spikes >5× baseline)
- [ ] Sending frequency does not exceed audience preference (check against suppression flags)
- [ ] Segment sends by engagement tier — engaged contacts first, unengaged last or withheld

---

## 6. Monitoring and Alerting

Set up alerts. Review metrics within 24 hours of every major send.

| Metric | Healthy Range | Warning Threshold | Action Required |
|--------|-------------|-----------------|----------------|
| Delivery rate | ≥98% | <97% | Investigate bounces; check blacklists |
| Open rate | ≥20% (B2B) | <15% | Review subject line; check spam folder placement |
| Click-to-open rate | ≥10% | <5% | Review content relevance and CTAs |
| Hard bounce rate | <0.5% | >1% | Remove bounces; validate list before next send |
| Soft bounce rate | <2% | >3% | Review infrastructure; check receiving server issues |
| Spam complaint rate | <0.08% | >0.1% | Immediately reduce volume; review segmentation |
| Unsubscribe rate | <0.2% | >0.5% | Review content relevance and frequency |

- [ ] Google Postmaster Tools connected and monitored
- [ ] Microsoft SNDS (Smart Network Data Services) account active
- [ ] Blacklist monitoring configured (MXToolbox, Spamhaus manual check)
- [ ] ESP reputation dashboard reviewed weekly

---

## 7. Bounce Handling Workflow

- [ ] Hard bounce → suppress immediately; remove from all future sends
- [ ] Soft bounce (1st) → monitor; do not suppress
- [ ] Soft bounce (3rd consecutive) → suppress; treat as inactive
- [ ] Complaint (FBL report) → suppress immediately; add to global suppression list
- [ ] Spam trap hit → investigate source of address; remove list segment that sourced it

---

## 8. Compliance

- [ ] CAN-SPAM: physical address in footer; honour opt-outs within 10 business days
- [ ] GDPR: consent documented; right-to-erasure process in place
- [ ] CASL (Canada): express or implied consent recorded with timestamp
- [ ] CCPA: opt-out of sale/sharing link present if California contacts in list
- [ ] Consent timestamps and source recorded in CRM for all contacts
