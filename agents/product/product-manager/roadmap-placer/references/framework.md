# Framework: Roadmap Placement

## Core Model

Capacity-aware placement of initiatives onto a time-based roadmap using weighted scoring against strategic alignment, dependency risk, and team capacity.

## Placement Evaluation Criteria

| Criterion | Weight | Scoring (1-5) |
|-----------|--------|---------------|
| Strategic alignment | 30% | 5 = directly advances top company goal; 1 = tangential |
| Dependency risk | 25% | 5 = no dependencies; 1 = blocked by 3+ teams |
| Capacity fit | 25% | 5 = team has open capacity; 1 = requires displacement |
| Stakeholder commitment | 20% | 5 = contractual deadline; 1 = internal wish |

**Placement Score** = Σ (criterion score x weight)

## Slot Option Template

| Option | Quarter | Displaced Initiative | Dependency Status | Placement Score | Risk |
|--------|---------|---------------------|-------------------|----------------|------|
| A | Q2 2026 | None | All dependencies resolved | 4.2 | Low |
| B | Q3 2026 | Initiative X (shifts to Q4) | 1 dependency pending | 3.5 | Medium |
| C | Q2 2026 | Initiative Y (cancelled) | All resolved | 3.8 | High (stakeholder impact) |

## Roadmap Entry Format

Each roadmap entry must contain:
1. **Initiative name** and link to initiative brief
2. **Assigned slot** (quarter or sprint range)
3. **Placement rationale** (why this slot, not just which slot)
4. **Dependencies** with status and owner
5. **Effort estimate** and team allocation
6. **Review date** for re-evaluation

## Sequencing Rules

1. Hard deadlines (contractual, regulatory, event-driven) are placed first
2. Dependencies determine ordering within a quarter (prerequisites before dependents)
3. Capacity determines density (never exceed 85% utilisation per team per quarter)
4. Strategic alignment breaks ties when two initiatives compete for the same slot

## Communication Protocol

| Audience | What They Need | When |
|----------|---------------|------|
| Affected engineering teams | Capacity implications, dependency timelines | Within 24 hours of decision |
| Stakeholders with displaced initiatives | Change rationale, new timeline | Within 24 hours of decision |
| Leadership | Updated roadmap view with change summary | Weekly roadmap sync |
