---
name: risk-register-builder
description: >
  This skill builds and maintains a product risk register that identifies, categorises, and scores
  delivery, market, and technical risks for an initiative or release. Use when asked to assess
  risks before committing to a roadmap slot, sprint plan, or go-live decision. Also consider when
  a project has changed scope significantly and existing risk assumptions may be stale.
  Suggest when the user is about to approve a launch or major milestone without a documented risk
  assessment.
department: product
agent: product-manager
version: 1.0.0
complexity: complex
related-skills: []
---

# risk-register-builder

## Agent: Product Manager
L2 product manager (multi-instance) responsible for customer discovery, requirements extraction, sprint planning, backlog management, and go-live approval. Bridges customer needs and engineering delivery.

Department ethos: [ideal-product.md](../../../departments/product/ideal-product.md)

## Skill Description
Builds and maintains the product risk register, identifying delivery, market, and technical risks with likelihood and impact scores, mitigation plans, and ownership assignments.

## When to Use
- When a new initiative is entering the roadmap and needs a formal risk assessment before resources are committed
- When an in-flight project encounters scope changes, dependency shifts, or team changes that invalidate prior risk assumptions
- When preparing for a go/no-go decision on launch and stakeholders need a consolidated view of outstanding risks and their mitigations
- When a post-mortem reveals risks that were known but undocumented, signalling that the risk capture process has gaps

## Workflow
1. **Define risk scope**: Establish the boundaries of the assessment — which initiative, release, or milestone is covered. Identify the decision the register will inform (roadmap placement, sprint commitment, go-live approval). Deliverable: one-paragraph scope statement naming the initiative, time horizon, and decision context.
2. **Identify risk candidates**: Conduct a structured risk brainstorm across four categories — delivery (schedule, staffing, dependencies), technical (architecture, scalability, integration), market (competition, timing, adoption), and compliance (regulatory, data privacy, contractual). Source risks from engineering estimates, discovery findings, competitive intel, and past post-mortems. Deliverable: flat list of candidate risks with source attribution.
3. **Score likelihood and impact**: Rate each risk on a 3-point scale for likelihood (low/medium/high) and impact (low/medium/high). Compute a composite risk score (likelihood x impact mapped to a 1-9 grid). Sort by composite score descending. Deliverable: scored risk table with columns for ID, category, description, likelihood, impact, composite score, and source.
4. **Assign ownership and mitigation**: For each medium- and high-severity risk, define a mitigation strategy (avoid, reduce, transfer, or accept) and assign a named owner responsible for executing it. Set a review-by date. For low-severity risks, document the accept rationale. Deliverable: mitigation plan appended to each risk row — strategy, owner, action items, and review date.
5. **Identify risk dependencies and cascades**: Map which risks compound each other — e.g., a staffing risk that amplifies a schedule risk. Flag cascade chains where one risk materialising triggers downstream risks. Deliverable: dependency notes on linked risk rows, with cascade chains highlighted.
6. **Define trigger thresholds**: For each high-severity risk, define a leading indicator that signals the risk is materialising — e.g., "if API latency exceeds 500ms in staging, the scalability risk has triggered." Specify the escalation path when a trigger fires. Deliverable: trigger column added to the risk table with indicator, threshold, and escalation action.
7. **Validate with cross-functional leads**: Review the full register with engineering, design, and business stakeholders. Confirm scoring accuracy, mitigation feasibility, and ownership assignments. Capture dissenting opinions as register annotations. Deliverable: sign-off record or revision log with dissent notes.
8. **Establish review cadence**: Set a recurring review schedule tied to the initiative's rhythm — per-sprint for active delivery, monthly for roadmap-level risks. Define the update process: who reviews, what triggers an ad-hoc re-score, and where the living register is stored. Deliverable: review schedule and process note appended to the register header.

## Anti-Patterns
- **Risk theatre**: Creating a register once to satisfy a process gate, then never updating it. *Why*: A stale register is worse than none — it creates false confidence that risks are managed while actual conditions drift unchecked.
- **Uniform scoring**: Rating all risks as "medium/medium" to avoid difficult prioritisation conversations. *Why*: Flat scoring eliminates the signal the register exists to provide — it prevents the team from focusing mitigation effort where it matters most.
- **Mitigation without ownership**: Documenting a mitigation strategy like "monitor closely" without a named owner or concrete action. *Why*: Unowned mitigations are indistinguishable from wishes — no one is accountable, so the mitigation never executes.
- **Ignoring cascade effects**: Treating each risk as independent when several share root causes or amplify each other. *Why*: Cascade-blind registers undercount total exposure and produce mitigation plans that address symptoms while the shared root cause persists.
- **Excluding non-technical risks**: Limiting the register to engineering and infrastructure risks while ignoring market timing, regulatory, or adoption risks. *Why*: Product failures are more often caused by market and business risks than by technical ones — an incomplete register misallocates mitigation effort.

## Output
**On success**: A living risk register document containing scored risks across delivery, technical, market, and compliance categories, each with mitigation strategy, owner, trigger thresholds, and review cadence — formatted as a markdown table with a header section summarising scope, total risk count, and high-severity count. Suitable for embedding in a PRD, attaching to a go/no-go decision brief, or maintaining as a standalone artefact linked from the initiative tracker.

**On failure**: Report which risk categories could not be assessed (missing engineering estimates, unavailable competitive data, absent compliance guidance), which stakeholders did not participate in validation, and recommend specific information-gathering actions to complete the register. Flag any high-severity risks that were identified but lack feasible mitigation — these require immediate escalation regardless of register completeness.

## Related Skills
- (none yet — cross-references added in Phase 1.6)
