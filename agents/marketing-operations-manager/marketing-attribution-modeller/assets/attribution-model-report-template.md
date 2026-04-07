# Marketing Attribution Model Report

**Version**: 1.0  
**Owner**: Marketing Operations Manager  
**Reporting Period**: [Q? YYYY] or [Month YYYY]  
**Prepared**: YYYY-MM-DD  
**Distribution**: VP Marketing, CRO, CFO, Demand Gen, Finance  

---

## 1. Executive Summary

[2–3 sentences: key findings, top-performing channels by attributed pipeline, and any model changes this period.]

**Total Attributed Pipeline This Period**: $[X]M  
**Closed-Won Revenue (Marketing Influenced)**: $[X]M  
**Marketing-Sourced Pipeline %**: [X]% of total pipeline  

---

## 2. Attribution Model in Use

| Model | Description | When Applied |
|-------|-------------|-------------|
| First Touch | 100% credit to the first marketing touchpoint | Used for Awareness / ToFu channel decisions |
| Last Touch | 100% credit to the final touchpoint before conversion | Used for closing channel decisions |
| Linear | Equal credit across all touchpoints | Used for full-funnel decisions |
| **W-Shaped (Primary)** | 30% first touch / 30% lead creation / 30% opp creation / 10% other | **Default model for pipeline attribution** |
| Time Decay | More credit to recent touchpoints | Used for short sales cycles (<30 days) |
| Data-Driven (ML) | Statistical credit based on conversion patterns | Used when sufficient data volume (>1,000 conversions/mo) |

**Active Model**: [W-Shaped / Other] — [rationale for selection]

---

## 3. Pipeline Attribution by Channel

### W-Shaped Attribution

| Channel | Touches | Attributed Pipeline | % of Total | Attributed Revenue | CAC (est.) |
|---------|---------|--------------------|-----------|--------------------|-----------|
| Paid Search | [X] | $[X]K | [X]% | $[X]K | $[X] |
| Paid Social (LinkedIn) | [X] | $[X]K | [X]% | $[X]K | $[X] |
| Organic Search / SEO | [X] | $[X]K | [X]% | $[X]K | $[X] |
| Content / Gated Assets | [X] | $[X]K | [X]% | $[X]K | $[X] |
| Email (Nurture) | [X] | $[X]K | [X]% | $[X]K | $[X] |
| Events / Webinars | [X] | $[X]K | [X]% | $[X]K | $[X] |
| Direct / Dark Social | [X] | $[X]K | [X]% | $[X]K | $[X] |
| Partner / Referral | [X] | $[X]K | [X]% | $[X]K | $[X] |
| Outbound / SDR | [X] | $[X]K | [X]% | $[X]K | $[X] |
| **Total** | **[X]** | **$[X]M** | **100%** | **$[X]M** | **$[X]** |

---

## 4. First-Touch vs Last-Touch Comparison

| Channel | First-Touch Pipeline | Last-Touch Pipeline | Delta | Insight |
|---------|---------------------|--------------------|----|---------|
| Paid Search | $[X]K | $[X]K | [+/-X]% | [e.g. Strong awareness driver; closes via organic] |
| Paid Social | $[X]K | $[X]K | [+/-X]% | [e.g. Strong awareness; rarely last touch] |
| Events | $[X]K | $[X]K | [+/-X]% | [e.g. Strong last touch; deal accelerator] |
| Email | $[X]K | $[X]K | [+/-X]% | [e.g. Mid-funnel nurture; rarely first or last] |

---

## 5. Campaign-Level Attribution

### Top 10 Campaigns by Attributed Pipeline (W-Shaped)

| Rank | Campaign | Type | Spend | Attributed Pipeline | ROI |
|------|----------|------|-------|--------------------|----|
| 1 | [Campaign name] | [Paid / Event / Content] | $[X]K | $[X]K | [X]x |
| 2 | [Campaign name] | | $[X]K | $[X]K | [X]x |
| 3 | [Campaign name] | | $[X]K | $[X]K | [X]x |
| 4 | [Campaign name] | | $[X]K | $[X]K | [X]x |
| 5 | [Campaign name] | | $[X]K | $[X]K | [X]x |

---

## 6. Multi-Touch Path Analysis

### Most Common Paths to Closed-Won

| Path | Frequency | Avg Deal Size | Avg Sales Cycle |
|------|-----------|--------------|----------------|
| Paid Search → Demo Request → Closed Won | [X]% | $[X]K | [X] days |
| Content Download → Webinar → SDR → Closed Won | [X]% | $[X]K | [X] days |
| Event → Email Nurture → Demo Request → Closed Won | [X]% | $[X]K | [X] days |
| Organic → Pricing Page → Demo → Closed Won | [X]% | $[X]K | [X] days |

---

## 7. Model Limitations & Caveats

| Limitation | Impact | Mitigation |
|------------|--------|-----------|
| Dark social / word-of-mouth not captured | Undercount of brand influence | Self-reported "how did you hear" survey at demo |
| Offline touchpoints (field sales, events) have partial tracking | Attribution gap for enterprise deals | Manual UTM tagging; event check-in data synced to CRM |
| Cookie deprecation affecting cross-device tracking | Inflated direct traffic | First-party data strategy; server-side tagging in progress |
| Short attribution window (90 days) for long sales cycles | Misses early-funnel influence on >90-day deals | Extended window analysis run quarterly |

---

## 8. Recommendations

1. **Increase investment in [Channel A]** — Highest ROI channel; currently underfunded vs contribution.
2. **Reduce spend on [Channel B]** — High spend, low attributed pipeline; reassess audience targeting.
3. **Expand attribution window to 180 days** — [X]% of enterprise deals exceed current 90-day window.
4. **Instrument [offline touchpoint]** — Currently a black-box; CRM integration in progress.

---

## 9. Methodology Notes

- Data source: [Salesforce + HubSpot / Marketo / other]
- Attribution tool: [Rockerbox / Northbeam / Triple Whale / custom]
- Date range: [Start] – [End]
- Deals included: Closed-won + open opportunities created in period
- Minimum touchpoints required for attribution: 1
- Touchpoint lookback window: [90 / 180] days
