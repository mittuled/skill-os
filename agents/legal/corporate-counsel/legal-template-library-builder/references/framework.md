# Legal Template Library Framework

Reference framework for building and maintaining a standardized legal template library with usage guardrails and version control.

## Template Prioritization Matrix

### Priority 1 — High Volume, High Risk
Templates needed immediately based on frequency of use and legal exposure:

| Template | Use Case | Risk if Missing |
|----------|----------|----------------|
| Mutual NDA | Pre-deal discussions, vendor evaluations, partnerships | Confidential information disclosed without protection |
| Consulting/Contractor Agreement | Engaging independent contractors | IP ownership gaps, misclassification liability, no confidentiality |
| Employee Offer Letter | Hiring employees | Missing at-will language, incorrect comp terms, no IP assignment |
| IP Assignment Agreement | Founder/employee/contractor IP transfer | Broken chain of title discovered in diligence |
| SAFE/Convertible Note | Angel/pre-seed fundraising | Non-standard terms, missing investor protections |

### Priority 2 — Moderate Volume, Moderate Risk
| Template | Use Case | Risk if Missing |
|----------|----------|----------------|
| SaaS/Software License Agreement | Customer contracts | Revenue recognition issues, unlimited liability |
| Data Processing Agreement (DPA) | GDPR/CCPA processor relationships | Regulatory non-compliance, fines |
| Advisor Agreement | Engaging advisors with equity | Unclear scope, vesting disputes |
| Vendor Terms of Service | Procuring third-party services | Unfavorable default terms accepted |

### Priority 3 — Lower Volume, Specialized
| Template | Use Case | Risk if Missing |
|----------|----------|----------------|
| Joint Venture Agreement | Strategic partnerships | Unclear profit sharing, IP ownership |
| Reseller/Channel Agreement | Partner distribution | Revenue terms, exclusivity confusion |
| Data Sharing Agreement | B2B data partnerships | Privacy violations, unauthorized use |
| Settlement Agreement | Dispute resolution | Incomplete release, recurring liability |

## Template Structure Standards

### Required Elements for Every Template
1. **Header Block**: Template name, version, last updated date, approved by, usage scope
2. **Instructions Section**: When to use this template, who can use it without legal review, and when legal review is required
3. **Deviation Limits**: Which clauses can be modified by non-legal users and which require legal approval
4. **Fill-in Fields**: Clearly marked with brackets `[COMPANY NAME]` and guidance notes
5. **Fallback Positions**: For each negotiable term, document the company's preferred position, acceptable fallback, and walk-away point
6. **Defined Terms**: Consistent definitions across the template library (use a shared glossary)

### Deviation Authority Matrix

| Modification Type | Self-Serve OK | Legal Review Required |
|-------------------|---------------|----------------------|
| Fill in party names, dates, addresses | Yes | No |
| Adjust payment terms within approved range | Yes | No |
| Modify liability cap | No | Yes |
| Remove indemnification clause | No | Yes |
| Change governing law | No | Yes |
| Modify IP ownership provisions | No | Yes |
| Add non-standard representations | No | Yes |
| Extend term beyond 2 years | No | Yes |

## Version Control Requirements

- Every template versioned with semantic versioning (MAJOR.MINOR.PATCH)
- MAJOR: Legal terms changed (new liability cap, different IP treatment)
- MINOR: Clarifications or formatting changes that do not change legal meaning
- PATCH: Typo fixes, updated addresses, cosmetic changes
- Changelog maintained with: version, date, author, summary of changes, reason for change
- Prior versions archived (never deleted) for reference on executed agreements
- All templates review-cycled at least annually or upon material regulatory change

## Quality Standards

### Drafting Principles
- **Plain English**: Avoid unnecessary legalese; prefer "if" over "in the event that," "begin" over "commence"
- **Consistent Definitions**: Defined terms capitalized and used consistently; definitions section at the beginning
- **Severability**: Include severability clause so invalid provisions do not void the entire agreement
- **Entire Agreement**: Integration clause preventing reliance on oral representations
- **Counterparts**: Allow execution in counterparts and electronic signatures (ESIGN Act, UETA compliance)
- **Governing Law**: Default to Delaware law for corporate matters, company's home state for commercial agreements

### Regulatory Compliance per Template Type
- **NDAs**: Whistleblower carve-out (DTSA 18 USC 1833(b)), reasonable scope and duration
- **Employment**: At-will disclaimers (where applicable), state-specific wage/hour compliance, non-compete limitations per state law
- **Contractor Agreements**: IRS 20-factor test considerations for independent contractor classification, no employee benefits language
- **Data Agreements**: GDPR Article 28 processor requirements, CCPA service provider provisions, standard contractual clauses for cross-border transfers
- **Customer Agreements**: Limitation of liability, warranty disclaimers per UCC Article 2, DMCA safe harbor provisions if applicable
