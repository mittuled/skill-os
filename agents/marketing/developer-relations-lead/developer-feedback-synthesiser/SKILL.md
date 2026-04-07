---
name: developer-feedback-synthesiser
description: >
  This skill synthesises developer feedback into actionable product and documentation improvements.
  Use when asked to consolidate developer feedback, create improvement recommendations, or prioritize developer pain points.
  Also consider when multiple feedback channels have accumulated unprocessed developer input.
  Suggest when the user is about to start a planning cycle without synthesised developer feedback.
department: marketing
agent: developer-relations-lead
version: 1.0.0
complexity: medium
related-skills: []
triggers:
  - "summarize developer feedback"
  - "what are developers saying"
  - "consolidate dev community feedback"
  - "synthesize developer pain points"
---

# developer-feedback-synthesiser

## Agent: Developer Relations Lead

L2 developer relations lead responsible for developer community signal extraction, developer GTM, experience review, feedback synthesis, and community growth.

Department ethos: [ideal-marketing.md](../../../../departments/marketing/ideal-marketing.md)

## Skill Description

Synthesises developer feedback from multiple channels into actionable product and documentation improvements prioritized by impact and feasibility.

## When to Use

- When a product planning cycle is starting and developer feedback needs to be consolidated into actionable input.
- When multiple feedback channels (support, community, surveys, interviews) have accumulated developer input that no one has synthesised.
- When a specific developer pain point keeps surfacing and needs a structured analysis to justify prioritization.
- When preparing a developer advisory board meeting and needing a synthesised view of feedback themes.

## Workflow

1. **Collect feedback sources**: Gather developer feedback from all channels using the source inventory in [framework.md](references/framework.md) (support tickets, community forums, NPS surveys, user interviews, GitHub issues, social media). Deliverable: raw feedback inventory with source and date.
2. **Normalize and deduplicate**: Apply the normalization protocol from the framework to standardize feedback format, merge duplicates, and tag each item with required metadata (developer segment, product area, category, sentiment, severity). Deliverable: normalized feedback database.
3. **Identify themes**: Cluster feedback using the affinity mapping protocol from the framework. Apply segment weighting (Enterprise 3×, SMB 2×, Startup 1.5×). Flag themes appearing in 3+ consecutive cycles as chronic. Deliverable: theme map with quantification.
4. **Assess impact and feasibility**: Score each theme on the impact-feasibility matrix in the framework and assign to a priority quadrant (Quick Win, Strategic Bet, Backlog Filler, Deprioritize). Deliverable: impact-feasibility matrix.
5. **Write synthesis report**: Use the recommendation format from the framework to produce actionable recommendations ranked by impact-feasibility score. Connect themes to product strategy. Deliverable: developer feedback synthesis report.
6. **Present and track**: Share the synthesis with product and engineering stakeholders. Track which recommendations are accepted, rejected, or deferred with rationale. Deliverable: recommendation tracking log.

## Anti-Patterns

- **Recency bias**: Over-weighting recent feedback while ignoring persistent themes from earlier periods. *Why*: Long-standing pain points may be underreported because developers have given up mentioning them, not because they are resolved.
- **Synthesis without recommendation**: Producing a summary of themes without concrete, actionable improvement proposals. *Why*: Feedback summaries without recommendations create awareness but not action; product teams need specific proposals to prioritize.
- **Single-channel synthesis**: Synthesising from only one feedback channel while ignoring others. *Why*: Each channel attracts a different developer segment; single-channel synthesis produces a biased view that misrepresents the full developer population.

## Output

**On success**: Produces a developer feedback synthesis report containing theme map, impact-feasibility matrix, and prioritized recommendations. Delivered to product, engineering, and developer relations leadership.

**On failure**: Report which feedback sources were unavailable, what coverage gaps exist, and recommend how to fill them. Every error must be actionable.

## Related Skills

- [`developer-community-signal-extractor`](../developer-community-signal-extractor/SKILL.md) — Signal extraction provides one of the key inputs to the synthesis process.
- [`developer-experience-reviewer`](../developer-experience-reviewer/SKILL.md) — Experience review findings are validated against synthesised feedback themes.
- [`api-developer-experience-reviewer`](../api-developer-experience-reviewer/SKILL.md) — API-specific feedback themes feed into targeted API experience reviews.
