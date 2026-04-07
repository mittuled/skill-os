# Platform Capability Gap Report: [Platform / Quarter]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | Platform Engineer |
| Analysis Period | [Q1–Q4 YYYY / Last 6 months] |
| Data Sources | [Developer surveys / Support tickets / Postmortems / Team interviews] |
| Skill | platform-capability-gap-detector |
| Status | [Draft / Final] |

## Executive Summary

[2–3 sentences: total gaps identified, most critical gap, and recommended top priority for next quarter.
GUIDANCE: Lead with the highest-impact gap — "Three capability gaps identified. The absence of a self-service secret rotation capability is the highest-priority gap — 7 teams have manually rotated secrets incorrectly in the last quarter, resulting in 2 production incidents. Recommending this as Platform Q2 top priority."]

**Gaps identified**: [N total — N critical, N high, N medium]
**Top priority**: [Gap name and one-line description]

## Capability Gaps

### Critical Gaps (Blocking engineering work or causing incidents)

| ID | Gap | Evidence | Teams Affected | Incident Count (90d) | Priority |
|----|-----|----------|---------------|---------------------|---------|
| G-001 | [Self-service secret rotation] | [7 support tickets + 2 postmortems] | [All teams] | [2] | P1 |

### High Gaps (Causing significant friction but no incidents)

| ID | Gap | Evidence | Teams Affected | Friction Incidents (90d) | Priority |
|----|-----|----------|---------------|-------------------------|---------|
| G-010 | [No standard local development environment] | [Onboarding survey: avg 3 days to first run] | [All] | — | P1 |

### Medium Gaps (Toil or inefficiency without major impact)

| ID | Gap | Evidence | Teams Affected | Priority |
|----|-----|----------|---------------|---------|
| G-020 | [No database migration scaffolding in template repos] | [Teams writing boilerplate manually] | [6 of 8 teams] | P2 |

## Gap Analysis Detail

### G-001: [Gap Name]

**Description**: [What is missing and what teams must do instead]

**Current workaround**: [How teams are solving this today — this is the cost we're eliminating]

**Evidence collected**:
- [Support ticket count]: [N in last 90 days]
- [Postmortem citations]: [N postmortems mention this gap]
- [Survey data]: [X% of developers rated this as top friction point]
- [Time cost estimate]: [N hours/team/month on workaround]

**Proposed solution**: [One-line description of the platform capability that would close this gap]
**Estimated effort to close**: [X sprints]
**Expected benefit**: [Quantified: eliminate N support tickets/month, save X hrs/team/month, prevent Y class of incidents]

---

### G-010: [Gap Name]

[Repeat structure]

## Prioritization Matrix

| Gap ID | Impact (1–5) | Urgency (1–5) | Effort to Close (1–5, inverse) | Priority Score | Recommendation |
|--------|-------------|--------------|-------------------------------|---------------|----------------|
| G-001 | [5] | [5] | [4] | [14] | Roadmap Q2 |
| G-010 | [4] | [3] | [3] | [10] | Roadmap Q2 |
| G-020 | [3] | [2] | [4] | [9] | Roadmap Q3 |

> Score = Impact + Urgency + Effort (inverse: 5 = low effort). Higher = more urgent to address.

## Recommended Platform Roadmap Inputs

| Quarter | Gap | Capability to Build | Expected Outcome |
|---------|-----|--------------------|--------------------|
| Q[N] | G-001 | [Self-service secret rotation via platform CLI] | [Eliminate N support tickets/month; prevent credential-rotation incidents] |
| Q[N] | G-010 | [Devcontainer-based dev environment for all golden path services] | [Reduce new engineer onboarding from 3 days to < 4 hours] |
| Q[N+1] | G-020 | [Database migration scaffold in service template] | [Eliminate migration boilerplate for 6 teams] |

## Methodology

**Data collection methods used**:
- [ ] Quarterly developer survey (N respondents)
- [ ] Support ticket analysis (last 90 days)
- [ ] Postmortem review (last 6 months)
- [ ] Team lead interviews (N interviews)
- [ ] Incident review for platform-related root causes

**Next gap analysis scheduled**: [YYYY-MM-DD (next quarter)]
