# Email Deliverability Health — mail.meridianai.com

| Field | Value |
|---|---|
| Company | Meridian AI |
| Sending Domain | mail.meridianai.com |
| Score | 67/100 |
| Grade | C |
| Verdict | ACCEPTABLE |
| Issues Found | 4 |
| Criteria Passing | 8 |
| Skill | email-deliverability-manager |

## Dimension Scores

| Dimension | Score | Weight | Weighted Contribution |
|---|---|---|---|
| Sender Authentication | 67% | 25 | 17/25 |
| List Hygiene | 100% | 30 | 30/30 |
| Sending Practices | 58% | 25 | 15/25 |
| Engagement | 88% | 20 | 18/20 |
| **Total** | | **100** | **80/100** |

Wait — recalculating correctly:
- Sender Auth: SPF✓ DKIM✓ DMARC✗ → 17/25 points → 68% → weighted: 17
- List Hygiene: all pass → 30/30 → weighted: 30
- Sending Practices: warmup✗ consistent✓ double-optin✓ → 17/25 → 68% → weighted: 17
- Engagement: open✓ click✓ inactive✗ → 14/20 → 70% → weighted: 14

**Adjusted Total: 78/100 — Grade B (GOOD)**

## Current Metrics

| Metric | Value | Threshold | Status |
|---|---|---|---|
| Hard Bounce Rate | 1.8% | <2.0% | PASS |
| Unsubscribe Rate | 0.4% | <0.5% | PASS |
| Spam Complaint Rate | 0.08% | <0.1% | PASS |
| Open Rate | 24.0% | >20% | PASS |
| Click Rate | 2.5% | >2.0% | PASS |

## Issues (4 Criteria Failing)

| Issue | Dimension | Risk | Recommended Action |
|---|---|---|---|
| DMARC policy not set | Sender Authentication | HIGH | Add DMARC record: `v=DMARC1; p=quarantine; rua=mailto:dmarc@meridianai.com` — do this before the launch campaign |
| Domain warmup incomplete | Sending Practices | MEDIUM | Domain warmed only 3 weeks — limit campaign send to 2,000/day maximum until 6-week warmup is complete |
| Inactive contacts not suppressed | Engagement | MEDIUM | Suppress contacts with no opens/clicks in 90+ days before launch — improves sender score |

## Strengths (8 Criteria Passing)

- SPF configured
- DKIM configured
- Hard bounce rate within threshold (1.8%)
- Unsubscribe rate within threshold (0.4%)
- Spam complaint rate within threshold (0.08%)
- Consistent send volume
- Double opt-in in use
- Open rate above target (24%)
- Click rate above target (2.5%)

## Pre-Launch Recommendations

### Must Do Before Campaign (Blocking)
1. **DMARC record:** Add `v=DMARC1; p=quarantine; rua=mailto:dmarc@meridianai.com` to DNS. Gmail and Yahoo now require DMARC for bulk senders (>5,000/day). Without it, the 12,000-send campaign risks significant inbox-to-spam filtering.
2. **Suppress inactive contacts:** Remove contacts with no engagement in 90+ days from the launch send list. Sending to cold contacts on a warming domain will damage sender score.

### Recommended Before Campaign
3. **Limit send volume:** Given incomplete warmup, send the 12,000-contact campaign over 6 days (2,000/day) rather than all at once.

### Monitor During Campaign
4. Set up DMARC reporting (once configured) to catch authentication failures in real time.
