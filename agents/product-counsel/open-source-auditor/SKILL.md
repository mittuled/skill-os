---
name: open-source-auditor
description: >
  This skill audits the use of open-source software for licence compliance and legal
  risk. Use when asked to review open-source dependencies, assess licence compatibility,
  or evaluate copyleft exposure. Also consider when the product includes new third-party
  libraries. Suggest when the user is adding open-source dependencies without licence
  review.
department: legal
agent: product-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../product-legal-reviewer/SKILL.md
  - ../../security-compliance-programme-manager/compliance-framework-implementer/SKILL.md
---

# open-source-auditor

## Agent: Product Counsel

L2 product counsel (1x) responsible for legal review of business models, positioning, pricing, product compliance, and security audit oversight.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)

## Skill Description

Audits the use of open-source software across the product by reviewing licence compliance, assessing copyleft exposure, and ensuring open-source obligations are met before release.

## When to Use

- When preparing for a product release and needing to verify that all open-source dependencies are licence-compliant.
- When a developer proposes adding a new open-source library with an unfamiliar or restrictive licence.
- When the company is undergoing due diligence and investors or acquirers request an open-source audit.

## Workflow

1. **Dependency Inventory**: Generate a complete bill of materials for all open-source dependencies including transitive dependencies. Record the licence type, version, and source for each component. Deliverable: software bill of materials (SBOM).
2. **Licence Classification**: Classify each licence by type (permissive, weak copyleft, strong copyleft, proprietary) and compatibility with the company's distribution model. Flag incompatible or ambiguous licences. Deliverable: licence classification matrix.
3. **Copyleft Exposure Analysis**: For copyleft-licensed components (GPL, AGPL, LGPL), analyse whether the usage pattern triggers copyleft obligations (static linking, dynamic linking, network interaction). Assess whether the company's proprietary code is at risk of forced disclosure. Deliverable: copyleft exposure analysis.
4. **Compliance Verification**: Verify that all licence obligations are met: attribution notices, licence text inclusion, source code availability (where required), and modification documentation. Deliverable: compliance checklist with remediation items.

## Anti-Patterns

- **Ignoring transitive dependencies**: Auditing only direct dependencies without examining the full dependency tree. *Why*: copyleft licences in transitive dependencies carry the same obligations as direct dependencies; a single GPL component deep in the tree can affect the entire distribution.
- **Licence check at release only**: Reviewing open-source licences only before release rather than at the point of adoption. *Why*: discovering a licence conflict at release time forces expensive rework; catching it at adoption prevents wasted effort.
- **Permissive means no obligation**: Treating permissive licences (MIT, Apache) as obligation-free. *Why*: even permissive licences require attribution and licence text inclusion; failing to comply creates licence breach even with the most permissive terms.

## Output

**On success**: Produces an SBOM, licence classification matrix, copyleft exposure analysis, and compliance checklist. Delivered before each product release with incremental reviews at dependency addition.

**On failure**: Report which dependencies could not be classified (missing licence files, dual-licensed ambiguity), what copyleft exposure was identified, and recommended actions (replace component, obtain commercial licence, or accept risk with documentation).

## Related Skills

- [`product-legal-reviewer`](../product-legal-reviewer/SKILL.md) -- Open-source audit findings feed into the broader product legal review.
- [`compliance-framework-implementer`](../../security-compliance-programme-manager/compliance-framework-implementer/SKILL.md) -- Compliance frameworks may require open-source audit as part of software supply chain controls.
