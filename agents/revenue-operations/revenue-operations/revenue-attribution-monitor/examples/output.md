# Revenue Attribution Audit — Q1 2026

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Author | Revenue Operations |
| Attribution Model | Linear Multi-Touch |
| Overall Quality Score | 5.93 / 10 |
| Verdict | ATTRIBUTION_UNRELIABLE |
| Skill | revenue-attribution-monitor |

## Recommendation

**ATTRIBUTION_UNRELIABLE** — 2 channels (Paid Search and Events) have attribution coverage below 70%. Do NOT use current attribution data for Q1 budget reallocation decisions. Fix critical channels first, then re-audit before QBR.

---

## Channel Quality Summary

| Channel | Quality Score | Coverage | Status | Attributed Revenue |
|---|---|---|---|---|
| Content / SEO | 8.65 | 92% | HEALTHY | $310,000 |
| Outbound SDR | 8.00 | 88% | HEALTHY | $280,000 |
| Paid Search (Google Ads) | 5.50 | **68%** | **UNRELIABLE** | $420,000* |
| Events / Conferences | 4.25 | **55%** | **UNRELIABLE** | $190,000* |

*Revenue figures for unreliable channels are estimates only — actual attribution may differ significantly.

---

## Critical Issues

### Paid Search — Coverage 68% (UNRELIABLE)

| Dimension | Score |
|---|---|
| UTM Coverage | 5 |
| CRM Source Accuracy | 6 |
| Pixel Integrity | 4 |
| Dedup Accuracy | 7 |

**Issues:**
1. UTM tags missing on 3 active campaigns — fix immediately; tag all campaigns in Google Ads
2. Conversion pixel fires on thank-you page only — add form submit event trigger in GTM

**Impact:** $420K in attributed revenue is likely overstated. Fixing UTM gaps may reveal that 15-25% of "paid search" credit belongs to organic/direct.

---

### Events / Conferences — Coverage 55% (UNRELIABLE)

| Dimension | Score |
|---|---|
| UTM Coverage | 4 |
| CRM Source Accuracy | 5 |
| Pixel Integrity | 3 |
| Dedup Accuracy | 6 |

**Issues:**
1. Event badge scans not synced to CRM — configure Eventbrite/Cvent → HubSpot integration
2. No UTM tracking on post-event follow-up emails — add UTM parameters to all email campaigns
3. Pixel not deployed on event landing pages — deploy tracking before next event

**Impact:** $190K in events revenue is likely underattributed. Events channel is underrepresented in attribution.

---

## Remediation Priority

| Priority | Action | Owner | Deadline |
|---|---|---|---|
| 1 | Add UTM tags to all active Paid Search campaigns | Marketing | 3 days |
| 2 | Add form submit pixel trigger in GTM | Marketing Ops | 5 days |
| 3 | Configure event badge scan → CRM sync | RevOps | 1 week |
| 4 | Add UTM to all event follow-up email sequences | Marketing | 1 week |
| 5 | Deploy pixel on all event landing pages | Marketing Ops | 2 weeks |

Re-audit all channels after remediation. Do not present Q1 attribution data at QBR until Paid Search coverage reaches ≥ 85%.
