# Scoring Rubric: Cross-Platform Tester

Evaluates the thoroughness of cross-browser and cross-device testing against the defined support matrix.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Matrix Coverage | 25% | Percentage of browser/device/OS combinations in the support matrix that were actually tested |
| 2 | Visual Regression Quality | 20% | Depth of visual comparison testing across matrix targets |
| 3 | Interaction Validation | 20% | Thoroughness of interactive behaviour testing (forms, gestures, animations) per platform |
| 4 | Performance Comparison | 15% | Cross-platform performance measurement and regression detection |
| 5 | Defect Documentation | 20% | Quality of defect reports with reproduction steps, platform details, and mitigation plans |
| **Total** | | **100%** | |

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score × weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Exceptional | Full matrix tested; visual regressions caught; interactions verified; performance profiled; all defects documented with mitigations | Clear for release on all platforms |
| A | 8.0 – 8.9 | Strong | Matrix mostly covered; visual and interaction testing thorough; performance checked; defects well-documented | Release with monitoring on untested edge combinations |
| B | 7.0 – 7.9 | Good | Major browser/device combinations tested; visual checks done; interaction testing partial; defects documented | Release with caveats for untested platforms |
| C | 5.0 – 6.9 | Adequate | Core browsers tested but mobile or Safari gaps; visual checks incomplete; interaction testing limited | Block until mobile and Safari testing complete |
| D | 3.0 – 4.9 | Weak | Chrome-only testing; no visual regression tools; minimal interaction testing | Block; expand testing to full support matrix |
| F | 0.0 – 2.9 | Failing | No cross-platform testing performed | Reject; cross-platform validation required |

## Signal Tables

### Matrix Coverage
| Score | Evidence |
|-------|----------|
| 9-10 | 100% of support matrix combinations tested including real devices for mobile; documented which combination each test ran on |
| 7-8 | 80%+ of matrix tested; real devices for primary mobile targets; emulators for secondary targets |
| 5-6 | Desktop browsers tested; mobile testing via emulators only; some matrix entries skipped |
| 3-4 | 2-3 browsers tested on desktop; no mobile testing |
| 0-2 | Single browser tested or no testing evidence |

### Visual Regression Quality
| Score | Evidence |
|-------|----------|
| 9-10 | Percy/Chromatic or Playwright screenshots for all key pages across matrix; diff reports reviewed; acceptable deviations documented |
| 7-8 | Visual regression tool run on critical pages; diffs reviewed for major browsers |
| 5-6 | Manual visual comparison on critical pages; no automated visual regression |
| 3-4 | Spot-check visual review on one or two browsers |
| 0-2 | No visual comparison performed |

### Interaction Validation
| Score | Evidence |
|-------|----------|
| 9-10 | Form submissions, animations, touch gestures, hover states, and keyboard interactions verified on each target platform; platform-specific interaction quirks documented |
| 7-8 | Core interactions tested on major platforms; touch and hover tested on respective device types |
| 5-6 | Form submissions tested; animations and gestures not verified across platforms |
| 3-4 | Basic click-through on desktop; no touch or gesture testing |
| 0-2 | No interaction testing across platforms |

### Performance Comparison
| Score | Evidence |
|-------|----------|
| 9-10 | Lighthouse or WebPageTest scores for each matrix target; P50/P95 load times compared across platforms; regressions from baseline identified |
| 7-8 | Performance measured on primary browser/device targets; major regressions identified |
| 5-6 | Lighthouse run on Chrome desktop only; no cross-platform performance comparison |
| 3-4 | Subjective "feels fast" assessment; no quantitative measurement |
| 0-2 | No performance measurement |

### Defect Documentation
| Score | Evidence |
|-------|----------|
| 9-10 | Each defect includes platform, browser version, OS, reproduction steps, expected vs. actual, severity, screenshots, and proposed polyfill or fallback |
| 7-8 | Defects documented with platform and reproduction steps; mitigations proposed for critical defects |
| 5-6 | Defects listed with platform but reproduction steps incomplete; no mitigation plans |
| 3-4 | Defects mentioned verbally or in chat without structured documentation |
| 0-2 | No defect documentation |
