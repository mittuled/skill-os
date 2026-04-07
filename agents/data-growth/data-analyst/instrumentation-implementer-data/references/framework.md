# Framework: Instrumentation Implementer

Defines the implementation patterns and integration approach for translating an approved instrumentation spec into correct tracking code across analytics platforms.

## SDK Integration Patterns

### Client-Side (Web)

```
Trigger point:  User interaction event handler (onClick, onSubmit, onChange)
SDK call:       analytics.track('event_name', { property: value })
Context:        Populated via analytics.identify() on login + global middleware for session/platform
Error handling: try-catch around SDK call; log warning if required property is undefined; send event with null marker — do not suppress
```

### Mobile (iOS / Android)

```
Trigger point:  View lifecycle callbacks or gesture recognizers (not viewDidAppear for interaction events)
SDK call:       Analytics.shared.track(event: 'event_name', properties: ['property': value])
Context:        Set on app launch via identify; platform/app_version auto-populated by SDK middleware
Error handling: Guard against nil required properties; send with nil value and log; never drop the event
```

### Server-Side

```
Trigger point:  After the operation completes successfully (not before; not on attempt)
SDK call:       analytics.track(userId, 'event_name', { property: value })
Context:        userId required; server-side events must include IP anonymization if applicable
Error handling: Non-blocking async call; retry once on network failure; log failed sends to error queue
```

## Property Population Rules

| Property Type | Source | Implementation Pattern |
|--------------|--------|----------------------|
| User ID | Auth session / JWT claim | Read from session context; never hardcode |
| Session ID | Analytics SDK middleware | Auto-populated by SDK if configured correctly |
| Plan tier | User object from database/API | Fetch from user context, not from URL parameters |
| Feature flags | Feature flag service | Read at event fire time, not at page load |
| Enum properties | Spec allowed-values list | Validate against allowed list before sending; log unexpected values |
| Timestamp | Server-side: UTC now; client-side: SDK auto-populates | Let SDK handle; only override for server-timestamp correction |

## Context Properties (Required on Every Event)

| Property | Type | Source |
|---------|------|--------|
| user_id | string (hashed) | Auth session |
| anonymous_id | string | Analytics SDK |
| session_id | string | Analytics SDK |
| platform | enum: web / ios / android / server | SDK config |
| app_version | string | Build metadata |
| environment | enum: development / staging / production | Environment variable |

## Edge Case Handling

| Scenario | Implementation |
|---------|---------------|
| Required property is null/undefined at fire time | Send event with `property: null`; log a warning with event name and property name; never drop the event |
| User is logged out but event fires | Use `anonymous_id`; set `user_id: null`; do not block the event |
| Duplicate submission (double-click, back-navigation) | Implement client-side deduplication using a request ID or idempotency key on the event payload |
| Bot / automation traffic | Check user agent against bot list in SDK middleware; suppress at SDK level, not at call site |
| Feature flag not yet evaluated | Do not fire the event if the feature gate has not resolved; wait for resolution |

## Verification Handoff Checklist

Before handing off to the instrumentation verifier, the implementer must confirm:
- [ ] All spec-defined events are implemented and deployed to staging
- [ ] Context middleware is configured (user_id, session_id, platform, app_version)
- [ ] Internal test account suppression is active
- [ ] Each event has a documented test scenario (user action → expected event)
- [ ] Edge cases (null properties, duplicate submissions) are handled per the framework above
