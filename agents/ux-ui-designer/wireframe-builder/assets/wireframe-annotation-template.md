# Wireframe Annotation Document

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [UX/UI Designer] |
| Feature | [Feature name] |
| Version | [1.0] |
| Figma Link | [URL to wireframe file] |
| Status | [Draft / In Review / Approved] |

## Screen Index

[List all screens included in this wireframe set. Link to Figma frames where possible.]

| # | Screen Name | Flow Stage | Figma Frame | Notes |
|---|------------|-----------|-------------|-------|
| 1 | [e.g. Onboarding — Step 1: Email entry] | [Entry] | [Frame link] | |
| 2 | [e.g. Onboarding — Step 2: Profile setup] | [Core flow] | [Frame link] | |
| 3 | [e.g. Onboarding — Step 3: Confirm email] | [Core flow] | [Frame link] | |
| 4 | [e.g. Onboarding — Empty state (no profile photo)] | [Edge case] | [Frame link] | |
| 5 | [e.g. Onboarding — Error state (email taken)] | [Error] | [Frame link] | |

## Interaction Annotations

[Document all interaction annotations by screen. One row per annotated element.]

### Screen 1: [Screen Name]

| ID | Element | Annotation | Type |
|----|---------|------------|------|
| 1.1 | [e.g. "Continue" CTA button] | [→ Navigates to Screen 2 if email is valid; triggers inline validation error if field is empty] | Interaction |
| 1.2 | [e.g. Email input field] | [CONTENT: Max 320 chars. Validates on blur. Error inline below field: "Enter a valid email address."] | Content + Conditional |
| 1.3 | [e.g. "Sign in instead" link] | [→ Routes to Sign In screen. Does not save partial onboarding state.] | Interaction |
| 1.4 | [e.g. Progress indicator] | [Shows step 1 of 3. Updates on navigation to each step.] | Behaviour |

### Screen 2: [Screen Name]

| ID | Element | Annotation | Type |
|----|---------|------------|------|
| 2.1 | [Element] | [Annotation] | [Type] |
| 2.2 | [Element] | [Annotation] | [Type] |

## States Covered

[Confirm which states are wireframed for each key screen.]

| Screen | Default | Empty | Loading | Error | Success |
|--------|---------|-------|---------|-------|---------|
| [Screen 1] | [✓] | [✓] | [✓] | [✓] | [–] |
| [Screen 2] | [✓] | [–] | [✓] | [✓] | [✓] |
| [Screen 3] | [✓] | [–] | [–] | [✓] | [✓] |

**States key**: ✓ = wireframed | – = not applicable | ✗ = missing (flag as gap)

## Open Questions

[List unresolved design decisions that need stakeholder input before wireframes can be finalised.]

| # | Question | Context | Owner | Due |
|---|----------|---------|-------|-----|
| Q1 | [e.g. Should the profile photo upload be mandatory or skippable?] | [Affects empty state and progress logic] | [PM name] | [Date] |
| Q2 | [e.g. Do we show the email confirmation step or use magic link?] | [Affects flow length and Screen 3 design] | [Engineering + PM] | [Date] |

## Component Notes

[Document design system components used or gaps identified.]

| Element | DS Component | Status | Notes |
|---------|-------------|--------|-------|
| [e.g. CTA button — primary] | [Button / Primary] | [Existing] | [Use current DS component as-is] |
| [e.g. Stepper / progress indicator] | [None] | [New component needed] | [Brief visual-interaction-designer on requirements] |
| [e.g. Inline validation error text] | [Form / Error text] | [Existing] | [Confirm DS error text token applies here] |

## Reviewer Notes

[Space for review feedback captured during the wireframe review session.]

| Reviewer | Comment | Screen | Resolution |
|----------|---------|--------|------------|
| [Name] | [Feedback] | [Screen #] | [Designer response / action] |
