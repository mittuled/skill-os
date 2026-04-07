# SEO Auditor Framework

Reference framework for comprehensive SEO audits covering technical health, keyword gap analysis, Core Web Vitals, and E-E-A-T signals.

## Technical SEO Checklist

### Crawlability and Indexation

| Check | Pass Criteria | Severity if Failed |
|-------|--------------|-------------------|
| robots.txt accessible | Returns 200, does not block key directories | Critical |
| XML sitemap present and valid | Sitemap URL returns 200, all URLs return 200 | High |
| Sitemap submitted to Search Console | Sitemap submitted and no errors reported | High |
| Noindex tags on correct pages | Noindex only on non-SEO pages (thank you, admin, duplicate) | Critical |
| Canonical tags consistent | Self-referencing canonicals on all canonical pages | High |
| Duplicate content rate | < 10% of indexed pages are near-duplicates | High |
| Thin content (< 300 words) | < 5% of indexed pages | Medium |
| Orphaned pages | < 5% of pages have zero internal links | Medium |

### Site Architecture

| Check | Pass Criteria | Severity if Failed |
|-------|--------------|-------------------|
| Click depth from homepage | All key pages reachable within 3 clicks | High |
| Internal link distribution | No page has fewer than 3 internal inbound links (excluding homepage) | Medium |
| Redirect chains | No redirect chains longer than 2 hops | High |
| Redirect loops | Zero redirect loops | Critical |
| Broken internal links (404) | Zero broken internal links | High |
| URL structure | All URLs are lowercase, hyphenated, descriptive, < 115 characters | Low |

### Technical Signals

| Check | Pass Criteria | Severity if Failed |
|-------|--------------|-------------------|
| HTTPS across all pages | 100% of pages served over HTTPS | Critical |
| HTTP to HTTPS redirect | All HTTP URLs redirect to HTTPS equivalent | Critical |
| Structured data (schema) | Key page types have valid schema (Article, Product, FAQPage, Organization) | Medium |
| Structured data errors | Zero critical schema errors in Google's Rich Results Test | High |
| Hreflang tags (if multi-language) | All hreflang tags reference valid URLs with reciprocal tags | High |
| Mobile usability | Zero mobile usability errors in Search Console | High |

---

## Keyword Gap Analysis Framework

### Intent Classification

Map all target keywords to intent categories before gap analysis:

| Intent Type | Searcher Goal | SERP Signals | Funnel Stage |
|------------|--------------|-------------|-------------|
| Informational | Learn / understand | Wikipedia, blog posts, how-to content | TOFU |
| Commercial | Compare / evaluate | Review sites, comparison pages, listicles | MOFU |
| Transactional | Buy / sign up | Product pages, pricing pages, trial CTAs | BOFU |
| Navigational | Find a specific brand | Brand pages, login pages | Existing customers |

### Keyword Prioritisation Matrix

| Priority Tier | Criteria | Action |
|-------------|---------|--------|
| Tier 1 — Win Now | High commercial intent, moderate difficulty (KD < 50), site already ranks 11–30 | Optimise existing content; push to page 1 |
| Tier 2 — Build For | High commercial intent, high difficulty (KD 50–80), competitor in top 5 | Create comprehensive content; build internal links |
| Tier 3 — Defend | Keywords site already ranks 1–5 for | Monitor; update content to maintain rankings |
| Tier 4 — Monitor | High difficulty (KD > 80), not currently ranking | Track; address in 6–12 month horizon |

### Competitor Keyword Gap Template

For each competitor, identify:
- Keywords competitor ranks 1–10 for where the site does not appear in top 20
- Estimated monthly search volume (use tool data)
- Keyword difficulty score (0–100)
- Intent classification
- Recommended content response (new article, optimise existing, landing page)

---

## Core Web Vitals Benchmarks

### Thresholds

| Metric | Good | Needs Improvement | Poor |
|--------|------|------------------|------|
| LCP (Largest Contentful Paint) | ≤ 2.5s | 2.5–4.0s | > 4.0s |
| CLS (Cumulative Layout Shift) | ≤ 0.1 | 0.1–0.25 | > 0.25 |
| INP (Interaction to Next Paint) | ≤ 200ms | 200–500ms | > 500ms |

### Common LCP Causes and Fixes

| Cause | Diagnosis | Fix |
|-------|----------|-----|
| Unoptimised hero image | LCP element is an image > 200KB | Compress, convert to WebP/AVIF, use `loading="eager"` and `fetchpriority="high"` |
| Render-blocking CSS | LCP delayed by stylesheet loading | Inline critical CSS; defer non-critical styles |
| Slow server response (TTFB > 600ms) | Network waterfall shows long first byte | Use CDN; implement server-side caching; optimise database queries |
| Client-side rendering | LCP element rendered by JavaScript | Move critical content to server-side rendering |

### Common CLS Causes and Fixes

| Cause | Diagnosis | Fix |
|-------|----------|-----|
| Images without dimensions | Layout shifts when image loads | Add explicit `width` and `height` attributes to all images |
| Dynamic content injection | Ads, banners, or banners inserted above existing content | Reserve space with min-height; inject content below existing elements |
| Web fonts causing FOUT | Text shifts when custom font loads | Use `font-display: swap`; preload critical fonts |

---

## E-E-A-T Assessment Framework

E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) is a quality signal framework used in Google's Search Quality Evaluator Guidelines.

### Experience Signals

Evidence that content was created by someone with first-hand experience with the topic.

| Signal | Strong | Adequate | Weak |
|--------|--------|---------|------|
| Original research or data | Own studies, surveys, proprietary data cited | References to third-party research with analysis | No original data; only aggregates existing sources |
| Product screenshots and demos | Real product UI, not stock images | Mix of real and generic visuals | Stock imagery only |
| Case study specificity | Named customers, specific metrics, before/after data | Anonymous case studies with metrics | Generic success stories with no data |

### Expertise Signals

Evidence that content creators have subject matter knowledge.

| Signal | Strong | Adequate | Weak |
|--------|--------|---------|------|
| Author credentials | Named authors with relevant job titles, bios, LinkedIn links | Named authors without credentials | No author attribution |
| About page | Detailed team page with individual bios | Company overview without team detail | No about page or team information |
| Content depth and accuracy | Content passes subject matter expert review; no factual errors | Minor inaccuracies; content covers topic adequately | Shallow coverage; factual errors present |

### Authoritativeness Signals

Evidence that the site and its authors are recognised as authorities by others.

| Signal | Strong | Adequate | Weak |
|--------|--------|---------|------|
| Referring domain count | > 500 unique referring domains | 100–500 | < 100 |
| Referring domain quality | Majority from DA 50+ sites; editorial placements | Mix of DA 30–50 sites; some directory links | Predominantly low-quality or spammy referring domains |
| Media mentions | Cited or quoted in industry publications | Listed in directories or review sites | No external mentions |
| Industry awards or recognition | Named in analyst reports, award lists | Self-reported awards | No external recognition |

### Trustworthiness Signals

Evidence that the site can be trusted with user data and intent.

| Signal | Strong | Adequate | Weak |
|--------|--------|---------|------|
| HTTPS | 100% HTTPS with valid certificate | HTTPS on key pages | HTTP on any page |
| Privacy policy and terms | Clearly linked from footer; GDPR/CCPA compliant | Present but hard to find | Missing or outdated |
| Contact information | Physical address, phone number, named contacts | Email contact only | No contact information |
| Review profile | 4.0+ rating with 100+ reviews on independent platform | Reviews present but < 50 or < 4.0 rating | No independent reviews |
| Return/refund policy (e-commerce) | Clearly stated, linked from product pages | Present but unclear | Missing |

---

## Organic CTR Curve Reference

Estimated average CTR by organic position (all industries, desktop):

| Position | Avg CTR | Notes |
|---------|---------|-------|
| 1 | 28–35% | Featured snippet can capture position 0 traffic |
| 2 | 15–20% | |
| 3 | 10–14% | |
| 4 | 7–10% | |
| 5 | 5–7% | Below-the-fold on some screens |
| 6–10 | 2–5% | Significant drop-off after position 5 |
| 11–20 | 0.5–2% | Page 2; rarely clicked |
| 21+ | < 0.5% | Effectively invisible |

> Use these CTR estimates to model traffic upside: `Est. Monthly Traffic = Monthly Search Volume × CTR at Target Position`.

---

## SEO Issue Severity Classification

| Severity | Definition | Example |
|---------|-----------|---------|
| Critical | Directly blocks indexation or ranking | Noindex on all pages, robots.txt blocking Googlebot |
| High | Significantly reduces ranking potential | Broken canonical tags, 404 errors on key pages |
| Medium | Reduces efficiency or performance | Thin content, missing schema markup, slow LCP |
| Low | Best practice gap with minor impact | Inconsistent URL structure, missing alt text on decorative images |
