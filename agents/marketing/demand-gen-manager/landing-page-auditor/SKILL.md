---
name: landing-page-auditor
description: >
  This skill audits landing pages against a structured quality rubric covering
  headline clarity, CTA placement, social proof, form friction, and page speed,
  producing a scored report with prioritised fixes. Use when a campaign is driving
  traffic but conversion rate is below target, when a new landing page needs
  pre-launch review, or when A/B test results are ambiguous and the control page
  needs a baseline audit. Suggest when paid CAC is rising without a change in
  targeting.
department: marketing
agent: demand-gen-manager
version: 1.0.0
complexity: medium
related-skills:
  - ../../../marketing/demand-gen-manager/funnel-optimizer/SKILL.md
  - ../../../marketing/demand-gen-manager/ad-campaign-builder/SKILL.md
  - ../../../marketing/marketing-operations-manager/campaign-analytics-reporter/SKILL.md
  - ../../../design/brand-designer/brand-voice-analyst/SKILL.md
  - ../../content-marketer/copywriting-analyst/SKILL.md
  - ../../marketing-operations-manager/seo-auditor/SKILL.md
triggers:
  - "audit the landing page"
  - "why is conversion rate low"
  - "review landing page before launch"
  - "landing page is underperforming"
  - "score the landing page"
---

# landing-page-auditor

## Agent: Demand Gen Manager

L2 Demand Gen Manager (1x) responsible for channel strategy, paid and organic demand generation, content distribution, and pipeline contribution from marketing programmes.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Audits landing pages against a five-dimension quality rubric — headline clarity, CTA placement, social proof, form friction, and page speed — scoring each dimension and producing a prioritised fix list with estimated conversion impact.

## When to Use

- When a paid campaign is delivering traffic at target CPCs but form submission rate is below 3% for B2B or 8% for B2C.
- When preparing a new landing page for launch and a structured pre-live review is needed.
- When an A/B test is running but traffic has not reached statistical significance and the control page quality needs baselining.
- When overall site conversion rate has declined without a corresponding traffic quality change.
- When onboarding a new client or campaign and a legacy landing page has not been audited in the past six months.

## Workflow

1. **Page capture and context**: Capture the landing page URL, the traffic source (paid search, paid social, organic, email), the campaign objective (lead gen, trial, demo request, purchase), and the target ICP. This context determines which rubric thresholds apply. Reference `references/scoring-rubric.md` for dimension definitions and scoring criteria. Deliverable: audit brief with URL, traffic source, objective, and ICP.

2. **Headline and above-the-fold audit**: Evaluate the headline against the scoring rubric: does it state what the product does, who it is for, and what they get — within 10 seconds of reading? Score message match between the ad or email that drove the traffic and the headline. Assess sub-headline and hero image alignment. Deliverable: headline score (0-10) with specific copy findings.

3. **CTA placement and clarity audit**: Identify all CTA instances on the page. Score primary CTA for specificity (action-oriented, not generic), visibility (above the fold, contrast ratio), and repetition (appears at logical scroll milestones). Check that secondary CTAs do not compete with the primary action. Deliverable: CTA score (0-10) with placement map notation.

4. **Social proof audit**: Inventory all social proof elements: customer logos, testimonials, case study links, review ratings, usage statistics, media mentions. Score relevance (is the social proof from the same ICP segment?), recency (less than 18 months old), and specificity (quantified outcomes vs. vague praise). Deliverable: social proof score (0-10) with gap list.

5. **Form friction audit**: Assess the lead capture form for field count, field type (text vs. select reduces friction), progressive profiling opportunity, privacy assurance copy, and submit button copy. Score against the rubric thresholds in `references/scoring-rubric.md`. Flag any fields that are not required for qualification. Deliverable: form friction score (0-10) with specific field recommendations.

6. **Page speed and technical audit**: Measure Core Web Vitals (LCP, CLS, INP) using available tooling or reference data. Score against the thresholds in `references/scoring-rubric.md`. Flag render-blocking resources, unoptimised images, and missing mobile responsiveness. Deliverable: page speed score (0-10) with technical issues list.

7. **Prioritised fix list and report**: Compile all dimension scores into a total audit score. Rank fixes by estimated conversion impact (high/medium/low) and implementation effort (low/medium/high). Generate the audit report using `assets/landing-page-audit-report-template.md`. Deliverable: scored landing page audit report with prioritised fix list.

## Anti-Patterns

- **Auditing without message match context**: Scoring a landing page in isolation without knowing the ad or email that drove the traffic. *Why*: A technically strong page with low message match to the ad source will underperform regardless of on-page quality.
- **Over-indexing on design aesthetics**: Rating visual polish highly when conversion elements are weak. *Why*: Beautiful pages with unclear CTAs or excessive form fields consistently underperform plainer pages with clear actions.
- **Recommending form field reduction without qualification context**: Removing form fields that sales needs for lead routing and qualification. *Why*: Lower-friction forms that generate unqualified leads increase volume but reduce SQL conversion rates, netting negative revenue impact.
- **Ignoring mobile experience**: Auditing only the desktop version of the page. *Why*: Mobile traffic often accounts for 40-60% of paid social traffic; a page that scores well on desktop can score critically on mobile.

## Output

**On success**: Produces a landing page audit report (using `assets/landing-page-audit-report-template.md`) with scores across all five dimensions, a total score, specific findings per dimension, and a prioritised fix list with effort and impact ratings. Delivered as a document ready for the design or web team to action.

**On failure**: Report which dimensions could not be scored and why (no access to analytics, page behind authentication, missing traffic source context), what was completed, and what access or information is needed to finish. Every gap is an actionable ask.

## Related Skills

- [`funnel-optimizer`](../../../marketing/demand-gen-manager/funnel-optimizer/SKILL.md) — Landing page conversion rate is a primary TOFU-to-MOFU transition metric; audit fixes should be tracked in the funnel optimisation roadmap.
- [`ad-campaign-builder`](../../../marketing/demand-gen-manager/ad-campaign-builder/SKILL.md) — Ad creative must match landing page messaging; campaign builder should be updated when headline or offer changes are recommended.
- [`campaign-analytics-reporter`](../../../marketing/marketing-operations-manager/campaign-analytics-reporter/SKILL.md) — Analytics data (bounce rate, scroll depth, conversion rate) provides the evidence base for audit findings.
