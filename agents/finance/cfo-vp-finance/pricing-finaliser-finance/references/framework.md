# Framework: Pricing Sign-Off

This framework guides CFO-level pricing approval decisions with margin and revenue model validation.

## The Pricing Sign-Off Decision Tree

```
Pricing proposal received
         │
         ▼
Step 1: Is the volume mix modelled?
   NO → Request volume mix assumptions before proceeding
   YES ↓
         │
         ▼
Step 2: Does gross margin meet the board-approved floor?
   Floor = [Company-specific: typically 65% for SaaS, 70%+ for pure software]
   NO → REJECTED — margin below floor
   YES ↓
         │
         ▼
Step 3: Does contribution margin (gross margin − variable S&M per customer) remain positive?
   NO → CONDITIONAL — require reduction in variable S&M or pricing increase before approval
   YES ↓
         │
         ▼
Step 4: Does the revenue forecast reconcile with current financial model ARR targets?
   Threshold: reforecast delta must be < 10% of target ARR
   >10% deviation → CONDITIONAL — requires board notification
   <10% deviation ↓
         │
         ▼
Step 5: Does the downside scenario (lower-tier adoption, higher discount utilization) still meet margins?
   NO → CONDITIONAL — add discount guardrails or minimum deal size
   YES ↓
         │
         ▼
→ APPROVED
```

## Margin Impact Analysis Framework

### Gross Margin Test

```
Gross Margin = (Revenue − COGS) / Revenue

COGS for SaaS includes:
  • Hosting / infrastructure (AWS, GCP, Azure)
  • Customer support (fully-loaded headcount)
  • Implementation services
  • Third-party licensing embedded in the product
  
Does NOT include (common errors):
  • Sales commissions (belongs in S&M)
  • Customer success (should be separated from support)
```

### Contribution Margin Test

```
Contribution Margin per Customer = 
  ACV × Gross Margin % 
  − Fully-Loaded CAC 
  − Annual Customer Success Cost per Customer

Minimum threshold: Must be > 0 at the time of first renewal
Preferred threshold: Positive by end of year 1
```

### Volume Mix Sensitivity

Model outcomes across three mix scenarios:

| Scenario | Description | Margin Impact |
|----------|-------------|---------------|
| Plan Mix | Expected tier distribution per sales team input | Baseline |
| Downside Mix | 30% more customers on lower tiers than expected | Quantify margin compression |
| Premium Upside | 20% more customers on highest tier | Quantify margin expansion |

## Discount Policy Framework

| Discount Band | Approval Level | Conditions |
|---------------|---------------|------------|
| 0-10% | AE discretion | No conditions |
| 11-20% | Sales Manager | Document competitive justification |
| 21-30% | VP Sales + Finance | Requires minimum deal size, no auto-renew discounts |
| >30% | CFO sign-off required | Case-by-case, must maintain GM floor |

## Downside Scenario Thresholds

Conditions that would flip APPROVED to CONDITIONAL or REJECTED:

| Variable | Movement | Threshold |
|----------|----------|-----------|
| Tier adoption (lower vs. expected) | +30% lower tier | Re-run margin analysis |
| Discount utilization | >25% of deals at max discount | Revenue model reconciliation required |
| Volume shortfall | -20% unit volume | Contribution margin goes negative |
| COGS increase | +15% hosting/infrastructure | Check GM floor compliance |

## Sign-Off Decision Framework

| Decision | Conditions |
|----------|------------|
| APPROVED | All five decision tree steps pass, no threshold breaches in downside scenarios |
| APPROVED WITH CONDITIONS | Steps 1-3 pass; conditions exist on steps 4-5. Conditions must specify: metric threshold, measurement timeline, escalation owner |
| REJECTED | Any of steps 1-3 fail; margin floor breach is non-negotiable |

### Condition Writing Standard

A condition must be: measurable, time-bound, and assigned to an owner.

Good: "Maximum discount rate capped at 20% until Q3 review confirms gross margin >70% at blended deal mix."

Bad: "Keep an eye on margins."
