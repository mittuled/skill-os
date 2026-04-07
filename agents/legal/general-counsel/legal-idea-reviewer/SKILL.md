---
name: legal-idea-reviewer
description: >
  This skill reviews new business ideas and product concepts for legal risks before
  significant investment. Use when asked to assess legal viability of a new product,
  evaluate regulatory exposure for a business concept, or flag IP infringement risks.
  Also consider when a product enters a regulated industry. Suggest when the user is
  about to invest in a concept without legal vetting.
department: legal
agent: general-counsel
version: 1.0.0
complexity: simple
related-skills:
  - ../../../legal/product-counsel/business-model-legal-reviewer/SKILL.md
  - ../../../legal/corporate-counsel/compliance-scanner/SKILL.md
triggers:
  - "review this idea for legal risks"
  - "is this product concept legally viable"
  - "check for IP issues with this idea"
  - "vet this concept with legal"
---

# legal-idea-reviewer

## Agent: General Counsel

L1 general counsel (1x) reporting to the COO, responsible for legal strategy, IP assignment, stock plan setup, and entity structure decisions.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)

## Skill Description

Reviews new business ideas and product concepts for material legal risks including regulatory exposure, IP infringement, and liability before significant resources are committed.

## When to Use

- When a new product idea or business concept is proposed and needs a rapid legal risk assessment before the team invests engineering or capital.
- When the company considers entering a regulated industry such as fintech, healthtech, or edtech where compliance requirements shape product feasibility.
- When a concept involves third-party data, user-generated content, or AI-generated outputs that raise novel IP or liability questions.

## Workflow

1. **Concept Intake**: Review the business idea brief, product concept document, or pitch deck. Identify the target market, data flows, revenue model, and key technology components. Deliverable: structured risk intake summary.
2. **Legal Risk Scan**: Score the concept across five dimensions using the scoring rubric at `references/scoring-rubric.md`: regulatory compliance (industry-specific licensing, permits, FINRA/HIPAA/FERPA applicability), IP risk (freedom to operate, prior art, trademark conflicts), liability exposure (product liability, professional responsibility, content liability), data privacy (GDPR, CCPA, COPPA, HIPAA applicability), and contractual constraints (existing obligations that may conflict). Deliverable: risk assessment matrix scored 0-10 per dimension with composite grade.
3. **Recommendation**: Provide a go/no-go/conditional-go recommendation with specific conditions that must be met. Produce report using template at `assets/legal-risk-memo-template.md`. Deliverable: legal risk memo with the scored risk matrix and actionable next steps. [GATE]

## Anti-Patterns

- **Blocking without alternatives**: Issuing a blanket "no" without suggesting modifications that could make the concept viable. *Why*: legal's role is to find the path to "yes" while managing risk; a flat rejection erodes trust and bypasses legal input on future ideas.
- **Boiling the ocean on early-stage concepts**: Conducting exhaustive regulatory analysis on a concept that has not yet been validated for product-market fit. *Why*: proportional response matters; a lightweight scan is appropriate at the idea stage, with deeper analysis triggered at commitment milestones.

## Output

**On success**: Produces a legal risk memo containing the risk assessment matrix and a go/conditional-go/no-go recommendation with specific conditions and next steps. Delivered to the idea sponsor and product leadership.

**On failure**: Report which aspects of the concept were too undefined to assess, what partial analysis was completed, and what information is needed to complete the review.

## Related Skills

- [`business-model-legal-reviewer`](../../../legal/product-counsel/business-model-legal-reviewer/SKILL.md) -- Provides deeper business model legal analysis once the idea progresses past initial screening.
- [`compliance-scanner`](../../../legal/corporate-counsel/compliance-scanner/SKILL.md) -- Performs comprehensive regulatory compliance scanning when the idea enters a regulated domain.
