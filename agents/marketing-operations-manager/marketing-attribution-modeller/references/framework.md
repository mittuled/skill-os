# Framework: marketing-attribution-modeller

Defines multi-touch attribution model types, selection criteria, touchpoint tracking standards, and governance processes for crediting marketing touchpoints to pipeline and revenue.

## Attribution Model Comparison

| Model | Credit Distribution | Best For | Avoid When |
|-------|-------------------|---------|-----------|
| **First-touch** | 100% to first interaction | Understanding which channels drive initial awareness | Sales cycles > 60 days with many mid-funnel touches |
| **Last-touch** | 100% to last interaction before conversion | Crediting conversion-closing channels | Short sales cycles only; starves awareness channels |
| **Linear** | Equal credit to all touchpoints | Simple; balanced across the journey | Many noisy touchpoints that inflate mid-funnel credit |
| **Time-decay** | More credit to recent touches (exponential decay) | Long enterprise sales cycles where recent touches matter more | TOFU strategy evaluation; penalizes early channels |
| **U-shaped (Position-based)** | 40% first, 40% last, 20% distributed to middle | B2B with clear first-touch (awareness) and last-touch (closing) importance | Cycles with more than 5–7 touchpoints |
| **W-shaped** | 30% first, 30% lead creation, 30% opportunity creation, 10% other | Full-funnel B2B with defined lead and opportunity stages | Less than 6 months of clean stage data |
| **Data-driven (algorithmic)** | ML-assigned credit based on conversion correlation | Mature data environments with 1,000+ attributed deals | Insufficient data volume; requires validation |

## Model Selection Decision Tree

| Question | If Yes → | If No → |
|----------|----------|---------|
| Sales cycle < 30 days? | Consider last-touch or linear | Move to next question |
| Sales cycle 30–90 days with 3–6 touchpoints? | U-shaped (position-based) | Move to next question |
| Sales cycle > 90 days with 6+ touchpoints? | W-shaped or time-decay | Move to next question |
| 1,000+ attributed deals in CRM? | Evaluate data-driven model | Stick with rule-based model |
| Strong awareness investment (SEO, brand, events)? | First-touch or U-shaped to protect TOFU credit | Last-touch acceptable |

**Recommended for most B2B SaaS companies**: U-shaped (position-based) as primary model; first-touch as supplementary view.

## Touchpoint Tracking Requirements

Every marketing touchpoint must capture the following data to be included in attribution:

| Channel | Required Tracking | Implementation |
|---------|-----------------|----------------|
| Paid search | UTM parameters (source, medium, campaign, content, term) | Applied to all ad destination URLs |
| Paid social | UTM parameters; pixel on conversion pages | Platform pixel + UTMs |
| Email | UTM on all links; CRM activity record | MAP native tracking |
| Organic / SEO | CRM form capture; anonymous session stitching | Analytics + identity resolution |
| Events / Webinars | CRM activity record with event name and date | MAP + CRM integration |
| Direct mail | Unique URL or promo code per campaign | Landing page UTM |
| Sales-assisted | CRM activity log by rep | CRM field completion requirement |
| Partner / Referral | Referral tracking parameter or partner code | UTM or native partner portal |

**Data quality standard**: Attribution model requires < 10% of deals with zero touchpoints before opportunity creation.

## Attribution Data Pipeline Architecture

```
Ad Platforms          Marketing Automation     CRM
(Google, LinkedIn) → (Marketo, HubSpot)    → (Salesforce)
        ↓                    ↓                    ↓
     UTM data           Email activity       Opportunity + Deal
                        Form submissions     Stage dates
                              ↓
                    Attribution Engine
                  (Bizible, RockerBox, or
                   native CRM rules)
                              ↓
                    Attribution Dashboard
                  (Pipeline + Revenue by
                   channel, campaign, content)
```

## Attribution Accuracy Validation

Before publishing attribution reports, validate accuracy:

| Validation Check | Method | Threshold |
|-----------------|--------|-----------|
| Touchpoint coverage | % of deals with ≥ 1 attributed marketing touchpoint | ≥ 90% |
| Double-counting check | Total attributed pipeline vs. CRM pipeline | < 5% discrepancy |
| Missing touchpoint audit | Random sample of 20 deals; verify all known touches captured | ≥ 85% accuracy |
| Model vs. revenue reconciliation | Attribution model revenue vs. finance reported revenue | < 10% discrepancy |
| New channel coverage | All active channels represented in attribution data | 100% |

## Attribution Governance

| Element | Standard |
|---------|---------|
| Model change approval | VP Marketing + RevOps sign-off required |
| Methodology documentation | Published and accessible to all stakeholders |
| Dispute resolution | Bi-quarterly marketing + sales + RevOps review of attribution disputes |
| Update cadence | Quarterly model recalibration; annual full methodology review |
| Stakeholder access | Attribution dashboard accessible to marketing, sales, RevOps, and finance |
| Historical consistency | Do not retroactively reattribute closed deals; only apply model changes to new data |

## Reporting Dimensions

Attribution dashboards must include views across:

| Dimension | Time Granularity | Required Views |
|-----------|-----------------|----------------|
| Channel | Monthly, quarterly | Pipeline sourced, pipeline influenced, revenue attributed |
| Campaign | Monthly | Pipeline per campaign, cost-per-opportunity |
| Content piece | Monthly | Pipeline influenced, views, conversion rate |
| Sales cycle stage | Monthly | Touchpoints per stage, touchpoint-to-stage conversion |
| Cohort (by quarter) | Quarterly | Time-to-pipeline by channel cohort |
