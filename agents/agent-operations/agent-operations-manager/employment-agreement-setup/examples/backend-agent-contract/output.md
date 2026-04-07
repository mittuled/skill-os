# Agent Contract: sr-backend-developer v1.0

## Metadata
| Field | Value |
|-------|-------|
| Date | 2026-03-10 |
| Author | Agent Operations Manager |
| Version | 1.0 |
| Status | Final |
| Skill | employment-agreement-setup |

## Executive Summary
Defines the interaction contract for sr-backend-developer covering 3 skills: code generation, code review, and API design.

## Input Schema
```json
{"task": "code-generation", "language": "typescript", "requirements": "...", "context": {"repo": "...", "files": [...]}}
```

## SLA Requirements
| Metric | Target |
|--------|--------|
| Latency p50 | < 8s |
| Latency p95 | < 15s |
| Accuracy | >= 8.0/10 |
