# Wireframe Principles Reference

## Purpose

Foundational principles for creating effective low-fidelity wireframes that communicate layout, content hierarchy, and interaction intent without visual design distraction.

## Core Principles

### 1. Fidelity Discipline

Lo-fi wireframes use greyscale only — no colour, no real typography, no icons. This forces stakeholders to focus on structure rather than aesthetics.

| Fidelity Level | Purpose | When to Use |
|----------------|---------|-------------|
| Lo-fi (sketches / boxes) | Explore layout options rapidly | Early ideation, concept validation |
| Mid-fi (Figma greyscale) | Communicate structure for review | User flow approval, team alignment |
| Hi-fi annotated | Spec for engineering | Post visual design sign-off |

**Rule**: Never jump to hi-fi until the lo-fi structure has been reviewed and approved.

### 2. Content Hierarchy via Scale and Position

Use scale and placement — not colour — to establish hierarchy:

- Primary content: largest area, top-left in reading flow (F-pattern)
- Secondary content: smaller, below or right of primary
- Supporting content: smallest, tucked to edge or footer zones
- Actions (CTAs): positioned at natural decision points in the flow — not at fixed bottom of screen by default

### 3. Atomic Design Structure (Brad Frost)

Wireframes are built from the inside out:

| Level | Description | Example |
|-------|-------------|---------|
| Atoms | Indivisible UI elements | Button, input field, label |
| Molecules | Simple component groups | Search bar (input + button + icon) |
| Organisms | Complex UI sections | Navigation bar, product card grid |
| Templates | Page-level structure | Dashboard layout, settings page layout |
| Pages | Specific instances with real content | Onboarding step 2 with real copy |

Wireframe at the Template level first; annotate atom-level decisions where interaction is non-obvious.

### 4. The Five States

Every wireframe must account for all five states, not just the success state:

| State | Description | Most Commonly Missed |
|-------|-------------|---------------------|
| Default / Loaded | Content loaded, user hasn't interacted | Often the only state wired |
| Empty | No data, first use, or filtered to zero results | Frequently omitted |
| Loading / Skeleton | Content fetching or processing | Often replaced with spinner only |
| Error | Network failure, invalid input, system error | Commonly deferred to engineering |
| Success / Confirmation | Task completed, feedback given | Sometimes confused with default |

### 5. Gestalt Principles in Layout

Apply Gestalt to direct perception of groupings without decoration:

| Principle | Application | Wireframe Technique |
|-----------|-------------|---------------------|
| Proximity | Group related elements | White space separates groups; tight spacing bonds related items |
| Similarity | Show that items belong to the same category | Consistent box dimensions for list items |
| Continuity | Guide the eye across the layout | Align elements on a grid; column structure |
| Closure | Let users infer complete shapes | Partially visible cards to indicate scrollable content |
| Figure/Ground | Distinguish interactive from static | Boxes with corner radii for tappable elements |

## Annotation Standards

| Annotation Type | Format | When Required |
|----------------|--------|--------------|
| Interaction note | "[→] Click navigates to [screen name]" | Any tap target with non-obvious destination |
| Conditional note | "[IF] user is not logged in → show login prompt" | Any conditional state or branch |
| Content note | "[CONTENT] Max 120 chars; truncates with ellipsis" | Text fields with character constraints |
| Component note | "[DS] Uses existing Card component variant: condensed" | Any element referencing design system |
| Open question | "[?] Should this CTA be sticky or scroll with content?" | Unresolved decisions needing stakeholder input |

## Wireframe Checklist

Before presenting a wireframe for review:

- [ ] All in-scope screens covered
- [ ] Happy path flow connected end-to-end
- [ ] At least three states per key screen (default, empty, error)
- [ ] All tap targets labelled
- [ ] Annotations added to non-obvious interactions
- [ ] Content placeholders use realistic length estimates (not "Lorem ipsum")
- [ ] Navigation and wayfinding elements present
- [ ] Responsive layout indicated if multi-breakpoint feature

## Common Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|-------------|-------------|-----------------|
| Wireframing only the happy path | Edge cases discovered late, costly rework | Always wireframe empty, error, and loading states |
| Adding colour to "help understanding" | Pulls attention to aesthetics, not structure | Use annotations; reserve colour for visual design phase |
| Skipping mobile layout | Mobile constraints surface late | Wireframe mobile first or in parallel |
| Using Lorem ipsum for all copy | Obscures content hierarchy and truncation issues | Use realistic placeholder content at realistic lengths |
| Wireframing in isolation without user flow | Screens become disconnected; navigation logic lost | Produce flow diagram before wireframes |
