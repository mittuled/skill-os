# Disaster Recovery Drill Results Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Security & Compliance Programme Manager] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | disaster-recovery-drill-runner |

## Executive Summary

[2-3 sentences summarizing the drill type, systems tested, overall RTO/RPO achievement, and critical gaps found.
GUIDANCE: Lead with pass/fail against targets and the most significant finding.]

## Drill Plan Summary

[Drill scope and parameters.

GUIDANCE:
- Good: "Drill Type: Full failover. Scope: Production database (PostgreSQL), application servers (3x), CDN origin. RTO Target: 4 hours. RPO Target: 1 hour. Window: 2026-03-15 02:00-08:00 UTC. Participants: SRE team (3), DBA (1), Engineering lead (1), Security (1)."
- Bad: "We did a DR drill"
- Format: Table with Drill Type, Scope, RTO Target, RPO Target, Window, Participants, Rollback Plan]

## Execution Log

[Timestamped drill actions and observations.

GUIDANCE:
- Good: "02:00 — Initiated failover. 02:03 — Primary DB connection severed. 02:07 — Replica promoted to primary. 02:15 — Application servers reconnected to new primary. 02:22 — Health checks passing. 02:25 — CDN origin updated. 02:31 — Full application availability confirmed."
- Bad: "Drill was completed successfully"
- Format: Timestamped log with action, result, and observations per step]

## RTO/RPO Achievement

[Actual vs. target recovery metrics.

GUIDANCE:
- Good: Table with System, RTO Target, Actual RTO, RTO Met (Y/N), RPO Target, Actual RPO, RPO Met (Y/N), Data Integrity Verified (Y/N)
- Bad: "We met our targets"
- Format: Per-system comparison table with pass/fail]

## Gap Analysis

[Identified issues during drill execution.

GUIDANCE:
- Good: "Gap 1: Database replica promotion took 7 minutes vs. expected 2 minutes. Root cause: Replica lag of 450MB due to batch job running during drill window. Impact: Added 5 minutes to RTO. Remediation: Schedule batch jobs outside failover-eligible windows."
- Bad: "Some things were slow"
- Format: Per-gap analysis with description, root cause, impact on RTO/RPO, and remediation]

## Remediation Actions

[Actions to address identified gaps.

GUIDANCE:
- Good: Table with Gap ID, Remediation Action, Owner, Deadline, Follow-Up Drill Required (Y/N)
- Bad: "We'll fix things"
- Format: Action tracker with accountability]

## Recommendations

[Post-drill improvements.
GUIDANCE: Each recommendation should be:
- Specific (not "improve DR" but "add replica lag monitoring alert with 100MB threshold to prevent failover during high-lag periods")
- Actionable (assignable to SRE/DBA/Engineering)
- Prioritized (P1/P2/P3)]

## Appendices

### A. Methodology

[Scoring rubric applied per `references/scoring-rubric.md`. Drill executed per SOC 2 A1.3 (recovery testing) and ISO 27001 A.17.1.3 (verify/review/evaluate continuity). Metrics captured via monitoring platform.]

### B. Supporting Data

[Monitoring dashboards, backup restoration logs, failover automation logs, communication transcripts, pre-drill readiness checklist sign-offs.]
