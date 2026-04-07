# Spec Translation Framework

A guide for converting product requirements documents (PRDs) into design-ready briefs.

---

## Core Methodology

Product specs are written from a **feature** perspective (what the system does). Design briefs are written from a **user** perspective (what the user accomplishes). Spec translation bridges this gap by extracting user intent, adding design-specific requirements, and specifying success conditions in observable terms.

---

## Translation Mapping

| PRD Element | Design Brief Element | Translation Notes |
|-------------|---------------------|------------------|
| Feature description | Problem statement | Reframe from system behaviour to user need |
| User stories | User goals + entry conditions | Expand to include entry context and emotional state |
| Acceptance criteria | Design acceptance criteria | Add: all states, breakpoints, accessibility, content |
| Non-functional requirements | Design constraints | Surface performance-relevant UI constraints (skeleton states, lazy loading) |
| Out of scope | Explicit exclusions | Call out explicitly to prevent scope creep |
| Success metrics | Design success indicators | Map metrics to observable UI behaviours |

---

## Design Gap Categories

When reading a product spec, systematically check for gaps in these categories:

### Interaction Requirements
- [ ] What happens on tap/click/keyboard activation for every interactive element?
- [ ] What is the transition between states (loading → loaded, error → retry)?
- [ ] Are there conditional behaviours based on user state (logged in vs. guest, free vs. paid)?

### State Completeness
- [ ] **Empty state**: What does the user see when there is no data?
- [ ] **Loading state**: What shows while content is fetching?
- [ ] **Error state**: What shows when the operation fails, and what can the user do?
- [ ] **Success state**: What confirms the user's action succeeded?
- [ ] **Disabled state**: Under what conditions is an element non-interactive?
- [ ] **Partial data state**: What shows when only some data is available?

### Responsive Behaviour
- [ ] Which breakpoints are in scope (mobile, tablet, desktop, large desktop)?
- [ ] Does layout change or just reflow at each breakpoint?
- [ ] Are any elements hidden at certain breakpoints?

### Accessibility Requirements
- [ ] What WCAG level is required (A, AA, AAA)?
- [ ] Are there known assistive technology use cases to support?
- [ ] Do any interactions require keyboard navigation specification?

### Content Requirements
- [ ] What microcopy and labels are needed (headings, button labels, placeholder text)?
- [ ] Are there character limits for any text elements?
- [ ] Are error messages specified, or must content design write them?
- [ ] Is there onboarding or instructional copy needed?

---

## Brief Quality Checklist

Before distributing the design brief, verify each section is complete:

- [ ] **Problem statement** — Describes user need, not feature behaviour
- [ ] **Target users** — Persona or segment with relevant context
- [ ] **In-scope surfaces** — Explicit list of screens and platforms
- [ ] **Out-of-scope** — Explicit list of what is excluded
- [ ] **Design constraints** — Component library, tokens, patterns to reuse
- [ ] **Interaction requirements** — All conditional behaviours documented
- [ ] **State requirements** — All states listed (empty, loading, error, success, disabled)
- [ ] **Responsive requirements** — Breakpoints and layout behaviour
- [ ] **Accessibility targets** — WCAG level and known edge cases
- [ ] **Content requirements** — Copy needs, character limits, tone guidance
- [ ] **Acceptance criteria** — Measurable, state-specific, testable conditions
- [ ] **Open questions resolved** — No unanswered questions that block design start

---

## Acceptance Criteria Template

Acceptance criteria in a design brief should be testable by a reviewer without asking the designer for clarification.

**Format:**
> Given [context / user state], when [user action / system event], then [expected UI behaviour].

**Examples:**
- Given the list is empty, when the user lands on the page, then an empty state with [headline], [body copy], and [primary CTA] is shown.
- Given the form is submitted with an invalid email, when validation fires, then the email field shows an inline error with the message "[error copy]".
- Given the viewport is 375px, when the layout renders, then the navigation collapses into a hamburger menu.
