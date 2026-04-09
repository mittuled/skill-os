---
name: landing-page-builder
description: >
  This skill builds high-converting landing pages for acquisition campaigns.
  Use when asked to create a landing page, build a campaign page, or set up
  a conversion-optimized page. Also consider when running paid acquisition
  without dedicated landing pages. Suggest when the user is sending ad traffic
  to the homepage instead of a targeted page.
department: data-growth
agent: growth-engineer
version: 1.0.0
complexity: simple
related-skills:
  - ../growth-loop-activator/SKILL.md
  - ../instrumentation-implementer-growth/SKILL.md
triggers:
  - "build landing page"
  - "create landing page"
  - "launch landing page"
  - "develop conversion page"
  - "landing page development"
---

# landing-page-builder

## Agent: Growth Engineer

L2 growth engineer (Nx) responsible for growth instrumentation, metrics dashboards, funnel analysis, and growth loop activation.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

Builds high-converting landing pages for acquisition campaigns, optimized for page speed, conversion rate, and analytics instrumentation.

## When to Use

- When a marketing campaign, product launch, or paid acquisition channel needs a dedicated landing page with conversion tracking.
- When A/B testing landing page variants to optimize conversion rates.
- When the existing homepage is not optimized for a specific acquisition channel or audience segment.

## Workflow

1. **Brief Review**: Review the campaign brief including target audience, value proposition, desired action (sign-up, demo request, download), and traffic source. Deliverable: technical requirements derived from brief.
2. **Page Build**: Build the landing page with conversion-optimized layout: hero with clear CTA, social proof, benefit statements, and minimal navigation. Ensure sub-3-second load time and mobile responsiveness. Deliverable: deployed landing page.
3. **Instrumentation**: Add analytics tracking for page views, CTA clicks, form submissions, and conversion events. Set up UTM parameter capture and attribution. Deliverable: instrumented page with analytics verification.
4. **Launch and Handoff**: Publish the page, verify it works across devices and browsers, and hand off the URL and tracking details to the campaign owner. Deliverable: live page URL with tracking documentation.

## Anti-Patterns

- **Heavy pages for paid traffic**: Building landing pages with large assets and slow load times for paid acquisition. *Why*: every second of load time reduces conversion rate; paid traffic amplifies the cost of lost conversions.
- **Missing conversion tracking**: Launching a landing page without proper conversion event tracking and attribution. *Why*: without tracking, campaign ROI cannot be measured and optimization is impossible.

## Output

**On success**: Produces a live, instrumented landing page with sub-3-second load time, conversion tracking, and campaign attribution. Delivered to the campaign owner.

**On failure**: Report what blocked the page launch (e.g., design assets unavailable, CMS limitations), what interim options exist, and timeline for resolution. Escalate to Growth Lead.

## Related Skills

- [`growth-loop-activator`](../growth-loop-activator/SKILL.md) -- Landing pages serve as entry points for growth loops.
- [`instrumentation-implementer-growth`](../instrumentation-implementer-growth/SKILL.md) -- Landing page analytics use the same instrumentation patterns.
