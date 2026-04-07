# Scoring Rubric: Mcp Server Builder

Evaluates the quality of an MCP server build from API documentation.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | Endpoint Coverage | 20% | Percentage of API endpoints successfully mapped to MCP tools |
| 2 | Tool Granularity | 20% | Appropriateness of endpoint-to-tool mapping (not too coarse, not too fine) |
| 3 | Authentication Handling | 20% | Security of credential management using env vars, not hardcoded |
| 4 | Error Mapping Quality | 20% | MCP-compatible error responses for all HTTP error codes |
| 5 | Server Validity | 20% | Syntax correctness, no duplicate tools, transport initializes cleanly |
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
| A+ | 9.0 – 10.0 | Exceptional | All criteria fully met with evidence | Approve and schedule next review cycle |
| A | 8.0 – 8.9 | Strong | Minor gaps in 1-2 criteria | Approve with noted improvements for next cycle |
| B | 7.0 – 7.9 | Good | Moderate gaps in 2-3 criteria | Approve for use; address gaps within 30 days |
| C | 5.0 – 6.9 | Adequate | Significant gaps across multiple criteria | Revise before deployment; targeted improvements needed |
| D | 3.0 – 4.9 | Weak | Major gaps; core objectives not met | Return for substantial rework with specific guidance |
| F | 0.0 – 2.9 | Failing | Fundamentally incomplete or missing | Restart from requirements gathering |

## Signal Tables

### Endpoint Coverage

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Percentage of API endpoints successfully mapped to MCP tools; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Percentage of API endpoints successfully mapped to MCP tools; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Percentage of API endpoints successfully mapped to MCP tools; significant gaps but core elements present |
| 3-4 | Weakly addresses: Percentage of API endpoints successfully mapped to MCP tools; major gaps, core elements missing or vague |
| 0-2 | Does not address: Percentage of API endpoints successfully mapped to MCP tools; absent or fundamentally incomplete |

### Tool Granularity

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Appropriateness of endpoint-to-tool mapping (not too coarse, not too fine); evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Appropriateness of endpoint-to-tool mapping (not too coarse, not too fine); minor gaps in completeness or evidence |
| 5-6 | Partially meets: Appropriateness of endpoint-to-tool mapping (not too coarse, not too fine); significant gaps but core elements present |
| 3-4 | Weakly addresses: Appropriateness of endpoint-to-tool mapping (not too coarse, not too fine); major gaps, core elements missing or vague |
| 0-2 | Does not address: Appropriateness of endpoint-to-tool mapping (not too coarse, not too fine); absent or fundamentally incomplete |

### Authentication Handling

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Security of credential management using env vars, not hardcoded; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Security of credential management using env vars, not hardcoded; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Security of credential management using env vars, not hardcoded; significant gaps but core elements present |
| 3-4 | Weakly addresses: Security of credential management using env vars, not hardcoded; major gaps, core elements missing or vague |
| 0-2 | Does not address: Security of credential management using env vars, not hardcoded; absent or fundamentally incomplete |

### Error Mapping Quality

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: MCP-compatible error responses for all HTTP error codes; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: MCP-compatible error responses for all HTTP error codes; minor gaps in completeness or evidence |
| 5-6 | Partially meets: MCP-compatible error responses for all HTTP error codes; significant gaps but core elements present |
| 3-4 | Weakly addresses: MCP-compatible error responses for all HTTP error codes; major gaps, core elements missing or vague |
| 0-2 | Does not address: MCP-compatible error responses for all HTTP error codes; absent or fundamentally incomplete |

### Server Validity

| Score | Evidence |
|-------|----------|
| 9-10 | Fully meets all aspects of: Syntax correctness, no duplicate tools, transport initializes cleanly; evidence-based, comprehensive, no gaps |
| 7-8 | Mostly meets: Syntax correctness, no duplicate tools, transport initializes cleanly; minor gaps in completeness or evidence |
| 5-6 | Partially meets: Syntax correctness, no duplicate tools, transport initializes cleanly; significant gaps but core elements present |
| 3-4 | Weakly addresses: Syntax correctness, no duplicate tools, transport initializes cleanly; major gaps, core elements missing or vague |
| 0-2 | Does not address: Syntax correctness, no duplicate tools, transport initializes cleanly; absent or fundamentally incomplete |
