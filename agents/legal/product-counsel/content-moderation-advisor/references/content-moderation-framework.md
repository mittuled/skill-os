# Content Moderation Legal Framework

Reference framework for advising on content moderation policies, enforcement procedures, and regulatory compliance.

## Applicable Regulations by Jurisdiction

| Regulation | Jurisdiction | Key Requirements |
|-----------|-------------|-----------------|
| Section 230 (CDA) | US | Immunity for good-faith moderation; no immunity for federal criminal law, IP violations, or sex trafficking (FOSTA-SESTA) |
| Digital Services Act (DSA) | EU | Transparency reports, notice-and-action mechanisms, trusted flaggers, risk assessments for VLOPs, illegal content removal obligations |
| Online Safety Act | UK | Duty of care for illegal content and content harmful to children, risk assessments, transparency reporting |
| NetzDG | Germany | 24-hour removal for manifestly illegal content, 7-day removal for other illegal content, transparency reports |
| CSAM Laws | US/EU/Global | Mandatory reporting to NCMEC (US), EU CSAM Regulation proposals, hash-matching obligations |
| State Social Media Laws | US (various) | Age verification (Utah, Louisiana), parental consent (Arkansas), algorithmic feed opt-out (California) |

## Moderation Policy Design Checklist

1. **Content Categories**: Define prohibited content categories (illegal content, harassment, hate speech, misinformation, spam, NSFW, CSAM)
2. **Severity Tiers**: Map content types to enforcement actions (warning, content removal, temporary suspension, permanent ban, law enforcement referral)
3. **Detection Methods**: Specify automated detection (hash-matching, ML classifiers, keyword filters) and human review processes
4. **Escalation Criteria**: Define when moderation decisions require legal review (government requests, public figures, legally ambiguous speech, cross-border content)
5. **Appeal Mechanism**: Design user appeal process meeting DSA requirements (clear reasons, human review of automated decisions, timely resolution)
6. **Transparency Reporting**: Plan required transparency reports (DSA Article 15/24/42, NetzDG Section 2)
7. **Record Retention**: Define moderation decision retention periods for regulatory compliance and litigation holds

## Section 230 Analysis Framework

| Factor | Increases Protection | Decreases Protection |
|--------|---------------------|---------------------|
| Content Source | User-generated | Editorially curated or algorithmically promoted |
| Moderation Approach | Good-faith community standards enforcement | Selective enforcement suggesting editorial control |
| Product Feature | Passive hosting | Active recommendation, ranking, or curation |
| Knowledge | No specific knowledge of illegal content | Actual knowledge with failure to act |

## DSA Compliance Requirements by Platform Size

| Requirement | Micro/Small | Medium | VLOP (45M+ EU users) |
|------------|------------|--------|----------------------|
| Terms of Service | Required | Required | Required |
| Notice-and-Action | Required | Required | Required |
| Transparency Reports | Exempt | Annual | Semi-annual + database |
| Trusted Flaggers | N/A | Required | Required |
| Risk Assessments | N/A | N/A | Required (annual) |
| Audit | N/A | N/A | Required (annual, independent) |
| Recommender Transparency | N/A | N/A | Required |
