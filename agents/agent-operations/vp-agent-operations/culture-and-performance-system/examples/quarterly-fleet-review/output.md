# Fleet Performance Review: Q1 2026

## Metadata
| Field | Value |
|-------|-------|
| Date | 2026-04-05 |
| Author | VP Agent Operations |
| Version | 1.0 |
| Status | Final |
| Skill | culture-and-performance-system |

## Executive Summary
Fleet composite score is 6.8/10 (Adequate). Two critical regressions: sr-backend-developer accuracy regression post-model upgrade and growth-engineer latency spike. Immediate remediation required for both.

## Per-Agent Scorecards
### sr-backend-developer
| Metric | Q4 | Q1 | Delta |
|--------|-----|-----|-------|
| Accuracy | 8.2 | 6.8 | -1.4 |
| Latency p95 | 4.2s | 4.5s | +0.3s |
| Error Rate | 2.1% | 5.3% | +3.2% |
**Tier**: Needs Improvement

## Remediation Plan
| # | Action | Owner | Deadline | Metric |
|---|--------|-------|----------|--------|
| 1 | Rollback sr-backend model | Config Mgr | Apr 12 | Accuracy >= 8.0 |
| 2 | Investigate growth-eng latency | Trainer | Apr 15 | p95 < 5s |
