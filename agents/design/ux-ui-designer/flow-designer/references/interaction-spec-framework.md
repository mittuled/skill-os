# Interaction Specification Framework

A guide for documenting detailed interaction flows, decision points, and micro-interaction specifications.

---

## Core Methodology

An interaction flow specifies three layers for every step:
1. **Trigger** — What causes the transition (user action or system event)
2. **Response** — What the UI does in response
3. **Feedback** — How the user knows it worked

All three layers must be documented before handing off to engineering.

---

## Flow Notation Standards

### Node Types

| Symbol | Meaning |
|--------|---------|
| Rectangle | Screen or view |
| Diamond | Decision point (conditional branch) |
| Rounded rectangle | Micro-interaction or component state change |
| Parallelogram | System process (background action, API call) |
| Oval | Entry point or exit point |
| Bold border | [GATE] — explicit approval required before proceeding |

### Annotation Conventions

- **Solid arrow** — Primary path (happy path)
- **Dashed arrow** — Error or alternative path
- **Dotted arrow** — System-initiated (no user action required)
- **Red highlight** — Blocking error state
- **Yellow highlight** — Warning or recoverable state

---

## Interaction Specification Table

Document each step in the flow with this format:

| Step | Screen | Trigger | Element | Response | Feedback | Timing | Error Path |
|------|--------|---------|---------|----------|---------|--------|-----------|
| 1 | Home | Tap | "Add item" CTA | Open add-item bottom sheet | Sheet slides up; scrim fades in | 300ms ease-out | — |
| 2 | Add item sheet | System | Form mounted | Focus first input | Keyboard appears; cursor in field | Immediate | — |
| 3 | Add item sheet | Tap | "Save" button | Validate form | Loading spinner in button | — | Inline error on invalid fields |

---

## State Transition Map

For each screen, document the complete state machine:

```
State: [Screen Name]

Entry conditions:
  - [What triggers arrival at this screen]

Active states:
  - Default
  - Loading (triggered by: [action])
  - Error (triggered by: [condition], recovery: [action])
  - Empty (triggered by: [condition], CTA: [action])
  - Success (triggered by: [condition], exit: [next screen])

Exit conditions:
  - [User action] → [Next screen]
  - [System event] → [Next screen]
  - [Back navigation] → [Previous screen]
```

---

## Nielsen's Heuristics Checklist

Apply to every flow before finalising:

| Heuristic | Question to Answer |
|-----------|-------------------|
| 1. Visibility of system status | Does the user always know what the system is doing? (loading states, progress indicators) |
| 2. Match between system and real world | Does the language and sequence match the user's mental model? |
| 3. User control and freedom | Can the user undo or escape from any state? |
| 4. Consistency and standards | Does this flow use the same patterns as other flows in the product? |
| 5. Error prevention | Are there validation or confirmation steps that prevent irreversible errors? |
| 6. Recognition over recall | Does the user ever have to remember something from a previous screen? |
| 7. Flexibility and efficiency | Can power users shortcut steps? |
| 8. Aesthetic and minimalist design | Does each step show only the information the user needs right now? |
| 9. Help users recognise errors | Are error messages specific and actionable? |
| 10. Help and documentation | Is inline guidance available at steps where users are likely to struggle? |

---

## Error Path Documentation Template

For every significant error or alternative path:

```
Error Path: [Name]

Trigger: [What causes this path]
User state: [What the user was trying to do]

System response:
  - [What the UI shows]
  - [Error message text or reference to content brief]

Recovery options available:
  1. [Action the user can take] → [Outcome]
  2. [Alternative action] → [Outcome]

Fallback if all recovery fails:
  - [Contact support / clear data / escalate]
```

---

## Micro-Interaction Specification Format

For each micro-interaction (button tap, toggle, swipe):

```
Interaction: [Name]
Trigger: [tap / swipe / hover / keyboard]
Element: [Component name]
States: idle → [trigger] → active → [response] → resolved
Duration: [ms]
Easing: [linear / ease-in / ease-out / ease-in-out / spring]
Haptic (mobile): [none / light / medium / heavy / selection]
```
