---
name: brand-voice-analyst
description: >
  This skill evaluates brand voice consistency across content assets by scoring
  tone spectrum adherence, vocabulary alignment, and clarity against a defined
  brand voice standard, producing a consistency report with specific copy
  corrections. Use when new content is being reviewed before publication, when
  a brand voice guide has been updated and existing assets need re-evaluation,
  or when multiple content contributors are producing inconsistent-sounding
  material. Suggest when customer feedback indicates the brand sounds different
  across touchpoints.
department: design
agent: brand-designer
version: 1.0.0

complexity: medium
related-skills:
  - ../../../design/brand-designer/brand-foundation/SKILL.md
  - ../../../design/brand-designer/positioning-crafter-brand/SKILL.md
  - ../../../marketing/demand-gen-manager/landing-page-auditor/SKILL.md
  - ../../../marketing/vp-marketing/marketing-audit-orchestrator/SKILL.md
  - ../../../marketing/content-marketer/copywriting-analyst/SKILL.md
triggers:
  - "audit brand voice"
  - "check content consistency"
  - "does this sound like us"
  - "brand voice review"
  - "tone of voice check"
---

# brand-voice-analyst

## Agent: Brand Designer

L2 Brand Designer (1x) responsible for visual identity systems, brand standards, design language, and cross-channel brand consistency across all customer-facing materials.

Department ethos: [ideal-design.md](../../../../departments/design/ideal-design.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Evaluates brand voice consistency across content assets by scoring tone spectrum adherence, vocabulary alignment, and clarity against the brand voice standard, producing a scored consistency report with annotated copy corrections and a rewrite guide for content contributors.

## When to Use

- When new content (blog posts, ads, emails, product copy, social posts) is ready for brand review before publication.
- When a brand voice guide has been updated or created and existing content assets need to be evaluated against the new standard.
- When multiple contributors are producing content and voice drift is creating inconsistency across channels.
- When customer research or feedback indicates that the brand sounds different across touchpoints or does not match brand positioning.
- When onboarding a new content agency or freelancer and a calibration review is needed to align their output with brand standards.

## Workflow

1. **Establish brand voice baseline**: Confirm that a brand voice standard exists and is documented. If no standard exists, halt and route to the `brand-foundation` skill before proceeding. Retrieve the tone spectrum (e.g., confident-not-arrogant, direct-not-terse, warm-not-casual), the approved vocabulary list, and the clarity guidelines. Reference `references/scoring-rubric.md` for dimension definitions and scoring thresholds. Deliverable: brand voice baseline confirmation with tone spectrum and vocabulary source documents.

2. **Content asset inventory**: Collect all content assets submitted for review. Categorise by asset type (website copy, ads, email, social, product UI, sales material) and channel. For each asset, note the author, date, and intended audience. Deliverable: content asset inventory with metadata.

3. **Tone spectrum scoring**: Read each asset and score it against the tone spectrum dimensions in `references/scoring-rubric.md`. For each dimension, assign a score (0-10) and flag specific sentences or phrases that deviate from the target tone. Distinguish between tone-too-formal, tone-too-casual, tone-inconsistent-within-asset, and tone-correct. Deliverable: tone spectrum score per asset with annotated deviations.

4. **Vocabulary audit**: Check each asset against the approved vocabulary list in `references/scoring-rubric.md`. Flag banned words (jargon, competitor terms, deprecated product names), preferred alternatives, and missing preferred vocabulary. Score vocabulary alignment (0-10) per asset. Deliverable: vocabulary audit log per asset with flagged terms and suggested replacements.

5. **Clarity scoring**: Evaluate each asset for reading level, sentence length, passive voice frequency, and unnecessary qualifiers. Score clarity (0-10) using the thresholds in `references/scoring-rubric.md`. Flag sentences that score below the clarity threshold with specific rewrites. Deliverable: clarity score per asset with annotated rewrites.

6. **Consistency report and rewrite guide**: Compile all dimension scores into an overall brand voice consistency score per asset and across the full asset set. Identify the most common deviation patterns to highlight systemic issues versus one-off errors. Generate the brand voice analysis using `assets/brand-voice-analysis-template.md`. Include a rewrite guide with before-and-after examples for the top five deviation patterns. Deliverable: brand voice consistency report with rewrite guide, ready for content team use.

## Anti-Patterns

- **Applying voice standards without knowing the audience context**: Scoring enterprise sales collateral against the same tone benchmark as social media posts. *Why*: Brand voice has a consistent core but flexes by channel and audience formality; rigid application produces copy that is wrong for the context.
- **Flagging deviation without providing corrections**: Marking content as off-brand without offering specific rewrites. *Why*: Content teams cannot improve systematically without concrete examples of what "on-brand" looks like for each type of deviation.
- **Confusing brand voice with brand messaging**: Evaluating whether the content says the right things (messaging) rather than whether it says things in the right way (voice). *Why*: Voice analysis is about style and tone, not message accuracy; conflating the two produces an unfocused review that neither fixes voice nor validates messaging.
- **Over-correcting toward uniformity**: Flagging all stylistic variation as a voice problem. *Why*: Healthy brand voice allows range — a product changelog and a customer story should sound like the same company but not identical; over-correction produces robotic, interchangeable copy.

## Output

**On success**: Produces a brand voice consistency report (using `assets/brand-voice-analysis-template.md`) with per-asset scores across tone spectrum, vocabulary, and clarity dimensions, a summary consistency rating for the full asset set, the top five deviation patterns, and a rewrite guide with before-and-after examples. Delivered as a document ready for the content team and brand review process.

**On failure**: Report which assets could not be scored and why (no brand voice standard to compare against, missing asset access, ambiguous tone spectrum definition), what was completed, and what is needed to finish. Every gap is a specific, actionable request.

## Related Skills

- [`brand-foundation`](../../../design/brand-designer/brand-foundation/SKILL.md) — Brand voice standards originate from the brand foundation; voice analysis requires a documented standard to score against.
- [`positioning-crafter-brand`](../../../design/brand-designer/positioning-crafter-brand/SKILL.md) — Brand positioning drives tone and vocabulary choices; positioning changes should trigger a voice audit of existing content.
- [`landing-page-auditor`](../../../marketing/demand-gen-manager/landing-page-auditor/SKILL.md) — Landing pages must pass both brand voice and conversion quality checks; findings from both audits may affect the same page.
