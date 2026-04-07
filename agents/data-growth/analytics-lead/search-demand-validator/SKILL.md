---
name: search-demand-validator
description: >
  This skill validates product demand using search volume, keyword trends, and category data. Use when asked to validate demand signals, assess keyword trends, or quantify search interest for a product category. Also consider when a new idea enters the pipeline without demand evidence. Suggest when a market sizer needs search-based inputs.
department: data-growth
agent: analytics-lead
version: 1.0.0
complexity: medium
related-skills:
  - market-sizer-data
  - demand-validator
---

# search-demand-validator

## Agent: Analytics Lead

L1 analytics leader (1x) responsible for search demand validation, market sizing, goal framing, instrumentation strategy, and north star metric governance.

Department ethos: [ideal-data-growth.md](../../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The search demand validator assesses whether meaningful demand exists for a product concept by analysing search volume, keyword trend trajectories, category growth rates, and competitive keyword density to produce an evidence-based demand signal.

## When to Use

- When a new product idea needs demand validation before committing development resources.
- When the growth team needs to assess organic acquisition potential for SEO or content strategy.
- When a market sizing exercise requires bottom-up demand data from search behaviour.
- When a pivot is proposed and the team needs to compare demand signals between the current and proposed directions.

## Workflow

1. **Define seed keywords**: Extract 10-20 seed keywords from the product concept, covering the problem space, solution category, and competitor brand names.
2. **Pull search volume data**: Query keyword research tools for monthly search volume, trend direction (12-month trajectory), cost-per-click as a proxy for commercial intent, and keyword difficulty.
3. **Expand keyword universe**: Use related keywords, long-tail variants, and question-format queries to build a comprehensive keyword map. Group by intent category (informational, navigational, transactional).
4. **Analyse trends**: Plot 12-24 month trend lines for the top keyword clusters. Classify each as growing (>10% YoY), stable, or declining. Flag seasonal patterns.
5. **Benchmark against comparables**: Compare search demand for the target category against 2-3 analogous categories or competitor products to calibrate whether the volume is meaningful for the business model.
6. **Synthesize demand signal**: Produce a demand validation scorecard rating volume adequacy, trend direction, commercial intent, and competitive density. Deliver a go/caution/no-go recommendation.

## Anti-Patterns

- **Relying on a single keyword**: Validating demand using one head term ignores the long tail where most organic traffic lives. *Why*: a single keyword may have high volume but low relevance, or low volume but high intent.
- **Ignoring trend direction**: High current volume on a declining trend signals a shrinking market. *Why*: entering a declining category means fighting for a smaller pie each year.
- **Conflating search volume with willingness to pay**: High search volume for "free X" does not validate demand for a paid product. *Why*: informational intent does not equal transactional intent.
- **Skipping competitive density**: High-volume keywords dominated by established players may be unreachable for a new entrant. *Why*: keyword difficulty affects whether organic demand is capturable, not just whether it exists.

## Output

**Success:**
- A demand validation scorecard with keyword clusters, monthly volumes, trend trajectories, intent classification, competitive density, and a go/caution/no-go recommendation.

**Failure:**
- Insufficient search data exists for the category (emerging market or niche). Report the data limitation, suggest alternative demand signals (community activity, waitlist signups, adjacent category proxy), and flag the validation as inconclusive.

## Related Skills

- [`market-sizer-data`](../market-sizer-data/SKILL.md) -- search demand data feeds the bottom-up market sizing model.
- [`demand-validator`](../../../product/product-manager/demand-validator/SKILL.md) -- the PM demand validator uses broader signals; this skill provides the search-specific quantitative layer.
