---
name: sales-signal-synthesizer-am
description: >
  This skill synthesises account signals to identify expansion, risk, and relationship health trends
  across the portfolio. Use when asked to analyse account health trends, build portfolio risk reports,
  or identify systemic patterns. Also consider when churn increases without explanation.
  Suggest when quarterly portfolio reviews need a data-driven foundation.
department: account-management
agent: account-management-lead
version: 1.0.0
complexity: medium
related-skills: []
---

# sales-signal-synthesizer-am

## Agent: Account Management Lead

L1 account management leader (1x) reporting to the CBO, responsible for account management strategy, opportunity framing, and sales playbook for existing accounts.

Department ethos: [ideal-account-management.md](../../../departments/account-management/ideal-account-management.md)

## Skill Description

The sales signal synthesiser aggregates signals collected from individual account interactions, usage data, and support tickets to identify portfolio-level trends in expansion opportunity, churn risk, and relationship health.

## When to Use

- When the quarterly portfolio review needs a synthesised view of account health across all accounts.
- When churn rate increases and the team needs to understand whether it is systemic or account-specific.
- When leadership needs a pipeline forecast for expansion revenue from the existing customer base.
- When account managers submit signals that need to be aggregated into actionable portfolio insights.

## Workflow

1. **Collect signals**: Aggregate signals from account manager reports, CRM data, usage analytics, support tickets, and NPS scores. Deliverable: consolidated signal dataset.
2. **Classify signals**: Tag each signal as expansion opportunity, churn risk, relationship health indicator, or competitive threat. Deliverable: classified signal inventory.
3. **Identify patterns**: Analyse signals for portfolio-level trends: segments at risk, common expansion triggers, recurring complaints. Deliverable: pattern analysis report.
4. **Prioritise actions**: Rank portfolio-level actions by revenue impact and urgency. Deliverable: prioritised action list.
5. **Brief stakeholders**: Present the synthesis to AM leadership and cross-functional partners (product, CS) with specific recommendations. Deliverable: portfolio signal synthesis briefing.

## Anti-Patterns

- **Synthesising without standardised signal collection**: Aggregating signals when account managers use inconsistent formats and definitions. *Why*: inconsistent inputs produce unreliable synthesis; standardise collection before aggregation.
- **Ignoring weak signals**: Focusing only on strong positive or negative signals and dismissing ambiguous ones. *Why*: weak signals often precede major shifts; early detection of churn risk or expansion opportunity depends on catching subtle patterns.
- **Synthesis without cross-functional distribution**: Keeping portfolio insights within account management. *Why*: product needs churn-risk signals to prioritise fixes; CS needs health trends to adjust engagement; siloed synthesis limits impact.

## Output

**On success**: A portfolio signal synthesis report with classified signals, identified trends, prioritised actions, and cross-functional recommendations, distributed to AM leadership, product, and CS.

**On failure**: Report which signal sources were unavailable or inconsistent (e.g., AMs not submitting signals, usage data gaps), what partial synthesis was produced, and recommend improvements to signal collection.

## Related Skills

- [`sales-signal-collector-am`](../../account-manager/sales-signal-collector-am/SKILL.md) -- signal collection provides the raw data that this skill synthesises.
- [`opportunity-framer-am`](../opportunity-framer-am/SKILL.md) -- framing uses synthesised signals to identify which accounts have expansion potential.
