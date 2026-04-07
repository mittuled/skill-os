# User Research Insight Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Manager] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | user-researcher |

## Executive Summary

[2-3 sentences summarizing the research question, number of participants, and the top insight.
GUIDANCE: Lead with the product recommendation, not the methodology.]

## Research Objective

[The decision this research informs.

GUIDANCE:
- Good: "Decision: Should we invest in granular RBAC or improve the existing admin/member model? Question: What permission-related workflows do admins currently perform, and where do the current two roles create friction? Scope: Enterprise and mid-market workspace admins managing 10+ users."
- Bad: "Learn about user needs"
- Format: Labeled fields: Decision, Question, Scope]

## Participants

[Anonymised participant profiles.

GUIDANCE:
- Good: Table with Participant ID (P1-P8), Segment, Company Size, Role, Tenure with Product, Screening Criteria Met
- Bad: "We talked to some admins"
- Format: Markdown table, one row per participant, no PII]

## Affinity Map Summary

[Theme clusters with frequency and evidence.

GUIDANCE:
- Good: Table with Theme, Frequency (N/M participants), Evidence Type (stated preference / revealed behaviour), Representative Quote
- Bad: "We found some themes"
- Format: Markdown table sorted by frequency descending]

## Insights

[Ranked insights in observed/because/means format.

GUIDANCE:
- Good: "Insight 1 (7/8 participants): We observed that admins create shared 'service accounts' with admin permissions for team members who need billing access but should not manage users, because the current binary model forces a choice between full admin or no billing access. This means we should prioritize billing-specific permissions as the first custom role template. Supporting evidence: P1: 'I have a fake admin account just for my finance person.' P3: 'We rotate the admin password monthly because three people need billing.'"
- Bad: "Users want more roles"
- Format: Numbered insight with observed/because/means structure, supporting quotes, participant count]

## Divergence Log

[Where findings split across segments.

GUIDANCE:
- Good: "Enterprise participants (P1, P2, P5) prioritize audit logging of permission changes. Mid-market participants (P3, P4, P6) do not mention audit needs. Hypothesis: Enterprise compliance requirements drive audit demand; mid-market teams are too small for audit to matter yet."
- Bad: "Some disagreement"
- Format: Per-divergence paragraph with segments, pattern, and hypothesis]

## Recommendations

[Product actions based on research findings.
GUIDANCE: Each recommendation should be:
- Specific (not "build RBAC" but "prioritize billing-viewer and user-manager as the first two custom role templates based on Insight 1 and Insight 3")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Research approach: semi-structured interviews, 30-45 minutes each, affinity mapping for analysis, insight ranking by frequency and impact.]

### B. Supporting Data

[Interview guide, raw interview notes (anonymised), screening questionnaire, session recordings (consent obtained).]
