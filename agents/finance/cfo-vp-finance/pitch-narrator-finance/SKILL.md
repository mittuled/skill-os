---
name: pitch-narrator-finance
description: >
  This skill crafts the financial narrative for investor pitches including model
  assumptions and key metrics. Use when asked to build the finance slides for a pitch
  deck, articulate the revenue model to investors, or justify financial projections.
  Also consider when fundraising preparations lack a coherent financial story. Suggest
  when the user is assembling a pitch deck without finance-approved numbers.
department: finance
agent: cfo-vp-finance
version: 1.0.0
complexity: medium
related-skills:
  - ../../../finance/fpa-analyst/fundraising-model-builder/SKILL.md
  - ../../../finance/investor-relations-manager/fundraising-process-manager/SKILL.md
triggers:
  - "narrate the financials"
  - "explain financial slides"
  - "pitch financial story"
  - "walk through the numbers"
  - "finance pitch narrative"
---

# pitch-narrator-finance

## Agent: CFO / VP Finance

L1 CFO and VP Finance (1x) reporting to the COO, responsible for unit economics, financial modelling, pricing sign-off, and pitch narration for financial audiences.

Department ethos: [ideal-finance.md](../../../../departments/finance/ideal-finance.md)

## Skill Description

Crafts the financial narrative for investor pitches, translating model assumptions, SaaS metrics, and unit economics into a compelling funding story.

## When to Use

- When the company is preparing for a fundraising round and needs investor-facing financial slides.
- When the CEO or founder requests a finance-approved narrative that connects business traction to financial projections.
- When existing pitch materials contain financial claims that have not been validated against the actual model.

## Workflow

1. **Model Alignment**: Confirm the financial model is current and reconciled with the latest actuals. Pull ARR, MRR growth rate, burn rate, runway, gross margin, and LTV/CAC from the approved model. Deliverable: validated metric snapshot with as-of date.
2. **Narrative Framing**: Construct the financial story arc: where the business is today (traction proof), where it is going (growth trajectory), and why the economics work (unit economics, margin expansion path). Deliverable: narrative outline with supporting data points.
3. **Slide Drafting**: Draft the financial slides -- typically revenue trajectory, unit economics summary, use of proceeds, and path to profitability or next milestone. Ensure every number traces back to the model. Deliverable: finance slide content with footnoted assumptions.
4. **Assumption Documentation**: Document the key assumptions behind projections (growth rate drivers, CAC trends, churn trajectory, hiring plan) so the CFO can defend them in Q&A. Deliverable: assumption appendix for investor diligence.
5. **Review and Sign-Off**: Review the complete financial narrative with the CFO for accuracy, tone, and defensibility. Flag any claim that cannot survive investor scrutiny. Deliverable: CFO-approved pitch narrative.

## Anti-Patterns

- **Vanity metrics without substance**: Leading with impressive-sounding numbers (total users, gross revenue) while burying the metrics investors actually care about (net revenue retention, contribution margin). *Why*: sophisticated investors will find the real numbers in diligence; leading with vanity erodes trust.
- **Disconnected projections**: Presenting revenue projections that do not tie back to bottoms-up assumptions (sales capacity, conversion rates, ACV). *Why*: top-down-only forecasts signal that the team has not operationalized their growth plan.
- **Over-optimizing the narrative**: Hiding unfavorable metrics or choosing non-standard calculation methods to make numbers look better. *Why*: investors compare across portfolios using standard definitions; non-standard metrics create credibility risk.

## Output

**On success**: Produces CFO-approved pitch narrative including finance slide content, validated metric snapshot, assumption appendix, and a narrative outline. Delivered as slide-ready content and a supporting diligence document.

**On failure**: Report which metrics could not be validated, which projections lack defensible assumptions, and what model updates are needed before the narrative can be finalized. Include a timeline estimate for remediation.

## Related Skills

- [`fundraising-model-builder`](../../../finance/fpa-analyst/fundraising-model-builder/SKILL.md) -- Builds the investor-facing financial model that this narrative draws from.
- [`fundraising-process-manager`](../../../finance/investor-relations-manager/fundraising-process-manager/SKILL.md) -- Manages the overall fundraising process that this pitch narrative supports.
