import json
from pathlib import Path
import pandas as pd

from analysis import build_search_space, combo_stats, scan_all_combos
from timing_utils import timed_spinner


def run_search(
    enriched_csv: str = "payload_H1.csv",
    payload_path: str = "payload.json",
):
    # ── Load data ─────────────────────────────────────────
    with timed_spinner(f"Loading enriched data: {enriched_csv}"):
        df = pd.read_csv(enriched_csv, parse_dates=["UTC"])
        df = df.sort_values("UTC").reset_index(drop=True)

    # ── Load payload ──────────────────────────────────────
    payload = json.loads(Path(payload_path).read_text())

    # ── Build search space ────────────────────────────────
    with timed_spinner("Building search space"):
        combos = build_search_space(payload)

    stats = combo_stats(combos)

    print(f"  Total combinations : {stats['total']:,}")
    print(f"  By depth           : {stats['by_depth']}")

    # ── Scan ──────────────────────────────────────────────
    print(
        f"\nScanning {stats['total']:,} combinations "
        f"against {len(df):,} candles …"
    )

    matches = scan_all_combos(df, combos, payload)

    print(
        f"  Passed min_samples="
        f"{payload.get('min_samples', 30)}: "
        f"{len(matches):,} candidates\n"
    )

    if not matches:
        print("No matches found.")
        return df, payload, matches

    # detect key otomatis
    first = matches[0]

    count_key = next(
        k for k in first.keys()
        if "count" in str(k).lower()
    )

    combo_key = next(
        k for k in first.keys()
        if k != count_key
    )

    # sort descending
    sorted_matches = sorted(
        matches,
        key=lambda x: x[count_key],
        reverse=True,
    )

    # ── Top 10 terminal ───────────────────────────────────
    print("Top 10 by match count:")

    for item in sorted_matches[:10]:
        print(
            f"  {item[count_key]:>6} hits | "
            f"{item[combo_key]}"
        )

    # ── Save ALL results ──────────────────────────────────
    pd.DataFrame(sorted_matches).to_csv(
        "all_matches.csv",
        index=False,
        encoding="utf-8",
    )

    print(
        f"\n✓ Saved all {len(sorted_matches):,} matches "
        f"to all_matches.csv"
    )

    return df, payload, sorted_matches


if __name__ == "__main__":
    df, payload, matches = run_search()