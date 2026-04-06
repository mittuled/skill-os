# Framework: Growth Instrumentation Planning

Defines the structured approach for planning growth tracking rollout across product surfaces, sequencing experiment infrastructure, attribution pipeline setup, and verification gates.

## Instrumentation Planning Architecture

```
Growth Experiment Roadmap
         │
         ▼
Surface Inventory (web / iOS / Android / server)
         │
         ▼
Event Priority Sequencing (next experiment first)
         │
         ▼
Experiment Infrastructure Plan (A/B test SDK + variant assignment)
         │
         ▼
Attribution Pipeline Design (UTM → first-touch → multi-touch → CAC)
         │
         ▼
Verification Gates (events pass QA before experiment launches)
         │
         ▼
Phased Rollout Plan (with timeline and ownership)
```

## Product Surface Classification

| Surface | Tracking Layer | Event Ownership |
|---------|---------------|----------------|
| Marketing site (web) | Client-side JS (Segment, Mixpanel, or custom) | Growth Engineer |
| Signup flow (web/mobile) | Client-side + server-side (server-side for reliability) | Growth Engineer + Backend |
| Onboarding flow (web/mobile) | Client-side | Growth Engineer |
| Activation points (in-app) | Client-side + server-side | Growth Engineer + Backend |
| Referral mechanics (web/mobile) | Server-side (authoritative for attribution) | Growth Engineer + Backend |
| Upgrade / conversion flow | Server-side + client-side | Growth Engineer + Backend |
| Re-engagement notifications | Server-side (send events) + client-side (open/click) | Growth Engineer |

## Event Prioritization by Experiment Dependency

Events ship in dependency order — if the next experiment requires `activation_completed`, that event ships first.

| Priority | Event Category | Experiment Dependency | Platform |
|----------|---------------|----------------------|----------|
| P0 | Experiment exposure event (`experiment_viewed`) | All experiments | All |
| P0 | Signup started / signup completed | Signup funnel experiments | Web + Mobile |
| P1 | Onboarding step N completed | Onboarding experiments | Web + Mobile |
| P1 | Activation event (first core action) | Activation experiments | Web + Mobile + Server |
| P2 | Referral link generated / referral link clicked | Referral experiments | Web + Mobile |
| P2 | Upgrade page viewed / upgrade completed | Monetization experiments | Web + Server |
| P3 | Notification sent / opened / clicked | Re-engagement experiments | Server + Client |

## Experiment Infrastructure Components

### A/B Test SDK Integration

| Component | Options | Decision Criteria |
|-----------|---------|-----------------|
| Client-side assignment | LaunchDarkly, Optimizely, GrowthBook | Choose if low-latency assignment needed (UI flicker prevention) |
| Server-side assignment | LaunchDarkly, Statsig, custom | Choose for server-rendered pages, API-gated features |
| Hybrid | Client flags + server logging | Standard for most B2B/SaaS products |

### Variant Assignment Requirements

- [ ] User-stable assignment: same user always gets same variant
- [ ] Consistent across platforms: mobile and web user in same variant
- [ ] Logged at time of first exposure (not first conversion)
- [ ] Mutually exclusive experiments configured where needed

### Experiment Configuration Management

| Requirement | Implementation |
|-------------|---------------|
| Experiment definition (variants, traffic split, targeting rules) | Feature flag platform or config file in version control |
| Kill switch | Ability to disable experiment and return all traffic to control within 5 minutes |
| Traffic ramp | Start at 10% → 50% → 100% with manual approval gates |

## Attribution Pipeline Design

### UTM Capture Requirements

| Parameter | Required? | Storage | Example |
|-----------|-----------|---------|---------|
| `utm_source` | Yes | User profile + events | `google`, `facebook`, `referral` |
| `utm_medium` | Yes | User profile + events | `cpc`, `email`, `organic` |
| `utm_campaign` | Yes | User profile + events | `q1-2026-retargeting` |
| `utm_content` | Recommended | Events only | `hero-cta-v2` |
| `utm_term` | Paid search only | Events only | `crm+software` |

### Attribution Model

| Model | Use Case | Limitation |
|-------|----------|-----------|
| First-touch (first UTM source) | Top-of-funnel channel attribution | Ignores nurture channels |
| Last-touch (last UTM source) | Conversion channel attribution | Ignores awareness channels |
| Linear multi-touch | Balanced channel credit | Requires complete session history |
| Time-decay | Recency-weighted credit | More complex; accurate for long cycles |

**Recommended default**: First-touch for channel CAC calculation; last-touch for conversion attribution.

### Attribution Persistence Requirements

- First UTM parameters persisted to user profile at signup (not overwritten by subsequent visits)
- Last UTM parameters persisted per session for conversion attribution
- Attribution persists through email verification → login → activation journey
- Cross-device attribution: link mobile and web sessions via email (post-login) or probabilistic matching (pre-login)

## Verification Gate Requirements

Every event must pass these checks before its dependent experiment can launch:

| Gate | Check | Tool |
|------|-------|------|
| Event fires | Event appears in tracking backend within 5 seconds of user action | Segment Debugger / Mixpanel Live Events |
| Event schema | All required properties present with correct types | Schema validation (Segment Protocols / custom) |
| Volume sanity check | Event count matches expected user action frequency (±20%) | Monitoring dashboard |
| Deduplication | No duplicate events for same user action in same session | Event-level deduplication check |
| Cross-platform parity | Same event name and schema on web and mobile | Platform-by-platform schema comparison |

**Gate rule**: No experiment launches until ALL its required events have passed ALL verification gates.

## Rollout Plan Template

| Phase | Surfaces | Events | Experiment Infrastructure | Due Date | Owner |
|-------|---------|--------|--------------------------|----------|-------|
| Phase 1 | [Landing page, signup flow] | [signup_started, signup_completed, experiment_viewed] | [A/B SDK on signup flow] | [Date] | [@engineer] |
| Phase 2 | [Onboarding flow] | [onboarding_step_N_completed, activation_completed] | | [Date] | [@engineer] |
| Phase 3 | [Referral, upgrade flow] | [referral_link_generated, upgrade_completed] | | [Date] | [@engineer] |
