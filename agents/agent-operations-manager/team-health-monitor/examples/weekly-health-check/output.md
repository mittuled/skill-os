# Fleet Health Report: Mar 22-28 2026

## Metadata
| Field | Value |
|-------|-------|
| Date | 2026-03-28 |
| Author | Agent Operations Manager |
| Version | 1.0 |
| Status | Final |
| Skill | team-health-monitor |

## Executive Summary
22/24 agents healthy. 2 in warning state: growth-engineer (error rate 7.2%) and data-analyst (context usage 88%). No critical issues.

## Fleet Summary
| Status | Count | Trend |
|--------|-------|-------|
| Healthy | 22 | → (stable) |
| Warning | 2 | ↑ (was 1) |
| Critical | 0 | → |

## Anomalies
### growth-engineer: Error Rate Spike
- Expected: < 5% | Actual: 7.2% | Since: Mar 25
- Root cause: Upstream API returning malformed JSON since deployment v2.3.1
