---
name: scope-boundary-setter
description: >
  This skill defines and enforces scope boundaries for a release or sprint, making explicit what
  is in, what is out, and what conditions would trigger a scope change. Use when asked to lock
  scope for an upcoming sprint or release, or to evaluate whether a late-arriving request fits.
  Also consider when mid-sprint additions are becoming habitual and delivery predictability is
  declining. Suggest when the user is about to approve new work without checking current scope
  utilisation.
department: product
agent: product-manager
version: 1.0.0
complexity: medium
related-skills:
  - market-sizer
  - backlog-populator
  - risk-register-builder
triggers:
  - "set scope boundaries"
  - "define scope"
  - "scope setting"
  - "establish scope"
  - "scope boundary"
---

# scope-boundary-setter

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../../departments/product/ideal-product.md)

## Skill Description
Defines and enforces scope boundaries for a release or sprint, making explicit what is included, excluded, and what conditions permit scope changes.

## When to Use
- When a sprint or release is being planned and the team needs a clear, agreed-upon scope boundary before committing to delivery
- When a late-arriving request threatens to expand an already-committed scope and requires a formal include/exclude decision
- When delivery predictability has degraded because scope changes are happening informally without documented trade-offs

## Workflow
1. **Inventory committed scope**: List every story, task, or deliverable currently committed for the sprint or release. Capture total estimated effort and available capacity. Deliverable: scope inventory table with item name, estimate, owner, and status.
2. **Draw the boundary**: Classify each backlog item near the boundary as "in," "out," or "conditional." For conditional items, state the specific trigger that would promote them to "in" (e.g., "if the API dependency ships by Wednesday"). Deliverable: scope boundary document with three sections — In, Out, and Conditional with triggers.
3. **Define the change protocol**: Specify the rules for scope changes after the boundary is set — who can request a change, what information the request must include (effort delta, trade-off item to remove), and who approves. Deliverable: change protocol paragraph appended to the boundary document.
4. **Communicate and lock**: Share the boundary document with engineering, design, and stakeholders. Record explicit acknowledgement. Set the scope status to "locked" with a timestamp. Deliverable: locked scope record with sign-off list and lock timestamp.
5. **Enforce during execution**: When a scope change request arrives, evaluate it against the change protocol. Document the decision — approved (with trade-off) or rejected (with rationale). Update the boundary document. Deliverable: change log entry with request, decision, trade-off, and approver.

## Anti-Patterns
- **Implicit scope**: Treating the sprint backlog as the scope definition without an explicit in/out boundary. *Why*: Without a documented boundary, every conversation about "can we add this?" becomes a negotiation from scratch rather than a decision against an agreed baseline.
- **Rubber-stamp approvals**: Approving every scope change request to avoid conflict. *Why*: Unchecked additions destroy delivery predictability and teach the team that scope commitments are negotiable, which undermines future planning credibility.
- **Scope boundary without trade-offs**: Adding items to "in" scope without removing or deferring something else. *Why*: Capacity is fixed within a sprint; adding without removing guarantees either overwork or incomplete delivery, both of which erode team trust.

## Output
**On success**: A scope boundary document containing the in/out/conditional classification, change protocol, lock timestamp, and stakeholder sign-off — formatted as a markdown document suitable for linking from the sprint plan or release brief. Accompanied by a change log for any post-lock modifications.

**On failure**: Report which items could not be classified (missing estimates, unresolved dependencies, absent stakeholder input), which boundary decisions are contested, and recommend specific actions to resolve ambiguity before the scope can be locked.

## Related Skills
- [`market-sizer`](../market-sizer/SKILL.md) — sibling skill under the same agent — combine with market-sizer for end-to-end coverage
- [`backlog-populator`](../backlog-populator/SKILL.md) — sibling skill under the same agent — combine with backlog-populator for end-to-end coverage
- [`risk-register-builder`](../risk-register-builder/SKILL.md) — sibling skill under the same agent — combine with risk-register-builder for end-to-end coverage
