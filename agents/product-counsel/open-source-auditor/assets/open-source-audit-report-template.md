# Open Source Audit Report

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Author | [Product Counsel] |
| Version | [1.0] |
| Status | [Draft / Review / Final] |
| Skill | open-source-auditor |

## Executive Summary

[2-3 sentences summarizing total dependency count, licence risk findings, and release readiness.
GUIDANCE: Lead with the release decision and the most critical finding (e.g., copyleft exposure in a core dependency).]

## Software Bill of Materials Summary

[SBOM overview with dependency statistics.

GUIDANCE:
- Good: "Total components: 342 (87 direct, 255 transitive). Licence breakdown: 298 permissive (MIT: 156, Apache 2.0: 89, BSD: 53), 12 weak copyleft (LGPL: 8, MPL: 4), 3 strong copyleft (GPL-2.0: 2, AGPL-3.0: 1), 29 unclassified."
- Bad: "We use many open source libraries"
- Format: Summary table with counts by licence category, full SBOM in appendix]

## Licence Classification Matrix

[Classification of each flagged component by licence type and compatibility.

GUIDANCE:
- Good: Table with Component, Version, Licence, Category (Permissive/Weak Copyleft/Strong Copyleft), Distribution Compatibility (Compatible/Incompatible/Requires Analysis), Action Required
- Bad: "Most licences are fine"
- Format: Matrix for all non-permissive or unclassified components]

## Copyleft Exposure Analysis

[Detailed analysis of copyleft-licensed components and their usage patterns.

GUIDANCE:
- Good: "Component: libgmp (LGPL-3.0). Usage: dynamically linked via FFI. Isolation: separate process boundary. Copyleft trigger: No — dynamic linking with LGPL does not require proprietary source disclosure. Risk: Low."
- Bad: "We use some GPL libraries but it should be fine"
- Format: Per-component analysis with usage pattern, linking type, isolation boundary, copyleft trigger assessment, and risk rating]

## Compliance Checklist

[Verification of licence obligation fulfillment.

GUIDANCE:
- Good: Table with Obligation Type, Component(s), Requirement, Status (Complete/Incomplete), Remediation Action
- Bad: "We include attribution"
- Format: Checklist covering attribution notices, licence text inclusion, source code availability, modification documentation]

## Recommendations

[Prioritized list of remediation actions.
GUIDANCE: Each recommendation should be:
- Specific (not "fix licensing" but "replace AGPL-3.0 dependency on libfoo with MIT-licensed alternative libbar before SaaS deployment")
- Actionable (assignable to engineering team)
- Prioritized (P1: release blocker, P2: next sprint, P3: backlog)]

## Appendices

### A. Methodology

[Scoring rubric applied per `references/scoring-rubric.md`. SBOM generated via [tool]. Licence identification via SPDX licence list. Copyleft analysis per FSF licence compatibility guidelines.]

### B. Supporting Data

[Full SBOM in SPDX/CycloneDX format, licence text archive, copyleft legal analysis memos, component replacement candidates.]
