---
name: ux-copy-writer
description: >
  This skill writes UX copy including microcopy, labels, error messages, and empty states.
  Use when asked to write product copy, create microcopy, or draft UI text for a feature.
  Also consider when designs contain placeholder text that needs to be replaced with
  production copy. Suggest when the user is about to hand off designs with lorem ipsum
  or developer-written placeholder strings.
department: design
agent: content-design-lead
version: 1.0.0
complexity: medium
related-skills: []
---

# ux-copy-writer

## Agent: Content Design Lead

L2 content design lead (1x) (moved from Product, now reports to Head of Design) responsible for microcopy, voice standards, UX copy, and help content architecture.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Writes UX copy including microcopy, labels, error messages, empty states, and onboarding text that guides users through the product experience in the established voice and tone.

## When to Use

- When a new feature or flow needs production-ready UX copy before design handoff to engineering.
- When existing product copy needs rewriting to align with an updated content design spec or brand voice.
- When usability testing or user feedback has identified specific copy that confuses users and needs to be revised.

## Workflow

1. **Context Gathering**: Review the design mockups, user flow diagrams, user stories, and any relevant research insights for the feature. Understand the user's goal, emotional state, and context at each copy touchpoint. Deliverable: copy context brief.
2. **Copy Inventory**: List every copy string needed for the feature: headings, body text, button labels, form labels, placeholder text, validation messages, error messages, success confirmations, empty states, tooltips, and notifications. Deliverable: copy string inventory.
3. **Draft Writing**: Write copy for each string following the content design spec: voice and tone appropriate to context (celebratory for success, empathetic for errors, instructive for onboarding), correct terminology from the glossary, and pattern library conventions. Deliverable: draft copy deck.
4. **Constraint Validation**: Verify that copy fits within UI space constraints (character limits for buttons, line limits for modals). Check that error messages are specific and actionable (state what went wrong and how to fix it). Deliverable: constraint-validated copy deck.
5. **Design & Engineering Review**: Review copy in context with the designer (in Figma or equivalent) and with engineering for any string-handling concerns (pluralisation, variable interpolation, truncation). Deliverable: approved copy deck ready for implementation.

## Anti-Patterns

- **Generic error messages**: Writing vague error copy like "Something went wrong" without specifying what failed or what the user should do. *Why*: generic errors leave users stuck; actionable error messages ("Your file exceeds 10MB. Try a smaller file.") resolve issues without support contact.
- **Copy in isolation**: Writing copy without seeing the design context or understanding where in the flow it appears. *Why*: copy that reads well in a spreadsheet may not work within the UI's spatial constraints or emotional context.
- **Clever over clear**: Prioritising wit or brand personality over user clarity, especially in instructional or error contexts. *Why*: users in task mode need to understand instantly; cleverness that requires interpretation adds friction.
- **Ignoring empty states**: Treating empty states as edge cases that can use default "No items" text. *Why*: empty states are often the first thing new users see; they are a critical onboarding moment that should guide the user toward their first action.
- **Skipping pluralisation review**: Writing copy without considering singular/plural variations and variable-length content. *Why*: "You have 1 items" or truncated strings degrade perceived quality and confuse users.

## Output

**On success**: Produces a copy deck containing all UX copy strings for the feature, organised by screen and element, with annotations for context, tone rationale, and any implementation notes (pluralisation rules, character limits). Delivered as a shared document or directly annotated in the design file.

**On failure**: Report which copy strings could not be finalised (e.g., undefined user flow branches, missing error state specifications), what placeholder copy was provided, and recommend the design or product decisions needed to complete the copy.

## Related Skills

- [`content-design-spec`](../content-design-spec/SKILL.md) — All UX copy must conform to the standards in the content design spec.
- [`copy-implementation-reviewer`](../copy-implementation-reviewer/SKILL.md) — Reviews whether the approved copy was implemented correctly.
- [`help-content-creator`](../../../design/content-designer-ux-writer/help-content-creator/SKILL.md) — Help content may need to reference or expand on UX copy for feature documentation.
