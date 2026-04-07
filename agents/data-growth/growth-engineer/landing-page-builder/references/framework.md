# Framework: High-Converting Landing Page Design

Defines the layout hierarchy, performance requirements, and instrumentation standards for acquisition landing pages.

## Conversion-Optimized Layout Hierarchy

Every landing page should follow this element order (above the fold through page bottom):

| Section | Element | Purpose | Conversion Impact |
|---------|---------|---------|-----------------|
| Hero | Headline (1 sentence, benefit-led) | Communicate the value proposition immediately | Highest — first 5 seconds |
| Hero | Sub-headline (1–2 sentences) | Clarify who it's for and how it works | High |
| Hero | Primary CTA (1 button) | Drive the single desired action | Highest |
| Hero | Social proof signal (number, logo, or quote) | Reduce initial skepticism | High |
| Below fold | Feature benefits (3–4 items, icon + 1 line) | Substantiate the headline claim | Medium |
| Below fold | Second CTA | Capture users who scrolled | Medium |
| Below fold | Detailed social proof (testimonials, case studies, logos) | Build trust for hesitant users | Medium |
| Bottom | Final CTA + urgency or incentive | Last capture opportunity | Medium-Low |

**Rule**: One primary CTA per page. Repeat the same CTA at multiple scroll depths. Never offer multiple competing actions.

## Performance Requirements

| Metric | Target | Minimum Acceptable |
|--------|--------|-------------------|
| Largest Contentful Paint (LCP) | < 2.5 seconds | < 4.0 seconds |
| Total Blocking Time (TBT) | < 200ms | < 600ms |
| Cumulative Layout Shift (CLS) | < 0.1 | < 0.25 |
| Total page weight | < 1 MB | < 2 MB |
| Mobile pass (Core Web Vitals) | Pass all | Pass LCP minimum |

Measure using PageSpeed Insights or Lighthouse on target audience devices. Paid traffic amplifies the revenue impact of every 1-second delay (estimated 1–3% conversion rate drop per additional second).

## UTM and Attribution Requirements

Landing pages must:
1. Read all UTM parameters from the URL on page load
2. Store them in localStorage and a first-party cookie (30-day expiry)
3. Pass them as hidden fields on the signup or lead-capture form
4. NOT require UTM to be present on the success/confirmation page (read from storage)

## A/B Test Priority for Landing Pages

Test in this sequence (expected impact order):
1. **Headline** — the single highest-impact element; test value framing vs. problem framing vs. outcome framing
2. **CTA button text** — test action verbs ("Start free", "Try for free", "Get started") vs. benefit-led ("Build my first X")
3. **Hero image / video** — product screenshot vs. use-case illustration vs. person-using-product
4. **Social proof format** — logo bar vs. quote testimonials vs. user count number
5. **Page length** — minimal (hero + CTA only) vs. full-length with features and social proof

## Instrumentation Checklist

Before launch every landing page must have:
- [ ] `page_viewed` event firing on load with `page_path`, `utm_source`, `utm_medium`, `utm_campaign`
- [ ] `cta_clicked` event on every CTA button with `button_text`, `page_section`, `utm_*`
- [ ] `form_submitted` event if a lead capture or signup form is present
- [ ] UTM params captured in localStorage and cookie on page load
- [ ] Google Tag Manager or direct SDK verified in browser dev tools
- [ ] Conversion goal configured in ad platform (Google Ads, Meta Ads) for ROAS measurement
