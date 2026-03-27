---
name: founder-equity-issuance
description: >
  This skill manages issuance of founder equity including restricted stock
  agreements and vesting schedules. Use when asked to issue founder shares,
  draft stock purchase agreements, or set up vesting. Also consider when a new
  co-founder joins or equity splits are being negotiated. Suggest when the user
  is forming an entity without addressing founder equity.
department: legal
agent: corporate-counsel
version: 1.0.0
complexity: medium
related-skills:
  - ../83b-election-coordinator/SKILL.md
  - ../entity-formation/SKILL.md
---

# founder-equity-issuance

## Agent: Corporate Counsel

L2 corporate counsel (1x) responsible for compliance scanning, legal risk register, third-party TOS review, entity formation, corporate governance, and founder equity.

Department ethos: [ideal-legal.md](../../../departments/legal/ideal-legal.md)

## Skill Description

Manages the issuance of founder equity including drafting restricted stock purchase agreements, establishing vesting schedules, and ensuring proper board authorization and securities compliance.

## When to Use

- When co-founders have agreed on equity splits and need the legal documents to formalize share issuance.
- When a new co-founder or key early hire is joining and needs to receive founding-level equity with vesting.
- When the company needs to restructure founder equity before a fundraising round (e.g., adding reverse vesting to unvested founder shares).

## Workflow

1. **Equity Structure Design**: Confirm the number of shares, share class, par value, vesting schedule (standard 4-year with 1-year cliff), acceleration provisions, and repurchase rights. Deliverable: founder equity term sheet.
2. **Board Authorization**: Prepare board resolutions authorizing the issuance of shares to each founder at the specified price and terms. Ensure the issuance falls within authorized share limits. Deliverable: board consent resolution.
3. **Agreement Drafting**: Draft the Restricted Stock Purchase Agreement (RSPA) for each founder covering purchase price, vesting schedule, repurchase rights, transfer restrictions, and representations. Deliverable: executed RSPAs. [GATE]
4. **Securities Compliance**: Verify the issuance qualifies for a securities exemption (typically Rule 701 or Section 4(a)(2)). Prepare any required state blue sky filings. File Form D if needed. Deliverable: securities exemption memo and filings.
5. **83(b) Election Coordination**: Notify each founder of the 83(b) election option and coordinate filing within the 30-day deadline. Hand off to the 83b-election-coordinator for tracking. Deliverable: 83(b) election notification and handoff confirmation.

## Anti-Patterns

- **Issuing equity without vesting**: Giving founders fully vested shares with no repurchase rights. *Why*: if a founder leaves early, the remaining founders have no mechanism to recover unvested equity, which damages the cap table and deters investors.
- **Verbal equity promises**: Agreeing on equity splits verbally without executing stock purchase agreements. *Why*: verbal agreements are unenforceable for equity transfers and create disputes that can destroy the company.
- **Ignoring securities law**: Issuing shares without confirming a securities exemption. *Why*: unregistered securities offerings violate federal and state law, creating rescission rights and personal liability for officers.

## Output

**On success**: Produces executed RSPAs for each founder, board authorization resolutions, securities exemption documentation, and 83(b) election handoff. Delivered to founders with copies in the corporate minute book.

**On failure**: Report which issuances could not be completed (e.g., unresolved equity split, missing board authorization, securities exemption uncertainty), what the current equity status is, and what decisions or filings are needed. Escalate to General Counsel.

## Related Skills

- [`83b-election-coordinator`](../83b-election-coordinator/SKILL.md) -- 83(b) elections must be filed within 30 days of restricted stock issuance.
- [`entity-formation`](../entity-formation/SKILL.md) -- The entity must be formed before shares can be legally issued.
