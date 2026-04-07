# Growth Instrumentation Rollout Plan

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Growth Engineer name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | instrumentation-planner-growth |
| Sprint / Quarter | [Q2 2026 / Sprint 14] |
| Growth Lead | [Name] |

## Executive Summary

[2-3 sentences summarizing the instrumentation scope, the experiment roadmap it enables, and the critical path.
GUIDANCE: Lead with what experiments become unblocked by this plan. Example: "This rollout plan instruments 12 growth events across web and iOS to unblock 3 experiments in Q2: signup flow optimization, onboarding completion nudge, and referral launch. The critical path is Phase 1 (signup events) which must complete by April 14 to allow the signup experiment to launch on April 21. Phase 2 and 3 can proceed in parallel after Phase 1 completes."]

## Surface Inventory

[All product surfaces where growth events must fire.

GUIDANCE:
- Good: List each surface with platform and the specific user flows that require instrumentation
- Bad: "Web and mobile app"]

| Surface | Platform | Growth Flows | Priority |
|---------|----------|-------------|----------|
| [e.g., Marketing landing page] | [Web] | [CTA clicks, form starts] | [P0] |
| [e.g., Signup flow] | [Web + iOS] | [Signup started/completed, email verification] | [P0] |
| [e.g., Onboarding wizard] | [Web + iOS] | [Step completions, skip events, activation] | [P1] |
| [e.g., Referral share flow] | [Web + iOS] | [Link generated, shared, clicked] | [P2] |
| [e.g., Upgrade modal] | [Web] | [Modal viewed, upgrade clicked, upgrade completed] | [P2] |

## Event Priority Sequencing

[Events ordered by experiment dependency — highest-priority experiment's events ship first.

GUIDANCE:
- Good: Show which experiment each event enables, so stakeholders understand the sequencing rationale
- Bad: Alphabetical list of events]

| Priority | Event Name | Platform | Required By Experiment | Status |
|----------|-----------|----------|----------------------|--------|
| P0 | [experiment_viewed] | [All] | [All A/B tests] | [ ] Planned / [ ] In Progress / [ ] Done |
| P0 | [signup_started] | [Web, iOS] | [Signup funnel experiment] | [ ] |
| P0 | [signup_completed] | [Web, iOS] | [Signup funnel experiment] | [ ] |
| P1 | [onboarding_step_completed] | [Web, iOS] | [Onboarding experiment] | [ ] |
| P1 | [activation_completed] | [Server] | [Onboarding experiment] | [ ] |
| P2 | [referral_link_generated] | [Web, iOS] | [Referral launch] | [ ] |

## Experiment Infrastructure Plan

[A/B test tooling setup required before experiments can launch.

GUIDANCE:
- Good: Specify the SDK, assignment logic, and kill-switch mechanism
- Bad: "We will set up A/B testing"]

| Component | Design | Owner | Due Date |
|-----------|--------|-------|----------|
| A/B SDK integration | [e.g., GrowthBook SDK on web; LaunchDarkly on iOS] | [@engineer] | [Date] |
| Variant assignment | [e.g., User-stable, server-side, consistent across platforms] | [@engineer] | [Date] |
| Experiment config | [e.g., Feature flag JSON in GitHub; deployed via CI] | [@engineer] | [Date] |
| Kill switch | [e.g., Flag disables experiment; returns all traffic to control within 5 min] | [@engineer] | [Date] |

## Attribution Pipeline Design

[UTM capture and attribution model.

GUIDANCE:
- Good: Specify which UTM parameters are captured, where they're stored, and which attribution model drives CAC reporting
- Bad: "We will track UTM parameters"]

| Component | Design | Storage | Persistence |
|-----------|--------|---------|------------|
| First UTM capture | [On landing page load] | [User profile at signup] | [Permanent — not overwritten] |
| Last-touch UTM | [On each session start] | [Events table] | [Per session] |
| Attribution model | [First-touch for channel CAC; last-touch for conversion] | [Analytics warehouse] | [30-day lookback window] |
| Cross-device stitching | [Email-based post-login; probabilistic pre-login] | [User identity graph] | |

## Verification Gates

[Checkpoints that must pass before each experiment is allowed to launch.

GUIDANCE:
- Good: Specify the exact test for each gate and who is responsible for sign-off
- Bad: "QA the events before launching"]

| Phase | Required Events | Gate Test | Sign-Off Owner | Gate Status |
|-------|----------------|-----------|---------------|------------|
| Phase 1 | [signup_started, signup_completed, experiment_viewed] | [Events fire in Segment Debugger within 5s; schema validates; volume matches signup rate ±20%] | [Growth Lead] | [ ] Not Started / [ ] Testing / [ ] Passed |
| Phase 2 | [onboarding_step_N_completed, activation_completed] | [Same checks + server-side event reconciliation] | [Growth Lead] | [ ] |
| Phase 3 | [referral_link_generated, upgrade_completed] | [Same checks] | [Growth Lead] | [ ] |

**Rule**: No experiment in a phase launches until its phase gate is `Passed`.

## Phased Rollout Plan

[Task-level breakdown with owners, platforms, and timeline.

GUIDANCE:
- Good: Each task is a specific code change or configuration with a single owner and clear done criteria
- Bad: "Phase 1: Instrument signup"]

### Phase 1: [Name] — Due: [Date]

| Task | Platform | Owner | Done Criteria |
|------|----------|-------|--------------|
| [Add signup_started event to signup form component] | [Web] | [@engineer] | [Event fires in Segment Debugger with required properties] |
| [Add experiment_viewed event to A/B SDK wrapper] | [Web + iOS] | [@engineer] | [Fires on first exposure; not on subsequent renders] |

### Phase 2: [Name] — Due: [Date]

| Task | Platform | Owner | Done Criteria |
|------|----------|-------|--------------|

### Phase 3: [Name] — Due: [Date]

| Task | Platform | Owner | Done Criteria |
|------|----------|-------|--------------|

## Recommendations

[Prioritized recommendations for the growth lead and engineering team.

GUIDANCE: Focus on schedule risks, missing dependencies, and cross-platform consistency gaps.]

- **P1**: [Critical blocker or dependency that puts the experiment calendar at risk]
- **P2**: [Important improvement for tracking reliability or attribution accuracy]
- **P3**: [Long-term instrumentation architecture improvement]

## Appendices

### A. Event Schema Definitions

[Schema for each event in this plan, to be implemented consistently across platforms.]

| Event Name | Required Properties | Optional Properties | Notes |
|-----------|--------------------|--------------------|-------|
| [experiment_viewed] | [experiment_id, variant_id, user_id, timestamp] | [page, session_id] | |
| [signup_started] | [user_id (anonymous), source, timestamp] | [utm_source, utm_campaign] | |

### B. Dependency Map

[External dependencies (SDK releases, backend API changes) that could affect the timeline.]

| Dependency | Required By | Owner | ETA | Risk |
|-----------|------------|-------|-----|------|
| [iOS app release with A/B SDK] | [Phase 1] | [@mobile-team] | [Date] | [High if delayed] |
