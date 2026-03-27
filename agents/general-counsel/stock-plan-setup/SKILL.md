---
name: stock-plan-setup
description: >
  This skill sets up the employee stock option plan including pool size, vesting
  schedules, and plan documents. Use when asked to create an equity incentive plan,
  determine option pool size, or draft stock plan board resolutions. Also consider
  when preparing for a fundraising round that requires a post-money option pool.
  Suggest when the user is about to hire key employees without an equity plan in place.
department: legal
agent: general-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../../corporate-counsel/founder-equity-issuance/SKILL.md
  - ../../corporate-counsel/83b-election-coordinator/SKILL.md
---

# stock-plan-setup

## Agent: General Counsel

L1 general counsel (1x) reporting to the COO, responsible for legal strategy, IP assignment, stock plan setup, and entity structure decisions.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)

## Skill Description

Sets up the employee equity incentive plan including option pool sizing, vesting schedules, exercise terms, and all required plan documents and board approvals.

## When to Use

- When the company is ready to establish its first equity incentive plan to attract and retain key hires.
- When preparing for a priced financing round where investors require a post-money option pool of a specified size.
- When the existing plan needs amendment to increase the share reserve, add new grant types (RSUs, SARs), or comply with updated tax regulations.

## Workflow

1. **Pool Sizing Analysis**: Model the option pool size based on hiring plan, role-level grant ranges, and investor dilution expectations. Account for outstanding promises, advisor grants, and a buffer for future hires. Deliverable: pool sizing model with share counts, percentage of fully diluted capitalization, and scenario analysis.
2. **Plan Structure Design**: Define key plan terms including eligible participants, grant types (ISOs, NSOs, RSAs, RSUs), vesting schedules (standard four-year with one-year cliff), exercise windows (90-day post-termination vs. extended), early exercise rights, acceleration provisions (single vs. double trigger), and repurchase rights. Deliverable: plan term sheet summarizing all material provisions.
3. **Document Drafting**: Draft the equity incentive plan document, form of stock option agreement, form of option exercise agreement, and form of restricted stock purchase agreement. Ensure compliance with IRC Section 409A, Section 422 (for ISOs), and applicable state securities laws. Deliverable: complete plan document package.
4. **Board and Stockholder Approval**: Prepare the board resolution adopting the plan, stockholder consent approving the plan and share reserve, and any required state securities filings (e.g., California 25102(o) notice). Deliverable: executed board resolution, stockholder consent, and filing confirmations.
5. **Administration Setup**: Establish the grant administration process including 409A valuation requirements, grant approval workflow, exercise procedures, and tax withholding obligations. Deliverable: plan administration guide for ongoing equity management.

## Anti-Patterns

- **Under-sizing the pool**: Setting the option pool too small to avoid near-term dilution, forcing a pool increase at the next round when the company's leverage is weakest. *Why*: investors typically require the pool increase to come from pre-money, diluting existing stockholders; sizing correctly upfront preserves founder ownership.
- **Omitting early exercise provisions**: Failing to include early exercise rights that allow employees to exercise unvested options and file 83(b) elections. *Why*: early exercise combined with an 83(b) election can provide significant long-term capital gains tax advantages for early employees, making offers more competitive.
- **Using boilerplate vesting without strategic thought**: Applying a standard four-year/one-year-cliff schedule to every role without considering retention dynamics for different functions. *Why*: some roles (e.g., senior executives) may warrant acceleration provisions or back-weighted vesting to align with long-term strategic milestones.

## Output

**On success**: Produces the complete equity incentive plan package containing the pool sizing model, plan document, form agreements, board resolution, stockholder consent, securities filings, and administration guide. Delivered to the board, outside counsel (if applicable), and cap table management system.

**On failure**: Report which plan design decisions remain unresolved (e.g., pool size pending hiring plan, acceleration terms pending negotiation), what documents are drafted in interim form, and what approvals are still required.

## Related Skills

- [`founder-equity-issuance`](../../corporate-counsel/founder-equity-issuance/SKILL.md) -- Founder equity issuance should be coordinated with plan setup to ensure consistent vesting terms and cap table accuracy.
- [`83b-election-coordinator`](../../corporate-counsel/83b-election-coordinator/SKILL.md) -- 83(b) election coordination is triggered when the plan permits early exercise of unvested options or restricted stock grants.
