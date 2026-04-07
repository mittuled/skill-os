#!/usr/bin/env python3
"""
generate.py — Generates a financial model v1 scaffold with SaaS metrics.

Produces a structured financial model framework with revenue cohorts,
cost structure, cash flow, and SaaS metrics calculations.

Usage:
    python3 generate.py                                    # interactive
    python3 generate.py --arr 1200000 --months 24          # with parameters
    python3 generate.py --json -o model.json               # JSON output
"""

from __future__ import annotations

import json
import math
import sys
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ModelInputs:
    initial_customers: int = 10
    monthly_new_customers: int = 5
    new_customer_growth_rate: float = 0.08  # monthly growth in new customer acquisition
    acv: float = 18000.0
    annual_churn_rate: float = 0.10
    nrr: float = 1.15
    gross_margin_pct: float = 0.78
    cac: float = 8000.0
    months: int = 24
    annual_prepay_pct: float = 0.65
    dso_days: int = 38
    monthly_opex_base: float = 150000.0
    opex_growth_rate: float = 0.03  # monthly


@dataclass
class MonthResult:
    month: int
    new_customers: int
    total_customers: int
    mrr: float
    arr: float
    revenue: float
    cogs: float
    gross_profit: float
    opex: float
    ebitda: float
    cash_in: float
    cash_out: float
    net_cash: float
    cumulative_cash: float
    runway_months: float


def build_model(inputs: ModelInputs) -> list[MonthResult]:
    results: list[MonthResult] = []
    cumulative_cash = 0.0
    monthly_churn_rate = 1.0 - (1.0 - inputs.annual_churn_rate) ** (1.0 / 12.0)
    monthly_expansion = (inputs.nrr ** (1.0 / 12.0)) - 1.0 + monthly_churn_rate

    total_customers = inputs.initial_customers
    mrr = total_customers * (inputs.acv / 12.0)

    for m in range(1, inputs.months + 1):
        # New customers with growth
        new_raw = inputs.monthly_new_customers * ((1 + inputs.new_customer_growth_rate) ** (m - 1))
        new_customers = int(round(new_raw))

        # Churn and expansion on existing base
        churned = total_customers * monthly_churn_rate
        expansion_mrr = mrr * monthly_expansion

        total_customers = total_customers - churned + new_customers
        total_customers = max(0, total_customers)

        new_mrr = new_customers * (inputs.acv / 12.0)
        churn_mrr = churned * (inputs.acv / 12.0)
        mrr = mrr - churn_mrr + new_mrr + expansion_mrr
        arr = mrr * 12.0
        revenue = mrr

        cogs = revenue * (1.0 - inputs.gross_margin_pct)
        gross_profit = revenue - cogs

        opex = inputs.monthly_opex_base * ((1 + inputs.opex_growth_rate) ** (m - 1))
        ebitda = gross_profit - opex

        # Cash flow: annual prepay collected upfront, monthly billed with DSO lag
        annual_portion = new_customers * inputs.acv * inputs.annual_prepay_pct
        monthly_portion = revenue * (1 - inputs.annual_prepay_pct)
        collection_factor = max(0, 1.0 - (inputs.dso_days / 30.0 * 0.1))
        cash_in = annual_portion + monthly_portion * collection_factor

        cac_spend = new_customers * inputs.cac
        cash_out = cogs + opex + cac_spend
        net_cash = cash_in - cash_out
        cumulative_cash += net_cash

        monthly_burn = cash_out - cash_in if cash_out > cash_in else 0
        runway = abs(cumulative_cash / monthly_burn) if monthly_burn > 0 else 999

        results.append(MonthResult(
            month=m,
            new_customers=new_customers,
            total_customers=int(round(total_customers)),
            mrr=round(mrr, 2),
            arr=round(arr, 2),
            revenue=round(revenue, 2),
            cogs=round(cogs, 2),
            gross_profit=round(gross_profit, 2),
            opex=round(opex, 2),
            ebitda=round(ebitda, 2),
            cash_in=round(cash_in, 2),
            cash_out=round(cash_out, 2),
            net_cash=round(net_cash, 2),
            cumulative_cash=round(cumulative_cash, 2),
            runway_months=round(runway, 1),
        ))

    return results


def compute_saas_metrics(results: list[MonthResult], inputs: ModelInputs) -> dict:
    last = results[-1]
    first = results[0]
    ltv = (inputs.acv * inputs.gross_margin_pct) / inputs.annual_churn_rate
    ltv_cac = ltv / inputs.cac if inputs.cac > 0 else 0
    payback_months = inputs.cac / (inputs.acv / 12.0 * inputs.gross_margin_pct)
    total_new_arr = sum(r.new_customers * inputs.acv for r in results)
    total_burn = sum(max(0, r.cash_out - r.cash_in) for r in results)
    burn_multiple = total_burn / total_new_arr if total_new_arr > 0 else 0

    return {
        "ending_arr": last.arr,
        "ending_mrr": last.mrr,
        "ending_customers": last.total_customers,
        "nrr": inputs.nrr,
        "gross_churn_rate": inputs.annual_churn_rate,
        "gross_margin_pct": inputs.gross_margin_pct,
        "ltv": round(ltv, 2),
        "cac": inputs.cac,
        "ltv_cac_ratio": round(ltv_cac, 2),
        "cac_payback_months": round(payback_months, 1),
        "burn_multiple": round(burn_multiple, 2),
        "ending_runway_months": last.runway_months,
    }


def format_currency(v: float) -> str:
    if abs(v) >= 1_000_000:
        return f"${v / 1_000_000:.1f}M"
    if abs(v) >= 1_000:
        return f"${v / 1_000:.0f}K"
    return f"${v:.0f}"


def print_report(results: list[MonthResult], metrics: dict, inputs: ModelInputs) -> None:
    print("=" * 70)
    print("FINANCIAL MODEL V1 — SCAFFOLD OUTPUT")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 70)

    print(f"\n{'REVENUE MODEL':=^70}")
    print(f"  Initial customers: {inputs.initial_customers}")
    print(f"  Monthly new customers (base): {inputs.monthly_new_customers}")
    print(f"  ACV: {format_currency(inputs.acv)}")
    print(f"  NRR: {inputs.nrr:.0%}")
    print(f"  Annual churn: {inputs.annual_churn_rate:.0%}")

    print(f"\n{'MONTHLY SUMMARY (quarterly snapshots)':=^70}")
    print(f"  {'Month':<7} {'Customers':>10} {'MRR':>12} {'ARR':>12} {'EBITDA':>12} {'Cash':>12}")
    print(f"  {'-'*7} {'-'*10} {'-'*12} {'-'*12} {'-'*12} {'-'*12}")
    for r in results:
        if r.month % 3 == 0 or r.month == 1 or r.month == len(results):
            print(f"  {r.month:<7} {r.total_customers:>10} {format_currency(r.mrr):>12} "
                  f"{format_currency(r.arr):>12} {format_currency(r.ebitda):>12} "
                  f"{format_currency(r.cumulative_cash):>12}")

    print(f"\n{'SAAS METRICS':=^70}")
    print(f"  Ending ARR:          {format_currency(metrics['ending_arr'])}")
    print(f"  Ending MRR:          {format_currency(metrics['ending_mrr'])}")
    print(f"  Ending Customers:    {metrics['ending_customers']}")
    print(f"  NRR:                 {metrics['nrr']:.0%}")
    print(f"  Gross Margin:        {metrics['gross_margin_pct']:.0%}")
    print(f"  LTV:                 {format_currency(metrics['ltv'])}")
    print(f"  CAC:                 {format_currency(metrics['cac'])}")
    print(f"  LTV/CAC:             {metrics['ltv_cac_ratio']:.1f}x")
    print(f"  CAC Payback:         {metrics['cac_payback_months']:.0f} months")
    print(f"  Burn Multiple:       {metrics['burn_multiple']:.1f}x")
    print(f"  Runway:              {metrics['ending_runway_months']:.0f} months")


def main() -> None:
    args = sys.argv[1:]
    json_output = "--json" in args
    inputs = ModelInputs()

    # Parse CLI overrides
    for i, arg in enumerate(args):
        if arg == "--arr" and i + 1 < len(args):
            target_arr = float(args[i + 1])
            inputs.acv = target_arr / (inputs.initial_customers + inputs.monthly_new_customers * 12)
        elif arg == "--months" and i + 1 < len(args):
            inputs.months = int(args[i + 1])
        elif arg == "--acv" and i + 1 < len(args):
            inputs.acv = float(args[i + 1])
        elif arg == "--customers" and i + 1 < len(args):
            inputs.initial_customers = int(args[i + 1])

    results = build_model(inputs)
    metrics = compute_saas_metrics(results, inputs)

    if json_output:
        output = {
            "model_inputs": {
                "initial_customers": inputs.initial_customers,
                "monthly_new_customers": inputs.monthly_new_customers,
                "acv": inputs.acv,
                "nrr": inputs.nrr,
                "annual_churn_rate": inputs.annual_churn_rate,
                "gross_margin_pct": inputs.gross_margin_pct,
                "months": inputs.months,
            },
            "monthly_results": [
                {"month": r.month, "customers": r.total_customers,
                 "mrr": r.mrr, "arr": r.arr, "ebitda": r.ebitda,
                 "cumulative_cash": r.cumulative_cash}
                for r in results
            ],
            "saas_metrics": metrics,
        }
        out_file = None
        if "-o" in args:
            idx = args.index("-o") + 1
            if idx < len(args):
                out_file = args[idx]
        text = json.dumps(output, indent=2)
        if out_file:
            Path(out_file).write_text(text + "\n", encoding="utf-8")
            print(f"Model written to {out_file}")
        else:
            print(text)
    else:
        print_report(results, metrics, inputs)


if __name__ == "__main__":
    main()
