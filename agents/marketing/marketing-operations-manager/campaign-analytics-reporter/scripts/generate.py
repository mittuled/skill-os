#!/usr/bin/env python3
"""
generate.py — Generate weekly campaign performance report with spend, leads, and CAC by channel.

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

# Standard performance benchmarks by channel
BENCHMARKS = {
    "paid_search": {"ctr_min": 0.03, "conversion_rate_min": 0.05, "cac_max_usd": 2000},
    "paid_social": {"ctr_min": 0.01, "conversion_rate_min": 0.02, "cac_max_usd": 3000},
    "email": {"open_rate_min": 0.20, "click_rate_min": 0.02, "cac_max_usd": 500},
    "content": {"conversion_rate_min": 0.02, "cac_max_usd": 1500},
    "webinar": {"attendance_rate_min": 0.40, "cac_max_usd": 1000},
    "organic_search": {"cac_max_usd": 800},
    "referral": {"cac_max_usd": 600},
    "default": {"cac_max_usd": 2000},
}

# Performance status thresholds
PERFORMING_WELL = "PERFORMING"
NEEDS_ATTENTION = "NEEDS_ATTENTION"
UNDERPERFORMING = "UNDERPERFORMING"


def validate_input(data: dict) -> list[str]:
    errors = []
    if "company_name" not in data:
        errors.append("Missing required field: company_name")
    if "report_period" not in data:
        errors.append("Missing required field: report_period")
    if "channels" not in data or not isinstance(data["channels"], list):
        errors.append("Missing required field: channels (list of channel performance data)")
    return errors


def generate_campaign_report(data: dict) -> dict:
    errors = validate_input(data)
    if errors:
        return {"error": errors, "result": None}

    company = data["company_name"]
    period = data["report_period"]
    channels = data["channels"]
    targets = data.get("targets", {})

    # Process each channel
    channel_results = []
    total_spend = 0
    total_leads = 0
    total_mqls = 0
    total_sqls = 0
    total_pipeline = 0
    underperforming = []

    for ch in channels:
        channel_type = ch.get("channel_type", "default")
        spend = ch.get("spend_usd", 0)
        leads = ch.get("leads", 0)
        mqls = ch.get("mqls", 0)
        sqls = ch.get("sqls", 0)
        pipeline_usd = ch.get("pipeline_usd", 0)
        impressions = ch.get("impressions", 0)
        clicks = ch.get("clicks", 0)

        # Compute derived metrics
        cac = round(spend / sqls) if sqls > 0 else None
        cpl = round(spend / leads) if leads > 0 else None
        ctr = round(clicks / impressions * 100, 2) if impressions > 0 else None
        mql_rate = round(mqls / leads * 100, 1) if leads > 0 else None
        sql_rate = round(sqls / mqls * 100, 1) if mqls > 0 else None
        roi = round((pipeline_usd - spend) / spend * 100, 1) if spend > 0 else None

        # Assess performance
        benchmark = BENCHMARKS.get(channel_type, BENCHMARKS["default"])
        cac_ok = cac is None or cac <= benchmark["cac_max_usd"]
        status = PERFORMING_WELL if cac_ok else NEEDS_ATTENTION
        if cac and cac > benchmark["cac_max_usd"] * 1.5:
            status = UNDERPERFORMING

        entry = {
            "channel": ch.get("channel_name", channel_type),
            "channel_type": channel_type,
            "spend_usd": spend,
            "leads": leads,
            "mqls": mqls,
            "sqls": sqls,
            "pipeline_usd": pipeline_usd,
            "cpl_usd": cpl,
            "cac_usd": cac,
            "mql_rate_pct": mql_rate,
            "sql_rate_pct": sql_rate,
            "roi_pct": roi,
            "ctr_pct": ctr,
            "status": status,
        }
        channel_results.append(entry)
        total_spend += spend
        total_leads += leads
        total_mqls += mqls
        total_sqls += sqls
        total_pipeline += pipeline_usd
        if status == UNDERPERFORMING:
            underperforming.append(entry)

    # Sort by pipeline contribution desc
    channel_results.sort(key=lambda x: x["pipeline_usd"], reverse=True)

    # Overall metrics
    blended_cac = round(total_spend / total_sqls) if total_sqls > 0 else None
    overall_roi = round((total_pipeline - total_spend) / total_spend * 100, 1) if total_spend > 0 else None

    # Target comparison
    target_mqls = targets.get("mqls", 0)
    target_pipeline = targets.get("pipeline_usd", 0)
    mql_attainment = round(total_mqls / target_mqls * 100, 1) if target_mqls > 0 else None
    pipeline_attainment = round(total_pipeline / target_pipeline * 100, 1) if target_pipeline > 0 else None

    return {
        "error": None,
        "result": {
            "company": company,
            "report_period": period,
            "total_spend_usd": total_spend,
            "total_leads": total_leads,
            "total_mqls": total_mqls,
            "total_sqls": total_sqls,
            "total_pipeline_usd": total_pipeline,
            "blended_cac_usd": blended_cac,
            "overall_roi_pct": overall_roi,
            "mql_attainment_pct": mql_attainment,
            "pipeline_attainment_pct": pipeline_attainment,
            "channel_results": channel_results,
            "underperforming_channels": underperforming,
            "summary": (
                f"Campaign report for {company} ({period}): "
                f"${total_spend:,.0f} spend, {total_mqls} MQLs, {total_sqls} SQLs, "
                f"${total_pipeline:,.0f} pipeline. Blended CAC: ${blended_cac:,.0f}. "
                f"{len(underperforming)} underperforming channel(s)."
                if blended_cac else
                f"Campaign report for {company} ({period}): ${total_spend:,.0f} spend, {total_mqls} MQLs."
            ),
        },
    }


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"Invalid JSON: {exc}"}))
        sys.exit(1)
    result = generate_campaign_report(data)
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
