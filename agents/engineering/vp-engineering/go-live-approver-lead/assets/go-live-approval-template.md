# Go-Live Approval: [Project / Feature Name]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Approver | VP Engineering |
| Project | [Project name] |
| Target Go-Live | [YYYY-MM-DD HH:MM UTC] |
| Skill | go-live-approver-lead |
| Decision | [APPROVED / APPROVED WITH CONDITIONS / DELAYED / REJECTED] |

## Go-Live Readiness Gates

All gates must be green for approval. Status = Green (met), Amber (minor gaps), Red (blocking).

| Gate | Owner | Status | Evidence |
|------|-------|--------|---------|
| All milestones complete | Engineering Lead | [Green/Amber/Red] | [Link] |
| Production readiness review passed | DevOps | [Green/Amber/Red] | [Link] |
| Staging validation passed | QA | [Green/Amber/Red] | [Link] |
| Security review complete | Security Engineer | [Green/Amber/Red] | [Link] |
| Performance targets met | QA / DevOps | [Green/Amber/Red] | [Link] |
| Runbooks authored and reviewed | DevOps | [Green/Amber/Red] | [Link] |
| Monitoring and alerting active | DevOps | [Green/Amber/Red] | [Link] |
| On-call rotation includes this service | DevOps | [Green/Amber/Red] | [Link] |
| Rollback plan documented and tested | DevOps | [Green/Amber/Red] | [Link] |
| Data migration tested in staging | Engineering | [Green/Amber/Red] | [Link] |
| Customer support briefed | CS Lead | [Green/Amber/Red] | [Link] |
| Marketing comms scheduled (if external) | Marketing | [Green/Amber/Red] | [Link] |

**Gate summary**: [N Green / N Amber / N Red]

## Open Issues

| # | Issue | Severity | Owner | Resolution Plan |
|---|-------|---------|-------|----------------|
| 1 | [Issue description] | [Blocking / Acceptable] | [Role] | [Plan and ETA] |

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation in Place |
|------|-----------|--------|---------------------|
| [Top risk] | [H/M/L] | [H/M/L] | [Mitigation] |
| Rollback needed | [H/M/L] | [H/M/L] | [Rollback plan: link] |

## Decision

**Approval decision**: [APPROVED / APPROVED WITH CONDITIONS / DELAYED / REJECTED]

**Conditions** (if applicable):
1. [Specific condition that must be met before traffic is enabled]

**Go-live window**: [YYYY-MM-DD HH:MM – HH:MM UTC]
**Rollout strategy**: [Canary 1% → 10% → 100% / Immediate full release / Feature flag]

**Approver sign-off**: VP Engineering: [Name] | Date: [YYYY-MM-DD HH:MM UTC]
