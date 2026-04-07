# Architecture Review: [System / Component Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Reviewer | VP Engineering |
| Proposal Author | [Name / Team] |
| Version | [1.0] |
| Skill | architecture-reviewer |
| Decision Needed By | [YYYY-MM-DD] |
| Status | [In Review / Approved / Rejected / Deferred] |

## Executive Summary

[2–3 sentences covering the proposal scope, the overall recommendation, and the single biggest risk or concern.
GUIDANCE: State the verdict first — "Approving this event-sourcing proposal with two conditions: a bounded-context partitioning decision must be made before implementation begins, and the event schema versioning strategy must be documented in an ADR within Sprint 1."]

## Proposal Overview

**What is being proposed?**
[1–2 sentences describing the architectural change or new system being introduced.]

**Why is this change needed?**
[Problem statement: the current limitation, business driver, or opportunity this addresses.]

**Scope of change**
[Services, components, teams, and users affected.]

## Architecture Assessment

### Fitness for Purpose

| Requirement | Met? | Evidence / Gap |
|------------|------|----------------|
| [Functional requirement 1] | [Yes / Partial / No] | [Evidence or gap description] |
| [Functional requirement 2] | [Yes / Partial / No] | [Evidence or gap description] |
| [Non-functional: latency target] | [Yes / Partial / No] | [Evidence or gap description] |
| [Non-functional: availability target] | [Yes / Partial / No] | [Evidence or gap description] |
| [Non-functional: scalability target] | [Yes / Partial / No] | [Evidence or gap description] |

### Trade-Off Analysis

| Attribute | Current Approach | Proposed Approach | Delta |
|-----------|-----------------|-------------------|-------|
| Scalability | [Assessment] | [Assessment] | [Better/Worse/Same] |
| Operational complexity | [Assessment] | [Assessment] | [Better/Worse/Same] |
| Data consistency | [Assessment] | [Assessment] | [Better/Worse/Same] |
| Development velocity | [Assessment] | [Assessment] | [Better/Worse/Same] |
| Cost (infra) | [Assessment] | [Assessment] | [Better/Worse/Same] |
| Cost (engineering) | [Assessment] | [Assessment] | [Better/Worse/Same] |
| Reversibility | [Assessment] | [Assessment] | [Better/Worse/Same] |

### Design Concerns

| # | Concern | Severity | Proposed Resolution |
|---|---------|----------|---------------------|
| 1 | [Specific design concern] | [Critical / High / Medium / Low] | [How to address] |
| 2 | | | |

> Severity guide: Critical = blocks approval | High = conditional approval | Medium = tracked in backlog | Low = noted

### Alignment with Engineering Principles

| Principle | Aligned? | Notes |
|-----------|----------|-------|
| Single responsibility | [Yes/No/Partial] | |
| Clear failure modes | [Yes/No/Partial] | |
| Observability-first | [Yes/No/Partial] | |
| Security by design | [Yes/No/Partial] | |
| Cloud-native patterns | [Yes/No/Partial] | |
| Avoid premature optimisation | [Yes/No/Partial] | |

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| [Risk description] | [H/M/L] | [H/M/L] | [Mitigation action] |
| Data migration failure | | | |
| Performance under load | | | |
| Dependency on external system | | | |

## Decision

**Verdict**: [Approved / Approved with conditions / Rejected / Deferred]

### Conditions (if applicable)

1. [Specific condition that must be met before implementation begins or within Sprint N]
2. [ADR or design document that must be authored]

### Required ADRs

| ADR Topic | Owner | Due |
|-----------|-------|-----|
| [Decision that needs to be recorded] | [Name] | [Date] |

## Review Notes

[Freeform section for detailed observations, open questions, and context that does not fit the structured sections above.]

---

## Appendix: Questions for Proposal Author

[List of open questions that must be answered before or during the review.]

1. [Question]
2. [Question]
