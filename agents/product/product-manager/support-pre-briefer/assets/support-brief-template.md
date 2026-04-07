# Support Briefing Package

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Manager] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | support-pre-briefer |

## Executive Summary

[2-3 sentences summarizing the release, who it affects, and the top support concern.
GUIDANCE: Lead with what support agents need to know to handle the first day of customer questions.]

## Release Summary

[What changed, who is affected, and when.

GUIDANCE:
- Good: "Release: Custom Roles (RBAC). Ship date: 2026-04-15. Affected users: All workspace admins on Business and Enterprise plans. What changed: Admins can now create custom roles with granular permissions. Existing admin/member roles remain as defaults. No migration action required from users."
- Bad: "New feature shipping"
- Format: Labeled fields: Release Name, Ship Date, Affected Users, What Changed, User Action Required (if any)]

## FAQ

[Anticipated customer questions with answers.

GUIDANCE:
- Good: Table with #, Question, Answer, Applies To. Example: "1 | 'How do I create a custom role?' | 'Go to Settings > Roles > Create Role. Select a name and check the permissions you want to grant.' | Admins on Business/Enterprise"
- Bad: Generic FAQ
- Format: Markdown table, 5-10 questions, answers in customer-facing language]

## Troubleshooting Guide

[Known issues with step-by-step workarounds.

GUIDANCE:
- Good: Per-issue section with Symptom, Cause, Workaround, Resolution Timeline. Example: "Symptom: Custom role does not appear in role assignment dropdown. Cause: Known caching issue; roles list refreshes on 5-minute interval. Workaround: Hard refresh the page (Ctrl+Shift+R). Resolution: Fix scheduled for 2026-04-22 hotfix."
- Bad: "Try refreshing"
- Format: Subsection per known issue with structured fields]

## Escalation Guide

[When and how to escalate.

GUIDANCE:
- Good: Decision tree format. "Customer reports data loss → Escalate immediately to #eng-oncall. Customer reports permission denied after role assignment → Check known issue #1 above, if not matching → Escalate to #product-ops with workspace ID and role name. Customer requests a permission not in the catalogue → Log as feature request in Productboard, tag 'rbac-permissions'."
- Bad: "Escalate if needed"
- Format: Numbered decision tree with specific channels and required information per escalation]

## Recommendations

[Actions for support readiness.
GUIDANCE: Each recommendation should be:
- Specific (not "train the team" but "schedule 30-min live walkthrough of role creation flow with support team by T-2 days")
- Actionable (assignable to support lead)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Sources: Sprint review outputs, known issues list, release notes, product FAQ draft.]

### B. Supporting Data

[Release notes, known issues with JIRA links, screenshots of new UI flows.]
