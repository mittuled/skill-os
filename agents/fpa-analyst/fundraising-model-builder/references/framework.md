# Framework: fundraising-model-builder

Defines the structural framework for building investor-grade fundraising financial models including projections, use of proceeds, dilution analysis, and scenario modelling.

## Model Architecture

### Workbook Structure

A fundraising model should be organized into discrete tabs:

| Tab | Purpose | Audience |
|-----|---------|---------|
| Cover | Model summary, version, disclaimers | All |
| Assumptions | All input drivers in one place, color-coded | Internal + Investor |
| Revenue | Bottoms-up ARR/MRR build from sales capacity and NRR | All |
| P&L | Full income statement, monthly Year 1, quarterly/annual Years 2-3+ | All |
| Cash Flow | Monthly cash position and burn | All |
| Use of Proceeds | Capital deployment schedule tied to milestones | All |
| Cap Table | Pre- and post-round ownership with SAFE/note conversions | Internal + Lead Investor |
| Dilution Scenarios | Multiple raise amounts and valuations | Internal |
| Scenarios | Base / Upside / Conservative model toggle | All |
| Sensitivity | Variable impact on valuation-relevant KPIs | All |

### Color Coding Standard

- **Blue fill**: Hard-coded inputs (change intentionally)
- **Black, no fill**: Formulas (do not edit)
- **Green fill**: Scenario-controlled inputs (driven by scenario selector)
- **Yellow fill**: External reference data (market research, benchmark)

## Revenue Projection Standards

### Bottoms-Up Revenue Build

Revenue must trace from operational drivers, not top-line growth rates:

```
New ARR = (Sales capacity × quota × attainment assumption) + (inbound leads × conversion rate × ACV)
Expansion ARR = Beginning ARR × NRR expansion component
Churned ARR = Beginning ARR × gross churn rate
Ending ARR = Beginning ARR + New ARR + Expansion ARR - Churned ARR
```

### Attainment Ramp Model

New sales hires require ramp time before full productivity:

| Hire Month | Month 1-3 | Month 4-6 | Month 7-12 | Month 13+ |
|-----------|-----------|-----------|-----------|-----------|
| AE Attainment | 0% | 33% | 66% | 100% |
| SDR Attainment | 25% | 50% | 75% | 100% |

Apply ramp to new hires only; assume existing quota-carrying reps at full attainment unless there is evidence otherwise.

### NRR Decomposition

NRR must be decomposed, not a single assumption:

```
NRR = 100% + expansion rate - contraction rate - gross churn rate
```

Show each component separately with trailing 6-month actuals as anchors.

## Use of Proceeds Framework

### Deployment Categories

| Category | Typical % of Round | Milestone Tied To |
|---------|-------------------|-------------------|
| Sales & Marketing headcount | 30–45% | ARR growth target at next raise |
| Product & Engineering headcount | 25–35% | Product milestone (feature launch, platform scalability) |
| Customer Success headcount | 10–15% | NRR and expansion targets |
| R&D and infrastructure | 5–10% | Technical capability or compliance milestone |
| G&A and operations | 5–10% | Supporting organizational scale |

### Milestone Mapping Rule

Every dollar allocated must map to at least one specific milestone. Generic allocations like "general working capital" signal poor planning to investors.

Format:
```
Category | $ Amount | FTEs | Start Quarter | Milestone | KPI Impact
```

## Dilution Analysis Framework

### SAFE Conversion Mechanics

For post-money YC SAFEs:
```
SAFE shares = SAFE investment amount / conversion price
Conversion price = MIN(valuation cap / (post-money shares + all SAFEs + new option pool), 
                       next round price × (1 - discount rate))
```

Model each SAFE separately. Stack them in chronological order. Show total SAFE dilution before the new round.

### Cap Table Scenarios

Build three scenarios:

| Scenario | Pre-Money | Raise Amount | Option Pool Top-Up | Lead Investor % |
|---------|-----------|-------------|-------------------|-----------------|
| Conservative | -15% vs. target | -20% | Minimum viable | 20% |
| Base | Target valuation | Target raise | Standard (10-15% post-money) | 20-25% |
| Aggressive | +20% vs. target | +20% | Full new pool | 20% |

Show post-money ownership table for founders, employees (pool), existing investors, new investors, and SAFEs for each scenario.

### Waterfall Analysis

For each scenario, show the liquidation preference distribution at exit multiples of 0.5x, 1x, 2x, 3x, 5x, and 10x. This reveals whether the preference stack creates a material overhang that reduces common stockholder returns.

## Scenario Matrix Standards

### Base Case Calibration

The base case must:
- Be achievable with 70% probability given current trajectory
- Show a path to raising the next round at a higher valuation (typically 2-3x ARR multiple expansion)
- Achieve the milestones in the Use of Proceeds within the runway period

### Conservative Case Calibration

The conservative case must:
- Reflect a scenario the company would survive (runway does not reach zero)
- Show a path to either default alive or a bridge raise
- Use 70-80% of base case revenue with 90-95% of base case costs

### Investor Presentation Rules

Only share the base and upside scenarios with investors. Internal models include the downside. Never present a model where the downside case runs out of cash — this undermines negotiating position.
