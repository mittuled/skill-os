# Enterprise Implementation Playbook v1.0

| Field | Value |
|---|---|
| Date | 2026-03-31 |
| Tier | Enterprise (500+ seats) |
| Total Duration | 18 weeks |
| Phases | 8 |
| Prepared by | Implementation Lead |
| Status | Draft — pending team review |
| Skill | implementation-playbook-builder |

## Executive Summary

The Enterprise Implementation Playbook standardizes the end-to-end implementation process for enterprise customers. It defines 8 phases over 18 weeks, from signed contract to hypercare completion. Each phase has defined entry criteria, deliverables, and RACI assignments. The playbook includes a template library covering all key customer-facing documents.

## Phase Plan

| Phase | Duration | Entry Criteria | Deliverables |
|---|---|---|---|
| Discovery & Requirements | 2 weeks | Contract signed | Requirements document, Customer sign-off |
| Security Review | 1 week | Discovery complete | Security questionnaire, BAA signed |
| Environment Configuration | 3 weeks | Requirements & security complete | Provisioned environment, SSO/auth configured |
| Integration Setup | 4 weeks | Environment configured | Connected integrations, Data flow verified |
| Data Migration | 2 weeks | Integrations live | Migrated dataset, Quality report |
| Acceptance Testing | 2 weeks | Migration complete | Test results, Customer sign-off |
| Training | 2 weeks | Acceptance testing passed | Admin training, End-user training, Training materials |
| Go-Live & Hypercare | 2 weeks | Training complete | Production launch, Hypercare monitoring report |

**Total: 18 weeks from contract signed to hypercare close**

## Go-Live Criteria

All of the following must be met before go-live:

1. All acceptance criteria documented in requirements doc are passed and customer-signed
2. 100% of contracted integrations are live and data flow verified
3. Executive sponsor has approved go-live in writing
4. Support team has received handoff brief with customer context
5. Hypercare monitoring plan is active

## RACI Roles

| Role | Responsibility |
|---|---|
| Implementation Engineer | Executes technical configuration, integration setup, and data migration |
| Implementation Lead | Governs the process, escalates blockers, owns the playbook |
| Customer Admin | Provides access, credentials, and technical resources |
| Customer Executive Sponsor | Approves decisions, removes customer-side blockers |

## Template Library

1. Executive kickoff deck
2. Technical discovery questionnaire
3. Requirements document template
4. RACI matrix template
5. Weekly status report template
6. Acceptance testing checklist
7. Go-live readiness checklist
8. Hypercare incident log

## Complexity Tier Guidance

This playbook is for **enterprise** customers (500+ seats, 3+ integrations, data migration required). For smaller customers:

- **Mid-market** (50-499 seats): Remove security review phase, reduce integration and configuration phases by 1 week each → ~12 weeks
- **SMB** (< 50 seats): Self-serve onboarding with 1-week assisted setup → ~6 weeks

## Next Steps

1. Review with implementation engineering team — 60-minute session
2. Pilot this playbook with the next enterprise customer (Bright Horizons Healthcare)
3. Collect feedback after Phase 1 and 2 to refine the discovery questionnaire
4. Publish to the internal knowledge base and link from the implementation CRM deal template
