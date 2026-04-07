# Instrumentation Implementation Plan

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Analytics Lead name] |
| Product Surface | [e.g., Web App v3, Mobile iOS, Checkout Flow] |
| Spec Reference | [Link to instrumentation-spec] |
| Version | [1.0] |
| Status | [Draft / Engineering Review / Approved] |
| Skill | instrumentation-planner-data |

## Executive Summary

[2-3 sentences covering what surface is being instrumented, the number of events across how many phases, and the expected rollout timeline.

GUIDANCE: Example: "This plan covers 38 events across 3 platforms (Web, iOS, Server) for the redesigned onboarding flow. Implementation spans 3 phases over 6 sprints, with verification gates between each phase. Full coverage is expected by [date]."]

## Current State Audit

| Platform | SDK Installed | SDK Version | Last Event Fired | Coverage Grade |
|----------|--------------|-------------|-----------------|----------------|
| Web (client) | [Yes / No] | [vX.X] | [event_name, date] | [A/B/C/D/None] |
| iOS | [Yes / No] | [vX.X] | [event_name, date] | [A/B/C/D/None] |
| Android | [Yes / No] | [vX.X] | [event_name, date] | [A/B/C/D/None] |
| Server-side | [Yes / No] | [vX.X] | [event_name, date] | [A/B/C/D/None] |

Coverage grades: A = comprehensive, B = partial gaps, C = critical gaps, D = minimal, None = absent.

## Tooling Selection

| Component | Selected Tool | Rationale | Alternatives Considered |
|-----------|--------------|-----------|------------------------|
| Analytics SDK | [Segment / Amplitude / Mixpanel SDK / Custom] | [reason] | [alternatives] |
| Event router / CDP | [Segment / Rudderstack / Custom] | [reason] | [alternatives] |
| Data destination | [BigQuery / Snowflake / Redshift] | [reason] | [alternatives] |
| Mobile tracking | [Amplitude SDK / Mixpanel iOS / Branch] | [reason] | [alternatives] |

## Event Routing Architecture

[Describe the flow from event trigger to final warehouse table.]

```
[Platform] → [SDK] → [Event Router / CDP] → [Data Warehouse]
                                           → [Analytics Platform]
```

| Step | Component | Responsibility | Retry Policy | Deduplication Method |
|------|-----------|---------------|-------------|---------------------|
| 1 | Client SDK | Capture and batch events | 3 retries, exponential backoff | Client-generated UUID |
| 2 | CDP ingestion | Schema validation, enrichment | Dead-letter queue on failure | Idempotency key |
| 3 | Warehouse load | Store raw events | Replay from CDC | Unique event_id constraint |

## Rollout Phases

### Phase 1: Core Funnel Events (Sprint [X–Y])

Objective: Capture the minimum events needed to measure acquisition-to-activation funnel.

| Event Name | Platform | Trigger Point in Code | Properties Required | Owner | Verification Gate |
|-----------|---------|----------------------|--------------------|----|------------------|
| [event_name] | [Web] | [file:line or component] | [prop1, prop2] | [Engineer] | Phase 1 verification checklist |
| [event_name] | [iOS] | [ViewController method] | [prop1, prop2] | [Engineer] | Phase 1 verification checklist |

**Phase 1 Verification Gate**: Run `instrumentation-verifier` against all Phase 1 events before Phase 2 begins. Pass criteria: ≥95% event volume within 5% of expected, all required properties present.

### Phase 2: Engagement Events (Sprint [X–Y])

Objective: Capture feature-level engagement and activation milestone events.

| Event Name | Platform | Trigger Point in Code | Properties Required | Owner | Verification Gate |
|-----------|---------|----------------------|--------------------|----|------------------|
| [event_name] | [Server] | [endpoint / service method] | [prop1, prop2] | [Engineer] | Phase 2 verification checklist |

**Phase 2 Verification Gate**: Run `instrumentation-verifier` against all Phase 2 events. Pass criteria: same as Phase 1.

### Phase 3: Edge Case and Error Events (Sprint [X–Y])

Objective: Capture error states, edge-case flows, and secondary conversion events.

| Event Name | Platform | Trigger Point in Code | Properties Required | Owner | Verification Gate |
|-----------|---------|----------------------|--------------------|----|------------------|
| [event_name] | [Web] | [component] | [prop1, prop2] | [Engineer] | Phase 3 verification checklist |

## Per-Team Task Assignments

### [Engineering Team 1 Name]

Sprint allocation: [X points / Y hours]

| Task | Event(s) | Platform | Acceptance Criteria |
|------|---------|----------|---------------------|
| [Implement signup_completed] | signup_completed | Web | Fires on POST /auth/signup 200 response; includes user_id, plan, referral_source |
| [Implement onboarding_step_viewed] | onboarding_step_viewed | Web | Fires on component mount; includes step_number, step_name |

### [Engineering Team 2 Name]

Sprint allocation: [X points / Y hours]

| Task | Event(s) | Platform | Acceptance Criteria |
|------|---------|----------|---------------------|
| [Implement feature_activated] | feature_activated | iOS | Fires on first successful feature action; includes feature_name, user_id |

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Ad blocker interference on client-side events | High | Medium | Mirror critical events server-side |
| SDK version incompatibility on older iOS builds | Medium | High | Test against minimum supported iOS version |
| Engineering bandwidth conflicts with product sprint | Medium | High | Pre-align sprint allocation 2 weeks ahead |
| Event volume spike causing CDP throttling | Low | High | Configure CDP rate limits and burst capacity |

## Timeline Summary

| Phase | Start Date | End Date | Verification Gate Date | Status |
|-------|-----------|----------|----------------------|--------|
| Phase 1: Core Funnel | [YYYY-MM-DD] | [YYYY-MM-DD] | [YYYY-MM-DD] | [Not Started] |
| Phase 2: Engagement | [YYYY-MM-DD] | [YYYY-MM-DD] | [YYYY-MM-DD] | [Not Started] |
| Phase 3: Edge Cases | [YYYY-MM-DD] | [YYYY-MM-DD] | [YYYY-MM-DD] | [Not Started] |
