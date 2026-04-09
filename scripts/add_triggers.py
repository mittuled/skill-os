#!/usr/bin/env python3
"""
add_triggers.py — Injects triggers: into SKILL.md frontmatter for skills that lack them.
Usage: python3 scripts/add_triggers.py
"""

import os
import re
import subprocess

BASE = "/Users/mittul/Documents/Sidespace/_repos/skill-os/agents"
DIRS = ["marketing", "data-growth"]

# ---------------------------------------------------------------------------
# Trigger definitions — keyed by skill slug (directory name of skill folder)
# ---------------------------------------------------------------------------
TRIGGERS_MAP = {
    # ── marketing / demand-gen-manager ─────────────────────────────────────
    "roadmap-timing-input": [
        "align launch with campaign",
        "roadmap timing input",
        "marketing launch window",
        "schedule product release",
        "campaign calendar alignment",
    ],
    "ad-campaign-builder": [
        "build ad campaign",
        "launch paid campaign",
        "create ad set",
        "set up ads",
        "paid media campaign",
    ],
    "channel-signal-analyst": [
        "analyze channel signals",
        "channel performance audit",
        "which channels are working",
        "evaluate demand channels",
        "channel attribution review",
    ],
    "content-engine-builder-marketing": [
        "build content engine",
        "content production system",
        "scale content output",
        "editorial workflow setup",
        "content ops infrastructure",
    ],
    "funnel-optimizer": [
        "optimize conversion funnel",
        "fix funnel drop-off",
        "improve funnel conversion",
        "funnel audit",
        "reduce funnel leakage",
    ],
    "landing-page-auditor": [
        "audit landing page",
        "review landing page copy",
        "landing page CRO audit",
        "improve landing page",
        "landing page teardown",
    ],
    # ── marketing / event-marketing-manager ────────────────────────────────
    "conference-presence-manager": [
        "manage conference presence",
        "plan conference booth",
        "event sponsorship logistics",
        "conference attendance plan",
        "trade show presence",
    ],
    "event-calendar-planner": [
        "plan event calendar",
        "build events roadmap",
        "annual event schedule",
        "prioritize event calendar",
        "events planning calendar",
    ],
    "sales-kickoff-producer": [
        "produce sales kickoff",
        "plan SKO event",
        "sales kickoff agenda",
        "run sales kickoff",
        "SKO logistics",
    ],
    "user-conference-producer": [
        "produce user conference",
        "plan customer conference",
        "user summit logistics",
        "annual user event",
        "customer conference agenda",
    ],
    "company-offsite-producer": [
        "plan company offsite",
        "produce team retreat",
        "company retreat logistics",
        "all-hands offsite",
        "team offsite planning",
    ],
    "webinar-and-virtual-event-manager": [
        "run webinar",
        "plan virtual event",
        "host online event",
        "webinar logistics",
        "virtual event setup",
    ],
    # ── marketing / social-media-manager ───────────────────────────────────
    "social-listening-analyst": [
        "monitor social mentions",
        "social listening report",
        "brand sentiment analysis",
        "track social conversation",
        "social media monitoring",
    ],
    "influencer-coordination-manager": [
        "manage influencer program",
        "coordinate influencer outreach",
        "influencer campaign setup",
        "partner with influencers",
        "influencer brief",
    ],
    "social-content-calendar-manager": [
        "build social content calendar",
        "plan social posts",
        "social media schedule",
        "content calendar social",
        "schedule social content",
    ],
    "ugc-programme-designer": [
        "design UGC program",
        "user-generated content strategy",
        "build UGC campaign",
        "launch UGC initiative",
        "community content program",
    ],
    # ── marketing / marketing-operations-manager ───────────────────────────
    "marketing-attribution-modeller": [
        "build attribution model",
        "marketing attribution setup",
        "multi-touch attribution",
        "measure marketing ROI",
        "attribution modeling",
    ],
    "email-deliverability-manager": [
        "fix email deliverability",
        "improve email inbox rate",
        "email deliverability audit",
        "reduce email bounce rate",
        "email sender reputation",
    ],
    "campaign-analytics-reporter": [
        "report campaign analytics",
        "campaign performance report",
        "marketing analytics report",
        "summarize campaign results",
        "campaign ROI report",
    ],
    "martech-stack-manager": [
        "manage martech stack",
        "audit marketing tools",
        "evaluate martech vendors",
        "martech consolidation",
        "marketing tool assessment",
    ],
    "lead-scoring-model-builder": [
        "build lead scoring model",
        "define lead score",
        "score marketing leads",
        "lead qualification model",
        "MQL scoring setup",
    ],
    "seo-auditor": [
        "audit SEO",
        "run SEO audit",
        "SEO health check",
        "technical SEO review",
        "organic search audit",
    ],
    # ── marketing / analyst-relations-manager ──────────────────────────────
    "analyst-report-monitor": [
        "monitor analyst reports",
        "track analyst coverage",
        "analyst mention tracking",
        "AR intelligence report",
        "analyst landscape review",
    ],
    "analyst-briefing-scheduler": [
        "schedule analyst briefing",
        "book analyst meeting",
        "plan analyst briefings",
        "AR briefing calendar",
        "analyst outreach schedule",
    ],
    "analyst-inquiry-responder": [
        "respond to analyst inquiry",
        "handle analyst RFI",
        "analyst inquiry response",
        "draft analyst reply",
        "answer analyst questions",
    ],
    "peer-review-platform-manager": [
        "manage review platform",
        "G2 profile management",
        "Gartner Peer Insights program",
        "peer review strategy",
        "customer review collection",
    ],
    "magic-quadrant-strategy": [
        "Gartner Magic Quadrant strategy",
        "MQ positioning plan",
        "analyst quadrant submission",
        "improve Magic Quadrant rank",
        "AR MQ preparation",
    ],
    # ── marketing / developer-relations-lead ───────────────────────────────
    "api-developer-experience-reviewer": [
        "review API developer experience",
        "audit API DX",
        "developer experience review",
        "API usability audit",
        "DX improvement review",
    ],
    "developer-community-signal-extractor": [
        "extract dev community signals",
        "analyze developer feedback",
        "developer sentiment analysis",
        "community signal report",
        "dev forum signal mining",
    ],
    "developer-community-grower": [
        "grow developer community",
        "expand dev community",
        "developer community strategy",
        "build developer ecosystem",
        "dev community growth plan",
    ],
    "developer-experience-reviewer": [
        "review developer experience",
        "DX audit",
        "evaluate developer journey",
        "developer onboarding review",
        "SDK experience review",
    ],
    "developer-feedback-synthesiser": [
        "synthesise developer feedback",
        "summarize dev feedback",
        "developer feedback report",
        "compile developer insights",
        "dev community feedback digest",
    ],
    "developer-gtm-planner": [
        "plan developer GTM",
        "developer go-to-market",
        "dev GTM strategy",
        "technical audience launch plan",
        "developer segment launch",
    ],
    "developer-launch-packager": [
        "package developer launch",
        "prepare dev launch assets",
        "developer launch kit",
        "build developer release pack",
        "dev announcement package",
    ],
    # ── marketing / pr-communications-manager ──────────────────────────────
    "media-relationship-builder": [
        "build media relationships",
        "journalist outreach program",
        "media contact strategy",
        "cultivate press contacts",
        "PR relationship building",
    ],
    "crisis-communications-planner": [
        "plan crisis communications",
        "crisis comms playbook",
        "prepare for PR crisis",
        "crisis response plan",
        "reputational risk comms",
    ],
    "thought-leadership-programme-runner": [
        "run thought leadership program",
        "executive thought leadership",
        "build thought leadership plan",
        "place thought leadership pieces",
        "speaker program management",
    ],
    "earned-media-monitor": [
        "monitor earned media",
        "track press mentions",
        "media coverage report",
        "earned media analysis",
        "PR coverage tracking",
    ],
    "press-release-writer": [
        "write press release",
        "draft press release",
        "create press announcement",
        "news release writing",
        "product launch press release",
    ],
    # ── marketing / lifecycle-email-marketing-manager ──────────────────────
    "email-performance-optimiser": [
        "optimize email performance",
        "improve email open rates",
        "email A/B test",
        "email campaign optimization",
        "email metrics review",
    ],
    "nurture-campaign-builder": [
        "build nurture campaign",
        "create lead nurture sequence",
        "design drip campaign",
        "nurture email series",
        "MQL nurture program",
    ],
    "onboarding-sequence-designer": [
        "design onboarding email sequence",
        "build user onboarding emails",
        "new user email flow",
        "activation email sequence",
        "onboarding drip design",
    ],
    "retention-email-designer": [
        "design retention emails",
        "build re-engagement campaign",
        "win-back email sequence",
        "churn prevention emails",
        "retention email flow",
    ],
    "transactional-email-designer": [
        "design transactional emails",
        "build transactional email templates",
        "order confirmation email",
        "system notification email",
        "transactional email audit",
    ],
    # ── marketing / technical-writer ───────────────────────────────────────
    "documentation-requirements-extractor": [
        "extract documentation requirements",
        "gather docs requirements",
        "define documentation scope",
        "documentation needs analysis",
        "docs requirements gathering",
    ],
    "documentation-accuracy-auditor": [
        "audit documentation accuracy",
        "review docs for errors",
        "documentation accuracy check",
        "fact-check documentation",
        "docs quality audit",
    ],
    "documentation-writer": [
        "write documentation",
        "draft technical docs",
        "create user documentation",
        "write product docs",
        "technical writing",
    ],
    "api-documentation-designer": [
        "design API documentation",
        "create API reference docs",
        "API docs structure",
        "build API docs site",
        "developer reference design",
    ],
    "documentation-scale-planner": [
        "plan documentation at scale",
        "docs scaling strategy",
        "documentation team plan",
        "scale technical writing",
        "docs ops planning",
    ],
    # ── marketing / community-manager ──────────────────────────────────────
    "community-health-grower": [
        "grow community health",
        "improve community engagement",
        "community health metrics",
        "community vitality review",
        "boost community activity",
    ],
    "community-signal-extractor": [
        "extract community signals",
        "mine community insights",
        "community feedback synthesis",
        "community intelligence report",
        "forum signal extraction",
    ],
    "community-led-growth-designer": [
        "design community-led growth",
        "community growth loops",
        "CLG strategy design",
        "community flywheel design",
        "community-led acquisition",
    ],
    "community-launch-planner": [
        "plan community launch",
        "launch community platform",
        "community kickoff plan",
        "community go-live strategy",
        "new community launch",
    ],
    "early-community-builder": [
        "build early community",
        "seed founding members",
        "launch community from scratch",
        "bootstrap community",
        "early adopter community",
    ],
    # ── marketing / vp-marketing ───────────────────────────────────────────
    "demand-gen-planner": [
        "plan demand generation",
        "demand gen strategy",
        "build demand gen plan",
        "revenue pipeline planning",
        "demand generation roadmap",
    ],
    "gtm-activation-marketing": [
        "activate GTM plan",
        "marketing GTM execution",
        "launch GTM campaign",
        "go-to-market activation",
        "GTM readiness marketing",
    ],
    "gtm-planner-marketing": [
        "plan marketing GTM",
        "go-to-market strategy",
        "build GTM plan",
        "product launch planning",
        "GTM marketing strategy",
    ],
    "marketing-audit-orchestrator": [
        "orchestrate marketing audit",
        "run marketing audit",
        "marketing effectiveness review",
        "full marketing audit",
        "marketing health check",
    ],
    # ── marketing / content-marketer ───────────────────────────────────────
    "content-marketing-operations": [
        "manage content marketing ops",
        "content operations setup",
        "content marketing workflow",
        "editorial operations",
        "content production operations",
    ],
    "copywriting-analyst": [
        "analyze copywriting",
        "review marketing copy",
        "copywriting audit",
        "copy performance analysis",
        "messaging effectiveness review",
    ],
    # ── data-growth / analytics-lead ───────────────────────────────────────
    "statistical-significance-tracker": [
        "track statistical significance",
        "check A/B test significance",
        "experiment significance check",
        "call experiment winner",
        "assess test validity",
    ],
    "instrumentation-spec-data": [
        "write instrumentation spec",
        "define tracking spec",
        "analytics tracking specification",
        "data instrumentation plan",
        "event taxonomy spec",
    ],
    "goal-framer-data": [
        "frame analytics goals",
        "define data success metrics",
        "set measurement goals",
        "goal framework data",
        "analytics goal alignment",
    ],
    "alerting-configurator-data": [
        "configure data alerts",
        "set up metric alerts",
        "alerting rules data",
        "threshold alert setup",
        "anomaly alert configuration",
    ],
    "market-sizer-data": [
        "size the market",
        "market sizing analysis",
        "TAM SAM SOM estimate",
        "calculate market opportunity",
        "addressable market sizing",
    ],
    "effort-estimator-data": [
        "estimate analytics effort",
        "data project estimation",
        "analytics work estimation",
        "scope data initiative",
        "effort sizing data",
    ],
    "search-demand-validator": [
        "validate search demand",
        "check keyword search volume",
        "SEO demand validation",
        "organic search opportunity",
        "search demand analysis",
    ],
    "instrumentation-clarity-reviewer": [
        "review instrumentation clarity",
        "audit tracking clarity",
        "event naming review",
        "instrumentation legibility check",
        "tracking schema review",
    ],
    "north-star-metric-reviewer-data": [
        "review north star metric",
        "evaluate north star",
        "north star metric audit",
        "assess primary KPI",
        "validate NSM alignment",
    ],
    "instrumentation-planner-data": [
        "plan data instrumentation",
        "analytics instrumentation plan",
        "tracking plan data",
        "instrumentation roadmap",
        "data collection planning",
    ],
    # ── data-growth / growth-engineer ──────────────────────────────────────
    "paywall-builder": [
        "build paywall",
        "implement paywall",
        "design paywall flow",
        "create subscription gate",
        "monetization paywall",
    ],
    "instrumentation-verifier-prod-growth": [
        "verify production instrumentation",
        "check prod tracking growth",
        "validate live event data growth",
        "production event verification",
        "QA tracking in production",
    ],
    "funnel-analyser-growth": [
        "analyse growth funnel",
        "growth funnel analysis",
        "identify funnel drop-off growth",
        "conversion funnel review",
        "growth conversion analysis",
    ],
    "instrumentation-implementer-growth": [
        "implement growth tracking",
        "add analytics events growth",
        "instrument growth features",
        "code tracking events",
        "growth event implementation",
    ],
    "instrumentation-verifier-growth": [
        "verify growth instrumentation",
        "QA growth tracking",
        "validate analytics events",
        "check event firing growth",
        "instrumentation QA growth",
    ],
    "instrumentation-spec-growth": [
        "write growth instrumentation spec",
        "growth tracking specification",
        "define growth events spec",
        "analytics spec growth",
        "growth event taxonomy",
    ],
    "onboarding-engineer": [
        "engineer onboarding flow",
        "build onboarding experience",
        "implement onboarding steps",
        "onboarding UX engineering",
        "activation flow engineering",
    ],
    "ga-instrumentation-reviewer": [
        "review GA instrumentation",
        "audit Google Analytics setup",
        "GA4 implementation review",
        "validate GA tracking",
        "Google Analytics audit",
    ],
    "landing-page-builder": [
        "build landing page",
        "create landing page",
        "launch landing page",
        "develop conversion page",
        "landing page development",
    ],
    "growth-loop-activator": [
        "activate growth loop",
        "launch growth flywheel",
        "trigger growth loop",
        "growth loop implementation",
        "activate viral loop",
    ],
    "metrics-dashboard-growth": [
        "build growth metrics dashboard",
        "create growth KPI dashboard",
        "growth dashboard setup",
        "visualize growth metrics",
        "growth reporting dashboard",
    ],
    "referral-engine-builder": [
        "build referral engine",
        "create referral program",
        "implement referral system",
        "referral loop setup",
        "viral referral engine",
    ],
    "instrumentation-planner-growth": [
        "plan growth instrumentation",
        "growth tracking plan",
        "analytics plan growth",
        "instrumentation strategy growth",
        "event tracking roadmap growth",
    ],
    "notification-pipeline-builder": [
        "build notification pipeline",
        "set up push notifications",
        "create notification system",
        "notification infrastructure",
        "messaging pipeline setup",
    ],
    # ── data-growth / data-analyst ─────────────────────────────────────────
    "signal-synthesiser-data-p": [
        "synthesise data signals",
        "compile analytics signals",
        "synthesize product data",
        "data signal summary",
        "insight synthesis data",
    ],
    "instrumentation-verifier-data": [
        "verify data instrumentation",
        "QA analytics tracking data",
        "validate event data",
        "check data event firing",
        "instrumentation QA data",
    ],
    "instrumentation-implementer-data": [
        "implement data tracking",
        "add analytics events data",
        "instrument data layer",
        "code analytics events",
        "data event implementation",
    ],
    "instrumentation-verifier-prod-data": [
        "verify production data tracking",
        "production instrumentation QA",
        "validate live analytics data",
        "prod event verification data",
        "QA tracking production data",
    ],
    "data-model-designer-data": [
        "design data model",
        "build data schema",
        "data architecture design",
        "create data model",
        "analytics data modeling",
    ],
    "adoption-tracker-data": [
        "track feature adoption",
        "adoption rate analysis",
        "feature usage tracking",
        "monitor product adoption",
        "adoption metrics dashboard",
    ],
    "sprint-reviewer-data": [
        "review data sprint",
        "analytics sprint review",
        "data team sprint retrospective",
        "sprint output review data",
        "data sprint retrospective",
    ],
    "funnel-analyser": [
        "analyse funnel",
        "funnel analysis",
        "identify funnel drop-off",
        "conversion funnel breakdown",
        "funnel step performance",
    ],
    "metrics-dashboard-builder": [
        "build metrics dashboard",
        "create KPI dashboard",
        "metrics visualization setup",
        "analytics dashboard build",
        "reporting dashboard setup",
    ],
    "signal-synthesiser-data": [
        "synthesise data signals",
        "aggregate analytics signals",
        "data insights synthesis",
        "compile product signals",
        "analytics signal report",
    ],
    # ── data-growth / growth-lead ───────────────────────────────────────────
    "growth-model-designer": [
        "design growth model",
        "build growth framework",
        "growth model architecture",
        "create growth equation",
        "model growth levers",
    ],
    "demand-gen-planner-growth": [
        "plan demand gen growth",
        "growth demand generation plan",
        "demand acquisition strategy",
        "build growth demand plan",
        "growth pipeline planning",
    ],
    "retention-model-hypothesiser": [
        "hypothesise retention model",
        "build retention hypothesis",
        "retention driver analysis",
        "retention model ideation",
        "churn model hypotheses",
    ],
    "mvp-definer-growth": [
        "define growth MVP",
        "scope growth experiment MVP",
        "minimum viable growth test",
        "MVP scope growth",
        "growth MVP definition",
    ],
    "pricing-strategy-growth": [
        "define pricing strategy",
        "growth pricing plan",
        "pricing model design",
        "monetization strategy growth",
        "pricing approach growth",
    ],
    "pricing-finaliser-growth": [
        "finalise growth pricing",
        "lock pricing growth",
        "confirm pricing tiers",
        "finalize pricing model",
        "pricing sign-off growth",
    ],
    "activation-signal-definer": [
        "define activation signal",
        "set activation criteria",
        "activation metric definition",
        "identify activation moment",
        "activation event definition",
    ],
    "distribution-viability-check": [
        "check distribution viability",
        "assess distribution channels",
        "validate growth channels",
        "distribution channel audit",
        "channel viability review",
    ],
    "activation-moment-validator": [
        "validate activation moment",
        "verify aha moment",
        "confirm activation signal",
        "activation moment review",
        "aha moment validation",
    ],
    "growth-loop-optimiser": [
        "optimise growth loop",
        "improve growth flywheel",
        "growth loop tuning",
        "refine viral loop",
        "growth loop performance",
    ],
}


def inject_triggers(content, triggers):
    """Insert triggers: block before the closing --- of the frontmatter."""
    raw_lines = content.split('\n')

    # Find the two --- markers
    first_dash = None
    second_dash = None
    for i, line in enumerate(raw_lines):
        if line.strip() == '---':
            if first_dash is None:
                first_dash = i
            elif second_dash is None:
                second_dash = i
                break

    if first_dash is None or second_dash is None:
        return None  # Can't find frontmatter

    # Build triggers block
    trigger_lines = ['triggers:']
    for t in triggers:
        trigger_lines.append(f'  - "{t}"')

    # Insert before second_dash
    new_lines = raw_lines[:second_dash] + trigger_lines + raw_lines[second_dash:]
    return '\n'.join(new_lines)


def get_skill_slug(filepath):
    return os.path.basename(os.path.dirname(filepath))


def process_file(filepath):
    skill_slug = get_skill_slug(filepath)
    triggers = TRIGGERS_MAP.get(skill_slug)
    if triggers is None:
        print(f"  SKIP (no triggers defined): {skill_slug}")
        return False

    with open(filepath, 'r') as f:
        content = f.read()

    if 'triggers:' in content:
        print(f"  SKIP (already has triggers): {skill_slug}")
        return False

    new_content = inject_triggers(content, triggers)
    if new_content is None:
        print(f"  ERROR (no frontmatter found): {filepath}")
        return False

    with open(filepath, 'w') as f:
        f.write(new_content)

    print(f"  UPDATED: {skill_slug}")
    return True


def commit_file(filepath, skill_slug):
    repo = "/Users/mittul/Documents/Sidespace/_repos/skill-os"
    rel = os.path.relpath(filepath, repo)
    msg = f"feat: add triggers to {skill_slug} skill"
    subprocess.run(['git', '-C', repo, 'add', rel], check=True)
    subprocess.run(['git', '-C', repo, 'commit', '-m', msg], check=True)
    print(f"  COMMITTED: {msg}")


def main():
    files_to_process = []
    for d in DIRS:
        path = os.path.join(BASE, d)
        for root, _, files in os.walk(path):
            for f in files:
                if f == "SKILL.md":
                    fp = os.path.join(root, f)
                    with open(fp, 'r') as fh:
                        content = fh.read()
                    if 'triggers:' not in content:
                        files_to_process.append(fp)

    print(f"Files to process: {len(files_to_process)}\n")
    updated = 0
    for fp in sorted(files_to_process):
        skill_slug = get_skill_slug(fp)
        changed = process_file(fp)
        if changed:
            commit_file(fp, skill_slug)
            updated += 1

    print(f"\nDone. Updated and committed {updated} files.")


if __name__ == '__main__':
    main()
