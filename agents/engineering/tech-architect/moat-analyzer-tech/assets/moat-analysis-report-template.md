# Moat Analysis Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Tech Architect / author name] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | moat-analyzer-tech |

## Executive Summary

[2-3 sentences stating the overall moat strength score, the primary moat source, and the most critical risk.
GUIDANCE: Lead with the verdict, not the methodology. Example: "The platform's primary moat is its 18-month proprietary behavioral dataset (composite score: 7.4/10, Grade B). The most durable moat source is integration depth across 6 customer data systems. The most critical risk is the open-source model llm-oss reaching feature parity within 12 months."]

## Moat Source Inventory

[Catalogue every identified moat source with an initial strength assessment.

GUIDANCE:
- Good: List each source with its type (data, network, integration, algorithmic, regulatory), current strength, and whether it is compounding or static
- Bad: "We have a lot of proprietary data and our code is complex"
- Format: Table with one row per source]

| Moat Source | Type | Strength (1-10) | Compounding? | Evidence |
|-------------|------|----------------|-------------|----------|
| [Proprietary dataset name] | Data | [N] | [Yes/No] | [Observable evidence] |
| [Integration description] | Integration | [N] | [Yes/No] | [Observable evidence] |
| [Network effect description] | Network | [N] | [Yes/No] | [Observable evidence] |

## Replicability Assessment

[For each moat source, assess how difficult it would be for a well-funded competitor to replicate.

GUIDANCE:
- Good: "Replicating the behavioral dataset requires 18 months of user acquisition and $8M in infrastructure. The integration layer requires 6 engineer-months per customer system."
- Bad: "Hard to copy because our engineers are smart"
- Format: One section per moat source with time/cost/talent estimates]

### [Moat Source Name]

**Replication time estimate**: [X months / years]
**Capital required**: [$X range]
**Talent barrier**: [Specialist profile required, market scarcity]
**Data acquisition barrier**: [What a competitor must do to obtain equivalent data]
**Assessment**: [Hard / Medium / Easy to replicate — one sentence explanation]

## Moat-Strengthening Recommendations

[Specific architectural decisions that would widen the moat.

GUIDANCE:
- Good: "Implement a data flywheel by exposing model confidence scores to users as feedback signals, creating a labeled dataset that improves with each interaction."
- Bad: "Build more features"
- Format: Ranked list with implementation effort estimates]

| Priority | Recommendation | Moat Dimension Strengthened | Effort |
|----------|---------------|----------------------------|--------|
| P1 | [Specific architectural change] | [Data / Network / Integration / Algorithm] | [S/M/L] |
| P2 | [Specific architectural change] | [Data / Network / Integration / Algorithm] | [S/M/L] |

## Moat Risk Assessment

[Identify threats that could erode the moat.

GUIDANCE:
- Good: "open-source project X reached 70% feature parity in Q1 2026 and is adding 3 maintainers per month. At current pace, parity is expected in 14 months."
- Bad: "Competition is a risk"
- Format: Table with risk, probability, timeline, and mitigation]

| Risk | Type | Probability | Timeline | Current Mitigation | Recommended Action |
|------|------|-------------|----------|--------------------|--------------------|
| [Open-source near-parity] | Commoditization | [H/M/L] | [X months] | [Current action] | [Specific next step] |
| [Platform policy change] | Platform | [H/M/L] | [X months] | [Current action] | [Specific next step] |
| [Competitor data acquisition] | Competitive | [H/M/L] | [X months] | [Current action] | [Specific next step] |

## Recommendations

[Prioritized actions for engineering and leadership.
GUIDANCE: Each recommendation should be specific, assignable, and include the moat dimension it protects]

- **P1**: [Immediate action — addresses critical moat risk or accelerates strongest moat source]
- **P2**: [Near-term action — builds second moat source or addresses medium-probability risk]
- **P3**: [Strategic investment — compounds moat over 12+ months]

## Appendices

### A. Methodology

[Data sources used: competitive intelligence reports, architecture documentation, open-source project analysis, customer integration audits, time period covered]

### B. Supporting Data

[Competitive landscape summary, open-source project activity data, integration audit results, replication cost breakdown assumptions]
