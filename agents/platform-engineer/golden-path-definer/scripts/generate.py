#!/usr/bin/env python3
"""
generate.py — Define golden paths for standard engineering development tasks.

Usage:
    echo '<json>' | python3 generate.py
    python3 generate.py < input.json
    python3 generate.py < input.json -o output.json

Dependencies: Python 3.10+ standard library only.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

# Standard golden path domains
GOLDEN_PATH_DOMAINS = {
    "new_service": {
        "label": "New Service Creation",
        "components": [
            "Repository template (Cookiecutter or GitHub template repo)",
            "CI/CD pipeline (GitHub Actions or similar)",
            "Service mesh registration",
            "Logging and observability setup (Datadog/Grafana/CloudWatch)",
            "Secret management (Vault or AWS Secrets Manager)",
            "Local development environment (Docker Compose or devcontainers)",
            "README with runbook link",
        ],
    },
    "deployment": {
        "label": "Deployment",
        "components": [
            "GitOps workflow (merge to main → deploy to staging)",
            "Blue/green or canary deployment strategy",
            "Automated rollback trigger (error rate or latency threshold)",
            "Pre-deploy checklist (tests passed, migration ready, feature flag set)",
            "Post-deploy validation script",
        ],
    },
    "observability": {
        "label": "Observability",
        "components": [
            "Structured logging format (JSON with trace_id, service, level)",
            "Metrics: RED (Rate, Errors, Duration) + USE for infrastructure",
            "Distributed tracing (OpenTelemetry)",
            "Alerting rules (P50/P95/P99 latency, error rate, saturation)",
            "Runbook per alert with remediation steps",
            "On-call rotation configured",
        ],
    },
    "database_access": {
        "label": "Database Access",
        "components": [
            "ORM/query builder via approved library",
            "Read replica routing for non-transactional queries",
            "Connection pooling (PgBouncer or equivalent)",
            "Migration framework (Flyway or Liquibase)",
            "Schema change review process",
        ],
    },
    "api_design": {
        "label": "API Design",
        "components": [
            "REST or gRPC — per language-specific golden path",
            "OpenAPI spec generated from code",
            "Authentication via service identity token (not hardcoded credentials)",
            "Rate limiting at gateway",
            "Versioning strategy (/v1/, /v2/ or header-based)",
        ],
    },
    "security": {
        "label": "Security",
        "components": [
            "Dependency scanning (Snyk or Dependabot)",
            "Static code analysis (Semgrep or SonarQube)",
            "No secrets in code (pre-commit hook enforced)",
            "Least-privilege IAM roles per service",
            "HTTPS everywhere; no HTTP in production",
        ],
    },
}

# Adoption maturity levels
MATURITY_LEVELS = {
    "not_started": "Golden path not yet defined for this domain",
    "draft": "Draft exists but not enforced; teams may diverge",
    "active": "Defined and in use by some teams; not universally adopted",
    "enforced": "Enforced via CI/CD checks or linting; all new services comply",
}


def validate_input(data: dict) -> list[str]:
    errors = []
    if "team_name" not in data:
        errors.append("Missing required field: team_name")
    if "domains" not in data or not isinstance(data["domains"], list):
        errors.append("Missing required field: domains (list of domain status objects)")
    return errors


def generate_golden_paths(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    team = data["team_name"]
    domains_input = data["domains"]

    # Process each domain
    domain_results = []
    gaps = []
    enforced_count = 0

    for domain_input in domains_input:
        key = domain_input.get("domain", "")
        maturity = domain_input.get("maturity", "not_started")
        if maturity not in MATURITY_LEVELS:
            maturity = "not_started"
        existing_tools = domain_input.get("existing_tools", [])
        notes = domain_input.get("notes", "")

        domain_config = GOLDEN_PATH_DOMAINS.get(key, {"label": key, "components": []})
        is_gap = maturity in ("not_started", "draft")

        entry = {
            "domain": key,
            "label": domain_config["label"],
            "maturity": maturity,
            "maturity_description": MATURITY_LEVELS[maturity],
            "standard_components": domain_config["components"],
            "existing_tools": existing_tools,
            "notes": notes,
            "is_gap": is_gap,
        }
        domain_results.append(entry)
        if is_gap:
            gaps.append(entry)
        if maturity == "enforced":
            enforced_count += 1

    # Determine which domains are missing entirely
    covered_domains = {d.get("domain") for d in domains_input}
    missing_domains = [
        {"domain": k, "label": v["label"], "maturity": "not_started"}
        for k, v in GOLDEN_PATH_DOMAINS.items()
        if k not in covered_domains
    ]

    overall_pct = round(enforced_count / len(domain_results) * 100) if domain_results else 0

    return {
        "error": None,
        "result": {
            "team": team,
            "domains": domain_results,
            "gaps": gaps,
            "missing_domains": missing_domains,
            "enforced_count": enforced_count,
            "total_domains": len(domain_results),
            "enforcement_pct": overall_pct,
            "all_standard_domains": list(GOLDEN_PATH_DOMAINS.keys()),
            "summary": (
                f"Golden paths for {team}: {enforced_count}/{len(domain_results)} domains enforced ({overall_pct}%). "
                f"{len(gaps)} gap(s) requiring definition. "
                f"{len(missing_domains)} standard domain(s) not yet addressed."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_golden_paths(data)
    output = json.dumps(result, indent=2)
    args = sys.argv[1:]
    if "-o" in args:
        idx = args.index("-o") + 1
        if idx < len(args):
            Path(args[idx]).write_text(output + "\n", encoding="utf-8")
        else:
            sys.exit(1)
    else:
        print(output)


if __name__ == "__main__":
    main()
