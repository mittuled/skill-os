---
name: documentation-writer
description: >
  This skill writes technical documentation including guides, tutorials, and API references.
  Use when asked to write a developer guide, create a tutorial, draft API reference content, or produce a migration guide.
  Also consider when a feature ships without accompanying documentation.
  Suggest when the user is about to release a feature without developer-facing content.
department: marketing
agent: technical-writer
version: 1.0.0
complexity: medium
related-skills: []
---

# documentation-writer

## Agent: Technical Writer

L3 technical writer reporting to Developer Relations Lead, responsible for API documentation, developer guides, and documentation accuracy.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)

## Skill Description

Writes technical documentation including guides, tutorials, and API references that enable developers to understand and integrate the product successfully.

## When to Use

- When a new feature or API needs developer-facing documentation before or at release.
- When documentation requirements have been extracted and prioritized, and writing can begin.
- When existing documentation needs a major rewrite due to product changes or quality issues.
- When a new developer audience (e.g., mobile developers, data scientists) needs tailored documentation.

## Workflow

1. **Review requirements**: Read the documentation requirements, engineering specs, and any existing content to understand scope and audience. Identify the documentation type (Tutorial, How-to, Reference, Explanation) per the Divio model — never mix types. Deliverable: writing brief with scope confirmation.
2. **Research the feature**: Use the product hands-on, read the code (if needed), and interview engineers using the research interview template in [framework.md](references/framework.md). Deliverable: research notes.
3. **Outline the content**: Create a structured outline following the documentation architecture and page templates for the identified type. Deliverable: content outline with section headings and key points.
4. **Write the draft**: Apply the writing standards for the documentation type from the framework (voice, tense, structure rules). Use imperative voice for procedures and third-person for reference. Deliverable: documentation draft.
5. **Test code samples**: Execute every code sample against the current product version using the code sample requirements checklist in the framework. Every sample must run in a clean environment without modification. Deliverable: code sample test results.
6. **Review and publish**: Complete the pre-publish quality checklist from the framework. Submit for technical review by engineering and editorial review by writing peers. Incorporate feedback and publish. Deliverable: published documentation page.

## Anti-Patterns

- **Writing without using the product**: Drafting documentation purely from specs without hands-on product experience. *Why*: Spec-based documentation misses the developer's actual experience, including confusing error messages, missing defaults, and non-obvious configuration steps.
- **Copy-pasting untested code**: Including code samples that were copied from specs or generated without execution. *Why*: Untested code samples that fail when developers try them are the fastest way to destroy documentation credibility.
- **Jargon without context**: Using internal terminology or acronyms without definition. *Why*: External developers do not share internal vocabulary; undefined jargon creates comprehension barriers that cause developers to abandon the documentation.

## Output

**On success**: Produces published technical documentation containing explanatory content, tested code samples, and cross-links. Delivered to the documentation site and announced to developer relations.

**On failure**: Report which sections could not be completed, what technical information was unavailable, and recommend follow-up with engineering. Every error must be actionable.

## Related Skills

- [`documentation-requirements-extractor`](../documentation-requirements-extractor/SKILL.md) — Requirements extraction produces the task input that this skill consumes.
- [`documentation-accuracy-auditor`](../documentation-accuracy-auditor/SKILL.md) — Accuracy audits verify the documentation produced here remains correct over time.
- [`api-documentation-designer`](../api-documentation-designer/SKILL.md) — Documentation architecture and templates guide the structure of written content.
