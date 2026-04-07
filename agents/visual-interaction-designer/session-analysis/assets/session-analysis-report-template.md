# Session Analysis Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Visual Interaction Designer] |
| Feature / Surface | [Feature or product surface analysed] |
| Sessions Reviewed | [X sessions] |
| Session Source | [e.g. FullStory / PostHog / Hotjar / UserTesting recordings] |
| Date Range of Sessions | [From YYYY-MM-DD to YYYY-MM-DD] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |

## Executive Summary

[2-3 sentences: total sessions reviewed, number of issues found by severity, top finding, and recommended immediate action. GUIDANCE: e.g. "15 sessions reviewed covering the onboarding flow. 2 critical and 4 major issues identified. The most impactful finding is that 11/15 users miss the profile photo upload step due to visual hierarchy failure on Step 3. Recommend repositioning the upload prompt above the fold before the next release."]

## Analysis Scope

| Flow Analysed | Entry Point | Exit Point | Sessions | Notes |
|--------------|------------|-----------|---------|-------|
| [e.g. Onboarding: Steps 1-4] | [Sign up confirmation email] | [Dashboard first load] | [15] | |
| [e.g. Checkout: Cart to confirmation] | [Tap "Checkout" in cart] | [Order confirmation] | [10] | |

## Session Sample

| Session ID | User Segment | Platform | Completed Flow? | Notable Behaviour |
|-----------|-------------|---------|----------------|------------------|
| SES-001 | [New user] | [iOS] | [Yes] | [Smooth — no friction] |
| SES-002 | [New user] | [Web] | [No — abandoned at Step 3] | [Exited after 45s on profile setup] |
| SES-003 | [Returning user] | [Android] | [Yes] | [Rage-tapped payment button 3 times during loading] |

## Findings: Critical Issues

[Issues that prevent task completion or cause session abandonment.]

### [CRIT-01] [Issue Title]

**Screens affected**: [Screen name(s)]
**Sessions observed**: [X / Y total sessions]
**Friction type**: [From taxonomy]
**Observation**: [Factual description of what users did]
**Hypothesised cause**: [Design element causing the behaviour]
**Recommendation**: [Specific design fix]
**Effort estimate**: [Days]

---

### [CRIT-02] [Issue Title]

[Same structure]

---

## Findings: Major Issues

### [MAJ-01] [Issue Title]

**Screens affected**: [Screen name(s)]
**Sessions observed**: [X / Y total sessions]
**Friction type**: [Type]
**Observation**: [What users did]
**Hypothesised cause**: [Design element]
**Recommendation**: [Fix]
**Effort estimate**: [Days]

---

## Findings: Minor Issues

| ID | Issue | Screen | Sessions | Friction Type | Recommendation | Effort |
|----|-------|--------|---------|--------------|---------------|--------|
| MIN-01 | [e.g. Users pause 3s on "Skip for now" — label ambiguous] | [Profile setup] | [4/15] | Label ambiguity | [Rename to "Set up later" to signal reversibility] | [0.5d] |
| MIN-02 | [Issue] | [Screen] | [X/Y] | [Type] | [Recommendation] | [Effort] |

## Observations (No Friction)

[Behaviours worth noting for future reference but with no current action.]

| Observation | Screen | Sessions | Notes |
|------------|--------|---------|-------|
| [e.g. 12/15 users tapped the logo to return to home — not labelled] | [Any screen] | [12/15] | [May indicate desire for home shortcut — consider adding breadcrumb] |

## Pattern Summary

| Pattern | Sessions | Severity | Friction Type | Status |
|---------|---------|---------|--------------|--------|
| [e.g. Navigation confusion at checkout entry: 2 CTAs of equal weight] | [8/15] | Major | Navigation confusion | Recommended fix: CRIT-01 |

## Recommended Design Actions

[Prioritised list of design actions, ordered by impact.]

| Priority | Action | Addresses | Effort | Owner | Sprint |
|----------|--------|-----------|--------|-------|--------|
| P0 | [e.g. Redesign checkout CTA hierarchy — make "Checkout" primary] | [CRIT-01] | [1d] | [Designer name] | [Sprint X] |
| P1 | [e.g. Increase loading indicator prominence on order placement] | [MAJ-01] | [0.5d] | [Designer name] | [Sprint X] |
| P2 | [e.g. Rename "Skip for now" → "Set up later"] | [MIN-01] | [0.5d] | [Content Designer] | [Sprint X+1] |

## Appendix: Raw Observation Log

| Session | Timestamp | Screen | Behaviour | Friction Type | Severity |
|---------|-----------|--------|-----------|--------------|---------|
| SES-001 | 01:23 | [Screen] | [Behaviour] | [Type] | [Severity] |
| SES-002 | 02:45 | [Screen] | [Behaviour] | [Type] | [Severity] |
