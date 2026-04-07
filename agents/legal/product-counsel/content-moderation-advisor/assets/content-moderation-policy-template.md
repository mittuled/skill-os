# Content Moderation Policy Framework

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Counsel] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | content-moderation-advisor |

## Executive Summary

[2-3 sentences summarizing the moderation policy scope, key regulatory drivers, and primary recommendations.
GUIDANCE: Lead with the regulatory obligations that shape the policy (DSA, Section 230, NetzDG) and whether the current framework meets those obligations.]

## Policy Gap Analysis

[Assessment of current moderation policies against applicable laws.

GUIDANCE:
- Good: Table with Regulation, Requirement, Current Policy Coverage (Full/Partial/None), Gap Description, Risk Level
- Bad: "We need to update our moderation policies"
- Format: Gap analysis matrix by regulation and requirement]

## Prohibited Content Categories

[Defined content categories with severity tiers and enforcement actions.

GUIDANCE:
- Good: Table with Category, Definition, Examples, Detection Method, Enforcement Action, Response Timeframe, Legal Authority
- Bad: "Users cannot post bad content"
- Format: Tiered category table from most severe (CSAM, terrorism) to least severe (spam)]

## Enforcement Procedures

[Moderation enforcement workflow specification.

GUIDANCE:
- Good: "Tier 1 (CSAM): Automated hash-matching via PhotoDNA. Immediate removal without notice. NCMEC report within 24 hours. User permanent ban. No appeal for confirmed CSAM. Tier 2 (Hate Speech): ML classifier flags for human review. 24-hour review SLA. Content removal with notice citing specific policy violation. 7-day appeal window."
- Bad: "We review and remove content that violates our policies"
- Format: Per-tier workflow with detection, review SLA, action, notice, and appeal provisions]

## Appeal Mechanism

[User appeal process design meeting regulatory requirements.

GUIDANCE:
- Good: "Users receive moderation notice within 24 hours citing specific policy provision. Appeal submitted via in-app form. Human reviewer (not original moderator) reviews within 5 business days. Decision communicated with reasoning. DSA Article 20 out-of-court dispute settlement option referenced."
- Bad: "Users can appeal"
- Format: Step-by-step appeal workflow with SLAs and regulatory compliance mapping]

## Transparency Reporting

[Required transparency reports and compliance reporting.

GUIDANCE:
- Good: "DSA Article 15 annual report: content moderation decisions by category, automated vs. human decisions, appeal outcomes, government requests. Published by [date]. NetzDG Section 2 semi-annual report: complaints received, removal actions, response times."
- Bad: "We will publish a transparency report"
- Format: Table with Report Type, Regulatory Source, Frequency, Required Content, Publication Date]

## Recommendations

[Prioritized list of recommendations.
GUIDANCE: Each recommendation should be:
- Specific (not "improve moderation" but "implement PhotoDNA hash-matching for CSAM detection before UGC feature launch")
- Actionable (assignable to a person/team)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Legal framework analysis per `references/content-moderation-framework.md`. Regulations consulted: Section 230, DSA, Online Safety Act, NetzDG, CSAM reporting obligations, state social media laws.]

### B. Supporting Data

[Comparable platform moderation policies, regulatory guidance documents, enforcement action precedents, DSA compliance guidance from European Commission.]
