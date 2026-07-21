"""Report generation for the ranked analysis results.

This module turns the ranked candidates into human-readable output and export
files. It is the final stage of the execution pipeline and is responsible for
making the raw statistics understandable to a human operator.
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def _resolve_output_dir(output_dir: str | Path) -> Path:
    if isinstance(output_dir, Path):
        path = output_dir
    else:
        path = Path(output_dir)

    if path.is_absolute():
        return path
    return (PROJECT_ROOT / path).resolve()


def _split_summary(split_results: dict) -> str:
    """Format the per-split validation results as a readable block."""
    lines = []
    for name, s in split_results.items():
        if s.get("status") == "ok":
            lines.append(
                f"    {name:<6}  {s['count']:>4} samples  "
                f"{s['dominant_dir']:<8}  {s['dir_pct']:.1f}%  "
                f"mag_atr={s.get('mag_atr_mean') or 'n/a'}"
            )
        else:
            lines.append(f"    {name:<6}  [{s.get('status', '?')}]")
    return "\n".join(lines)


def _interpret(c: dict) -> str:
    """Create a natural-language interpretation of a candidate's statistics."""
    dom = c["dominant_dir"].upper()
    pct = c["dir_consistency"]
    mag = c.get("mag_atr_mean", "n/a")
    cv = c.get("mag_cv", "n/a")

    cv_label = "low variance" if isinstance(cv, float) and cv < 0.4 else \
               "moderate variance" if isinstance(cv, float) and cv < 0.6 else "high variance"
    mag_label = f"{mag:.2f} ATR" if isinstance(mag, float) else "n/a"

    return (
        f'When [{c["label"]}] occurs, price historically reacts {dom} '
        f'{pct:.1f}% of the time with an average move of {mag_label} '
        f'({cv_label}) and stable repetition across validation splits.'
    )


def generate_report(
    ranked: list[dict],
    payload: dict,
    output_dir: str = ".",
    top_n: int = 50,
) -> None:
    """Print the final summary and save markdown and CSV artifacts.

    Purpose:
        Emit the final ranked results to the terminal and write the report files.

    Inputs:
        ranked: Candidates sorted by consistency_score.
        payload: Configuration used to generate the report.
        output_dir: Directory where artifacts will be written.
        top_n: Number of ranked candidates to include in the report.

    Outputs:
        Writes report.md and final_results.csv into output_dir.

    Side effects:
        Creates directories and writes files.

    Algorithm:
        The function selects the top N candidates, prints a compact terminal
        summary, and writes a markdown report plus CSV table. The markdown report
        includes the same metrics that appear in the example summary:
        - Match Count
        - Direction %
        - Mag ATR Mean
        - Mag CV
        - Persistence
        - Overfit Status
    """
    output_dir = _resolve_output_dir(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    results = ranked[:top_n]

    # Terminal summary.
    print(f"\n{'='*70}")
    print(f"  ANALYSIS RESULTS  —  Top {len(results)} consistent conditions")
    print(f"{'='*70}\n")

    for i, c in enumerate(results, 1):
        print(f"#{i:>3}  [{c['consistency_score']:.4f}]  {c['label']}")
        print(
            f"       samples={c['valid_count']}  "
            f"dir={c['dominant_dir']} {c['dir_consistency']:.1f}%  "
            f"mag_atr={c.get('mag_atr_mean','?')}  cv={c.get('mag_cv','?')}  "
            f"freq={c.get('freq_pct','?')}%  timing={c.get('timing_mean','?')} candles"
        )
        print(f"       {_interpret(c)}\n")

    # Markdown report.
    md_path = output_dir / "report.md"
    lines = [
        "# Market Condition Analysis Report\n",
        f"**Lookahead:** {payload.get('lookahead')} candles  ",
        f"**Min direction:** {payload.get('min_direction_pct')}%  ",
        f"**Max mag CV:** {payload.get('max_mag_cv')}  \n",
        "---\n",
    ]

    for i, c in enumerate(results, 1):
        sp = _split_summary(c.get("split_results", {}))
        lines += [
            f"## #{i} — `{c['label']}`\n",
            f"| Field | Value |",
            f"|---|---|",
            f"| Consistency Score | **{c['consistency_score']:.4f}** |",
            f"| Match Count | {c['valid_count']} |",
            f"| Dominant Direction | {c['dominant_dir'].upper()} |",
            f"| Direction % | {c['dir_consistency']:.1f}% |",
            f"| Mag ATR Mean | {c.get('mag_atr_mean','n/a')} |",
            f"| Mag ATR Std | {c.get('mag_atr_std','n/a')} |",
            f"| Mag CV | {c.get('mag_cv','n/a')} |",
            f"| Timing (candles) | {c.get('timing_mean','n/a')} |",
            f"| Persistence | {c.get('persistence_mean','n/a')} |",
            f"| Frequency | {c.get('freq_pct','n/a')}% |",
            f"| Overfit Status | {c.get('overfit_status','?')} |\n",
            f"**Split Validation:**\n```\n{sp}\n```\n",
            f"> {_interpret(c)}\n",
            "---\n",
        ]

    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"✓ Report saved: {md_path}")

    # CSV summary.
    csv_path = output_dir / "final_results.csv"
    skip = {"reactions", "match_index", "split_results"}
    pd.DataFrame([
        {k: v for k, v in c.items() if k not in skip}
        for c in results
    ]).to_csv(csv_path, index=False)
    print(f"✓ CSV saved:    {csv_path}")