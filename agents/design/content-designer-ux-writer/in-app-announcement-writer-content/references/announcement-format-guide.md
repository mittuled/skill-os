# In-App Announcement Format Guide

## Purpose

A reference for selecting announcement formats, applying tone correctly, and avoiding announcement fatigue when communicating product changes to users within the product interface.

## Format Selection Matrix

| Announcement Type | Recommended Format | When to Use | Avoid |
|------------------|--------------------|-------------|-------|
| New feature launch (non-breaking) | Modal or tooltip coach mark | High-value feature that benefits most users; once per release | Banners — too easy to dismiss; tooltip only if contextual |
| Feature update (minor, non-breaking) | Persistent banner (dismissible) | Changes to existing flows that users will encounter next session | Modal — unnecessary interruption for incremental changes |
| Breaking change / workflow disruption | Modal (with CTA to learn more) | Any change that alters existing user behaviour; migration required | Toast — too transient for high-urgency information |
| Scheduled maintenance | System banner | Planned downtime > 5 minutes; displayed 24–48 h before | Modal — pre-maintenance modals are disruptive; use banner only |
| Deprecation notice | Persistent banner (30 days) | Feature being removed; users need time to migrate | Single-session toast; deprecation must be persistent |
| Low-adoption feature promotion | Contextual tooltip or empty state | Feature exists but uptake is low; surface at the moment it would help | Modal — promotion is lower priority; never interrupt primary flow |
| Security or compliance notice | Modal (mandatory acknowledgement) | Privacy policy updates, security alerts, terms changes | Dismissible banner — mandatory acknowledgement required |

---

## Copy Length Standards

| Format | Headline | Body | CTA |
|--------|----------|------|-----|
| Banner | ≤ 8 words | ≤ 25 words | ≤ 4 words |
| Modal | ≤ 10 words | ≤ 80 words | ≤ 6 words |
| Toast | ≤ 8 words | ≤ 20 words | ≤ 4 words (optional) |
| Tooltip coach mark | ≤ 10 words | ≤ 40 words | ≤ 4 words |
| Empty state | ≤ 8 words (headline) | ≤ 35 words | ≤ 4 words |

---

## Tone Calibration by Announcement Type

| Announcement Type | Tone | Tone Signals | Avoid |
|------------------|------|-------------|-------|
| New feature | Celebratory, warm | "Introducing", "Now available", first-person active voice | Hyperbole ("game-changing", "revolutionary") |
| Feature update | Informational, neutral | "We've updated", "You can now", factual | Over-celebrating minor tweaks |
| Breaking change | Clear, direct, empathetic | "This changes how X works", lead with impact, not blame | Passive voice that obscures responsibility |
| Deprecation | Empathetic, helpful | "X is going away on [date]", immediate next step offered | Abrupt "X is being removed" with no support path |
| Maintenance | Factual, reassuring | Specific time window, explicit scope, recovery expectation | Vague "brief maintenance" without time bounds |
| Security / compliance | Authoritative, unambiguous | Exact change stated, effective date, user action required | Legalese in body copy; link to full policy is sufficient |
| Low-adoption promo | Helpful, contextual | "Did you know you can…", problem-first framing | Aggressive marketing tone at point of friction |

---

## CTA Specificity Signal Table

Replace generic CTAs with goal-specific labels:

| Generic CTA | Specific Alternative | When to Use |
|-------------|---------------------|-------------|
| Learn more | See what's new | New feature announcement |
| Learn more | Read the migration guide | Breaking change / deprecation |
| Get started | Set up your workspace | First-run feature |
| Try it now | Open [Feature Name] | Direct feature access |
| Dismiss | Got it | Informational only; no further action |
| OK | Acknowledge | Mandatory security / compliance acknowledgement |
| Close | Maybe later | Optional feature promotion the user may want to revisit |

---

## Announcement Fatigue Guardrails

Limits to enforce before any new in-app announcement ships:

| Constraint | Limit |
|------------|-------|
| Maximum active banners at any time | 1 (system-level) |
| Maximum in-session modals | 1 per session (first login after release only) |
| Minimum days between modals for the same user | 14 days |
| Maximum coach mark tooltips in a single flow | 2 per page |
| Deprecation minimum notice period | 30 days before removal |
| Breaking change minimum notice period | 14 days before effective date |

---

## Dismissal Behaviour Reference

Every announcement must define a dismissal path at brief time:

| Dismissal Type | Use When | Behaviour |
|----------------|---------|-----------|
| Session dismiss | Informational updates; user may want to see again | Reappears next session until explicitly dismissed |
| Permanent dismiss | Promotions; user opted out | Never shows again for that user |
| Mandatory acknowledgement | Security / compliance | Cannot be bypassed; logged server-side |
| Auto-expire | Scheduled maintenance | Disappears after the maintenance window ends |
| Snooze | Deprecation / migration CTAs | Reappears in 7 days if user has not completed the required action |
