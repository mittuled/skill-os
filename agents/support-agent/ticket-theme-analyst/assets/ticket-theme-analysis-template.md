# Ticket Theme Analysis Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Support Agent / Analyst name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | ticket-theme-analyst |
| Analysis Period | [YYYY-MM-DD to YYYY-MM-DD] |
| Total Tickets Analysed | [N] |

## Executive Summary

[2-3 sentences covering: total ticket volume, the top 1-2 themes by impact score, and the most important recommended action. Example: "In Q3 2025, 847 tickets were analysed. The top theme by impact score was 'SSO configuration errors' (score 214, 23% of volume), driven by a documentation gap in the SAML setup guide. The highest-ROI action is updating the SAML setup article, estimated to deflect 35-50 tickets per month."]

## Dataset Summary

[Description of the raw data used in this analysis.

GUIDANCE:
- Good: Ticket counts by category, date range, data completeness rate (% of tickets with all required fields populated)
- Bad: "Tickets were exported from Zendesk."
- Format: Table with category, ticket count, % of total, avg resolution time]

| Product Area / Category | Ticket Count | % of Total | Avg Resolution Time (h) | Escalation Rate |
|------------------------|-------------|------------|------------------------|-----------------|
| [Category] | [N] | [%] | [hours] | [%] |
| **Total** | [N] | 100% | [avg] | [%] |

## Theme Analysis

[Ranked list of identified themes.

GUIDANCE:
- Good: Each theme entry includes theme name, ticket count, impact score, representative customer quotes, and signal classification.
- Bad: "Theme 1: Login issues. Theme 2: Billing problems."
- Format: One subsection per theme, sorted by impact score descending]

### Theme 1: [Theme Name]

| Field | Value |
|-------|-------|
| Impact Score | [calculated per framework formula] |
| Ticket Count | [N] ([%] of total) |
| Customer Tier Breakdown | Free: [N] / Pro: [N] / Enterprise: [N] |
| Avg Resolution Time | [hours] |
| Signal Type | [Product Bug / Documentation Gap / UX Confusion / Missing Feature / Onboarding Friction] |
| Recommended Owner | [Team] |

**Representative Customer Verbatim:**
> "[Direct quote from ticket #XXXX illustrating the theme]"

**Root Cause:** [1-2 sentences explaining why these tickets are occurring]

**Recommended Action:** [Specific, assignable action with expected impact]

*(Repeat for each theme)*

## Signal Heatmap

[Cross-tabulation of themes by signal type.

GUIDANCE: Shows at a glance where engineering, product, and content need to focus.

| Signal Type | Theme Count | Ticket Volume | Top Theme |
|------------|------------|--------------|-----------|
| Product Bug | [N] | [N] | [Theme name] |
| Documentation Gap | [N] | [N] | [Theme name] |
| UX Confusion | [N] | [N] | [Theme name] |
| Missing Feature | [N] | [N] | [Theme name] |
| Onboarding Friction | [N] | [N] | [Theme name] |
]

## Recommendations

[Prioritised action list with owners and expected ticket deflection.

GUIDANCE: Each recommendation should be specific and include estimated ticket deflection or cost savings.
- P1: High-impact, low-effort — action within 1 week
- P2: High-impact, moderate-effort — action within 1 sprint
- P3: Low-impact or high-effort — add to backlog with justification]

| Priority | Action | Owner | Estimated Deflection / Month | Deadline |
|----------|--------|-------|------------------------------|----------|
| P1 | [Specific action] | [Team] | [N tickets] | [Date] |

## Appendices

### A. Methodology

[Describe clustering approach, ticket extraction query, analysis period, and any data quality issues encountered.]

### B. Trend Comparison

[Compare this period's top themes against the previous period to show whether known issues are improving or worsening.]

| Theme | Previous Period Volume | This Period Volume | Trend |
|-------|----------------------|-------------------|-------|
| [Theme] | [N] | [N] | [↑ / ↓ / →] |
