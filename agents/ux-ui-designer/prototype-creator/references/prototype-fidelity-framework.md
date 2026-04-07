# Prototype Fidelity Framework

A guide for selecting the right prototype fidelity level, scoping interactive paths, and preparing prototypes for testing or stakeholder review.

---

## Core Methodology

Prototype fidelity must match the testing objective. Higher fidelity is not better — it is more expensive and anchors participants on polish rather than flow logic when used prematurely.

**Rule:** Use the minimum fidelity that reliably answers the question the prototype was built to answer.

---

## Fidelity Levels

### Low-Fidelity (Grey-Box / Wireframe Prototype)

**What it includes:**
- Monochrome or greyscale layouts
- Placeholder text and image blocks
- Basic navigation links between screens
- No animation or micro-interaction

**Best for:**
- Testing flow logic and information architecture
- Concept validation (does this approach solve the right problem?)
- Early stakeholder alignment on structure
- Design sprints and rapid iteration

**Participant instruction:** "Imagine you're using a rough draft of the app. We're testing the steps, not the visuals."

---

### Mid-Fidelity (Styled Components, Clickable)

**What it includes:**
- Styled components from design system
- Real or realistic content (not placeholder)
- Interactive navigation and key interactions
- Primary states (default, active, error)

**Best for:**
- Usability testing of specific flows
- Stakeholder review of interaction patterns
- Testing content legibility and hierarchy
- Cross-functional review sessions

---

### High-Fidelity (Production-Ready, Interactive)

**What it includes:**
- Full visual design with tokens and typography
- All states designed (hover, focus, error, loading, empty)
- Realistic content and imagery
- Smooth transitions and micro-interactions (Smart Animate)

**Best for:**
- Pre-handoff engineering reference
- Final stakeholder sign-off
- Benchmark usability testing
- Marketing demos and investor presentations

---

## Prototype Scope Planning

Before building, define:

| Path | Required in Prototype? | Fidelity Needed |
|------|----------------------|----------------|
| Primary happy path | Yes | Full interactivity |
| Primary error state | Yes (for usability tests) | Interactive |
| Alternative paths | If they are part of the test scenario | Interactive |
| Secondary features | No (unless testing them) | Static frame |
| Edge cases | No (unless testing them) | Static frame |

**Over-scoping prototypes wastes build time and introduces noise.** If a participant can click outside the test path, they will — and the data becomes harder to analyse.

---

## Figma Prototype Tooling Reference

| Feature | Use Case |
|---------|---------|
| Smart Animate | Smooth transitions between frames that share common layers |
| Overlays | Modals, tooltips, bottom sheets, dropdown menus |
| Component interactions | Button hover/press states, toggle on/off |
| Variables (string, number, boolean) | Conditional flows (e.g., logged-in vs. guest states) |
| Prototype flow start points | Define multiple entry points for different test scenarios |
| Scroll behaviour | Scrollable frames, fixed elements during scroll |

---

## Internal QA Checklist (Before Sharing)

Run this before sending a prototype link to a research participant or stakeholder:

- [ ] All interactive paths in scope walk through without dead ends
- [ ] Back navigation works where expected
- [ ] Hotspots do not extend beyond their intended elements
- [ ] Realistic content in place (no lorem ipsum, no placeholder images if hi-fi)
- [ ] Prototype starts from the correct entry point
- [ ] Sharing permissions set correctly (can view / can comment)
- [ ] Usage guide written noting entry points, supported flows, and known limitations
- [ ] Performance check: prototype does not lag or crash on target devices

---

## Prototype Usage Guide Template

Include with every shared prototype link:

```
Prototype: [Feature Name]
Version: [v1.0 / v1.2 / etc.]
Date: [YYYY-MM-DD]
Fidelity: [Lo / Mid / Hi]
Built by: [Designer name]

Entry point: [How to start — e.g., "Tap the blue button on the first screen"]

Supported flows:
1. [Primary flow — brief description]
2. [Secondary flow — brief description]

Known limitations:
- [e.g., "Settings screen is not interactive"]
- [e.g., "Keyboard does not appear — tap the input and proceed"]

Contact: [Designer name + slack handle]
```
