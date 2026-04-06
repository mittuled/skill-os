# Framework: Research Roadmap Contributor

Defines the method for mapping research evidence to roadmap items and generating a prioritised research question backlog.

## Research-Roadmap Alignment Model

### Evidence Quality Tiers

| Tier | Evidence Type | Confidence | Usage |
|------|--------------|-----------|-------|
| T1 | Primary research (interviews, usability tests, surveys with n≥30) | High | Directly supports or challenges roadmap assumptions |
| T2 | Secondary research (analyst reports, peer-reviewed studies, industry benchmarks) | Medium | Provides context; corroborate with T1 when stakes are high |
| T3 | Internal data (analytics, support tickets, sales notes) | Medium | Strong for "what" but weak for "why"; pairs with T1 |
| T4 | Expert opinion / analogous market | Low | Use only when T1-T3 unavailable; flag explicitly |

### Research-Roadmap Alignment Matrix Structure

For each roadmap item:

| Field | Content |
|-------|---------|
| Initiative | Roadmap item name |
| Assumption | The key user or market assumption the initiative depends on |
| Evidence | Existing research supporting or challenging the assumption (with tier rating) |
| Evidence Age | Date of most recent supporting evidence |
| Status | Validated / Challenged / Unvalidated |
| Priority for Research | High / Medium / Low (based on initiative size × evidence gap) |

### Research Question Prioritisation Formula

**Priority Score** = (Initiative Impact × Evidence Gap) − Research Cost

Where:
- **Initiative Impact**: 1-5 (revenue impact, strategic importance)
- **Evidence Gap**: 1-5 (5 = no evidence; 1 = strong T1 evidence exists)
- **Research Cost**: 1-5 (5 = requires 8+ week study; 1 = can be answered in 1 week)

Questions scoring above 12 are High priority; 7-12 are Medium; below 7 are Low.

## Research Contribution Cadences

| Planning Cycle | Research Input Type | Lead Time |
|---------------|-------------------|----------|
| Annual strategic planning | Market landscape synthesis, technology trends, TAM/SAM sizing | 6-8 weeks before |
| Quarterly roadmap planning | Alignment matrix, prioritised research questions | 2 weeks before |
| Sprint planning | Specific research findings for items entering active development | At sprint start |
| Post-launch review | Benchmark comparison for new feature performance | 4-6 weeks post-launch |

## TAM/SAM/SOM Reference (for Roadmap Context)

When validating market-size assumptions embedded in roadmap items:
- **TAM** (Total Addressable Market): Theoretical maximum if 100% market share captured
- **SAM** (Serviceable Addressable Market): TAM filtered for the company's geographic, technical, and segment reach
- **SOM** (Serviceable Obtainable Market): Realistic near-term share given go-to-market capacity and competitive position
