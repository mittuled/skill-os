---
name: seo-auditor
description: >
  This skill conducts comprehensive SEO audits covering technical health, keyword
  gap analysis, Core Web Vitals, and E-E-A-T signals, producing a prioritised
  remediation plan that maps directly to organic traffic and pipeline opportunity.
  Use when organic traffic is declining, when a site migration is planned, when
  a new content programme needs a baseline, or when SEO ROI needs to be quantified
  for budget justification. Suggest when paid CAC is rising and the organic channel
  needs development as a counterweight.
department: marketing
agent: marketing-operations-manager
version: 1.0.0
complexity: complex
related-skills:
  - ../../../marketing/demand-gen-manager/funnel-optimizer/SKILL.md
  - ../../../marketing/demand-gen-manager/landing-page-auditor/SKILL.md
  - ../../../marketing/marketing-operations-manager/campaign-analytics-reporter/SKILL.md
triggers:
  - "audit SEO"
  - "organic traffic is declining"
  - "run an SEO audit"
  - "keyword gap analysis"
  - "technical SEO review"
---

# seo-auditor

## Agent: Marketing Operations Manager

L2 Marketing Operations Manager (1x) responsible for marketing technology, data infrastructure, attribution modelling, campaign analytics, and operational efficiency across all marketing programmes.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Conducts a comprehensive SEO audit across four dimensions — technical health, keyword gap, Core Web Vitals performance, and E-E-A-T signals — scoring each dimension against framework benchmarks and producing a prioritised remediation plan with estimated traffic and pipeline impact.

## When to Use

- When organic search traffic has declined more than 15% month-over-month for two consecutive periods.
- When a site migration, domain change, or CMS change is planned and a pre-migration baseline is required.
- When a content programme is being launched or relaunched and keyword coverage gaps need to be identified.
- When SEO budget justification is required and organic traffic opportunity needs to be quantified in pipeline terms.
- When a competitor is gaining organic share and a gap analysis is needed to identify where they are winning.
- When Core Web Vitals are failing Google's thresholds and page experience signals need remediation.

## Workflow

1. **Scope and baseline definition**: Define the audit scope — full domain, subdomain, or specific URL cluster (e.g., blog, product pages, help centre). Pull current organic traffic, keyword rankings, and crawl data from available tooling. Establish baseline metrics: total indexed pages, organic sessions (trailing 90 days), top 20 ranking keywords, and average Core Web Vitals scores. Reference `references/framework.md` for all benchmark thresholds. Deliverable: audit scope document with baseline metrics snapshot.

2. **Technical SEO health check**: Crawl the in-scope pages and audit against the technical SEO checklist in `references/framework.md`. Cover: crawlability (robots.txt, XML sitemap, noindex tags), indexation (canonical tags, duplicate content, thin content), site architecture (internal linking depth, orphaned pages, redirect chains), HTTPS and security, structured data (schema markup validity), and mobile usability. Classify each issue by severity: critical (blocks indexation), high (reduces ranking potential), medium (efficiency issue), low (best practice gap). Deliverable: technical SEO issue log with severity classifications and affected URL counts.

3. **[GATE] Keyword gap analysis**: Using the keyword gap analysis framework in `references/framework.md`, map the site's current keyword coverage against target intent clusters (informational, commercial, transactional). Identify keywords where competitors rank in positions 1-10 but the site does not appear in the top 20. Estimate monthly search volume and keyword difficulty for each gap. Present gap analysis for stakeholder prioritisation before proceeding to content recommendations — keyword targeting must align with ICP and commercial intent. Deliverable: keyword gap matrix with search volume, difficulty, current position, and competitor positions.

4. **Core Web Vitals audit**: Measure LCP (Largest Contentful Paint), CLS (Cumulative Layout Shift), and INP (Interaction to Next Paint) against the thresholds in `references/framework.md`. Segment results by page template type (homepage, product pages, blog posts, landing pages) as performance issues are often template-level, not page-level. Identify the top 10 pages by organic traffic that are failing Core Web Vitals and flag them for priority remediation. Deliverable: Core Web Vitals performance report by template type with failing pages ranked by traffic impact.

5. **E-E-A-T signal assessment**: Evaluate the site's Experience, Expertise, Authoritativeness, and Trustworthiness signals using the E-E-A-T framework in `references/framework.md`. Assess: author bylines and credentials on content, about pages and team profiles, external links to the site from authoritative domains, link profile quality (referring domain authority distribution), customer reviews and ratings presence, and security signals. Score each E-E-A-T dimension qualitatively (strong, adequate, weak) with specific evidence. Deliverable: E-E-A-T signal assessment with gap list and improvement recommendations.

6. **Opportunity quantification**: For the top keyword gaps and technical issues identified, estimate the organic traffic and pipeline opportunity unlocked by remediation. Use the click-through rate curves in `references/framework.md` to model traffic upside from ranking improvements. Apply the site's current organic-to-lead conversion rate to estimate pipeline value. Deliverable: opportunity sizing table with estimated traffic uplift and pipeline value per initiative.

7. **[GATE] Prioritisation and roadmap**: Rank all identified issues and opportunities using a combined impact/effort matrix. Group into three categories: quick wins (high impact, low effort — execute within 30 days), structural fixes (high impact, high effort — plan within 60 days), and ongoing improvements (medium impact, recurring effort — build into operating rhythm). Present the roadmap to stakeholders for sign-off before committing engineering or content resources. Deliverable: prioritised SEO roadmap with 30/60/90-day buckets.

8. **Report generation**: Compile all findings into the SEO audit report using `assets/seo-audit-report-template.md`. Include baseline metrics, technical issue log, keyword gap matrix, Core Web Vitals performance, E-E-A-T assessment, opportunity sizing, and prioritised roadmap. Deliverable: complete SEO audit report ready for stakeholder review.

## Anti-Patterns

- **Technical SEO without keyword strategy alignment**: Fixing crawl errors and site speed without addressing whether the site is targeting the right keywords. *Why*: A technically perfect site ranking for keywords its ICP doesn't search for generates traffic that never converts.
- **Keyword research without search intent mapping**: Targeting keywords by volume alone without distinguishing informational, commercial, and transactional intent. *Why*: High-volume informational keywords attract researchers, not buyers; ranking for the wrong intent drives traffic that exits at the top of funnel.
- **Reporting Core Web Vitals at domain level**: Aggregating Core Web Vitals scores across all pages and reporting a single domain score. *Why*: Performance problems are template-specific; domain averages hide the pages with the worst user experience and highest traffic impact.
- **E-E-A-T as a content-only concern**: Treating E-E-A-T signals as solely a writing and editorial problem. *Why*: E-E-A-T encompasses technical signals (structured data, site architecture) and off-site signals (backlink quality, reviews) that content changes alone cannot address.
- **Prioritising low-difficulty keywords exclusively**: Targeting only keywords with low competition because they are easier to rank for. *Why*: Low-difficulty keywords frequently have low commercial intent or low volume; a portfolio of keyword targets must include high-value, high-difficulty terms with a longer-term ranking strategy.

## Output

**On success**: Produces an SEO audit report (using `assets/seo-audit-report-template.md`) containing the baseline metrics snapshot, technical issue log with severity ratings, keyword gap matrix, Core Web Vitals performance by template, E-E-A-T signal assessment, opportunity sizing, and prioritised 90-day roadmap. Delivered as a document ready for engineering, content, and leadership review.

**On failure**: Report which audit dimensions could not be completed and why (no access to Search Console, crawl blocked by robots.txt, no keyword tracking data), what was completed, and what access or tooling is required. Every blocker is an actionable request for access or data.

## Related Skills

- [`funnel-optimizer`](../../../marketing/demand-gen-manager/funnel-optimizer/SKILL.md) — Organic search is a top-of-funnel input channel; SEO audit findings inform TOFU volume and quality diagnoses in the funnel.
- [`landing-page-auditor`](../../../marketing/demand-gen-manager/landing-page-auditor/SKILL.md) — Landing pages targeted at commercial keywords must score well on conversion elements; SEO and CRO fixes are often co-located.
- [`campaign-analytics-reporter`](../../../marketing/marketing-operations-manager/campaign-analytics-reporter/SKILL.md) — Analytics data (organic sessions, bounce rate, landing page performance) provides the evidence base for SEO audit findings.
