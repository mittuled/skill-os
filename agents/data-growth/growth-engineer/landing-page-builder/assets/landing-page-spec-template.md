# Landing Page Specification

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Engineer name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | landing-page-builder |
| Campaign | [Campaign name or product launch] |
| Traffic source | [Paid search / Organic / Referral / Email] |
| Target URL | [/landing/[slug]] |

## Executive Summary

[2-3 sentences describing the page's purpose, target audience, and primary conversion action.
GUIDANCE: Example — "This landing page targets paid search traffic for the keyword 'AI writing tool' with a primary CTA of 'Start free trial'. The page is designed for individual content creators and must load in < 2.5 seconds on 4G mobile. Attribution flows from UTM capture through the signup form to the growth funnel."]

## Campaign Brief Summary

[Summarize the key inputs from the campaign brief.
GUIDANCE:
- Good: "Target audience: content creators at companies with 1–50 employees. Value proposition: 10x faster content creation with AI. Desired action: Start free trial (no credit card). Traffic source: Google Search — keyword cluster: 'AI writing', 'AI content tool'."
- Bad: "It's a landing page for our new feature."
- Format: Key-value pairs]

| Field | Value |
|-------|-------|
| Target audience | [Specific persona description] |
| Value proposition | [Single sentence — what the user gets] |
| Primary action (CTA) | [Specific action + destination] |
| Traffic source | [Channel and campaign details] |
| Unique incentive (if any) | [e.g., "14-day free trial, no credit card"] |

## Page Layout Specification

[Document each section with copy and design requirements.
GUIDANCE:
- Good: "Hero headline: '10x your content output with AI' (benefit-led, not feature-led). Sub-headline: 'The AI writing tool trusted by 50,000+ content teams.' CTA: 'Start free — no credit card' (green button, centered)."
- Bad: "Use a good headline and a CTA button."
- Format: Section-by-section with specific copy]

### Hero Section

| Element | Content | Notes |
|---------|---------|-------|
| Headline | [Specific copy] | [Benefit-led / Problem-led / Outcome-led] |
| Sub-headline | [Specific copy] | [Max 2 sentences] |
| Primary CTA | [Button text] | [Destination URL] |
| Social proof signal | [e.g., "Trusted by 50,000+ teams" / Logo bar] | [Above or below CTA] |
| Hero media | [Product screenshot / Illustration / Video URL] | |

### Feature Benefits Section

[3–4 feature benefits with icon + one-line description each]

| Benefit # | Icon | Headline | One-line description |
|-----------|------|---------|---------------------|
| 1 | [Icon description] | [Benefit headline] | [One sentence] |
| 2 | | | |
| 3 | | | |

### Social Proof Section

| Type | Content |
|------|---------|
| [Testimonial / Case study / Logo bar] | [Specific quote, company name, or logos to include] |

### Final CTA Section

| Element | Content |
|---------|---------|
| CTA button text | [Same as hero CTA] |
| Supporting copy | [e.g., "Join 50,000+ teams. Start free today."] |
| Incentive / urgency (if any) | [e.g., "14-day free trial. Cancel anytime."] |

## Performance Requirements

| Metric | Target | Measurement Tool |
|--------|--------|-----------------|
| LCP | < 2.5s | PageSpeed Insights |
| TBT | < 200ms | PageSpeed Insights |
| Total page weight | < 1 MB | Chrome DevTools |
| Mobile Core Web Vitals | Pass | PageSpeed Insights mobile |

## Instrumentation Plan

[List every analytics event this page must fire.
GUIDANCE: All events must capture UTM parameters from localStorage, not the current URL.]

| Event | Trigger | Properties |
|-------|---------|-----------|
| page_viewed | Page loads | page_path, utm_source, utm_medium, utm_campaign, utm_content |
| cta_clicked | Any CTA button clicked | button_text, page_section, utm_source, utm_campaign |
| [form_submitted] | If lead capture form exists | form_name, utm_source, utm_campaign |

## Recommendations

[Implementation decisions and post-launch A/B test plan.
GUIDANCE: Include the first experiment to run after baseline is established (minimum 2 weeks of data).]

| Priority | Recommendation | Owner | Timeline |
|----------|---------------|-------|---------|
| P1 | [e.g., Verify UTM capture and event firing before traffic launch] | [Growth Eng] | [Before launch] |
| P2 | [e.g., A/B test headline framing after 200+ conversions baseline] | [Growth Eng] | [30 days post-launch] |

## Appendices

### A. Methodology

[Campaign brief source. Performance benchmark based on Lighthouse on [device / network conditions]. UTM attribution approach: localStorage + cookie with 30-day expiry.]

### B. Supporting Data

[Competitive analysis of top 3 competitor landing pages. Current homepage conversion rate for reference. Ad copy used in campaigns (should align with landing page headline).]
