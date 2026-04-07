# Session Observation Checklist

## Purpose

A structured checklist for reviewing user session recordings to ensure consistent, thorough observation across all analysts and sessions.

## Pre-Review Setup

- [ ] Session recording tool is loaded and functioning
- [ ] Playback speed set to normal (1×) for first watch; 0.5× for second watch
- [ ] Observation log template open (one log per session)
- [ ] Product flows reference open (to map screen names correctly)
- [ ] Timer or timestamp reference ready

## Session Metadata to Record

Before reviewing, note:

| Field | Value |
|-------|-------|
| Session ID | |
| Recording date | |
| Platform (iOS / Android / Web) | |
| Device type | |
| User segment (if identifiable) | |
| Flow(s) visible in recording | |
| Session length | |
| Did user complete their apparent goal? | Yes / No / Unknown |

## Observation Pass 1: Full-Speed Watch

Goal: Experience the session as the user did. Note:

- [ ] What is the user's apparent goal?
- [ ] Did they achieve it?
- [ ] What was the emotional tone? (frustrated / smooth / confused / exploratory)
- [ ] Any moment that felt unexpected or notable?

## Observation Pass 2: Slow-Speed Analysis

Goal: Identify specific friction moments. Check for:

### Navigation Signals
- [ ] User uses back button unexpectedly (note screen and context)
- [ ] User pogo-sticks between two screens more than once
- [ ] User visits the same screen multiple times (possible confusion about navigation)
- [ ] User taps a non-interactive element (invisible affordance issue)

### Interaction Signals
- [ ] Rage taps — multiple taps on the same element in quick succession (frustration or loading)
- [ ] Long dwell times (5+ seconds with no action — confusion or deliberation)
- [ ] User starts a task and abandons it mid-way (note the exact abandonment point)
- [ ] User corrects an entry (typed, deleted, retyped — form friction)

### Form and Input Signals
- [ ] User deletes and re-enters text more than once in a single field
- [ ] User encounters a validation error (note which field and what message appeared)
- [ ] User uses copy-paste instead of typing (note what they pasted — may reveal expected behaviour)
- [ ] User switches between keyboard and another app (looking something up — missing information)

### CTA and Hierarchy Signals
- [ ] User scrolls past a primary CTA without tapping (visual hierarchy issue)
- [ ] User taps the wrong CTA first, then corrects (label ambiguity or hierarchy confusion)
- [ ] User pauses and scans before selecting an option (decision friction or unclear labels)
- [ ] User does not engage with a secondary action that is relevant to their context

### Loading and Feedback Signals
- [ ] User taps a CTA during loading (system feedback insufficient)
- [ ] User navigates away from a loading screen (wait time too long or uncertainty about outcome)
- [ ] User sees an error state (note the error type and subsequent behaviour)
- [ ] User does not notice a success confirmation (confirmation visibility issue)

### Trust and Commitment Signals
- [ ] User scrolls up and down on a commitment screen before acting (anxiety)
- [ ] User exits at a confirmation or payment screen (trust signal gap)
- [ ] User spends unusually long time on a step requiring personal data entry

## Friction Classification

For each friction moment identified, classify using the standard taxonomy:

| Friction Type | Behavioural Signal |
|--------------|-------------------|
| Navigation confusion | Pogo-sticking, unexpected back taps, wrong destination tapped |
| Label ambiguity | Pause before tapping, wrong selection corrected, repeated reading behaviour |
| Interaction dead end | Idle 5+ seconds, rage taps, session abandonment |
| Form friction | Re-entry, validation errors, copy-paste instead of typing |
| Trust signal gap | Long dwell on commitment screens, exit before confirming |
| Load frustration | Taps during loading, navigation away from loading screen |
| Visual hierarchy failure | Scrolling past CTA, missing key information |

## Post-Watch Summary

After completing both passes, write:

1. **Session summary** (2-3 sentences): What was the user doing, did they succeed, and what was the most significant friction moment?
2. **Top finding from this session** (1 sentence): The single most actionable observation.
3. **Strongest signal type**: [Navigation confusion / Label ambiguity / Form friction / etc.]
4. **Severity**: [Critical / Major / Minor — for the top finding]
5. **Pattern connection**: Does this connect to findings from previous sessions reviewed? (Yes / No / Possible)

## Quality Standards

- Every session reviewed at both speeds — no single-pass reviews
- Every friction moment has a classified friction type and severity
- Observations are factual descriptions of behaviour, not design conclusions
- Design hypotheses are labelled as hypotheses, not observations
- Pattern flags only raised when 3+ sessions show the same signal
