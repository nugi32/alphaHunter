import json
from pathlib import Path
import pandas as pd

from analysis import (
    build_search_space, combo_stats, scan_all_combos,
    measure_reactions,
    run_consistency_filter,
    validate_overfit,
    rank_candidates,
    generate_report,
)
from timing_utils import timed_spinner
from analysis.consistency import diagnose_thresholds

def run_pipeline(
    enriched_csv: str = "payload_H1.csv",
    payload_path: str = "payload.json",
    output_dir:   str = "results",
):
    df      = pd.read_csv(enriched_csv, parse_dates=["UTC"])
    df      = df.sort_values("UTC").reset_index(drop=True)
    payload = json.loads(Path(payload_path).read_text())

    # ── Step 4+5 ──────────────────────────────────────────
    with timed_spinner("Building search space"):
        combos = build_search_space(payload)
    stats = combo_stats(combos)
    print(f"  Combinations: {stats['total']:,}  |  by depth: {stats['by_depth']}")

    print(f"\nStep 5 — Scanning {stats['total']:,} combos …")
    matches = scan_all_combos(df, combos, payload)
    print(f"  Candidates after min_samples: {len(matches):,}\n")

    # ── Step 6 ────────────────────────────────────────────
    print("Step 6 — Measuring price reactions …")
    enriched = measure_reactions(df, matches, payload)
    print(f"  Enriched: {len(enriched):,}\n")
    
    diagnose_thresholds(enriched)
    with timed_spinner("Step 7+8 — Consistency + frequency filter"):
        consistent = run_consistency_filter(enriched, payload, total_candles=len(df))
    print(f"  Passed consistency: {len(consistent):,}\n")

    # ── Step 7+8 ──────────────────────────────────────────
    with timed_spinner("Step 7+8 — Consistency + frequency filter"):
        consistent = run_consistency_filter(enriched, payload, total_candles=len(df))
    print(f"  Passed consistency: {len(consistent):,}\n")

    # ── Step 9 ────────────────────────────────────────────
    print("Step 9 — Overfit validation …")
    validated = validate_overfit(consistent, df, payload)
    print(f"  Stable candidates: {len(validated):,}\n")

    # ── Step 10 ───────────────────────────────────────────
    with timed_spinner("Step 10 — Ranking"):
        ranked = rank_candidates(validated, payload)

    # ── Step 11 ───────────────────────────────────────────
    generate_report(ranked, payload, output_dir=output_dir)

    return ranked


if __name__ == "__main__":
    run_pipeline()