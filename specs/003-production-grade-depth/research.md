# Research: Production-Grade Skill Depth

**Branch**: `003-production-grade-depth` | **Date**: 2026-03-28

## Research Questions Resolved

### RQ-001: What makes zubair-trabzada's skills "production-grade"?

**Decision**: Production-grade means every skill has quantitative scoring (not qualitative), pre-built output templates (not format descriptions), signal tables mapping evidence to scores, and domain-specific frameworks embedded in the skill rather than referenced by name only.

**Rationale**: The depth audit of 6 representative skills showed skill-os averages 3/5 depth — clear workflows but missing the artifacts that make them executable without guessing. Zubair's skills at 3,000-6,500 words achieve depth through inline content; skill-os achieves it through `references/` and `assets/` (progressive disclosure).

**Alternatives considered**:
- Match zubair's word count inline → Rejected: violates constitution Principle VI word limits
- Add depth selectively (only assessment skills) → Rejected: spec requires all 499+ skills deepened

### RQ-002: What scoring rubric structure works across all skill types?

**Decision**: Standardized rubric format with 3-6 weighted criteria, 0-10 scale per criterion, composite score, grade bands (A+ through F), and signal tables mapping observable evidence to score ranges.

**Rationale**: The 10 existing rubrics from 002 (threat-modelling, go-live-approver, accessibility-auditor-design, etc.) demonstrate this pattern works. Each has 3-6 criteria weighted to 100%, 0-10 scales, and signal tables. This is the proven pattern to scale.

**Alternatives considered**:
- Simple pass/fail checklists → Rejected: no granularity for prioritization
- 0-100 scales → Rejected: false precision; 0-10 is sufficient and easier to calibrate

### RQ-003: What output template structure works across skill types?

**Decision**: Every template has: title, metadata section (date, author, version), executive summary, main content sections with placeholder text and formatting guidance, appendices. Each section includes "good example" and "bad example" annotations.

**Rationale**: Templates must be specific enough that an AI agent can fill them in without guessing structure, but generic enough to apply across instances of the same skill.

**Alternatives considered**:
- Minimal templates (headings only) → Rejected: doesn't meet FR-003 requirement for "full output template"
- Overspecified templates (with sample data) → Rejected: agent may copy sample data instead of generating fresh content

### RQ-004: How should domain-cluster research be organized?

**Decision**: ~60 clusters across 16 departments, grouped by skill family (e.g., "sales qualification", "contract review", "DevOps pipelines"). Each cluster produces research that informs 3-10 skills.

**Rationale**: Per-skill research (500+ searches) is infeasible. Per-department research (16 batches) is too coarse — a department like Engineering has 8+ distinct skill families. Cluster-level research hits the sweet spot.

**Alternatives considered**:
- Per-skill research → Rejected: ~500 web searches, not scalable
- Per-department research → Rejected: too generic, misses domain specifics

### RQ-005: Which frameworks are essential per department?

**Decision**: Key frameworks identified per domain cluster:

**Sales**:
- Qualification: BANT, MEDDIC, CHAMP, GPCTBA/C&I
- Prospecting: Firmographic analysis, buying committee theory, org chart mapping
- Outreach: AIDA, PAS, BAB, cadence science (Salesloft/Outreach research)
- Execution: Challenger Sale, SPIN Selling, Sandler, battle card methodology

**Legal**:
- Contract analysis: Standard clause taxonomy, risk scoring matrices, favorability analysis
- Contract generation: GDPR Articles 13/14, CCPA sections, standard clause libraries
- Compliance: SOC 2 Type II (TSCs), HIPAA (18 identifiers), GDPR (8 principles), CCPA, ISO 27001 (Annex A), PCI DSS v4.0, SOX Section 404
- Employment: IRS 20-factor test, ABC test, worker classification frameworks

**Marketing**:
- SEO: E-E-A-T guidelines, Core Web Vitals (LCP, FID, CLS), technical SEO checklist, schema markup
- CRO: 5-dimension CRO scoring (value prop, clarity, relevance, urgency, anxiety reduction)
- Copy: Headline formulas (4U, PAS, AIDA), voice dimensions, readability scoring (Flesch-Kincaid, Gunning Fog)
- Ads: Google Ads quality score, Meta relevance score, LinkedIn campaign structure

**Product**:
- Prioritization: RICE, ICE, MoSCoW, WSJF, Kano model
- Strategy: Product vision canvas, OKR framework, North Star metric
- Analytics: Bayesian A/B testing, cohort analysis, funnel analysis, HEART framework

**Engineering**:
- Architecture: C4 model, ATAM, ADR (Michael Nygard format)
- Security: OWASP Top 10, STRIDE, DREAD, CWE Top 25
- DevOps: DORA metrics, GitOps principles, deployment strategies (blue-green, canary, rolling)
- Quality: Test pyramid, code review checklist, static analysis rules

**Rationale**: These are the most widely adopted frameworks in each domain. Including them in skill references makes the difference between "qualify the lead" (documentation) and "qualify using BANT scoring with signal-to-score tables" (operating system).

### RQ-006: How should existing 002 rubrics be upgraded?

**Decision**: Each of the 10 existing rubrics is reviewed against the 003 contract (see contracts/scoring-rubric-contract.md). Missing elements are added: signal tables if absent, grade bands if incomplete, domain framework references if generic.

**Rationale**: Spot-check of threat-modelling and go-live-approver rubrics shows they're close to 003 standard but may lack signal tables or complete grade band descriptions. Upgrading is faster than rewriting.

**Alternatives considered**:
- Accept as-is → Rejected per clarification session (all 002 artifacts upgraded)
- Rewrite from scratch → Rejected: existing rubrics are good foundations
