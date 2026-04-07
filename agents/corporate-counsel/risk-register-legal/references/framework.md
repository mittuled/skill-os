# Legal Risk Register Framework

Reference framework for building, assessing, and maintaining a legal risk register using standard enterprise risk management methodology.

## Risk Taxonomy

### Risk Categories

| Category | Subcategories | Examples |
|----------|--------------|---------|
| **Contractual** | Customer agreements, vendor agreements, partnership agreements, licensing | Unlimited liability clauses, missing indemnification, auto-renewal penalties, unfavorable IP terms |
| **Regulatory** | Data privacy, financial services, employment, industry-specific, environmental | GDPR fines, state AG enforcement, licensing violations, employment misclassification |
| **IP** | Patent, trademark, copyright, trade secret | Freedom-to-operate risk, trademark conflicts, open-source license violations, employee invention disputes |
| **Employment** | Hiring, termination, discrimination, wage/hour, classification | Wrongful termination claims, misclassification (W-2 vs. 1099), FLSA overtime violations, non-compete enforceability |
| **Litigation** | Pending claims, threatened claims, class action exposure | Customer lawsuits, patent trolls, employee claims, regulatory enforcement actions |
| **Corporate Governance** | Fiduciary duties, board compliance, stockholder disputes | Derivative suits, breach of fiduciary duty, unauthorized corporate actions, minute book deficiencies |

## Risk Assessment Methodology

### Likelihood Scale

| Rating | Label | Definition | Probability |
|--------|-------|-----------|-------------|
| 5 | Almost Certain | Expected to occur within 12 months; has occurred before | >80% |
| 4 | Likely | Probable within 12 months; common in industry | 60-80% |
| 3 | Possible | Could occur; some contributing factors present | 30-60% |
| 2 | Unlikely | Not expected but possible; limited contributing factors | 10-30% |
| 1 | Rare | Highly unlikely; no contributing factors identified | <10% |

### Impact Scale

| Rating | Label | Financial Impact | Operational Impact | Reputational Impact |
|--------|-------|-----------------|-------------------|-------------------|
| 5 | Critical | >$1M or >10% revenue | Business-threatening; regulatory shutdown | Public scandal; customer exodus |
| 4 | Major | $250K-$1M or 5-10% revenue | Significant disruption; product/market withdrawal | Media coverage; major customer loss |
| 3 | Moderate | $50K-$250K or 1-5% revenue | Partial disruption; feature removal or delay | Industry awareness; some customer concern |
| 2 | Minor | $10K-$50K or <1% revenue | Minor inconvenience; workaround available | Limited awareness; no customer impact |
| 1 | Negligible | <$10K | No operational impact | No external awareness |

### Risk Score Matrix

**Risk Score = Likelihood × Impact**

| | Impact 1 | Impact 2 | Impact 3 | Impact 4 | Impact 5 |
|---|---------|---------|---------|---------|---------|
| **Likelihood 5** | 5 (Medium) | 10 (High) | 15 (Critical) | 20 (Critical) | 25 (Critical) |
| **Likelihood 4** | 4 (Low) | 8 (Medium) | 12 (High) | 16 (Critical) | 20 (Critical) |
| **Likelihood 3** | 3 (Low) | 6 (Medium) | 9 (High) | 12 (High) | 15 (Critical) |
| **Likelihood 2** | 2 (Low) | 4 (Low) | 6 (Medium) | 8 (Medium) | 10 (High) |
| **Likelihood 1** | 1 (Low) | 2 (Low) | 3 (Low) | 4 (Low) | 5 (Medium) |

### Risk Response Types
- **Avoid**: Eliminate the activity that creates the risk
- **Mitigate**: Reduce likelihood or impact through controls, insurance, or process changes
- **Transfer**: Shift risk to third party (insurance, indemnification, contractual allocation)
- **Accept**: Acknowledge and monitor without active mitigation (for low-scoring risks)

## Register Update Cadence

| Trigger | Action | Owner |
|---------|--------|-------|
| Quarterly review | Full register reassessment; score updates; progress tracking | Corporate Counsel |
| New product launch | Risk identification for new product/market | Corporate Counsel + Product |
| Material contract | Risk assessment for contracts above $100K or non-standard terms | Corporate Counsel |
| Regulatory change | Impact assessment on existing risk scores | Corporate Counsel |
| Security incident | Immediate risk entry and escalation | Corporate Counsel + Security |
| Litigation/claim | Immediate risk entry with privilege preservation | Corporate Counsel + General Counsel |
| M&A activity | Full risk review for target and combined entity | General Counsel |

## Reporting Standards

### Board Report Format
1. **Dashboard**: Total risks by category and severity; trend vs. prior quarter
2. **Top 5 Risks**: Highest-scoring risks with mitigation status
3. **New Risks**: Risks added since last report
4. **Closed Risks**: Risks resolved or accepted since last report
5. **Overdue Mitigations**: Actions past deadline with escalation notes

### Executive Summary Format
- Total risk count and change since last period
- Critical/high risk count and trend direction
- Key mitigation milestones achieved
- Budget impact of risk mitigation activities
- Upcoming regulatory deadlines
