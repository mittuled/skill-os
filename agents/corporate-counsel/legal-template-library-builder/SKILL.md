---
name: legal-template-library-builder
description: >
  This skill builds the legal template library including NDAs, consulting
  agreements, and customer contracts. Use when asked to create contract
  templates, standardize legal documents, or build a self-serve legal library.
  Also consider when teams repeatedly request similar agreements. Suggest when
  the user is drafting one-off contracts that should be templatized.
department: legal
agent: corporate-counsel
version: 1.0.0
complexity: simple
related-skills:
  - ../third-party-tos-reviewer/SKILL.md
  - ../compliance-scanner/SKILL.md
---

# legal-template-library-builder

## Agent: Corporate Counsel

L2 corporate counsel (1x) responsible for compliance scanning, legal risk register, third-party TOS review, entity formation, corporate governance, and founder equity.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)

## Skill Description

Builds and maintains a library of standardized legal templates covering NDAs, consulting agreements, customer contracts, and other frequently used documents.

## When to Use

- When the company lacks standardized templates and teams are drafting contracts from scratch or using outdated versions.
- When a new contract type is needed repeatedly (e.g., vendor agreements, data processing addenda) and should be templatized.
- When existing templates need updating due to regulatory changes or business model evolution.

## Workflow

1. **Needs Assessment**: Identify the most frequently requested contract types and prioritize template creation by volume and risk. Deliverable: prioritized template backlog.
2. **Template Drafting**: Draft each template with company-favorable defaults, clear fill-in fields, and usage instructions. Include fallback positions for negotiable terms. Deliverable: completed templates with usage guides.
3. **Review and Approval**: Route templates through General Counsel for approval. Incorporate feedback and finalize. Deliverable: approved template library.
4. **Distribution**: Publish templates to a shared location accessible to all teams. Train stakeholders on when and how to use each template. Deliverable: published library with access documentation.

## Anti-Patterns

- **Templates without guardrails**: Publishing templates without usage instructions or deviation limits. *Why*: teams will modify protective clauses without understanding the risk, creating unreviewed legal exposure.
- **Stale templates**: Failing to update templates when laws change or the business model evolves. *Why*: outdated clauses (e.g., pre-GDPR data terms) expose the company to regulatory penalties and unenforceable provisions.

## Output

**On success**: Produces an approved template library with usage guides, published to a shared location. Delivered to all teams with training.

**On failure**: Report which templates could not be completed (e.g., requires external counsel input, regulatory uncertainty), what interim process teams should follow, and timeline for completion. Escalate to General Counsel.

## Related Skills

- [`third-party-tos-reviewer`](../third-party-tos-reviewer/SKILL.md) -- TOS review identifies clauses that should be addressed in outbound contract templates.
- [`compliance-scanner`](../compliance-scanner/SKILL.md) -- Compliance requirements inform mandatory clauses in templates.
