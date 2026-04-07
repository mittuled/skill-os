# Framework: Effort Estimator (Data)

Defines the sizing model for analytics and data engineering work, translating instrumentation specs and dashboard requirements into analyst-day estimates.

## T-Shirt Size Definitions

| Size | Analyst-Days | Characteristics |
|------|-------------|----------------|
| S (Small) | 0.5–1 | Single event or property addition; extends an existing schema; no new SDK integration; minimal QA surface |
| M (Medium) | 2–3 | New event taxonomy for one product surface; new dashboard with 3–5 charts; pipeline config for a known source |
| L (Large) | 4–6 | Multi-platform instrumentation (web + mobile + server); new data model table; complex funnel dashboard with cohort filters |
| XL (Extra Large) | 7–10 | Full instrumentation spec implementation across 3+ platforms; new data warehouse schema; migration of an existing model |

## Work Unit Taxonomy

| Work Unit | Typical Size | Complexity Factors that Upsize |
|-----------|------------|-------------------------------|
| Event schema design | S–M | New taxonomy vs. extension; PII review required |
| SDK integration (single platform) | S–M | First-time SDK vs. existing integration; custom context middleware |
| SDK integration (multi-platform) | M–L | Per-platform: multiply single-platform estimate × 0.8 per additional |
| Pipeline configuration | S–M | New source connector vs. known source; real-time vs. batch |
| Dashboard build | M–L | Number of charts; custom calculations; segment filters |
| Data model design | M–XL | New domain vs. extension; SCD handling; materialized views |
| QA and verification | 20–30% of implementation total | Always add; do not treat as optional |
| Stakeholder review cycles | 0.5 per cycle | Budget 2 cycles minimum |

## Complexity Scoring Factors

Apply these adjustments to the base t-shirt estimate:

| Factor | Adjustment |
|--------|-----------|
| New event taxonomy (no existing schema to extend) | +1 size |
| 3+ platforms required (web, iOS, Android, server) | +1 size |
| Real-time pipeline (vs. batch) | +1 size |
| Third-party integration (no internal SDK) | +1 size |
| PII review required | +0.5 days flat |
| Migration of existing tracking (not greenfield) | +1 size |
| Tight deadline (less than 50% of standard timeline) | +50% to account for context switching and rework |

## Dependency Mapping

| Dependency Type | Blocks | Mitigation |
|----------------|--------|-----------|
| Engineering SDK release | Instrumentation implementation | Schedule implementation after SDK branch cut; coordinate with eng lead |
| API schema finalization | Pipeline config and event property mapping | Use placeholder schema with migration plan |
| Third-party integration access | Pipeline extraction | Initiate access request in Sprint N-1 |
| Data warehouse provisioning | Data model and pipeline deployment | Initiate provisioning request ≥2 sprints ahead |

## Estimate Confidence Levels

| Confidence | Condition | Range Modifier |
|-----------|----------|---------------|
| High | Spec is approved, no dependencies outstanding | ±10% of midpoint |
| Medium | Spec is drafted, 1–2 dependencies unresolved | ±25% of midpoint |
| Low | Spec not written; dependencies unclear | ×2–3 range (treat as rough order of magnitude) |

## Velocity Calibration

After each sprint, log actuals vs. estimates for each work unit type. Recalibrate the t-shirt size definitions when actuals consistently deviate > 40% from estimates across two or more sprints.
