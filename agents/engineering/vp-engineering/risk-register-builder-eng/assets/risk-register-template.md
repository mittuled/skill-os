# Engineering Risk Register: [Project / Initiative Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Owner | VP Engineering |
| Project | [Project name] |
| Phase | [Phase N / Sprint N–M] |
| Review Cadence | [Weekly / Bi-weekly] |
| Last Reviewed | [YYYY-MM-DD] |
| Skill | risk-register-builder-eng |

## Risk Summary

| Severity | Count | Open | Mitigated | Closed |
|----------|-------|------|-----------|--------|
| Critical | [N] | [N] | [N] | [N] |
| High | [N] | [N] | [N] | [N] |
| Medium | [N] | [N] | [N] | [N] |
| Low | [N] | [N] | [N] | [N] |
| **Total** | **[N]** | **[N]** | **[N]** | **[N]** |

## Active Risks

### Critical Risks

| ID | Risk | Likelihood | Impact | Score | Owner | Mitigation | ETA | Status |
|----|------|-----------|--------|-------|-------|------------|-----|--------|
| R-001 | [Risk description] | [1–5] | [1–5] | [L×I] | [Role] | [Mitigation action] | [Date] | [Open] |

### High Risks

| ID | Risk | Likelihood | Impact | Score | Owner | Mitigation | ETA | Status |
|----|------|-----------|--------|-------|-------|------------|-----|--------|
| R-002 | [Risk description] | [1–5] | [1–5] | [L×I] | [Role] | [Mitigation action] | [Date] | [Open] |

### Medium Risks

| ID | Risk | Likelihood | Impact | Score | Owner | Mitigation | ETA | Status |
|----|------|-----------|--------|-------|-------|------------|-----|--------|
| R-003 | [Risk description] | [1–5] | [1–5] | [L×I] | [Role] | [Mitigation action] | [Date] | [Open] |

### Low Risks

| ID | Risk | Likelihood | Impact | Score | Owner | Mitigation | ETA | Status |
|----|------|-----------|--------|-------|-------|------------|-----|--------|
| R-004 | [Risk description] | [1–5] | [1–5] | [L×I] | [Role] | [Contingency] | [Date] | [Monitoring] |

## Scoring Guide

**Likelihood** (1–5): 1 = Rare (<10%) | 2 = Unlikely (10–25%) | 3 = Possible (25–50%) | 4 = Likely (50–75%) | 5 = Almost Certain (>75%)

**Impact** (1–5): 1 = Negligible | 2 = Minor (< 1 day delay) | 3 = Moderate (1–5 day delay) | 4 = Major (> 1 week delay or scope cut) | 5 = Critical (phase failure or data loss)

**Risk Score** = Likelihood × Impact

| Score | Severity | Response |
|-------|----------|----------|
| 20–25 | Critical | Immediate escalation; mitigation plan in 24 hrs |
| 12–19 | High | Weekly review; owner must present mitigation plan |
| 6–11 | Medium | Bi-weekly review; mitigation tracked in backlog |
| 1–5 | Low | Monthly review; contingency documented |

## Risk Categories

Mark each risk with its primary category:

| Category | Examples |
|----------|---------|
| Technical | Architecture complexity, third-party API instability, infrastructure capacity |
| Schedule | Dependency delays, under-estimation, scope creep |
| Resource | Key person dependency, hiring delays, team illness |
| External | Vendor changes, regulatory requirements, data access |
| Security | Credential exposure, unpatched CVEs, compliance gaps |
| Operational | Runbook gaps, on-call coverage, monitoring blind spots |

## Mitigated / Closed Risks

| ID | Risk | Closed Date | Resolution |
|----|------|-------------|------------|
| R-xxx | [Risk description] | [Date] | [How it was resolved] |

## Escalation Thresholds

| Condition | Action |
|-----------|--------|
| Any Critical risk open > 48 hrs without mitigation plan | Escalate to CTO |
| 3+ High risks simultaneously open | Trigger phase scope review |
| Risk score for any item increases by > 5 | Immediate re-review and owner notification |
| New risk identified < 1 week before phase end | Emergency planning session |
