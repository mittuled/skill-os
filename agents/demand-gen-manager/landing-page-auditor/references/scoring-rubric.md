# Landing Page Scoring Rubric

Reference rubric for auditing landing page quality across five dimensions. Each dimension is scored 0–10. Total score is the sum of all five dimensions (max 50).

## Score Interpretation

| Total Score | Rating | Action |
|------------|--------|--------|
| 45–50 | Excellent | No immediate changes needed; monitor performance |
| 35–44 | Good | Address low-scoring dimensions before next campaign |
| 25–34 | Needs Improvement | Prioritise fixes before scaling traffic |
| 15–24 | Poor | Pause traffic scaling; fix before continuing |
| 0–14 | Critical | Do not run paid traffic to this page |

---

## Dimension 1: Headline Clarity (0–10)

The headline must communicate what the product does, who it is for, and what the visitor gets — within 10 seconds of landing.

| Score | Criteria |
|-------|---------|
| 9–10 | Headline states the specific outcome for a specific audience. Sub-headline adds context without repeating. Message matches the ad/email that drove the click within 90% of the language. |
| 7–8 | Headline is clear and benefit-oriented but missing one of: specificity, audience clarity, or full message match. |
| 5–6 | Headline is present and readable but uses generic language ("The best solution for your business") with no specific audience or outcome. |
| 3–4 | Headline focuses on features or the company rather than visitor benefit. Message match to traffic source is weak. |
| 1–2 | Headline is ambiguous, jargon-heavy, or requires reading the rest of the page to understand the offer. |
| 0 | No meaningful headline or headline is identical to the company name with no descriptor. |

**Message Match Test**: Read the ad copy or email subject that drove the traffic, then read the landing page headline. The core promise must be present in both. Score a -2 penalty if it is not.

---

## Dimension 2: CTA Placement and Clarity (0–10)

The primary call-to-action must be visible above the fold, use action-oriented language, and repeat at logical scroll milestones.

| Score | Criteria |
|-------|---------|
| 9–10 | Primary CTA is above the fold, uses specific action language (e.g., "Start free trial", "Book a 30-minute demo"), passes 4.5:1 contrast ratio, and reappears at 50% and 90% scroll depth. No competing secondary CTAs. |
| 7–8 | CTA is above the fold and action-oriented but misses one of: scroll repetition, contrast threshold, or has one competing secondary CTA. |
| 5–6 | CTA is present but uses generic language ("Submit", "Learn More", "Click Here") or requires scrolling to find. |
| 3–4 | CTA is below the fold, poorly contrasted, or competes with 2+ other CTAs of equal visual weight. |
| 1–2 | CTA is unclear, buried, or requires the visitor to read fine print before understanding what action they are taking. |
| 0 | No clear CTA present. |

**CTA Language Test**: Replace the CTA button text with "Button". If the visitor cannot infer what happens after clicking from the surrounding context, the CTA is too generic.

---

## Dimension 3: Social Proof (0–10)

Social proof elements must be relevant to the target ICP, recent (within 18 months), and specific (quantified outcomes preferred).

| Score | Criteria |
|-------|---------|
| 9–10 | 3+ testimonials from named individuals at ICP-matching companies with quantified outcomes. Customer logos from recognisable ICP-segment companies. Review rating with source and count (e.g., "4.8/5 on G2, 1,200+ reviews"). |
| 7–8 | 2+ relevant testimonials with named individuals but outcomes are qualitative rather than quantified. Logos present but some are not ICP-relevant. |
| 5–6 | Generic testimonials without attribution to named individuals or companies. Logos present but no testimonials or reviews. |
| 3–4 | One vague testimonial without a name or company. No logos or review ratings. |
| 1–2 | Social proof is present but outdated (> 18 months), from irrelevant industries, or contradicts ICP targeting (e.g., enterprise page showing SMB logos). |
| 0 | No social proof of any kind. |

**Relevance Test**: Would a prospect from the target ICP recognise the companies or personas in the social proof as peers? If not, the social proof is not doing its job.

---

## Dimension 4: Form Friction (0–10)

The lead capture form must ask for the minimum fields required for qualification, use low-friction field types, and signal safety to the visitor.

| Score | Criteria |
|-------|---------|
| 9–10 | ≤ 4 fields for top-of-funnel; ≤ 6 for high-intent (demo, trial). Business email only (no personal email prompt). At least one select or checkbox field to reduce input effort. Privacy copy present ("No spam. Unsubscribe anytime."). Submit button uses CTA language matching the offer. |
| 7–8 | 5–6 fields for top-of-funnel with all fields justified for qualification. Missing privacy copy or submit button is generic. |
| 5–6 | 7–9 fields with some fields not required for qualification (e.g., phone number for a content download). |
| 3–4 | 10+ fields or required fields that are not needed for initial qualification (budget, team size, etc.) on a top-of-funnel page. |
| 1–2 | Multi-step form with no progress indicator, or CAPTCHA that requires puzzle solving, or required company description field. |
| 0 | No form, or form is broken / requires page reload to submit. |

**Field Justification Rule**: Every field on a lead form must answer "Which segment or qualification decision does this field enable?" If it cannot, remove it.

---

## Dimension 5: Page Speed and Technical Health (0–10)

Page performance is scored against Google's Core Web Vitals thresholds and mobile usability standards.

| Score | Criteria |
|-------|---------|
| 9–10 | LCP ≤ 2.5s (Good), CLS ≤ 0.1 (Good), INP ≤ 200ms (Good) on mobile. Page passes Google's mobile usability test. No render-blocking resources. Images are next-gen format (WebP/AVIF) with lazy loading. |
| 7–8 | All Core Web Vitals in "Needs Improvement" range: LCP 2.5–4s, CLS 0.1–0.25, INP 200–500ms. Mobile usable with minor issues. |
| 5–6 | One Core Web Vital in "Poor" range. Page is mobile-responsive but has layout shift issues or slow time-to-interactive. |
| 3–4 | Two Core Web Vitals in "Poor" range. Mobile experience requires horizontal scrolling or has overlapping elements. |
| 1–2 | All three Core Web Vitals in "Poor" range: LCP > 4s, CLS > 0.25, INP > 500ms. Page is not mobile-friendly. |
| 0 | Page fails to load within 10 seconds on a standard mobile connection, or fails Google's mobile usability test entirely. |

**Core Web Vitals Thresholds Reference**:

| Metric | Good | Needs Improvement | Poor |
|--------|------|------------------|------|
| LCP (Largest Contentful Paint) | ≤ 2.5s | 2.5–4.0s | > 4.0s |
| CLS (Cumulative Layout Shift) | ≤ 0.1 | 0.1–0.25 | > 0.25 |
| INP (Interaction to Next Paint) | ≤ 200ms | 200–500ms | > 500ms |

**Mobile Penalty**: If the page has a separate mobile experience that scores 2+ points lower than desktop, apply a -2 penalty to the Page Speed score.

---

## Audit Score Summary Template

| Dimension | Score (0–10) | Key Finding |
|-----------|-------------|-------------|
| Headline Clarity | | |
| CTA Placement and Clarity | | |
| Social Proof | | |
| Form Friction | | |
| Page Speed and Technical Health | | |
| **Total** | **/50** | |

## Fix Priority Matrix

| Score Range | Dimension Priority | Action |
|------------|-------------------|--------|
| 0–4 | Critical | Fix before running any paid traffic |
| 5–6 | High | Fix within current sprint |
| 7–8 | Medium | Address in next planned iteration |
| 9–10 | Healthy | Monitor only |
