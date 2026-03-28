# Technical Buyer Signal Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Solutions Engineering Manager] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | technical-buyer-signal-extractor |

## Executive Summary

[2-3 sentences summarizing the top 3 technical themes, total pipeline value at risk, and the highest-priority product recommendation.
GUIDANCE: Lead with the most revenue-impactful theme and its pipeline consequence. Do not describe the analysis process.]

## Signal Inventory

[Categorized technical signals from the analysis period.

GUIDANCE:
- Good: Table with signal category (security, integration, scalability, feature gap, architecture), count, affected deals, total pipeline value, and top 3 specific examples per category
- Bad: "We collected many technical signals"
- Format: Summary table plus detailed examples per category. Include analysis period and data source counts.]

## Theme Analysis

[Top technical themes by frequency and pipeline impact.

GUIDANCE:
- Good: One subsection per theme with: theme name, frequency (N deals), buyer's stated requirement (verbatim quotes), current product response (fully supported / workaround / gap), gap description (if any), and affected deal stages
- Bad: "Security is a common concern"
- Format: Structured subsection per theme. Order by revenue-weighted impact (highest first).]

## Revenue Impact Scoring

[Revenue-weighted prioritization of technical themes.

GUIDANCE:
- Good: Table with theme, pipeline stalled/lost, number of affected deals, average deal size, estimated pipeline recovery if addressed, and priority rank
- Bad: "These gaps cost us money"
- Format: Scored table sorted by pipeline impact. Include calculation methodology. Reference: `references/framework.md`]

## Product Recommendation Brief

[Recommendations for Product Engineering.

GUIDANCE:
- Good: One recommendation per theme with: gap description, suggested implementation approach (from field perspective), estimated engineering effort (S/M/L), pipeline at stake, customer quotes, and deal references
- Bad: "Build feature X"
- Format: Table with one row per recommendation. Each must include pipeline value and customer evidence.]

## SE Enablement Updates

[Changes to SE materials based on signal analysis.

GUIDANCE:
- Good: Table with update type (new objection response, workaround documentation, revised competitive positioning), description, affected playbook section, and status (drafted/reviewed/published)
- Bad: "Update the playbook"
- Format: Change log table with specific descriptions]

## Recommendations

[Cross-cutting improvements to signal capture and synthesis processes.

GUIDANCE: Each recommendation should be:
- Specific (not "capture more signals" but "add required POC outcome field to CRM by [date]")
- Actionable (assignable to SE Manager, RevOps, or Product)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Signal sources (SE deal notes, POC reports, RFP responses, technical discovery recordings), analysis period, filtering criteria, revenue impact scoring formula.]

### B. Supporting Data

[Raw signal frequency tables, deal-level technical gap data, POC outcome data, and competitive technical comparison evidence.]
