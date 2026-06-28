"""Command-line entry point for AlphaHunter.

This module orchestrates the full analysis pipeline:

1. Load market data for a timeframe.
2. Enrich the candles with technical indicators and patterns.
3. Build a search space of condition combinations.
4. Scan the full dataset for matching combinations.
5. Measure how price reacts after each match.
6. Filter candidates by statistical consistency and frequency.
7. Validate stability over multiple time splits.
8. Rank the surviving candidates and write reports.

The implementation intentionally keeps the execution flow explicit so new
contributors can follow the business logic end to end.
"""

import argparse
import copy
import json
from pathlib import Path
from typing import Optional

import pandas as pd

from prepare_utils import prepare
from loader import load_tf
from timing_utils import timed_spinner
from analysis import (
    build_search_space, combo_stats, scan_all_combos,
    measure_reactions,
    run_consistency_filter,
    validate_overfit,
    rank_candidates,
    generate_report,
)
from analysis.consistency import diagnose_thresholds


# ── Step 3: Prepare ───────────────────────────────────────────────────────────

def cmd_prepare(
    timeframe:   str,
    output_path: Optional[str] = None,
    limit:       Optional[int] = None,
) -> str:
    """Create an enriched CSV payload for a timeframe.

    Purpose:
        Load raw market data, apply every indicator and pattern module, and
        persist the enriched candles to disk for later analysis.

    Inputs:
        timeframe: The requested timeframe key such as M1, H1, or D1.
        output_path: Optional output filename; defaults to payload_{timeframe}.csv.
        limit: Optional row limit used to reduce the amount of data loaded.

    Outputs:
        The path to the generated CSV file.

    Side effects:
        Writes the enriched dataframe to disk.

    Algorithm:
        1. Load the raw candles for the timeframe.
        2. Apply all indicator and pattern modules in sequence.
        3. Persist the resulting dataframe to CSV.

    Assumptions:
        The data files referenced by loader.py exist locally.
    """
    if output_path is None:
        output_path = f"payload_{timeframe}.csv"

    with timed_spinner(f"Loading timeframe data: {timeframe}"):
        df = load_tf(timeframe, limit=limit)

    with timed_spinner("Applying indicators and patterns"):
        df = prepare(df)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"  Payload saved: {output_path} ({len(df):,} rows)")
    return output_path


# ── Steps 4–11: Analysis pipeline ────────────────────────────────────────────

def run_pipeline(
    df:         pd.DataFrame,
    payload:    dict,
    output_dir: str = "results",
) -> list[dict]:
    """Run the full brute-force analysis pipeline for one payload configuration.

    Purpose:
        Execute the complete search-and-rank workflow from search-space
        construction to report generation.

    Inputs:
        df: An enriched dataframe with OHLCV columns and derived indicators.
        payload: The analysis configuration, including conditions, limits, and
            lookahead settings.
        output_dir: Directory where the report artifacts should be written.

    Outputs:
        A ranked list of candidate condition combinations.

    Side effects:
        Prints progress information and writes report files to disk.

    Algorithm:
        The function follows the pipeline described in the project docs:
        search-space generation -> candidate scanning -> reaction measurement ->
        consistency filtering -> overfit validation -> ranking -> report generation.
    """
    lookahead = payload.get("lookahead", 5)
    depth     = payload.get("max_depth", 3)

    print(f"\n{'='*60}")
    print(f"  lookahead={lookahead}  |  max_depth={depth}  |  output → {output_dir}")
    print(f"{'='*60}")

    # Step 4+5: Generate the condition combinations and scan them against the
    # dataframe. This is the brute-force engine of the project.
    with timed_spinner("Building search space"):
        combos = build_search_space(payload)
    stats = combo_stats(combos)
    print(f"  Combinations: {stats['total']:,}  |  by depth: {stats['by_depth']}")

    print(f"\nStep 5 — Scanning {stats['total']:,} combos …")
    matches = scan_all_combos(df, combos, payload)
    print(f"  Candidates after min_samples: {len(matches):,}\n")

    if not matches:
        print("  No matches — skipping remaining steps.\n")
        return []

    # Step 6: Measure how price reacts after each candidate condition fires.
    print("Step 6 — Measuring price reactions …")
    enriched = measure_reactions(df, matches, payload)
    print(f"  Enriched: {len(enriched):,}\n")

    diagnose_thresholds(enriched)

    # Steps 7+8: Remove candidates that are too noisy, too rare, or too volatile
    # in their measured reactions.
    with timed_spinner("Step 7+8 — Consistency + frequency filter"):
        consistent = run_consistency_filter(enriched, payload, total_candles=len(df))
    print(f"  Passed consistency: {len(consistent):,}\n")

    if not consistent:
        print("  Nothing passed consistency — skipping validation.\n")
        return []

    # Step 9: Check that the winning patterns remain stable across train/val/oos
    # time splits rather than only fitting one slice of history.
    print("Step 9 — Overfit validation …")
    validated = validate_overfit(consistent, df, payload)
    print(f"  Stable candidates: {len(validated):,}\n")

    if not validated:
        print("  Nothing passed validation.\n")
        return []

    # Step 10: Score the survivors by a weighted mix of direction consistency,
    # magnitude consistency, frequency, sample size, and split stability.
    with timed_spinner("Step 10 — Ranking"):
        ranked = rank_candidates(validated, payload)

    # Step 11: Save the final report artifacts to disk.
    generate_report(ranked, payload, output_dir=output_dir)

    return ranked


def cmd_run(
    timeframe:    str,
    payload_path: str        = "payload.json",
    output_root:  str        = "results",
    lookaheads:   Optional[list[int]]  = None,
    enriched_csv: Optional[str]        = None,
) -> None:
    """Run the analysis pipeline for one or more lookahead values.

    Purpose:
        Load an enriched CSV, run the analysis for each requested lookahead, and
        summarise the outcomes in a sweep CSV.

    Inputs:
        timeframe: The timeframe name used to locate the default CSV file.
        payload_path: JSON file containing the analysis configuration.
        output_root: Directory where per-lookahead result folders will be created.
        lookaheads: Optional list of lookahead values to sweep.
        enriched_csv: Optional explicit CSV path; otherwise a default is used.

    Side effects:
        Reads the enriched payload CSV and writes sweep summaries to disk.
    """
    if enriched_csv is None:
        enriched_csv = f"payload_{timeframe}.csv"

    if not Path(enriched_csv).exists():
        raise FileNotFoundError(
            f"Enriched CSV not found: {enriched_csv}\n"
            f"Run 'prepare' first:  python main.py prepare --tf {timeframe}"
        )

    print(f"Loading: {enriched_csv}")
    df           = pd.read_csv(enriched_csv, parse_dates=["UTC"])
    df           = df.sort_values("UTC").reset_index(drop=True)
    base_payload = json.loads(Path(payload_path).read_text())

    if lookaheads is None:
        lookaheads = [base_payload.get("lookahead", 5)]

    summary: list[dict] = []

    for la in lookaheads:
        payload    = copy.deepcopy(base_payload)
        payload["lookahead"] = la
        out_dir    = f"{output_root}/la{la}"
        ranked     = run_pipeline(df, payload, output_dir=out_dir)
        summary.append({
            "lookahead":        la,
            "max_depth":        payload.get("max_depth", 3),
            "valid_conditions": len(ranked),
            "top_score":        ranked[0]["consistency_score"] if ranked else None,
            "top_condition":    ranked[0]["label"]             if ranked else None,
        })

    # Sweep summary is a lightweight aggregate used to compare multiple
    # lookahead values at a glance.
    if len(lookaheads) > 1:
        print(f"\n{'='*60}")
        print("  SWEEP SUMMARY")
        print(f"{'='*60}")
        for row in summary:
            print(
                f"  la={row['lookahead']:<3}  depth={row['max_depth']}  "
                f"valid={row['valid_conditions']:<4}  "
                f"top={row['top_score']}  {row['top_condition'] or '—'}"
            )
        Path(output_root).mkdir(parents=True, exist_ok=True)
        pd.DataFrame(summary).to_csv(f"{output_root}/sweep_summary.csv", index=False)
        print(f"\n✓ Sweep summary → {output_root}/sweep_summary.csv")


# ── CLI ───────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    """Construct the CLI parser for prepare/run/all commands."""
    TF_CHOICES = ["M1", "M5", "M15", "H1", "H4", "D1", "W1", "MN1"]

    parser = argparse.ArgumentParser(
        prog="main",
        description="AlphaHunter — candlestick pattern brute-force analyser",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    # ── prepare ───────────────────────────────────────────
    p = sub.add_parser("prepare", help="Load raw data and generate enriched CSV.")
    p.add_argument("--tf",     default="H1", choices=TF_CHOICES)
    p.add_argument("--output", default=None, help="Output CSV path.")
    p.add_argument("--limit",  type=int, default=None, help="Max candles to load.")

    # ── run ───────────────────────────────────────────────
    r = sub.add_parser("run", help="Run analysis pipeline on enriched CSV.")
    r.add_argument("--tf",      default="H1",          choices=TF_CHOICES)
    r.add_argument("--csv",     default=None,          help="Override enriched CSV path.")
    r.add_argument("--payload", default="payload.json",help="Payload config path.")
    r.add_argument("--out",     default="results",     help="Output directory root.")
    r.add_argument(
        "--lookaheads",
        nargs="+", type=int, default=None,
        metavar="N",
        help="One or more lookahead values to sweep. E.g: --lookaheads 3 5 10",
    )

    # ── all ───────────────────────────────────────────────
    a = sub.add_parser("all", help="Prepare + run in one step.")
    a.add_argument("--tf",      default="H1",          choices=TF_CHOICES)
    a.add_argument("--limit",   type=int, default=None)
    a.add_argument("--payload", default="payload.json")
    a.add_argument("--out",     default="results")
    a.add_argument(
        "--lookaheads",
        nargs="+", type=int, default=None,
        metavar="N",
    )

    return parser


def main() -> None:
    """Parse CLI arguments and dispatch to the requested command."""
    parser = build_parser()
    args   = parser.parse_args()

    if args.cmd == "prepare":
        cmd_prepare(args.tf, args.output, args.limit)

    elif args.cmd == "run":
        cmd_run(
            timeframe    = args.tf,
            payload_path = args.payload,
            output_root  = args.out,
            lookaheads   = args.lookaheads,
            enriched_csv = args.csv,
        )

    elif args.cmd == "all":
        csv_path = cmd_prepare(args.tf, limit=args.limit)
        cmd_run(
            timeframe    = args.tf,
            payload_path = args.payload,
            output_root  = args.out,
            lookaheads   = args.lookaheads,
            enriched_csv = csv_path,
        )


if __name__ == "__main__":
    main()