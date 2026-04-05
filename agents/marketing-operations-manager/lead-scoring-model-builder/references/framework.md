# Framework: lead-scoring-model-builder

Defines the BANT scoring dimensions, behavioral scoring weights, MQL threshold calibration methodology, and decay rules for a two-axis lead scoring model.

## Two-Axis Scoring Architecture

Every lead is scored on two independent axes that combine to determine MQL status:

| Axis | What It Measures | Score Range | Triggered By |
|------|-----------------|-------------|-------------|
| **Fit Score** (Demographic/Firmographic) | How well the lead matches the ICP | 0–100 | Static attributes: company size, industry, title, tech stack |
| **Engagement Score** (Behavioral) | How actively the lead is showing purchase intent | 0–100 | Dynamic actions: page visits, downloads, email clicks, demo requests |

**MQL trigger**: Fit Score ≥ [threshold] AND Engagement Score ≥ [threshold], OR a single high-intent action (demo request, free trial, pricing page with 2+ visits).

## Fit Score — BANT Dimensions

| Dimension | Attribute | Points | Rationale |
|-----------|-----------|--------|-----------|
| **Budget** | Company size (revenue or employee proxy) | — | Larger companies have more budget; calibrate to ICP |
| | 500–5,000 employees | 25 | Core ICP |
| | 50–499 employees | 15 | Mid-market — qualified but lower ACV |
| | 5,001+ employees | 10 | Enterprise — longer cycle; lower conversion |
| | < 50 employees | 0 | SMB — typically below ACV threshold |
| **Authority** | Job function | — | Decision-making authority varies by role |
| | CxO or VP in target function | 20 | Primary decision-maker |
| | Director in target function | 15 | Key influencer / champion |
| | Manager in target function | 10 | Practitioner; strong influencer |
| | Individual contributor / unknown | 0 | — |
| **Need** | Industry vertical | — | Industry fit to ICP |
| | Primary target verticals | 15 | Highest conversion verticals |
| | Secondary target verticals | 8 | Good fit; lower conversion |
| | Non-target verticals | 0 | — |
| **Timing** | Technology stack signals | — | Tech stack signals intent and integration readiness |
| | Uses complementary tools (e.g., Salesforce CRM) | 15 | Higher integration need |
| | Evaluating alternatives (detected via intent data) | 20 | Active buying signal |
| | No signals | 0 | — |
| **Max Fit Score** | | **95** | Calibrate max to ~100 after validation |

## Engagement Score — Behavioral Signals

| Action | Points | Stage Signal | Decay |
|--------|--------|-------------|-------|
| Demo request | 50 | Decision | No decay — permanent |
| Free trial activation | 45 | Decision | No decay |
| Pricing page visit (2+ visits in 7 days) | 40 | Decision | No decay |
| ROI calculator use | 35 | Decision | 30-day decay (−50%) |
| Live webinar attendance | 25 | Consideration | 60-day decay |
| Case study download | 20 | Consideration | 60-day decay |
| Whitepaper / guide download | 15 | Consideration | 90-day decay |
| Webinar registration (did not attend) | 10 | Awareness | 90-day decay |
| Email click (non-nurture) | 8 | Awareness | 90-day decay |
| Blog post (2+ pages, same session) | 5 | Awareness | 90-day decay |
| Email open only | 2 | Engagement signal | 90-day decay |
| Social media follow | 1 | Brand awareness | No decay |

**Decay rules**: Points decay by the specified percentage after the period if no further action. Score does not drop below 0.

## MQL Threshold Calibration

Use historical data to set thresholds that produce the target MQL-to-SQL conversion rate.

| Step | Method |
|------|--------|
| 1. Pull closed-won data | Extract all closed-won deals from the last 12 months |
| 2. Map to scoring model | Retroactively score each closed-won lead under the model |
| 3. Identify score distribution | Find the score range that contains 80% of closed-won leads |
| 4. Set threshold at P80 | Set MQL threshold where 80% of historical closed-won leads qualify |
| 5. Back-test conversion | Verify that leads above threshold historically convert at ≥ 25% to SQL |
| 6. Adjust for volume | If too many MQLs: raise threshold. If too few: lower threshold or remove decay. |

**Target MQL-to-SQL conversion**: ≥ 25% for well-calibrated model.
**Sales rejection rate target**: < 20% of MQLs rejected by sales.

## Calibration Cadence

| Review | Frequency | Trigger | Output |
|--------|-----------|---------|--------|
| Lightweight calibration | Monthly | MQL→SQL rate drops below 20% | Weight adjustments |
| Full model recalibration | Quarterly | ICP changes, product pricing changes, > 25% sales rejection rate | Revised model with new back-test |
| MQL definition review | Quarterly | Joint Marketing + Sales session | Updated threshold with sales sign-off |
| ICP refresh | Annually | New target segments or market expansion | Full model rebuild |

## Model Governance

| Element | Standard |
|---------|---------|
| Sales sign-off | Required before any threshold change goes live |
| Change log | Document every score weight or threshold change with date and rationale |
| Notification | Sales ops notified ≥ 48 hours before model changes affect their queue |
| Rollback plan | Previous model weights preserved for 30 days post-change |
