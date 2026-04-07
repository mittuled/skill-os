# Scoring Rubric: help-content-reviewer

Evaluates the accuracy, completeness, and usability of a help centre article against the current state of the product.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Factual Accuracy | 35% | Every step, setting name, and screenshot matches the live product |
| 2 | Step Completeness | 25% | No steps are missing; a new user following the article can complete the task without external help |
| 3 | Terminology Consistency | 15% | All feature names, button labels, and navigation paths use current product terminology |
| 4 | Visual Currency | 15% | Screenshots and GIFs reflect the current UI; no outdated visuals present |
| 5 | Related Article Links | 10% | Cross-links point to existing, accurate articles; no broken or outdated links |
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
| A+ | 9.0 – 10.0 | Exceptional | All steps verified against live product; terminology matches UI exactly; all visuals current | Approve for publication; schedule next review at next release cycle |
| A | 8.0 – 8.9 | Strong | One minor factual discrepancy or one outdated screenshot; all critical steps correct | Publish with minor corrections; no review gate required |
| B | 7.0 – 7.9 | Good | 1-2 steps inaccurate or a feature renamed without reflection; no customer-blocking errors | Update before next release cycle; flag for quick fix |
| C | 5.0 – 6.9 | Adequate | Multiple inaccurate steps; screenshots significantly out of date; customer could be misled | Pull from publication or add "under review" banner; prioritise rewrite |
| D | 3.0 – 4.9 | Weak | Core workflow steps wrong; article would cause customer errors if followed | Unpublish immediately; escalate rewrite as P1 content task |
| F | 0.0 – 2.9 | Failing | Article describes a workflow that no longer exists or has been replaced entirely | Delete; create new article from scratch with product team input |

## Signal Tables

### Factual Accuracy

| Score | Evidence |
|-------|----------|
| 9-10 | Every step performed in the live product produces exactly the result the article describes; all field names, options, and confirmation messages match |
| 7-8 | One step produces a slightly different result (e.g., an extra confirmation dialog added); no step causes a customer error |
| 5-6 | 2-3 steps produce different results; customers following the article would reach an unexpected state but could self-correct |
| 3-4 | A critical step (e.g., "click Save") is missing or points to a removed UI element; customer cannot complete the task |
| 0-2 | The feature described has been redesigned or removed; the article describes a non-existent workflow |

### Step Completeness

| Score | Evidence |
|-------|----------|
| 9-10 | A first-time user with no prior knowledge completes the task end-to-end using only the article |
| 7-8 | One prerequisite step missing (e.g., enabling a setting first) but a savvy user works around it; no blocking gaps |
| 5-6 | 2-3 steps missing; most users need to contact support or search for supplementary help |
| 3-4 | Core steps absent; article reads as an overview rather than a procedure |
| 0-2 | No actionable steps; article is a feature description without instructions |

### Terminology Consistency

| Score | Evidence |
|-------|----------|
| 9-10 | Every button label, menu name, and setting matches current UI text exactly |
| 7-8 | 1-2 labels outdated (e.g., old button name) but context makes the correct action obvious |
| 5-6 | 3-5 terminology mismatches; customers unfamiliar with the old naming may be confused |
| 3-4 | A key navigation path renamed (e.g., "Settings > Integrations" now "Settings > Connections"); customer cannot follow the path |
| 0-2 | Throughout the article, product names and navigation paths are unrecognisable compared to the current UI |

### Visual Currency

| Score | Evidence |
|-------|----------|
| 9-10 | All screenshots taken from current product version; UI elements visible in images match the live product |
| 7-8 | 1-2 screenshots show minor UI differences (e.g., new sidebar colour) but core elements are recognisable |
| 5-6 | Several screenshots show a noticeably different UI (older design system or layout) but the general location of elements is similar |
| 3-4 | Screenshots show a previous major version with different navigation structure; customers cannot find referenced elements |
| 0-2 | No screenshots present where they are clearly needed, or all screenshots show a deprecated product version |

### Related Article Links

| Score | Evidence |
|-------|----------|
| 9-10 | All cross-links resolve to live, accurate articles; anchor links land on the correct section |
| 7-8 | 1 broken link present; all other links accurate and resolve correctly |
| 5-6 | 2-3 broken or outdated links; some link to articles that have been merged or renamed |
| 3-4 | More than half the related article links are broken or point to deprecated content |
| 0-2 | No related article links present where clearly needed, or all links return 404 |
