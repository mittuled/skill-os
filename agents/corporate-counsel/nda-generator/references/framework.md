# NDA Framework: Variants, Clauses, and Jurisdiction Considerations

This framework provides the clause library and variant comparison for generating Non-Disclosure Agreements.

## NDA Variant Comparison

| Aspect | Mutual | One-Way (Disclosing) | One-Way (Receiving) | Employee/Consultant |
|--------|--------|---------------------|--------------------|--------------------|
| **Parties** | Both disclose and receive | Company discloses, counterparty receives | Counterparty discloses, company receives | Individual bound to company |
| **Obligations** | Symmetric for both parties | Only receiving party has obligations | Only company (as receiver) has obligations | Individual has obligations to company |
| **Use case** | Partnerships, joint ventures, co-development | Vendor evaluations, investor pitches, sales demos | Acquisition targets, inbound technology review | Employment, consulting, contracting |
| **Typical term** | 2-3 years | 2-5 years | 2-3 years | Duration of employment + 2-5 years |
| **Non-solicitation** | Sometimes mutual | Rarely | Sometimes | Usually included |
| **Residuals clause** | Negotiable | Rarely granted | Sometimes requested | Not applicable |

## Standard Clause Library

### 1. Definition of Confidential Information

The definition should be broad enough to cover all sensitive information but specific enough to be enforceable. Two approaches:
- **Catch-all with marking**: All information disclosed is confidential, with optional marking requirement for written materials
- **Enumerated categories**: Specific categories listed (technical data, business plans, customer lists, financial information, trade secrets)

Best practice: use enumerated categories plus a catch-all residual, with clear exclusions.

### 2. Exclusions from Confidentiality

Standard exclusions (present in all variants):
- Information already known to the receiving party (with burden of proof on receiver)
- Information that becomes publicly available through no fault of the receiving party
- Information independently developed by the receiving party (documented evidence required)
- Information received from a third party without breach of obligation
- Information disclosed pursuant to legal compulsion (with notice to disclosing party)

### 3. Obligations of Receiving Party

Core obligations:
- Use confidential information only for the stated purpose
- Restrict access to need-to-know personnel
- Apply at least the same degree of care as for own confidential information (but not less than reasonable care)
- Not reverse-engineer products or materials containing confidential information
- Notify disclosing party promptly of any unauthorized disclosure

### 4. Term and Termination

- **Agreement term**: Period during which information may be disclosed (typically 1-3 years)
- **Confidentiality term**: Period during which obligations survive (typically 2-5 years from disclosure, or indefinite for trade secrets)
- **Termination**: Either party may terminate with written notice (typically 30 days)
- Trade secrets should be protected for as long as they remain trade secrets, regardless of term

### 5. Return or Destruction of Materials

Upon termination or request:
- Return or destroy all confidential materials and copies
- Certify destruction in writing if destruction is chosen
- Exception: archival copies required by law or regulation, subject to ongoing confidentiality
- Exception: electronic copies in routine backup systems, subject to ongoing confidentiality

### 6. Remedies

- Acknowledge that breach may cause irreparable harm
- Consent to injunctive relief without proof of actual damages and without posting bond
- Preserve all other legal and equitable remedies
- Optional: liquidated damages clause for quantifiable breaches

### 7. Miscellaneous Provisions

- **Governing law**: Specify jurisdiction (disclosing party's jurisdiction preferred)
- **Dispute resolution**: Arbitration (faster, private) vs. litigation (broader remedies)
- **Assignment**: Not assignable without written consent
- **Entire agreement**: Supersedes prior agreements on the subject matter
- **Severability**: Invalid provisions severed without affecting remainder
- **Waiver**: No waiver unless in writing
- **Counterparts**: May be executed in counterparts

## Jurisdiction Considerations

### United States
- State law governs; choice of law clause is critical
- California: non-compete provisions in NDAs generally unenforceable
- Delaware: common choice for corporate agreements
- Trade secret protection under DTSA (federal) and UTSA (state)

### United Kingdom
- Governed by English common law (or Scots law)
- Restrictive covenants must be reasonable in scope and duration
- GDPR applies if personal data is shared as part of confidential information
- Standard terminology differs (e.g., "undertaking" vs. "covenant")

### European Union
- GDPR compliance required if personal data is disclosed
- EU Trade Secrets Directive provides harmonized protection
- Some jurisdictions require specific formalities (notarization in certain countries)
- Language requirements may apply (local language translation)

## Common Pitfalls

1. **No purpose limitation**: Failing to define the permitted purpose lets the receiving party use information for any reason
2. **Residuals clause too broad**: Allowing the receiving party to use "retained knowledge" effectively nullifies the NDA for non-documented information
3. **Missing legal compulsion carve-out**: Without this, the receiving party faces a conflict between NDA obligations and legal requirements
4. **Symmetric obligations in asymmetric relationships**: Mutual obligations when only one party is disclosing create unnecessary burden
5. **No survival clause**: Confidentiality obligations that expire with the agreement term leave information unprotected
