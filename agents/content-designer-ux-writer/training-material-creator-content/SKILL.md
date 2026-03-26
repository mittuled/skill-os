---
name: training-material-creator-content
description: >
  This skill creates training materials for internal teams on new product features and
  processes. Use when asked to create training docs, build onboarding materials, or write
  internal product guides. Also consider when a new hire onboarding process lacks product
  training content. Suggest when the user is about to onboard new team members without
  structured training materials.
department: design
agent: content-designer-ux-writer
version: 1.0.0
complexity: medium
related-skills: []
---

# training-material-creator-content

## Agent: Content Designer UX Writer

L3 content designer and UX writer (Nx) responsible for support readiness, help content creation, in-app announcements, and training materials.

Department ethos: [ideal-design.md](../../../departments/design/ideal-design.md)

## Skill Description

Creates training materials for internal teams on new product features and processes, enabling support, sales, and customer success teams to use and explain the product confidently.

## When to Use

- When a major feature launch requires internal teams (support, sales, customer success) to understand the product deeply enough to demo, sell, or troubleshoot it.
- When new hire onboarding reveals that product knowledge is transferred informally and no structured training materials exist.
- When a process change (new workflow, tool migration, policy update) affects internal teams and needs documented training.

## Workflow

1. **Training Needs Assessment**: Identify the target audience (support, sales, CS, new hires), their current knowledge level, and the specific knowledge or skills the training must impart. Deliverable: training needs brief.
2. **Content Outline**: Structure the training material into modules with clear learning objectives per module. Sequence from foundational concepts to advanced workflows. Deliverable: training outline with learning objectives.
3. **Material Creation**: Write the training content using the appropriate format: written guide for reference material, annotated walkthrough for procedural training, or quiz/exercise for knowledge verification. Include screenshots, screen recordings, or interactive demos as appropriate. Deliverable: draft training materials.
4. **Subject Matter Review**: Review materials with the product team or subject matter experts for accuracy. Deliverable: accuracy-reviewed materials.
5. **Pilot & Feedback**: Run the training with a small group from the target audience, collect feedback on clarity, completeness, and usefulness. Revise based on feedback. Deliverable: finalised training materials.

## Anti-Patterns

- **Feature tour instead of task training**: Organising training by feature list rather than by the tasks the audience needs to perform. *Why*: internal teams need to know how to accomplish goals (demo a workflow, resolve a ticket), not memorise feature inventories.
- **No knowledge verification**: Delivering training without any mechanism to verify comprehension (quiz, exercise, role-play). *Why*: without verification, training completion does not guarantee capability; teams may still lack the knowledge to perform.
- **One format for all audiences**: Creating a single training document for support, sales, and new hires despite their different contexts and knowledge levels. *Why*: a sales team needs competitive positioning and demo scripts; support needs troubleshooting steps; the same material cannot serve both well.
- **Static-only materials**: Creating only written documents when the content would benefit from video walkthroughs or interactive exercises. *Why*: procedural training is absorbed better through visual demonstration; written steps alone miss interaction nuances.

## Output

**On success**: Produces training materials including guides, walkthroughs, and knowledge verification exercises tailored to the target audience. Delivered as shared documents, videos, or interactive modules accessible to the relevant teams.

**On failure**: Report which training modules could not be completed (e.g., feature not yet stable for screenshots, unclear process details), what partial materials were produced, and recommend a timeline for completing the remaining content.

## Related Skills

- [`support-readiness-briefer`](../support-readiness-briefer/SKILL.md) — Readiness briefs cover immediate release knowledge; training materials cover deeper product competency.
- [`help-content-creator`](../help-content-creator/SKILL.md) — External help content can serve as a foundation for internal training materials.
- [`content-design-spec`](../../content-design-lead/content-design-spec/SKILL.md) — Training materials should follow the content design spec for consistency with product terminology.
