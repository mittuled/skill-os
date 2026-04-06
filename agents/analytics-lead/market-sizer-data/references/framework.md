# Framework: Market Sizer (Data)

Defines the quantitative methodology for producing defensible TAM/SAM/SOM estimates using multi-source data models.

## TAM/SAM/SOM Definitions

| Market Layer | Definition | Typical Inputs | Common Mistake |
|-------------|-----------|---------------|----------------|
| TAM (Total Addressable Market) | Total revenue opportunity if 100% of the target category is captured | Industry analyst reports, census data, global category revenue | Using TAM as the pitch number overstates reachable opportunity |
| SAM (Serviceable Addressable Market) | Subset of TAM reachable given product constraints (geography, language, segment) | Filtered TAM × segment share, search demand proxy | Underestimating the SAM by applying too many constraints too early |
| SOM (Serviceable Obtainable Market) | Realistic capture of SAM given GTM capacity, competition, and timeline | SAM × realistic market share % per scenario | Using optimistic share without competitive density evidence |

## Sizing Methodologies

### Bottom-Up Model

1. Define the target customer segment precisely (role, company size, geography, use case).
2. Count potential customers: use LinkedIn Ads audience estimates, industry association member counts, or census business data.
3. Estimate adoption rate: use comparable product penetration rates from public S-1 filings or analyst reports.
4. Set ARPU: anchor to willingness-to-pay research; cross-check against competitor pricing tiers.
5. Compute SAM = addressable customers × adoption rate × ARPU.

### Top-Down Cross-Check

1. Source total category revenue from 2+ analyst reports (e.g., IDC, Gartner, Forrester, Statista).
2. Adjust for geography and segment to derive the applicable TAM slice.
3. Apply a realistic market share % (benchmark: 1-3% for early-stage; 5-10% for growth-stage with proven GTM).
4. Compute SOM top-down.
5. Compare to bottom-up SOM. If divergence > 2x: investigate assumption differences; document which is more conservative and why.

## Scenario Framework

| Scenario | Adoption Rate | ARPU | Segment Size | SOM Result |
|---------|-------------|------|-------------|-----------|
| Bear | [low %] | [low $] | [conservative N] | [$M] |
| Base | [mid %] | [mid $] | [mid N] | [$M] |
| Bull | [high %] | [high $] | [optimistic N] | [$M] |

**Confidence rating per scenario:**
- Bear: High confidence (each assumption is a lower bound)
- Base: Medium confidence (assumptions are midpoints from data)
- Bull: Low confidence (requires favorable market dynamics)

## Data Source Hierarchy

| Tier | Sources | Trust Level |
|------|---------|------------|
| Primary | Internal usage data, customer interviews, paid analyst reports | High |
| Secondary | S-1 filings, public earnings calls, LinkedIn Ads audience estimates | Medium-High |
| Tertiary | Free analyst summaries, blog market sizing posts, keyword search volume | Medium |
| Proxy | Adjacent category sizing applied with discount factor | Low — flag explicitly |

## Key Assumptions Log Template

| Assumption | Value Used | Source | Bear Variant | Bull Variant | Sensitivity to SOM |
|-----------|-----------|--------|-------------|-------------|-------------------|
| Target segment size | [N] | [source] | [N×0.7] | [N×1.3] | [high / medium / low] |
| Adoption rate Y1 | [%] | [source] | [%−5pp] | [%+5pp] | [high / medium / low] |
| ARPU | [$] | [source] | [$×0.8] | [$×1.2] | [high / medium / low] |
