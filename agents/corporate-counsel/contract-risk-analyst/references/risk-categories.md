# Risk Categories: contract-risk-analyst

Taxonomy of contract risk categories with sub-categories, severity definitions, and common hidden risk patterns.

## Risk Taxonomy

### 1. Financial Risk

| Sub-Category | Description | Example |
|--------------|-------------|---------|
| Direct Cost | Fees, payments, and charges explicitly stated | Uncapped usage-based pricing |
| Contingent Cost | Financial obligations triggered by events | Indemnification payments upon third-party claims |
| Opportunity Cost | Revenue or business limitations imposed | Non-compete restricting adjacent market entry |
| Cost Escalation | Mechanisms that increase costs over time | Auto-renewal with uncapped annual price increases |

### 2. IP Risk

| Sub-Category | Description | Example |
|--------------|-------------|---------|
| Ownership Transfer | Clauses that assign or transfer IP rights | Work-for-hire provisions claiming company IP |
| License Scope Creep | Overly broad license grants | Perpetual, irrevocable, worldwide license to all deliverables |
| Trade Secret Exposure | Inadequate protection of confidential information | 1-year confidentiality period for trade secrets |
| Derivative Works | Unclear ownership of modifications and improvements | Silence on who owns customizations built on company IP |

### 3. Data Risk

| Sub-Category | Description | Example |
|--------------|-------------|---------|
| Unauthorized Processing | Processing beyond agreed purposes | Broad "business purposes" processing language |
| Breach Exposure | Inadequate breach response obligations | No breach notification timeframe specified |
| Sub-Processor Chain | Uncontrolled data sharing downstream | Unlimited sub-processor delegation |
| Cross-Border Transfer | Data movement to non-compliant jurisdictions | No data localization or transfer mechanism provisions |

### 4. Termination Risk

| Sub-Category | Description | Example |
|--------------|-------------|---------|
| Lock-In | Inability to exit the contract | No termination for convenience, multi-year minimum |
| Transition Gaps | Unclear post-termination obligations | No data return or destruction requirements |
| Penalty Exposure | Financial consequences of termination | Early termination fee equal to remaining contract value |
| Vendor Dependency | Loss of access to critical capabilities | No transition assistance or data portability provisions |

### 5. Indemnification Risk

| Sub-Category | Description | Example |
|--------------|-------------|---------|
| Asymmetric Coverage | One-sided indemnification obligations | Company indemnifies counterparty but not vice versa |
| Scope Expansion | Overly broad indemnification triggers | Indemnification for "any claims arising from" the agreement |
| Cap Mismatch | Indemnification obligations exceeding liability cap | Uncapped indemnification alongside capped general liability |
| Defense Control | Loss of control over legal defense | Counterparty controls defense with company paying costs |

### 6. Liability Risk

| Sub-Category | Description | Example |
|--------------|-------------|---------|
| Uncapped Exposure | No maximum on potential liability | No liability cap for general obligations |
| Consequential Damages | Exposure to indirect damages claims | No consequential damages exclusion |
| Representation Risk | Liability for broad representations | Representing compliance with "all applicable laws" globally |
| Joint & Several | Shared liability that cannot be apportioned | Joint venture liability structure without clear allocation |

### 7. Compliance Risk

| Sub-Category | Description | Example |
|--------------|-------------|---------|
| Regulatory Conflict | Clauses conflicting with applicable regulations | Data retention requirements conflicting with GDPR deletion rights |
| Audit Exposure | Obligations that create regulatory audit risk | Agreeing to practices that trigger PCI-DSS scope |
| Reporting Burden | Compliance reporting requirements | Monthly compliance attestation requirements |
| Standard Conflict | Conflicts with existing certification requirements | Terms incompatible with SOC 2 Type II controls |

### 8. Operational Risk

| Sub-Category | Description | Example |
|--------------|-------------|---------|
| Resource Demand | Requirements needing dedicated personnel | 24/7 support obligations without corresponding SLA credits |
| Process Change | Obligations requiring new workflows | Mandatory change management process for all modifications |
| Technology Dependency | Lock-in to specific technology or platform | Exclusive use requirements for counterparty's tools |
| Timeline Risk | Unrealistic compliance or delivery timelines | 48-hour response requirements without severity tiers |

## Severity Definitions

| Severity | Description | Business Impact | Response Required |
|----------|-------------|-----------------|-------------------|
| Critical | Creates existential risk or regulatory violation | Could threaten business continuity, trigger regulatory action, or cause irreversible financial damage | Block signing; rewrite or remove clause |
| High | Creates material financial or legal exposure | Measurable negative impact on P&L, legal posture, or operations if triggered | Negotiate specific changes before signing |
| Medium | Creates manageable but unnecessary risk | Could cause operational friction or moderate financial impact | Flag for negotiation; accept only with documented justification |
| Low | Minor deviation from ideal terms | Minimal practical impact; theoretical risk | Accept with awareness; note for future renegotiation |

## Common Hidden Risk Patterns

1. **Definition Expansion**: Defined terms (e.g., "Confidential Information," "Services") that are defined so broadly they capture more than intended
2. **Cross-Reference Chains**: Clause A references Clause B which references Exhibit C, creating obligations that are not apparent from reading any single section
3. **Negative Implication**: Protections stated for one party that are conspicuously absent for the other (e.g., termination rights granted only to counterparty)
4. **Survival Scope**: Survival clauses that keep unfavorable obligations alive indefinitely after termination
5. **Amendment by Notice**: Clauses allowing one party to modify terms by providing notice rather than obtaining consent
6. **Cumulative Remedies**: "Rights and remedies are cumulative" language that prevents election of remedies and maximizes counterparty's enforcement options
7. **Basket Erosion**: Multiple indemnification triggers that individually seem minor but collectively erode or bypass the liability cap
8. **Incorporation by Reference**: External documents (policies, procedures, standards) incorporated by reference that can be changed unilaterally
