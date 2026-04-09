#!/usr/bin/env python3
"""
Add triggers to SKILL.md files under agents/engineering/ that don't already have them.
Triggers are inferred from the skill name and description.
"""

import re
import subprocess
import sys

REPO_ROOT = "/Users/mittul/Documents/Sidespace/_repos/skill-os"

TRIGGER_MAP = {
    # ai-ml-engineer
    "agents/engineering/ai-ml-engineer/ai-feasibility-assessor/SKILL.md": [
        "assess AI feasibility",
        "is ML the right approach",
        "AI viability check",
        "evaluate ML approach",
        "data readiness assessment",
    ],
    "agents/engineering/ai-ml-engineer/ml-architecture-designer/SKILL.md": [
        "design ML architecture",
        "ML system design",
        "model architecture",
        "machine learning architecture",
        "ML pipeline design",
    ],
    "agents/engineering/ai-ml-engineer/mlops-pipeline-builder/SKILL.md": [
        "build MLOps pipeline",
        "MLOps setup",
        "ML deployment pipeline",
        "model CI/CD",
        "MLOps infrastructure",
    ],
    "agents/engineering/ai-ml-engineer/model-evaluation-runner/SKILL.md": [
        "evaluate model",
        "run model evaluation",
        "model benchmarking",
        "ML model assessment",
        "model performance evaluation",
    ],
    "agents/engineering/ai-ml-engineer/model-performance-monitor/SKILL.md": [
        "monitor model performance",
        "model drift detection",
        "ML monitoring",
        "track model metrics",
        "model health check",
    ],
    "agents/engineering/ai-ml-engineer/model-requirements-definer/SKILL.md": [
        "define model requirements",
        "ML requirements",
        "model specs",
        "set ML requirements",
        "model requirement gathering",
    ],
    "agents/engineering/ai-ml-engineer/model-trainer/SKILL.md": [
        "train model",
        "ML training run",
        "fine-tune model",
        "model training",
        "run training job",
    ],
    # data-engineer
    "agents/engineering/data-engineer/data-pipeline-designer/SKILL.md": [
        "design data pipeline",
        "data pipeline architecture",
        "ETL pipeline design",
        "data flow design",
        "pipeline architecture",
    ],
    "agents/engineering/data-engineer/data-pipeline-feasibility-check/SKILL.md": [
        "check pipeline feasibility",
        "data pipeline viability",
        "can we build this pipeline",
        "pipeline feasibility",
        "data ingestion feasibility",
    ],
    "agents/engineering/data-engineer/data-quality-monitor/SKILL.md": [
        "monitor data quality",
        "data quality check",
        "data validation",
        "track data quality",
        "data health monitoring",
    ],
    "agents/engineering/data-engineer/data-warehouse-schema-designer/SKILL.md": [
        "design warehouse schema",
        "data warehouse design",
        "schema design",
        "data modeling",
        "warehouse schema",
    ],
    "agents/engineering/data-engineer/pipeline-builder/SKILL.md": [
        "build data pipeline",
        "implement pipeline",
        "create ETL pipeline",
        "data pipeline build",
        "pipeline implementation",
    ],
    "agents/engineering/data-engineer/pipeline-reliability-tester/SKILL.md": [
        "test pipeline reliability",
        "pipeline testing",
        "data pipeline QA",
        "pipeline resilience test",
        "test data pipeline",
    ],
    "agents/engineering/data-engineer/pipeline-scale-planner/SKILL.md": [
        "plan pipeline scaling",
        "scale data pipeline",
        "pipeline capacity planning",
        "pipeline scale strategy",
        "data pipeline scalability",
    ],
    # database-expert
    "agents/engineering/database-expert/data-model-designer/SKILL.md": [
        "design data model",
        "database schema design",
        "data modeling",
        "ER diagram",
        "relational schema design",
    ],
    # devops-infrastructure-engineer
    "agents/engineering/devops-infrastructure-engineer/alerting-configurator/SKILL.md": [
        "configure alerts",
        "set up alerting",
        "alert rules setup",
        "monitoring alerts",
        "alerting configuration",
    ],
    "agents/engineering/devops-infrastructure-engineer/ci-cd-pipeline-builder/SKILL.md": [
        "build CI/CD pipeline",
        "set up CI/CD",
        "CI/CD setup",
        "continuous integration setup",
        "deployment pipeline",
    ],
    "agents/engineering/devops-infrastructure-engineer/cloud-foundation-setup/SKILL.md": [
        "set up cloud foundation",
        "cloud account setup",
        "cloud infrastructure bootstrap",
        "cloud foundation",
        "bootstrap cloud environment",
    ],
    "agents/engineering/devops-infrastructure-engineer/deployment-architecture-designer/SKILL.md": [
        "design deployment architecture",
        "deployment design",
        "cloud architecture design",
        "hosting architecture",
        "deployment topology",
    ],
    "agents/engineering/devops-infrastructure-engineer/deployment-automation/SKILL.md": [
        "automate deployment",
        "deployment automation",
        "automated deploy",
        "deploy automation setup",
        "release automation",
    ],
    "agents/engineering/devops-infrastructure-engineer/environment-parity-planner/SKILL.md": [
        "plan environment parity",
        "dev prod parity",
        "environment consistency",
        "staging parity",
        "environment alignment",
    ],
    "agents/engineering/devops-infrastructure-engineer/feature-flag-configurator/SKILL.md": [
        "configure feature flags",
        "feature flag setup",
        "feature toggles",
        "launch darkly setup",
        "feature flag config",
    ],
    "agents/engineering/devops-infrastructure-engineer/github-org-setup/SKILL.md": [
        "set up GitHub org",
        "GitHub organization setup",
        "github org config",
        "configure GitHub org",
        "GitHub team structure",
    ],
    "agents/engineering/devops-infrastructure-engineer/incident-response-planner/SKILL.md": [
        "plan incident response",
        "incident runbook",
        "on-call setup",
        "incident management plan",
        "outage response plan",
    ],
    "agents/engineering/devops-infrastructure-engineer/infrastructure-cost-optimiser/SKILL.md": [
        "optimise infrastructure costs",
        "reduce cloud costs",
        "cloud cost optimization",
        "infra cost review",
        "FinOps analysis",
    ],
    "agents/engineering/devops-infrastructure-engineer/infrastructure-load-testing/SKILL.md": [
        "load test infrastructure",
        "infrastructure stress test",
        "load testing",
        "capacity stress test",
        "infra load test",
    ],
    "agents/engineering/devops-infrastructure-engineer/infrastructure-requirements-extractor/SKILL.md": [
        "extract infra requirements",
        "infrastructure requirements",
        "infra spec extraction",
        "define infra needs",
        "infra requirement gathering",
    ],
    "agents/engineering/devops-infrastructure-engineer/infrastructure-scaling-executor/SKILL.md": [
        "execute infra scaling",
        "scale infrastructure",
        "infra scale-up",
        "run scaling operation",
        "infrastructure scale out",
    ],
    "agents/engineering/devops-infrastructure-engineer/performance-monitor/SKILL.md": [
        "monitor performance",
        "system performance monitoring",
        "infra performance tracking",
        "APM setup",
        "track system metrics",
    ],
    "agents/engineering/devops-infrastructure-engineer/production-readiness-reviewer/SKILL.md": [
        "review production readiness",
        "prod readiness check",
        "go-live checklist",
        "production checklist",
        "pre-launch review",
    ],
    "agents/engineering/devops-infrastructure-engineer/progressive-rollout-executor/SKILL.md": [
        "execute progressive rollout",
        "canary deployment",
        "gradual rollout",
        "progressive release",
        "staged rollout",
    ],
    "agents/engineering/devops-infrastructure-engineer/rollback-planner/SKILL.md": [
        "plan rollback",
        "rollback strategy",
        "deployment rollback plan",
        "revert deployment plan",
        "rollback runbook",
    ],
    "agents/engineering/devops-infrastructure-engineer/rollout-configurator/SKILL.md": [
        "configure rollout",
        "rollout configuration",
        "deployment rollout setup",
        "release rollout config",
        "rollout strategy setup",
    ],
    "agents/engineering/devops-infrastructure-engineer/runbook-drafter/SKILL.md": [
        "draft runbook",
        "write runbook",
        "operational runbook",
        "create ops runbook",
        "runbook documentation",
    ],
    # platform-engineer
    "agents/engineering/platform-engineer/developer-experience-enabler/SKILL.md": [
        "improve developer experience",
        "DX enablement",
        "developer tooling",
        "enhance dev experience",
        "developer productivity",
    ],
    "agents/engineering/platform-engineer/golden-path-definer/SKILL.md": [
        "define golden path",
        "golden path setup",
        "paved road for developers",
        "platform golden path",
        "standard dev path",
    ],
    "agents/engineering/platform-engineer/platform-capability-gap-detector/SKILL.md": [
        "detect platform gaps",
        "platform gap analysis",
        "platform capability audit",
        "identify platform gaps",
        "platform capability gaps",
    ],
    "agents/engineering/platform-engineer/platform-roadmap-aligner/SKILL.md": [
        "align platform roadmap",
        "platform roadmap planning",
        "platform strategy alignment",
        "roadmap sync",
        "platform roadmap review",
    ],
    "agents/engineering/platform-engineer/platform-scale-preparation/SKILL.md": [
        "prepare platform for scale",
        "platform scaling",
        "scale platform",
        "platform capacity prep",
        "platform growth planning",
    ],
    # qa-test-engineer
    "agents/engineering/qa-test-engineer/instrumentation-verifier-prod/SKILL.md": [
        "verify prod instrumentation",
        "production instrumentation check",
        "verify analytics in prod",
        "prod tracking validation",
        "instrumentation audit prod",
    ],
    "agents/engineering/qa-test-engineer/instrumentation-verifier-qa/SKILL.md": [
        "verify QA instrumentation",
        "QA instrumentation check",
        "validate analytics in QA",
        "QA tracking validation",
        "instrumentation audit QA",
    ],
    "agents/engineering/qa-test-engineer/integration-test-runner/SKILL.md": [
        "run integration tests",
        "integration testing",
        "execute integration tests",
        "integration test suite",
        "run integration suite",
    ],
    "agents/engineering/qa-test-engineer/performance-tester/SKILL.md": [
        "run performance tests",
        "performance testing",
        "perf test",
        "load and performance tests",
        "benchmark application",
    ],
    "agents/engineering/qa-test-engineer/regression-test-runner/SKILL.md": [
        "run regression tests",
        "regression testing",
        "execute regression suite",
        "regression test run",
        "regression check",
    ],
    "agents/engineering/qa-test-engineer/security-auditor/SKILL.md": [
        "audit security",
        "security audit",
        "run security checks",
        "application security audit",
        "security vulnerability scan",
    ],
    "agents/engineering/qa-test-engineer/staging-validator/SKILL.md": [
        "validate staging",
        "staging environment check",
        "staging validation",
        "verify staging deploy",
        "pre-prod validation",
    ],
    "agents/engineering/qa-test-engineer/unit-test-runner/SKILL.md": [
        "run unit tests",
        "unit testing",
        "execute unit test suite",
        "unit test run",
        "run unit suite",
    ],
    # security-engineer
    "agents/engineering/security-engineer/compliance-ga-reviewer-eng/SKILL.md": [
        "review compliance for GA",
        "GA compliance check",
        "compliance review",
        "pre-GA compliance audit",
        "GA readiness compliance",
    ],
    "agents/engineering/security-engineer/continuous-security-monitoring/SKILL.md": [
        "set up security monitoring",
        "continuous security monitoring",
        "security event monitoring",
        "SIEM setup",
        "ongoing security monitoring",
    ],
    "agents/engineering/security-engineer/penetration-tester/SKILL.md": [
        "run penetration test",
        "pen test",
        "penetration testing",
        "ethical hacking",
        "security pen test",
    ],
    "agents/engineering/security-engineer/secure-code-reviewer/SKILL.md": [
        "review code for security",
        "secure code review",
        "security code audit",
        "SAST review",
        "code security review",
    ],
    "agents/engineering/security-engineer/security-architecture-reviewer/SKILL.md": [
        "review security architecture",
        "security design review",
        "architecture security audit",
        "security architecture assessment",
        "threat surface review",
    ],
    "agents/engineering/security-engineer/security-baseline-setup/SKILL.md": [
        "set up security baseline",
        "security baseline",
        "hardening baseline",
        "security configuration baseline",
        "baseline security controls",
    ],
    "agents/engineering/security-engineer/security-compliance-enabler/SKILL.md": [
        "enable security compliance",
        "compliance enablement",
        "SOC2 compliance setup",
        "security compliance framework",
        "compliance controls setup",
    ],
    "agents/engineering/security-engineer/security-requirements-extractor/SKILL.md": [
        "extract security requirements",
        "security requirements",
        "security spec extraction",
        "define security needs",
        "security requirement gathering",
    ],
    "agents/engineering/security-engineer/threat-model-sketch/SKILL.md": [
        "sketch threat model",
        "quick threat model",
        "threat model draft",
        "rapid threat modeling",
        "lightweight threat model",
    ],
    "agents/engineering/security-engineer/threat-modelling/SKILL.md": [
        "threat modelling",
        "full threat model",
        "STRIDE analysis",
        "threat model assessment",
        "security threat analysis",
    ],
    # sr-backend-developer
    "agents/engineering/sr-backend-developer/builder/SKILL.md": [
        "build backend feature",
        "implement backend",
        "backend implementation",
        "develop API",
        "backend development",
    ],
    "agents/engineering/sr-backend-developer/instrumentation-implementer/SKILL.md": [
        "implement instrumentation",
        "add observability",
        "instrument code",
        "add telemetry",
        "observability implementation",
    ],
    "agents/engineering/sr-backend-developer/instrumentation-planner-eng/SKILL.md": [
        "plan instrumentation",
        "instrumentation planning",
        "observability planning",
        "plan telemetry",
        "instrumentation design",
    ],
    "agents/engineering/sr-backend-developer/security-reviewer/SKILL.md": [
        "security review",
        "review for security issues",
        "code security review",
        "backend security check",
        "security vulnerability review",
    ],
    "agents/engineering/sr-backend-developer/third-party-integrator/SKILL.md": [
        "integrate third party API",
        "third-party integration",
        "external API integration",
        "API integration",
        "vendor integration",
    ],
    # sr-frontend-developer
    "agents/engineering/sr-frontend-developer/accessibility-auditor/SKILL.md": [
        "audit accessibility",
        "a11y audit",
        "accessibility check",
        "WCAG audit",
        "accessibility review",
    ],
    "agents/engineering/sr-frontend-developer/accessibility-checker-eng/SKILL.md": [
        "check accessibility",
        "a11y check",
        "accessibility verification",
        "WCAG compliance check",
        "frontend accessibility check",
    ],
    "agents/engineering/sr-frontend-developer/component-mapper-eng/SKILL.md": [
        "map components",
        "component mapping",
        "design to component map",
        "UI component inventory",
        "map design components",
    ],
    "agents/engineering/sr-frontend-developer/cross-platform-tester/SKILL.md": [
        "test cross-platform",
        "cross-browser testing",
        "cross-platform compatibility",
        "multi-browser test",
        "device compatibility test",
    ],
    "agents/engineering/sr-frontend-developer/design-implementer/SKILL.md": [
        "implement design",
        "convert design to code",
        "design to code",
        "frontend design implementation",
        "build UI from design",
    ],
    # tech-architect
    "agents/engineering/tech-architect/api-contract-definer/SKILL.md": [
        "define API contract",
        "API contract",
        "API spec definition",
        "OpenAPI contract",
        "API interface design",
    ],
    "agents/engineering/tech-architect/architecture-designer/SKILL.md": [
        "design architecture",
        "system architecture",
        "technical architecture",
        "software architecture design",
        "architecture blueprint",
    ],
    "agents/engineering/tech-architect/design-feasibility-reviewer/SKILL.md": [
        "review design feasibility",
        "feasibility review",
        "design viability check",
        "technical feasibility of design",
        "design feasibility assessment",
    ],
    "agents/engineering/tech-architect/moat-analyzer-tech/SKILL.md": [
        "analyze technical moat",
        "tech competitive advantage",
        "technical moat analysis",
        "defensibility analysis",
        "technical differentiation",
    ],
    "agents/engineering/tech-architect/performance-budget-setter-eng/SKILL.md": [
        "set performance budget",
        "performance budgets",
        "define perf targets",
        "performance thresholds",
        "web performance budget",
    ],
    "agents/engineering/tech-architect/scale-infrastructure-planner/SKILL.md": [
        "plan infrastructure scaling",
        "scale infra plan",
        "infrastructure growth plan",
        "scaling roadmap",
        "capacity planning",
    ],
    "agents/engineering/tech-architect/sla-definer-eng/SKILL.md": [
        "define SLA",
        "SLA definition",
        "service level agreement",
        "define uptime targets",
        "reliability targets",
    ],
    "agents/engineering/tech-architect/tech-scaffolder/SKILL.md": [
        "scaffold new project",
        "project scaffolding",
        "bootstrap codebase",
        "set up project structure",
        "new project setup",
    ],
    "agents/engineering/tech-architect/technical-feasibility-check/SKILL.md": [
        "check technical feasibility",
        "technical feasibility",
        "can we build this",
        "tech feasibility assessment",
        "feasibility analysis",
    ],
    # tech-lead-pr-reviewer
    "agents/engineering/tech-lead-pr-reviewer/backlog-groomer-eng/SKILL.md": [
        "groom backlog",
        "backlog grooming",
        "backlog refinement",
        "prioritize backlog",
        "engineering backlog review",
    ],
    "agents/engineering/tech-lead-pr-reviewer/dependency-mapper/SKILL.md": [
        "map dependencies",
        "dependency mapping",
        "task dependency map",
        "identify dependencies",
        "dependency graph",
    ],
    "agents/engineering/tech-lead-pr-reviewer/dependency-resolver/SKILL.md": [
        "resolve dependencies",
        "dependency resolution",
        "unblock dependencies",
        "fix dependency issues",
        "dependency conflict resolution",
    ],
    "agents/engineering/tech-lead-pr-reviewer/ga-rollout-executor-planner/SKILL.md": [
        "plan GA rollout",
        "GA rollout execution",
        "general availability rollout",
        "GA launch plan",
        "GA release plan",
    ],
    "agents/engineering/tech-lead-pr-reviewer/go-live-approver-eng/SKILL.md": [
        "approve go-live",
        "go-live approval",
        "launch sign-off",
        "pre-launch approval",
        "release approval",
    ],
    "agents/engineering/tech-lead-pr-reviewer/inter-phase-reviewer-eng/SKILL.md": [
        "review between phases",
        "inter-phase review",
        "phase gate review",
        "phase transition review",
        "milestone review",
    ],
    "agents/engineering/tech-lead-pr-reviewer/internal-demo-runner-eng/SKILL.md": [
        "run internal demo",
        "internal demo",
        "demo to team",
        "engineering demo",
        "sprint demo",
    ],
    "agents/engineering/tech-lead-pr-reviewer/iteration-prioritiser-f/SKILL.md": [
        "prioritize iteration",
        "iteration prioritization",
        "sprint prioritization",
        "rank iteration tasks",
        "iteration backlog prioritization",
    ],
    "agents/engineering/tech-lead-pr-reviewer/iteration-prioritiser-p-eng/SKILL.md": [
        "prioritize engineering iteration",
        "engineering sprint priority",
        "iteration scope priority",
        "rank eng iteration",
        "engineering prioritization",
    ],
    "agents/engineering/tech-lead-pr-reviewer/phase-scope-adjuster-eng/SKILL.md": [
        "adjust phase scope",
        "scope adjustment",
        "phase scope change",
        "trim phase scope",
        "scope negotiation",
    ],
    "agents/engineering/tech-lead-pr-reviewer/spec-translator-eng/SKILL.md": [
        "translate spec to tasks",
        "spec to engineering tasks",
        "break down spec",
        "spec translation",
        "engineering spec breakdown",
    ],
    "agents/engineering/tech-lead-pr-reviewer/sprint-reviewer-eng/SKILL.md": [
        "review sprint",
        "sprint review",
        "sprint retrospective",
        "sprint analysis",
        "end-of-sprint review",
    ],
    # vp-engineering
    "agents/engineering/vp-engineering/architecture-reviewer/SKILL.md": [
        "review architecture",
        "architecture review",
        "system design review",
        "tech architecture audit",
        "architecture assessment",
    ],
    "agents/engineering/vp-engineering/backlog-populator-eng/SKILL.md": [
        "populate engineering backlog",
        "fill engineering backlog",
        "backlog population",
        "create backlog items",
        "seed engineering backlog",
    ],
    "agents/engineering/vp-engineering/effort-estimator-eng/SKILL.md": [
        "estimate effort",
        "engineering effort estimate",
        "story point estimation",
        "task sizing",
        "effort estimation",
    ],
    "agents/engineering/vp-engineering/go-live-approver-lead/SKILL.md": [
        "approve go-live as lead",
        "VP go-live sign-off",
        "exec launch approval",
        "final go-live approval",
        "lead release sign-off",
    ],
    "agents/engineering/vp-engineering/inter-phase-retrospective/SKILL.md": [
        "run phase retrospective",
        "inter-phase retro",
        "phase retrospective",
        "post-phase retro",
        "cross-phase retrospective",
    ],
    "agents/engineering/vp-engineering/milestone-definer-eng/SKILL.md": [
        "define milestones",
        "engineering milestones",
        "set project milestones",
        "milestone planning",
        "milestone definition",
    ],
    "agents/engineering/vp-engineering/phase-planner-eng/SKILL.md": [
        "plan engineering phase",
        "phase planning",
        "engineering phase plan",
        "sprint phase plan",
        "delivery phase planning",
    ],
    "agents/engineering/vp-engineering/risk-register-builder-eng/SKILL.md": [
        "build risk register",
        "engineering risk register",
        "risk tracking setup",
        "create risk log",
        "risk register",
    ],
    "agents/engineering/vp-engineering/scope-boundary-setter-eng/SKILL.md": [
        "set scope boundaries",
        "define project scope",
        "scope boundary definition",
        "scope framing",
        "engineering scope setting",
    ],
    "agents/engineering/vp-engineering/spec-intake-review/SKILL.md": [
        "review spec intake",
        "spec intake",
        "review incoming spec",
        "spec triage",
        "evaluate new spec",
    ],
    "agents/engineering/vp-engineering/team-allocator/SKILL.md": [
        "allocate team",
        "team allocation",
        "assign engineers",
        "resource allocation",
        "engineering staffing",
    ],
    "agents/engineering/vp-engineering/velocity-monitor/SKILL.md": [
        "monitor team velocity",
        "engineering velocity",
        "track sprint velocity",
        "velocity tracking",
        "team throughput monitoring",
    ],
}


def add_triggers_to_file(rel_path: str, triggers: list) -> bool:
    full_path = f"{REPO_ROOT}/{rel_path}"
    content = open(full_path).read()

    if "triggers:" in content:
        print(f"SKIP (already has triggers): {rel_path}")
        return False

    m = re.match(r"^(---\n)(.*?)(\n---\n)", content, re.DOTALL)
    if not m:
        print(f"ERROR: could not find frontmatter in {rel_path}")
        return False

    opening_fence = m.group(1)
    frontmatter_body = m.group(2)
    closing_fence = m.group(3)
    rest = content[m.end():]

    trigger_lines = "\n".join(f'  - "{t}"' for t in triggers)
    triggers_block = f"triggers:\n{trigger_lines}"

    new_frontmatter = f"{opening_fence}{frontmatter_body}\n{triggers_block}{closing_fence}"
    new_content = new_frontmatter + rest

    with open(full_path, "w") as f:
        f.write(new_content)

    print(f"OK: {rel_path}")
    return True


def commit_file(rel_path: str, skill_name: str):
    full_path = f"{REPO_ROOT}/{rel_path}"
    result = subprocess.run(
        ["git", "add", full_path],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"ERROR git add: {result.stderr}")
        return

    result = subprocess.run(
        ["git", "commit", "-m", f"feat: add triggers to {skill_name} skill"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"ERROR git commit: {result.stderr}\n{result.stdout}")
    else:
        print(f"COMMITTED: {skill_name}")


def main():
    for rel_path, triggers in TRIGGER_MAP.items():
        skill_name = rel_path.split("/")[-2]
        changed = add_triggers_to_file(rel_path, triggers)
        if changed:
            commit_file(rel_path, skill_name)


if __name__ == "__main__":
    main()
