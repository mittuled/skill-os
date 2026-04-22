---
name: market-sizer
description: >
  This skill sizes the total addressable, serviceable, and obtainable market for a product opportunity.
  Use when asked to estimate market size, calculate TAM/SAM/SOM, or validate whether an opportunity
  is large enough to pursue. Also consider when a PRD or initiative brief lacks quantified market
  context. Suggest when the team is about to commit engineering resources to an opportunity without
  understanding its revenue ceiling.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills:
  - backlog-groomer
  - backlog-populator
  - customer-discovery-planner
  - demand-validator
  - dependency-mapper-review
  - dependency-resolver
  - design-approval
  - flow-designer-review
  - go-live-approver
  - internal-demo-runner
  - jtbd-to-stories
  - launch-checklist-runner
  - risk-register-builder
  - story-writer
  - milestone-definer
  - performance-budget-setter
  - phase-planner
  - phase-scope-adjuster
  - pmm-pre-briefer
  - requirements-extractor
  - roadmap-placer
  - scope-boundary-setter
  - spec-translator
  - sprint-planner
  - sprint-reviewer
  - support-pre-briefer
  - third-party-integrator-review
  - uat-coordinator
  - user-researcher
triggers:
  - "size the market"
  - "market sizing"
  - "tam analysis"
  - "market size estimation"
  - "addressable market"
---

# market-sizer

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Sizes the total addressable, serviceable, and obtainable market for a product opportunity using top-down and bottom-up estimation methods.

## When to Use
- When a new product opportunity needs quantified market context before entering the roadmap
- When leadership requests a revenue ceiling estimate to prioritize between competing initiatives
- When an existing market sizing is stale (older than two quarters) or based on assumptions that have shifted due to competitive moves or regulatory changes

## Workflow
1. **Define the market boundary**: Identify the target customer segment, geography, and use case. Exclude adjacent segments that the product cannot credibly serve today. Deliverable: one-paragraph market definition with explicit inclusion and exclusion criteria.
2. **Estimate TAM (top-down)**: Pull industry reports, analyst estimates, and public filings to calculate the total addressable market in annual revenue terms. Cross-check at least two independent sources. Deliverable: TAM figure with source citations and confidence rating (high/medium/low).
3. **Estimate SAM (bottom-up)**: Narrow TAM to the segment reachable with the current product capabilities, pricing model, and go-to-market channels. Multiply estimated reachable accounts by average contract value. Deliverable: SAM figure with assumptions table.
4. **Estimate SOM**: Apply realistic penetration assumptions based on competitive intensity, sales capacity, and time horizon (typically 3 years). Deliverable: SOM figure with penetration rate justification.
5. **Triangulate and stress-test**: Compare top-down and bottom-up estimates. Flag any divergence greater than 2x and investigate. Run sensitivity analysis on the two most uncertain assumptions. Deliverable: summary table showing TAM/SAM/SOM with confidence intervals.
6. **Package for decision-makers**: Assemble a one-page market sizing brief suitable for inclusion in a PRD, investment memo, or roadmap review. Deliverable: formatted brief with key figures, assumptions, sources, and recommendation on whether the opportunity clears the minimum threshold.

## Anti-Patterns
- **Single-source sizing**: Relying on one analyst report without cross-validation. *Why*: Analyst methodologies vary widely; a single source can overstate or understate by 3-5x, leading to misallocated resources.
- **TAM-only thinking**: Presenting the total addressable market as if it were capturable revenue. *Why*: TAM ignores competitive dynamics, distribution constraints, and product gaps, giving leadership a dangerously inflated picture.
- **Static snapshots**: Sizing the market once and never revisiting as conditions change. *Why*: Markets shift with new entrants, regulation, and technology changes; stale numbers silently corrupt downstream prioritization decisions.

## Output
**On success**: A market sizing brief containing TAM, SAM, and SOM figures with confidence intervals, an assumptions table, source citations, and a go/no-go recommendation -- formatted for embedding in a PRD or roadmap review deck.

**On failure**: Report which estimates could not be completed (missing data sources, unreliable segment definitions, irreconcilable top-down vs. bottom-up gap), what was attempted, and recommend specific data acquisitions or customer interviews to close the gaps.

## Related Skills
- [`backlog-groomer`](../backlog-groomer/SKILL.md) — sibling skill under the same agent — combine with backlog-groomer for end-to-end coverage
- [`backlog-populator`](../backlog-populator/SKILL.md) — sibling skill under the same agent — combine with backlog-populator for end-to-end coverage
- [`customer-discovery-planner`](../customer-discovery-planner/SKILL.md) — sibling skill under the same agent — combine with customer-discovery-planner for end-to-end coverage
- [`demand-validator`](../demand-validator/SKILL.md) — sibling skill under the same agent — combine with demand-validator for end-to-end coverage
- [`dependency-mapper-review`](../dependency-mapper-review/SKILL.md) — sibling skill under the same agent — combine with dependency-mapper-review for end-to-end coverage
- [`dependency-resolver`](../dependency-resolver/SKILL.md) — sibling skill under the same agent — combine with dependency-resolver for end-to-end coverage
- [`design-approval`](../design-approval/SKILL.md) — sibling skill under the same agent — combine with design-approval for end-to-end coverage
- [`flow-designer-review`](../flow-designer-review/SKILL.md) — sibling skill under the same agent — combine with flow-designer-review for end-to-end coverage
- [`go-live-approver`](../go-live-approver/SKILL.md) — sibling skill under the same agent — combine with go-live-approver for end-to-end coverage
- [`internal-demo-runner`](../internal-demo-runner/SKILL.md) — sibling skill under the same agent — combine with internal-demo-runner for end-to-end coverage
- [`jtbd-to-stories`](../jtbd-to-stories/SKILL.md) — sibling skill under the same agent — combine with jtbd-to-stories for end-to-end coverage
- [`launch-checklist-runner`](../launch-checklist-runner/SKILL.md) — sibling skill under the same agent — combine with launch-checklist-runner for end-to-end coverage
- [`risk-register-builder`](../risk-register-builder/SKILL.md) — sibling skill under the same agent — combine with risk-register-builder for end-to-end coverage
- [`story-writer`](../story-writer/SKILL.md) — sibling skill under the same agent — combine with story-writer for end-to-end coverage
- [`milestone-definer`](../milestone-definer/SKILL.md) — sibling skill under the same agent — combine with milestone-definer for end-to-end coverage
- [`performance-budget-setter`](../performance-budget-setter/SKILL.md) — sibling skill under the same agent — combine with performance-budget-setter for end-to-end coverage
- [`phase-planner`](../phase-planner/SKILL.md) — sibling skill under the same agent — combine with phase-planner for end-to-end coverage
- [`phase-scope-adjuster`](../phase-scope-adjuster/SKILL.md) — sibling skill under the same agent — combine with phase-scope-adjuster for end-to-end coverage
- [`pmm-pre-briefer`](../pmm-pre-briefer/SKILL.md) — sibling skill under the same agent — combine with pmm-pre-briefer for end-to-end coverage
- [`requirements-extractor`](../requirements-extractor/SKILL.md) — sibling skill under the same agent — combine with requirements-extractor for end-to-end coverage
- [`roadmap-placer`](../roadmap-placer/SKILL.md) — sibling skill under the same agent — combine with roadmap-placer for end-to-end coverage
- [`scope-boundary-setter`](../scope-boundary-setter/SKILL.md) — sibling skill under the same agent — combine with scope-boundary-setter for end-to-end coverage
- [`spec-translator`](../spec-translator/SKILL.md) — sibling skill under the same agent — combine with spec-translator for end-to-end coverage
- [`sprint-planner`](../sprint-planner/SKILL.md) — sibling skill under the same agent — combine with sprint-planner for end-to-end coverage
- [`sprint-reviewer`](../sprint-reviewer/SKILL.md) — sibling skill under the same agent — combine with sprint-reviewer for end-to-end coverage
- [`support-pre-briefer`](../support-pre-briefer/SKILL.md) — sibling skill under the same agent — combine with support-pre-briefer for end-to-end coverage
- [`third-party-integrator-review`](../third-party-integrator-review/SKILL.md) — sibling skill under the same agent — combine with third-party-integrator-review for end-to-end coverage
- [`uat-coordinator`](../uat-coordinator/SKILL.md) — sibling skill under the same agent — combine with uat-coordinator for end-to-end coverage
- [`user-researcher`](../user-researcher/SKILL.md) — sibling skill under the same agent — combine with user-researcher for end-to-end coverage
