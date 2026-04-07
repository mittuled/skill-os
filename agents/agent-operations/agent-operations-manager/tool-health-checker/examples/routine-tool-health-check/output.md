# Tool Health Report

## Metadata
| Field | Value |
|-------|-------|
| Date | 2026-03-28 |
| Author | Agent Operations Manager |
| Version | 1.0 |
| Status | Final |
| Skill | tool-health-checker |

## Executive Summary
14/15 tools healthy. Salesforce unreachable due to expired OAuth token. Immediate credential rotation required.

## Health Status
| Tool | Status | Latency | Auth |
|------|--------|---------|------|
| GitHub | Healthy | 145ms | Valid |
| Slack | Healthy | 89ms | Valid |
| Salesforce | Unreachable | — | Expired |

## Critical: Salesforce
**Error**: OAuth token expired Mar 26
**Impact**: Sales agents cannot access CRM data
**Remediation**: Rotate OAuth credentials in secret store, run connect-mcp.py
