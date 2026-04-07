# Framework: Peer Review Platform Manager

Defines the platform strategy, review generation methodology, velocity targets, response protocols, and sentiment tracking model for G2, Capterra, TrustRadius, and related peer review platforms.

## Platform Overview

| Platform | Primary Audience | Buyer Profile | Review Volume Importance | Key Categories |
|---------|----------------|---------------|------------------------|----------------|
| **G2** | B2B software buyers | Mid-market to enterprise; product-led | Very high — G2 categories drive analyst-style shortlists | Grid Reports, Category Leader badges |
| **Capterra** | SMB to mid-market buyers | Value-conscious; feature checklist buyers | High for SMB/mid-market categories | Top Rated, Best Value badges |
| **TrustRadius** | Enterprise and mid-market | Security and compliance-conscious; detailed evaluators | High for enterprise technical categories | TrustRadius Top Rated |
| **GetApp** | SMB software buyers | Often Gartner-owned, overlaps with Capterra | Medium — traffic lower than G2 | Best Functionality badges |
| **Software Advice** | SMB buyers needing guidance | Decision-support focused | Lower — complements Capterra | Less critical standalone |

### Platform Prioritisation Framework

| Company Stage | Primary Platform | Secondary Platform | Rationale |
|-------------|----------------|------------------|-----------|
| Seed / Series A | Capterra | G2 | Lower review bar to achieve badge; SMB audience matches early customers |
| Series B / C | G2 | TrustRadius | Enterprise buyers increasingly active; G2 Grid placement matters for deals |
| Enterprise market focus | G2 + TrustRadius | Capterra | Enterprise buyers research on G2 and TrustRadius; peer security validation critical |
| IPO / public company | All major platforms | Software Advice | Comprehensive coverage required; buyers check multiple platforms |

---

## Review Generation Strategy

### Review Solicitation Triggers

High-intent reviews come from customers at moments of peak satisfaction. Target these moments:

| Trigger | Timing | Mechanism | Expected Conversion |
|---------|--------|-----------|-------------------|
| Successful onboarding completion | Within 30 days of go-live | CS email or in-app prompt | 15–25% |
| Positive QBR (Quarterly Business Review) | Immediately following QBR | CS personal email with review link | 20–30% |
| NPS Promoter response (score 9–10) | Within 48 hours of survey | Automated follow-up with review link | 25–35% |
| Contract renewal | Within 1 week of renewal | CS personal email | 15–20% |
| Product milestone achievement | After first major outcome | In-app trigger or CS email | 10–20% |
| Customer expansion (upsell/cross-sell) | Within 2 weeks of expansion | CS or AM personal email | 20–30% |

### Review Solicitation Rules

| Rule | Detail |
|------|--------|
| Never solicit from detractors | Check NPS / CS health score before outreach; skip customers with score <7 |
| No incentive-for-review schemes | Offering gift cards or discounts in exchange for reviews violates G2, Capterra, and TrustRadius terms; platforms penalise this |
| Incentive programmes (compliant) | Platforms allow charitable donations or platform gift cards given after the review is published, not as quid pro quo |
| Personalise outreach | Template-based mass emails to the entire customer list yield <5% conversion; personalised CS emails yield 15–30% |
| One platform at a time | Avoid asking a customer to review on multiple platforms in the same outreach; platform hopping signals manipulation |
| Verified purchase requirement | G2 requires LinkedIn verification or email domain verification; ensure customers can complete this |

---

## Review Velocity Targets

Review recency is a ranking factor on G2 and Capterra. Stale reviews (>12 months old) receive lower weight.

| Platform | Minimum Monthly Reviews | Badge Threshold (typical) | Category Leader Threshold |
|---------|------------------------|--------------------------|--------------------------|
| G2 | 2–3 per month to maintain recency | 10 reviews + 3.5 star avg | 25–50+ reviews, 4.0+ avg, category volume-dependent |
| Capterra | 1–2 per month | 10 reviews | 20+ reviews, 4.5+ avg |
| TrustRadius | 1 per month | 10 reviews + TrustRadius scoring | 25+ reviews |

### Seasonal Review Campaign Planning

| Period | Focus | Notes |
|--------|-------|-------|
| Q1 (January–March) | Annual refresh | Customers starting new budget cycles; renewal season for many SaaS products |
| Q2 (April–June) | Mid-year push | NPS survey cycle aligns with review campaigns |
| Q3 (July–September) | Low volume period | Reduce campaign frequency; maintain momentum with QBR-triggered reviews |
| Q4 (October–December) | Badge campaign | G2 Fall Reports and Capterra shortlists publish; maximise review volume for badges |

---

## Response Protocol

All reviews — positive and negative — require a response.

### Response by Sentiment

| Sentiment | Response Goal | Response Time | Template |
|-----------|--------------|--------------|---------|
| 5-star positive | Thank + reinforce key values | Within 1 week | Thank for specific feedback; restate company's key value dimension mentioned |
| 4-star positive with suggestions | Thank + acknowledge improvement area | Within 3 days | Acknowledge the specific improvement request; note it's been shared with product team |
| 3-star mixed | Empathise + problem solve | Within 48 hours | Validate the concern; offer to connect to CS for resolution; do not be defensive |
| 1–2 star negative | De-escalate + take offline | Within 24 hours | Acknowledge specific issue; apologise without admissions; offer personal follow-up |

### Response Don'ts

| Don't | Why |
|-------|-----|
| Do not copy/paste the same response to multiple reviews | Platforms and buyers notice; signals inauthentic engagement |
| Do not dispute factual claims publicly | Take disputes private; public arguments amplify the negative review |
| Do not offer compensation in public response | Signals that criticism can be monetised; violates platform terms |
| Do not reveal customer identity in response | Never confirm who the reviewer is even if obvious |
| Do not ignore negative reviews | Unresponded negative reviews signal to buyers that the company is unaccountable |

---

## Sentiment Tracking Model

Track review sentiment trends monthly at the platform and category level.

| Metric | What It Measures | Target | Alert Threshold |
|--------|-----------------|--------|----------------|
| Average rating (all platforms) | Overall customer satisfaction signal | 4.3+ | Drop below 4.0 on any major platform |
| Negative review rate | % of reviews rated 1–2 stars | <5% | >10% in any 30-day period |
| Review response rate | % of reviews receiving a company response | 100% | Any un-responded review >72 hours old |
| Dominant negative theme | Most common complaint topic | No single theme >20% of negative reviews | Any theme >30% signals systemic issue |
| Review recency score | % of reviews published within last 6 months | >50% of total review count | <30% = stale profile; launch review campaign |
| Competitive rating gap | Difference between company avg rating and top competitor avg | Within 0.2 stars | Company avg >0.5 stars below top competitor |

### Negative Theme Classification

| Theme Category | Internal Routing |
|---------------|-----------------|
| Onboarding / implementation difficulty | Customer Success + Professional Services |
| Missing feature / functionality | Product Management |
| Support quality / response time | Customer Support leadership |
| Pricing / value perception | Sales leadership + Marketing |
| Integration issues | Product / Engineering |
| Account management | Account Management leadership |
| Data security / compliance | Security / Legal |

---

## Platform Profile Optimisation Standards

A complete, current profile increases search visibility and trust.

| Profile Element | Update Frequency | Standard |
|----------------|-----------------|----------|
| Product description | Quarterly or on major positioning change | 200–400 words; current value proposition; no jargon |
| Feature list | Every major release | All current features listed; deprecated features removed |
| Screenshots / demo videos | Quarterly | Current UI only; no outdated screenshots |
| Integrations list | Every major integration release | All active integrations listed |
| Pricing information | On pricing changes | Accurate ranges or "contact for pricing" if custom |
| Profile logo / branding | On brand refresh | Current logo and brand colours |
| Categories listed | On new product line launch | Ensure correct category placement for discovery |
