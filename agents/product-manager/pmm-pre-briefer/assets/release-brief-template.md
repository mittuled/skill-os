# Release Brief

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Manager] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | pmm-pre-briefer |

## Executive Summary

[2-3 sentences covering the feature, target audience, and release date.
GUIDANCE: Lead with the user benefit, not the feature mechanism.]

## Feature Facts

[Core facts about what is shipping.

GUIDANCE:
- Good: "Feature: Granular Role-Based Access Control. Release Date: 2026-04-15. Target Audience: Team admins on Business and Enterprise plans. Key Capabilities: Custom role creation, permission-level assignment, role inheritance. Known Limitations: Maximum 20 custom roles per workspace (expandable in future release). Scope Change: Audit log deferred to Q3."
- Bad: "New RBAC feature shipping soon"
- Format: Labeled fields: Feature Name, Release Date, Target Audience, Key Capabilities (bulleted), Known Limitations (bulleted), Scope Changes from Original Plan]

## Value Narrative

[Problem solved and primary benefit.

GUIDANCE:
- Good: "Problem: Team admins currently choose between giving users full admin access or restricting them to basic member permissions, leading to over-permissioned accounts. Benefit: Custom roles let admins grant exactly the permissions each team member needs, reducing security risk while maintaining workflow flexibility. What is New: Custom role creation and assignment. What is Improved: Permission granularity (from 2 levels to unlimited)."
- Bad: "RBAC is a table-stakes feature"
- Format: Problem (1 sentence), Benefit (1 sentence), New vs. Improved (bulleted)]

## Competitive Context

[How this positions the product relative to alternatives.

GUIDANCE:
- Good: "Competitor A has had RBAC since 2024 with 5 preset roles. Our implementation allows fully custom roles, which is a differentiator for mid-market customers with complex team structures. Competitor B announced RBAC on their roadmap for H2 2026."
- Bad: "We are now competitive"
- Format: Prose paragraph covering direct competitors, differentiation, and timing]

## Sensitivities

[Items PMM should be aware of before crafting messaging.

GUIDANCE:
- Good: "Breaking change: Existing API integrations using the deprecated /permissions endpoint must migrate to /roles by 2026-06-15. Pricing: No pricing change; RBAC included in Business and Enterprise. Migration: Existing admin/member assignments auto-mapped to built-in Admin and Member roles."
- Bad: "Nothing special"
- Format: Bulleted list categorized as Breaking Changes, Pricing Impact, Migration Requirements, Known Gaps]

## Recommendations

[Actions for PMM to take based on this brief.
GUIDANCE: Each recommendation should be:
- Specific (not "prepare messaging" but "draft blog post highlighting custom role creation for mid-market admin persona")
- Actionable (assignable to PMM team member)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Sources: Sprint review outputs, PRD, competitive intelligence database, customer discovery notes.]

### B. Supporting Data

[User research quotes supporting the value narrative, competitive feature comparison matrix, customer request volume data.]
