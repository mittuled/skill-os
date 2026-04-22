---
name: spec-translator-design
description: >
  This skill translates product specifications into design briefs and acceptance criteria for
  the design team. Use when asked to convert a PRD into design requirements, create a design
  brief from a product spec, or define design acceptance criteria for a feature. Also consider
  when a product spec lacks design-specific detail. Suggest when a designer is about to start
  work from a raw product spec without a design brief.
department: design
agent: head-of-design
version: 1.0.0
complexity: medium
related-skills:
  - effort-estimator-design
  - backlog-populator-design
  - flow-designer
triggers:
  - "translate design spec"
  - "design spec translation"
  - "interpret design spec"
  - "spec to design"
  - "read design spec"
---

# spec-translator-design

## Agent: Head of Design

L1 design leader (1x) responsible for design strategy, review governance, and accessibility oversight. Oversees UX Research and Content Design as sub-disciplines reporting into Design.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)

## Skill Description

Translates product specifications into design briefs and acceptance criteria that give designers the context, constraints, and success measures needed to begin work.

## When to Use

- When a product requirements document (PRD) or feature spec has been approved and design work needs to be scoped and briefed.
- When a product specification lacks design-specific detail (interaction requirements, responsive behavior, accessibility targets, content needs).
- When multiple designers will work on the same feature and need a shared brief to ensure consistency.
- When a designer flags that a spec is ambiguous or missing information required to begin design work.

## Workflow

1. **Analyze the product spec**: Read the PRD or feature spec end to end. Identify user stories, functional requirements, success metrics, and technical constraints relevant to design. Use the translation mapping in the [translation framework](references/translation-framework.md) to convert spec elements into brief elements. Deliverable: annotated spec with design-relevant callouts.
2. **Identify design gaps**: Flag areas where the spec is silent on interaction behavior, edge cases, responsive breakpoints, empty/error/loading states, accessibility requirements, or content needs. Use the gap category checklist in the [translation framework](references/translation-framework.md). Deliverable: gap list with questions for product.
3. **Resolve gaps**: Collaborate with the product manager to close open questions. Document decisions and assumptions. Deliverable: resolved gap register.
4. **Draft the design brief**: Write a design brief using the [design brief template](assets/design-brief-template.md) covering: problem statement, target users, in-scope surfaces, design constraints, interaction requirements, state requirements, accessibility targets, and content requirements. Deliverable: design brief document.
5. **Define acceptance criteria**: Specify measurable conditions in Given/When/Then format per the [translation framework](references/translation-framework.md). Verify all states, breakpoints, accessibility checks, and design system compliance are covered. Deliverable: acceptance criteria checklist appended to the brief.
6. **Distribute and align**: Share the brief with the assigned designer(s) and walk through it. Confirm understanding and surface any remaining ambiguities. Deliverable: acknowledged brief with designer confirmation.

## Anti-Patterns

- **Passthrough without translation**: Forwarding the product spec to designers without adding design-specific context, constraints, or acceptance criteria. *Why*: designers are forced to guess at interaction requirements and edge cases, leading to rework when assumptions prove wrong.
- **Over-specifying the solution**: Dictating specific layouts, components, or visual treatments in the brief instead of defining the problem and constraints. *Why*: prescriptive briefs undermine the designer's ability to explore solutions and often produce worse outcomes than problem-framed briefs.
- **Omitting content requirements**: Writing the design brief without addressing microcopy, error messages, empty states, and onboarding text. *Why*: content is a design material; designs built with placeholder copy ship with placeholder-quality language.

## Output

**On success**: Produces a design brief containing problem statement, design constraints, interaction requirements, accessibility targets, content requirements, and acceptance criteria. Delivered to the assigned designer(s) with a walkthrough session.

**On failure**: Report which parts of the spec could not be translated (ambiguous requirements, missing user stories, undefined edge cases), what questions remain unresolved, and the product owner responsible for closing gaps.

## Related Skills

- [`effort-estimator-design`](../effort-estimator-design/SKILL.md) -- Design briefs are the primary input for accurate effort estimation.
- [`backlog-populator-design`](../../../design/ux-ui-designer/backlog-populator-design/SKILL.md) -- Translated briefs feed the design backlog as actionable tasks.
- [`flow-designer`](../../../design/ux-ui-designer/flow-designer/SKILL.md) -- Interaction requirements in the brief scope the flow design work.
