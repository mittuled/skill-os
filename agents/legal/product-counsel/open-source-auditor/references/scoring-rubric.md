# Scoring Rubric: open-source-auditor

Evaluates the completeness and rigour of an open-source software audit covering dependency inventory, licence classification, copyleft exposure, and compliance verification.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Dependency Inventory | 20% | Completeness of the software bill of materials including transitive dependencies |
| 2 | Licence Classification | 25% | Accuracy of licence type identification and compatibility analysis with company distribution model |
| 3 | Copyleft Exposure Analysis | 30% | Depth of analysis for copyleft-triggered obligations based on actual usage patterns (linking, network interaction) |
| 4 | Compliance Verification | 25% | Completeness of obligation fulfillment verification (attribution, licence text, source availability) |

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
| A+ | 9.0 – 10.0 | Exceptional | Complete SBOM with transitive deps, all licences classified and compatible, copyleft analysis thorough, all obligations met | Clear for release |
| A | 8.0 – 8.9 | Strong | SBOM complete, licences classified, minor attribution gaps identified with fixes planned | Clear for release with minor fixes pre-ship |
| B | 7.0 – 7.9 | Good | SBOM mostly complete, licence classification done, copyleft analysis present but missing some usage patterns | Clear with conditions: complete analysis within 2 weeks |
| C | 5.0 – 6.9 | Adequate | SBOM covers direct deps only, licence types identified but compatibility not fully analysed | Hold release: complete transitive dependency analysis |
| D | 3.0 – 4.9 | Weak | Partial SBOM, significant licence classification gaps, no copyleft analysis | Block release: major audit gaps |
| F | 0.0 – 2.9 | Failing | No systematic dependency inventory or licence review | Block release: full audit required |

## Signal Tables

### Dependency Inventory

| Score | Evidence |
|-------|----------|
| 9-10 | Automated SBOM generation covering all package managers (npm, pip, Maven, Go modules), transitive dependencies resolved to leaf level, licence and version recorded for each component, SBOM in standard format (SPDX or CycloneDX) |
| 7-8 | SBOM covers all direct and most transitive dependencies, generated via tooling, minor gaps in edge-case package managers |
| 5-6 | Direct dependencies inventoried, transitive dependencies partially resolved, some manual entries |
| 3-4 | Partial inventory of direct dependencies only, no transitive resolution |
| 0-2 | No dependency inventory or only ad-hoc list of known libraries |

### Licence Classification

| Score | Evidence |
|-------|----------|
| 9-10 | Every component classified as permissive (MIT, Apache 2.0, BSD), weak copyleft (LGPL, MPL), strong copyleft (GPL, AGPL), or proprietary. Compatibility with SaaS/on-premise/embedded distribution model analysed. Dual-licensed components resolved. |
| 7-8 | Most components classified, compatibility analysis for primary distribution model, dual-licensing noted |
| 5-6 | Licence types identified for most components but compatibility analysis incomplete or distribution model not considered |
| 3-4 | Some licences identified but many components unclassified or classification unreliable |
| 0-2 | No licence classification performed |

### Copyleft Exposure Analysis

| Score | Evidence |
|-------|----------|
| 9-10 | Each GPL/AGPL/LGPL component analysed for usage pattern (static linking, dynamic linking, process boundary, network interaction). AGPL network-use trigger assessed for SaaS deployment. Proprietary code isolation verified. Legal opinion on borderline cases documented. |
| 7-8 | Major copyleft components analysed for usage pattern, AGPL network trigger assessed, most isolation boundaries verified |
| 5-6 | Copyleft components identified but usage pattern analysis incomplete; linking type not verified for all components |
| 3-4 | Copyleft presence noted without usage pattern analysis |
| 0-2 | No copyleft analysis performed |

### Compliance Verification

| Score | Evidence |
|-------|----------|
| 9-10 | Attribution notices verified in product (NOTICES file, about screen, documentation), licence texts included for all components, source code offer published where required (GPL), modification documentation maintained |
| 7-8 | Attribution and licence text inclusion verified for most components, source offer in place where needed |
| 5-6 | Attribution partially implemented, some licence texts missing, source offer not yet published |
| 3-4 | Compliance obligations identified but not yet implemented |
| 0-2 | No compliance verification performed |
