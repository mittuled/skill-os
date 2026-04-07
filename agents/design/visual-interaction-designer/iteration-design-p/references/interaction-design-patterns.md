# Interaction Design Patterns Reference

## Purpose

Reference patterns for designing iterations on shipped features, grounded in post-launch data. Covers interaction design principles, motion standards, and iteration decision frameworks.

## Iteration Trigger Decision Table

Determine the right response to each type of post-launch signal:

| Signal Type | Source | Design Response | Urgency |
|-------------|--------|----------------|---------|
| Task completion rate drops >10% | Product analytics | Redesign the affected interaction path | High |
| Rage-tap frequency exceeds 5% of sessions | Session recordings | Audit loading states and interaction feedback | High |
| Error rate on form >15% | Analytics + session data | Review form validation UX and field labelling | High |
| Time-on-task increases by >20% | Usability metrics | Review navigation clarity and CTA hierarchy | Medium |
| Scroll depth plateaus before key CTA | Heatmaps | Investigate visual hierarchy and above-fold content | Medium |
| Qualitative feedback flags specific friction | User interviews | Validate with session data before redesigning | Medium |
| Minor aesthetic inconsistency noted | Design review | Queue for design debt sprint, not urgent | Low |

## Interaction Design Principles for Iterations

### 1. Preserve Mental Models

Users have built expectations from prior usage. Iterations should improve, not rewrite:

| Principle | Application |
|-----------|-------------|
| Keep primary actions in the same location | Move CTA position only when analytics shows it is being missed |
| Retain gesture conventions | If users swipe to dismiss, do not change to tap-to-dismiss without strong evidence |
| Maintain label consistency | Changing "Save" to "Confirm" across an app resets learned vocabulary |

### 2. Minimum Effective Change

Make the smallest interaction change that addresses the identified problem:

- Do not redesign the full screen when only the CTA label needs updating
- Do not add an animation when a layout fix solves the friction
- A/B test major interaction changes before full rollout when possible

### 3. Motion and Animation Standards

| Motion Type | When to Use | Duration | Easing |
|-------------|------------|---------|--------|
| Screen transition (push) | Navigation between pages | 300ms | ease-in-out |
| Modal appear | Overlay presentation | 250ms | ease-out |
| Toast / snackbar | Feedback confirmation | 200ms in / auto 2s / 200ms out | ease-out / ease-in |
| Loading skeleton | Content placeholder | Loop, 1.5s cycle | linear |
| Micro-interaction (button press) | Tactile feedback | 100ms | ease-out |
| Error shake | Invalid input alert | 300ms | ease-in-out |

**Reduced motion rule**: All animations must be disabled or minimised when `prefers-reduced-motion` media query is active. Non-negotiable.

### 4. Feedback Loop Design

Every user action requires a system response. Map the feedback loop:

| Action | Feedback Level | Response |
|--------|---------------|---------|
| Tap / click primary CTA | Immediate | Visual state change on button (loading state) within 100ms |
| Form submission | Process feedback | Loading state for >300ms wait; progress indicator for >1s wait |
| Successful completion | Confirmation | Success state visible for minimum 1.5s before auto-advancing |
| Error / validation fail | Inline error | Error appears next to the failing field, not at top of form |
| Destructive action | Confirmation gate | Require explicit confirm step — do not undo-only patterns for high-risk actions |

## Iteration Fidelity Decision Matrix

| Change Complexity | Stakeholder Alignment Needed | Recommended Fidelity |
|------------------|------------------------------|---------------------|
| Label / copy change only | None — unilateral designer decision | Ship via content update; no design mockup needed |
| Single-element visual tweak | Designer + PM | Updated Figma frame + annotated change note |
| CTA hierarchy or layout adjustment | Designer + PM + Engineering feasibility | Revised hi-fi screen + interaction annotation |
| New interaction pattern (new gesture, new state) | Designer + Head of Design + Engineering | Full screen redesign + prototype for validation |
| Structural flow change | Cross-functional review | Updated user flow + full wireframe + usability test |

## Anti-Patterns in Production Iteration

| Anti-Pattern | Why It Fails | Correct Approach |
|-------------|-------------|-----------------|
| Redesigning based on one session recording | Single sessions are noise, not signal | Establish pattern across 5+ sessions before acting |
| Changing multiple elements simultaneously | Cannot isolate which change fixed the problem | Change one element at a time; wait for data before next change |
| Skipping empty and loading states on iterations | New interactions often expose missing states | Always check all five states when redesigning an interaction |
| Iterating in a vacuum without analytics review | Risk of fixing symptom, not cause | Always start with data before touching Figma |
| Applying desktop interaction patterns to mobile | Hover states, tooltips, and dense menus fail on touch | Validate each pattern against the target input method |
