# Framework: phase-scope-adjuster-eng

Defines the methodology for assessing scope gaps, generating adjustment options, and reaching stakeholder alignment when a phase is at risk.

## Scope Gap Assessment

### Step 1: Quantify the Gap

Before any adjustment conversation, calculate the scope gap with data:

| Metric | How to Measure |
|--------|---------------|
| Remaining work (points) | Sum of incomplete and not-started tasks in the phase |
| Remaining capacity (points) | Team velocity × remaining sprint days ÷ avg sprint days |
| Gap | Remaining work − Remaining capacity |
| Gap percentage | (Gap ÷ Remaining work) × 100% |

**Trigger thresholds for scope conversation**:
- Gap ≥ 20% of committed scope → initiate scope review
- Gap ≥ 40% of committed scope → immediate stakeholder alignment required
- Gap > 60% → phase must be restructured

### Step 2: Identify Gap Causes

| Root Cause | Signal | Typical Resolution |
|------------|-------|--------------------|
| Estimation error | Consistently higher actuals than estimates | Reduce commitment; recalibrate story points for this task type |
| Scope creep | Tasks added after phase start not reflected in capacity | Remove unauthorized additions or formally expand capacity |
| External blocker | Task blocked by dependency; not progressing | Dependency resolution or task resequence |
| Technical discovery | Unforeseen complexity found during implementation | Cut to MVP subset or extend timeline |
| Capacity reduction | Team member unavailable (illness, PTO, attrition) | Reduce commitment proportionally |

## Adjustment Options Model

Generate at least two options before deciding. Avoid presenting a single "plan" to stakeholders — options preserve negotiation space.

### Option A: Scope Cut
Remove lower-priority items from the phase entirely. Suitable when items are independent and deferrable without breaking downstream phases.

**Template**:
> Cut items [IDs] from Phase N scope. These items will move to Phase N+1 backlog. Impact: [downstream dependency assessment]. No timeline change required.

### Option B: Feature Depth Reduction (MVP Subset)
Deliver a reduced version of in-scope features (e.g., happy path only, single segment, no edge cases). Suitable when the item is high-priority but over-estimated.

**Template**:
> Deliver [Feature X] at MVP depth: [specific scope reduction]. Full implementation deferred to Phase N+1. Impact: [user experience gap and mitigation].

### Option C: Timeline Extension
Add calendar days to the phase. Suitable only when: (a) downstream phases have slack, AND (b) the reason for the gap is a genuine technical blocker, not estimation error.

**Template**:
> Extend Phase N by [N days] to [new end date]. Downstream impact: Phase N+1 start shifts by [N days]. Approval required from: [stakeholder names].

### Option D: Capacity Addition
Add engineering resource (contractor, borrowed engineer, or overtime). Suitable for short-term gaps when timeline is fixed and scope is non-negotiable.

**Template**:
> Add [N] engineer-days of capacity via [contractor / internal transfer]. Cost: [estimated]. Risk: onboarding overhead reduces effective days by ~30%.

## Tradeoff Matrix

Present options in a tradeoff table to facilitate stakeholder decision-making:

| Option | Timeline Impact | Scope Impact | Quality Impact | Cost | Stakeholder Buy-In Required |
|--------|----------------|-------------|--------------|------|----------------------------|
| A: Scope Cut | None | Deferred items | None (if cuts are non-critical) | None | Product + Engineering |
| B: MVP Subset | None | Reduced depth | Minor (known gaps) | None | Product |
| C: Timeline Extension | +N days | None | None | Opportunity cost | Engineering Leadership |
| D: Capacity Addition | None | None | Risk of context-switching | $X | VP Engineering |

## Stakeholder Communication Template

> "Phase [N] has a [X]-point gap against [N] remaining days of capacity. Without adjustment, [N items] will not complete by [date]. I've analyzed three options: [A], [B], [C]. I recommend [Option X] because [rationale]. I need a decision by [date] so we can update sprint planning before [event]."

## Quality Protection Rules

These items may NEVER be cut to close a scope gap:
- Security controls or vulnerability fixes
- Automated test coverage for new code paths
- Observability (logging, metrics) for new services
- Rollback procedures for production deployments

If the only path to closing the gap requires cutting any of the above, escalate immediately — do not present it as an option.
