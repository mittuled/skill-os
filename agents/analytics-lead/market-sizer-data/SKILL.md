---
name: market-sizer-data
description: >
  This skill sizes the addressable market using quantitative data sources and modelling. Use when asked to estimate TAM/SAM/SOM, validate market opportunity, or quantify segment size. Also consider when a business case requires market size justification. Suggest when a new product idea lacks demand-side quantification.
department: data-growth
agent: analytics-lead
version: 1.0.0
complexity: medium
related-skills:
  - search-demand-validator
  - market-sizer
---

# market-sizer-data

## Agent: Analytics Lead

L1 analytics leader (1x) responsible for search demand validation, market sizing, goal framing, instrumentation strategy, and north star metric governance.

Department ethos: [ideal-data-growth.md](../../../departments/data-growth/ideal-data-growth.md)

## Skill Description

The market sizer quantifies the total addressable market (TAM), serviceable addressable market (SAM), and serviceable obtainable market (SOM) using bottom-up data models, search demand signals, and public data sources to validate whether a product opportunity justifies investment.

## When to Use

- When a new product concept needs market size validation before entering the build phase.
- When investors or leadership request a data-backed market sizing for a pitch or business case.
- When the growth team needs segment-level sizing to prioritize acquisition channels.
- When a pivot or expansion into an adjacent market requires re-sizing the opportunity.

## Workflow

1. **Define the market boundary**: Specify the product category, geography, customer segment, and time horizon. Document inclusion and exclusion criteria.
2. **Gather data sources**: Collect search volume data, industry reports, census data, competitor revenue proxies, and any internal usage data. Note the recency and reliability of each source.
3. **Build bottom-up model**: Estimate the number of potential customers in the segment, the expected adoption rate, and the average revenue per user (ARPU). Multiply to produce SAM and SOM.
4. **Build top-down cross-check**: Use industry revenue data or analyst reports to estimate TAM. Compare top-down and bottom-up figures; investigate divergences greater than 2x.
5. **Sensitivity analysis**: Vary key assumptions (adoption rate, ARPU, segment size) across low/mid/high scenarios. Present the range rather than a single point estimate.
6. **Document and present**: Produce a market sizing brief with methodology, data sources, assumptions, scenario outputs, and confidence level.

## Anti-Patterns

- **Single-source sizing**: Relying on one analyst report or one data source produces fragile estimates. *Why*: any single source may have sampling bias, outdated figures, or different market definitions.
- **TAM as the pitch number**: Presenting TAM instead of SOM inflates the opportunity and misleads stakeholders. *Why*: TAM includes segments the product cannot realistically reach; SOM is the actionable figure.
- **Point estimates without ranges**: Delivering a single market size number hides the uncertainty inherent in every assumption. *Why*: decision-makers need to understand the downside scenario, not just the midpoint.
- **Ignoring willingness to pay**: Sizing by headcount without validating price sensitivity overstates revenue potential. *Why*: a large addressable population at zero willingness to pay is not a market.

## Output

**Success:**
- A market sizing brief containing TAM, SAM, and SOM with methodology, data sources, assumption log, sensitivity analysis across three scenarios, and a confidence rating.

**Failure:**
- Market sizing relies on a single source or uses TAM as the primary figure. Report the data gap, recommend additional sources, and flag which assumptions need validation.

## Related Skills

- [`search-demand-validator`](../search-demand-validator/SKILL.md) -- search demand data is a key input to bottom-up market sizing.
- [`market-sizer`](../../product-manager/market-sizer/SKILL.md) -- the product manager's market sizer focuses on opportunity framing; this skill provides the quantitative backing.
