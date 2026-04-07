# Framework: email-deliverability-manager

Defines sender reputation factors, authentication standards, list hygiene thresholds, domain warmup protocol, and ISP-specific guidance for maintaining high email deliverability.

## Deliverability Health Thresholds

| Metric | Healthy | At Risk | Critical — Act Immediately |
|--------|---------|---------|---------------------------|
| Inbox placement rate | ≥ 95% | 90–94% | < 90% |
| Hard bounce rate | < 0.5% | 0.5–2% | > 2% |
| Soft bounce rate | < 2% | 2–5% | > 5% |
| Spam complaint rate | < 0.08% | 0.08–0.1% | > 0.1% (Google/Yahoo threshold) |
| Unsubscribe rate | < 0.5% | 0.5–1% | > 1% |
| Open rate (engagement baseline) | > 20% | 15–20% | < 15% |
| Sender reputation score (Postmaster) | High | Medium | Low / Bad |

## Authentication Protocol Standards

All sending domains must have these records correctly configured and aligned:

| Record | Purpose | Required Standard | Verification Tool |
|--------|---------|------------------|------------------|
| SPF (Sender Policy Framework) | Authorizes IP addresses to send on behalf of domain | All sending IPs listed; record does not exceed 10 DNS lookups | MXToolbox SPF Lookup |
| DKIM (DomainKeys Identified Mail) | Cryptographic signature proving message integrity | 2048-bit key minimum; selector published and active | MXToolbox DKIM Lookup |
| DMARC (Domain-based Message Authentication) | Policy for failed SPF/DKIM; enables reporting | Policy set to `quarantine` or `reject` (not `none`); RUA reports configured | Google Postmaster, DMARC Analyzer |
| BIMI (Brand Indicators for Message Identification) | Displays brand logo in inbox | VMC certificate required; DMARC at `enforce` level | BIMI Inspector (optional but preferred) |

**Alignment requirement**: SPF and DKIM must both align to the From: domain, not just pass for the sending infrastructure domain.

## Domain Warmup Schedule

For new sending domains or IPs, follow a graduated ramp-up:

| Week | Daily Volume Cap | Engagement Requirement | Action if Bounce Rate Spikes |
|------|----------------|----------------------|------------------------------|
| 1 | 500 emails/day | Send to highest-engagement segment only | Pause; review list quality |
| 2 | 1,000 emails/day | Maintain > 25% open rate | Reduce volume; investigate |
| 3 | 3,000 emails/day | Maintain > 20% open rate | — |
| 4 | 10,000 emails/day | Maintain > 15% open rate | — |
| 5–6 | 25,000 emails/day | Maintain > 15% open rate | — |
| 7–8 | 50,000 emails/day | Standard monitoring | — |
| 9+ | Full volume | Standard monitoring | — |

**Rule**: Never increase volume more than 3× in a single week. Always start with your most-engaged contacts.

## List Hygiene Cadence

| Action | Frequency | Threshold | Tool |
|--------|-----------|-----------|------|
| Hard bounce suppression | After every send | Immediate — remove within 24 hours of bounce | ESP native |
| Spam trap detection | Monthly | Any volume; use list cleaning service | ZeroBounce, NeverBounce, Kickbox |
| Unengaged contact sunset | Quarterly | No opens in 90 days → re-engagement campaign → suppress if no response in 30 days | ESP segment |
| Role-based address removal | At import | Remove info@, admin@, postmaster@ addresses | Validation at point of capture |
| Disposable email removal | At import | Block known disposable domains | ZeroBounce or similar |
| Full list audit | Semi-annual | Remove all contacts with 12+ months no engagement | Manual segment + suppression |

## ISP-Specific Reputation Monitoring

| ISP | Monitoring Tool | Key Signal | Access |
|-----|----------------|------------|--------|
| Google (Gmail) | Google Postmaster Tools | Domain reputation, spam rate, authentication status | Free; requires domain verification |
| Microsoft (Outlook/Hotmail) | Microsoft SNDS (Smart Network Data Services) | IP reputation, complaint rate | Free; IP registration required |
| Yahoo/AOL | Yahoo Postmaster | Complaint feedback loop | Free; application required |
| Apple (iCloud Mail) | No public tool | Monitor via ESP inbox placement data | — |
| Comcast / regional ISPs | ReturnPath / Validity | Aggregate reputation data | Paid service |

## Reputation Remediation Steps

If reputation degrades to Medium or Low:

1. **Pause high-volume sends** immediately to avoid further damage
2. **Identify affected IP or domain** using ISP postmaster tools
3. **Diagnose root cause**: Check spam complaint rate, bounce rate, authentication failures, and content triggers
4. **Execute emergency list hygiene**: Remove all unengaged contacts; validate remaining list
5. **Reduce sending volume** to warmup week 2–3 levels
6. **File postmaster feedback loop** requests with major ISPs
7. **Request delisting** from blacklists via MX Toolbox blacklist checker if applicable
8. **Rebuild reputation gradually** over 4–6 weeks before returning to full volume
