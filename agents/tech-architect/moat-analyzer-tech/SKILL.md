---
name: moat-analyzer-tech
description: >
  This skill analyses the technical defensibility and competitive moat of the proposed
  architecture. Use when asked to assess technical differentiation, evaluate
  defensibility of the technology stack, or identify technical moat opportunities.
  Also consider when the product strategy relies on technical advantages that need
  validation. Suggest when the user is building without considering technical
  defensibility.
department: engineering
agent: tech-architect
version: 1.0.0
complexity: medium
related-skills:
  - ../architecture-designer/SKILL.md
  - ../technical-feasibility-check/SKILL.md
---

# moat-analyzer-tech

## Agent: Tech Architect

L2 technical architect (1x) responsible for feasibility assessment, system design, API contract definition, and infrastructure planning. Ensures technical decisions support product goals and scale requirements.

Department ethos: [ideal-engineering.md](../../../departments/engineering/ideal-engineering.md)

## Skill Description

Analyses the technical defensibility and competitive moat of the proposed architecture by evaluating proprietary data advantages, technical complexity barriers, network effects, and switching costs that protect against competitive replication.

## When to Use

- When the product strategy claims technical differentiation and engineering needs to validate whether the technology creates a genuine competitive barrier.
- When architectural decisions are being made and the team should consider which choices build long-term defensibility versus commoditized capability.
- When investors or leadership ask for an assessment of the company's technical moat as part of fundraising or strategic planning.

## Workflow

1. **Moat Source Identification**: Identify potential sources of technical moat in the current or proposed architecture: proprietary data assets, unique data processing pipelines, network effects, integration depth, performance advantages, and algorithmic differentiation. Deliverable: moat source inventory.
2. **Replicability Assessment**: For each moat source, assess how difficult it would be for a well-funded competitor to replicate. Consider time to replicate, capital required, data acquisition barriers, and talent requirements. Deliverable: replicability analysis per moat source.
3. **Moat Strengthening Recommendations**: Identify architectural decisions that would strengthen the moat: data flywheel designs, compounding network effects, deeper integration patterns, and proprietary tooling that improves with scale. Deliverable: moat-strengthening architecture recommendations.
4. **Risk Assessment**: Identify threats to the moat: open-source alternatives approaching feature parity, platform risk from dependencies, commoditization of key capabilities, and regulatory changes that could erode data advantages. Deliverable: moat risk assessment.

## Anti-Patterns

- **Complexity as moat**: Treating accidental complexity (tangled codebase, undocumented systems) as a competitive barrier. *Why*: accidental complexity slows the company as much as competitors; it is a liability, not an asset.
- **Feature moat illusion**: Claiming features that are straightforward to build constitute a moat. *Why*: features without data, network, or integration advantages can be replicated in weeks by any competent team; true moats compound over time.
- **Ignoring open source**: Failing to monitor open-source projects that could commoditize the company's technical differentiation. *Why*: open-source alternatives erode moats faster than competitors; by the time a community project reaches parity, the moat is gone.

## Output

**On success**: Produces a moat analysis with source inventory, replicability assessment, strengthening recommendations, and risk assessment. Delivered during architecture design and updated during strategic planning cycles.

**On failure**: Report which moat sources could not be assessed (insufficient competitive intelligence, unclear architecture), what partial analysis was completed, and recommended steps to complete the assessment.

## Related Skills

- [`architecture-designer`](../architecture-designer/SKILL.md) -- Architecture decisions directly determine the technical moat; moat analysis should inform design choices.
- [`technical-feasibility-check`](../technical-feasibility-check/SKILL.md) -- Feasibility checks validate whether moat-building architectural choices are implementable.
