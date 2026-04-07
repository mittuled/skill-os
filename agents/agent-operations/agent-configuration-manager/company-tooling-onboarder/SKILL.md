---
name: company-tooling-onboarder
description: >
  This skill discovers, authenticates, and connects all tools an organization uses
  via MCP servers or CLI integrations. Use when setting up skill-os for a new company,
  onboarding a new tool to the agent ecosystem, or reconnecting after credential
  rotation. Also consider when agents report tool connectivity failures. Suggest when
  the user mentions connecting tools, setting up integrations, or onboarding a new SaaS
  product.
department: agent-operations
agent: agent-configuration-manager
version: 1.0.0
complexity: complex
related-skills: []
triggers:
  - "set up our tools"
  - "connect our SaaS tools"
  - "onboard company tools"
  - "configure tool integrations"
  - "connect Slack and GitHub"
---

# company-tooling-onboarder

## Agent: Agent Configuration Manager

L2 Agent Configuration Manager (1x) responsible for model selection per agent, compute budget allocation, context window sizing, tool access policies, and API key management.

Department ethos: [ideal-agent-operations.md](../../../../departments/agent-operations/ideal-agent-operations.md)
Tool policy: [allowed-tools.yaml](../../../../allowed-tools.yaml)

## Skill Description

Discovers, authenticates, and connects all tools an organization uses via MCP servers or CLI integrations so that every agent in the fleet can access the tooling it needs.

## When to Use

- When setting up skill-os for a new company and the full tool landscape needs to be mapped and connected.
- When onboarding a new SaaS product or internal tool into the agent ecosystem after the initial setup.
- When agents report tool connectivity failures or authentication errors that require credential rotation or reconnection.
- When a security review mandates re-verification of all tool connections and stored credentials.

## Workflow

1. **Interview the operator**: Ask the operator which tool categories the organization uses -- communication (Slack, Teams, Discord), source control (GitHub, GitLab, Bitbucket), project management (Linear, Jira, Asana), observability (Datadog, Grafana, PagerDuty), CRM (Salesforce, HubSpot), documentation (Notion, Confluence, Google Docs), finance (Stripe, QuickBooks), legal (DocuSign, Ironclad), and design (Figma, Canva). Record the specific tools selected per category. Deliverable: tool selection manifest listing every tool the organization wants connected.

2. **Detect MCP availability**: For each selected tool, check the known MCP server registry to determine whether a community or first-party MCP server exists. Classify each tool as MCP-available, CLI-only, or API-only. Run `scripts/discover-tools.py` to generate the structured manifest. Deliverable: tool manifest with MCP availability status per tool.

3. **Authenticate**: For each tool with an available MCP server, guide the operator through the authentication flow -- OAuth for tools that support it, API key for those that do not. Store every credential in the platform's native secret store using `scripts/configure-secrets.py`. NEVER write credentials to the repository, `allowed-tools.yaml`, or any checked-in file. Deliverable: authenticated credential entries in the platform secret store.

4. **Connect MCP servers**: Configure each MCP server endpoint with the stored credentials. Start the server process or register the endpoint with the agent runtime. Run `scripts/connect-mcp.py` per tool to validate the connection is live and responsive. Deliverable: running MCP server connections with validated health checks.

5. **Handle tools without MCP**: For tools classified as CLI-only or API-only with no existing MCP server, present the operator with two options -- (a) delegate to the `mcp-server-builder` skill to create a custom MCP wrapper from the tool's API documentation, or (b) defer the tool and add it to a backlog for later integration. Record the operator's decision for each tool. Deliverable: delegation requests to `mcp-server-builder` or deferred-tool backlog entries.

6. **Generate tool policy**: Create or update `allowed-tools.yaml` at the company-wide level with every connected tool. Include for each entry: tool name, category, MCP server identifier, connection status, and which agent roles have access. Do not include credentials or secrets in this file. Deliverable: updated `allowed-tools.yaml` reflecting the current connected tool landscape.

7. **Validate end-to-end**: Run a connectivity test for every connected tool -- send a lightweight read-only request (e.g., list channels, list repos, whoami) and confirm a valid response. Compile results into a health report with green/red status per tool. For any failures, include the specific error message and a remediation step. Deliverable: tool connectivity health report.

## Anti-Patterns

- **Storing credentials in the repo**: Writing API keys, tokens, or secrets to `allowed-tools.yaml`, `.env` files checked into version control, or any file inside the repository. *Why*: credentials in version control are exposed to every contributor and persist in git history even after deletion, creating a permanent security vulnerability.
- **Parallel authentication without validation**: Attempting to authenticate and connect all tools simultaneously without validating each connection before proceeding to the next. *Why*: a single misconfigured credential can cascade into confusing errors across dependent tools, and debugging interleaved failures is significantly harder than sequential validation.
- **Silent failure on auth errors**: Skipping tools that fail authentication and marking them as "not available" instead of reporting the specific failure. *Why*: the operator loses visibility into which tools are genuinely unavailable versus which ones failed due to a fixable configuration error, leading to an incomplete tool landscape that erodes trust.
- **Hardcoding tool registries**: Embedding a static list of supported tools and MCP servers directly in the workflow instead of referencing an updatable registry. *Why*: the MCP ecosystem evolves rapidly, and a hardcoded list becomes stale within weeks, causing the skill to miss newly available integrations.

## Output

**On success**: Produces an updated `allowed-tools.yaml` with all connected tools and their access policies, running MCP server connections for each authenticated tool, and a tool connectivity health report showing green status for every validated connection. Delivered to the operator and stored in the repository root.

**On failure**: Report the list of tools that failed to connect, the specific error encountered for each (authentication failure, network unreachable, MCP server not found, invalid API response), what was attempted, and actionable remediation steps (re-enter API key, check network policy, file issue on MCP server repo). Every failure must include a next step the operator can take.

## Related Skills

- [`mcp-server-builder`](../mcp-server-builder/SKILL.md) -- Builds custom MCP server wrappers for tools that lack native MCP support; delegated to in step 5 when no MCP server exists.
- [`409a-valuation-commissioner`](../409a-valuation-commissioner/SKILL.md) -- ROI assessment of agent compute spend may inform which tools are worth connecting and maintaining.
- [`option-pool-design`](../option-pool-design/SKILL.md) -- Initial tool allocation decisions should consider the compute and licensing costs of connected tools.
