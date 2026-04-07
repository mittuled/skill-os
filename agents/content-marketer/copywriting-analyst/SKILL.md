---
name: copywriting-analyst
description: >
  This skill analyses marketing copy for headline effectiveness, voice consistency,
  readability, and persuasion using structured frameworks. Use when asked to review
  landing page copy, evaluate headline variants, or audit brand voice in written
  materials. Also consider when A/B test results are inconclusive and copy quality
  may be the differentiator. Suggest when a new content piece is about to publish
  without a copy review.
department: marketing
agent: content-marketer
version: 1.0.0
complexity: medium
related-skills:
  - ../../brand-designer/brand-voice-analyst/SKILL.md
  - ../../demand-gen-manager/landing-page-auditor/SKILL.md
triggers:
  - "review this copy"
  - "analyse headline options"
  - "score our landing page text"
  - "check copy readability"
---

# copywriting-analyst

## Agent: Content Marketer

L3 Content Marketer (Nx) responsible for content creation, editorial operations, and ensuring all written marketing assets meet quality, brand voice, and conversion standards.

Department ethos: [ideal-marketing.md](../../../departments/marketing/ideal-marketing.md)
Tool policy: [allowed-tools.yaml](../../../allowed-tools.yaml)

## Skill Description

Analyses marketing copy against headline formulas, voice dimensions, and readability benchmarks, producing a scored assessment with specific rewrite recommendations.

## When to Use

- When a landing page, email, or ad copy draft needs quality review before publishing.
- When multiple headline variants need objective comparison beyond gut feeling.
- When brand voice drift is suspected and copy samples need consistency analysis.
- When A/B test results are flat and copy quality is a potential root cause.

## Workflow

1. **Collect copy samples**: Gather the copy to analyse — full page text, headline variants, or a set of assets for voice consistency review. Deliverable: copy corpus with source labels and intended audience context.
2. **Headline analysis**: Evaluate each headline against the frameworks in `references/framework.md` — score against 4U (Useful, Urgent, Unique, Ultra-specific), PAS (Problem-Agitate-Solve), and AIDA (Attention-Interest-Desire-Action). Identify which formula each headline follows (or fails to follow). Deliverable: headline scorecard with formula mapping.
3. **Voice dimension scoring**: Assess the copy across the four voice dimensions (Formal/Casual, Serious/Playful, Respectful/Irreverent, Enthusiastic/Matter-of-fact). Compare against the brand's target voice profile if available. Deliverable: voice dimension map with drift analysis.
4. **Readability and persuasion scoring**: Run `scripts/score.py` to compute Flesch-Kincaid grade level, average sentence length, passive voice percentage, and persuasion markers (social proof, specificity, power words). Deliverable: readability and persuasion scores.
5. **Report generation**: Compile findings into `assets/copy-analysis-report-template.md` with per-section grades, specific rewrite suggestions, and an overall copy quality score. Deliverable: copy analysis report.

## Anti-Patterns

- **Subjective feedback without framework**: Saying "this doesn't feel right" without referencing a specific dimension or formula. *Why*: Unstructured feedback is not actionable and leads to circular revision cycles.
- **Readability over persuasion**: Optimising exclusively for lower grade level without considering whether the copy still persuades. *Why*: Simple copy that fails to create urgency or desire will not convert regardless of readability score.
- **Ignoring audience context**: Scoring B2B enterprise copy against B2C readability benchmarks. *Why*: A technical audience expects domain-specific language; forcing simplification can undermine credibility.
- **Headline formula rigidity**: Rejecting every headline that does not perfectly fit 4U, PAS, or AIDA. *Why*: Formulas are diagnostic tools, not creative prisons; a headline can work for reasons outside these frameworks.

## Output

**On success**: Produces a markdown copy analysis report (using `assets/copy-analysis-report-template.md`) containing headline scorecards, voice dimension mapping, readability metrics, persuasion scoring, and prioritised rewrite recommendations. Delivered as a file or inline document.

**On failure**: Report which copy samples could not be analysed and why (insufficient text, missing audience context, no brand voice reference), what was attempted, and what additional inputs are needed. Every error must be actionable.

## Related Skills

- [`brand-voice-analyst`](../../brand-designer/brand-voice-analyst/SKILL.md) — Provides the target voice profile that copy should be evaluated against.
- [`landing-page-auditor`](../../demand-gen-manager/landing-page-auditor/SKILL.md) — Copy quality is one dimension of a broader landing page CRO audit.
