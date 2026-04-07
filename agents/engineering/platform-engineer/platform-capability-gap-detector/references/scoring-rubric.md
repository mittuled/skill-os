# Scoring Rubric: Platform Capability Gap Detector

Evaluates the quality of platform capability gap detection including signal collection, classification, impact assessment, and recommendations.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Signal Breadth | 20% | Number and diversity of signal sources used (surveys, tickets, retros, audit logs, architecture reviews) |
| 2 | Gap Classification | 25% | Accuracy of gap categorization by type, severity, and breadth |
| 3 | Impact Quantification | 25% | Quality of engineering time and team count impact estimates |
| 4 | Recommendation Actionability | 30% | Specificity of resolution recommendations (build, buy, document) with trade-offs |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | 5+ signal sources; gaps classified by type/severity/breadth; impact quantified with engineering hours; recommendations include build/buy/document with cost estimates | Feed directly into roadmap planning |
| A | 8.0 – 8.9 | Strong | Multiple signal sources; gaps well-classified; impact estimated; recommendations actionable | Review with platform lead; incorporate into next quarter |
| B | 7.0 – 7.9 | Good | 3+ signal sources; gaps classified; impact partially quantified; recommendations present | Present to leadership with additional impact data needed |
| C | 5.0 – 6.9 | Adequate | 1-2 signal sources; gaps listed but classification incomplete; impact estimated loosely | Gather additional signals before acting on findings |
| D | 3.0 – 4.9 | Weak | Single signal source; gaps not classified; no impact estimate; generic recommendations | Restart detection with broader signal collection |
| F | 0.0 – 2.9 | Failing | No systematic gap detection performed | Initiate gap detection process |

## Signal Tables

### Signal Breadth
| Score | Evidence |
|-------|----------|
| 9-10 | 5+ distinct sources analyzed (developer surveys, support tickets, retros, architecture reviews, infrastructure audit logs, team interviews); patterns cross-validated across sources |
| 7-8 | 3-4 sources analyzed; cross-validation attempted |
| 5-6 | 2 sources (e.g., surveys and tickets); limited cross-validation |
| 3-4 | Single source (e.g., only the loudest team's complaints) |
| 0-2 | No systematic signal collection |

### Gap Classification
| Score | Evidence |
|-------|----------|
| 9-10 | Each gap classified by type (missing, insufficient, discoverability), severity (blocking, slowing, inconvenient), and breadth (1 team, multiple, all); classification backed by evidence |
| 7-8 | Type and severity classified for most gaps; breadth estimated |
| 5-6 | Gaps listed with severity but type or breadth missing |
| 3-4 | Gaps listed without classification |
| 0-2 | No gap identification |

### Impact Quantification
| Score | Evidence |
|-------|----------|
| 9-10 | Engineering hours wasted on workarounds estimated per gap; number of teams affected counted; risk of current workaround assessed (security, reliability, maintainability) |
| 7-8 | Engineering time estimated for top gaps; team count provided; workaround risk noted |
| 5-6 | Qualitative impact assessment ("significant", "moderate"); team count approximate |
| 3-4 | Impact described anecdotally without quantification |
| 0-2 | No impact assessment |

### Recommendation Actionability
| Score | Evidence |
|-------|----------|
| 9-10 | Each high-priority gap has a specific recommendation (build capability, adopt tool, document pattern) with estimated cost, timeline, and trade-offs; connected to roadmap decisions |
| 7-8 | Recommendations specific with build/buy decision; cost estimates for top gaps; timeline approximate |
| 5-6 | Recommendations present but generic (e.g., "platform should address this"); no cost or timeline |
| 3-4 | Gap report without recommendations |
| 0-2 | No recommendations |
