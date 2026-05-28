import numpy as np
import pandas as pd

from .reaction_engine import measure_reactions


def _measure_on_split(
    df_full: pd.DataFrame,
    positions: list[int],
    start: int,
    end: int,
    payload: dict,
    candidate: dict,
) -> dict:
    """
    Re-measure a candidate's reactions using only candles in [start, end).
    Positions are rebased to the split slice.
    """
    split_df = df_full.iloc[start:end].reset_index(drop=True)

    split_pos = [
        p - start
        for p in positions
        if start <= p < end
    ]

    min_split_samples = max(
        10,
        payload.get("min_samples", 30) // 3,
    )

    if len(split_pos) < min_split_samples:
        return {
            "status": "insufficient",
            "count": len(split_pos),
        }

    fake = {
        **candidate,
        "match_index": split_pos,
    }

    result = measure_reactions(
        split_df,
        [fake],
        payload,
    )

    if not result:
        return {
            "status": "no_reactions",
            "count": len(split_pos),
        }

    r = result[0]

    return {
        "status": "ok",
        "count": r["valid_count"],
        "dominant_dir": r["dominant_dir"],
        "dir_pct": max(
            r["bull_pct"],
            r["bear_pct"],
        ),
        "mag_atr_mean": r.get("mag_atr_mean"),
        "mag_atr_std": r.get("mag_atr_std"),
    }


def validate_overfit(
    candidates: list[dict],
    df: pd.DataFrame,
    payload: dict,
) -> list[dict]:
    """
    Step 9 — Out-of-sample stability check.

    Splits:
        train
        validation
        oos
    """
    n = len(df)

    val_split = payload.get(
        "validation_split",
        0.2,
    )

    min_dir_pct = payload.get(
        "min_direction_pct",
        65.0,
    )

    dir_grace = payload.get(
        "dir_grace",
        0.80,
    )

    train_end = int(
        n * (1 - 2 * val_split)
    )

    val_end = int(
        n * (1 - val_split)
    )

    splits = {
        "train": (0, train_end),
        "val": (train_end, val_end),
        "oos": (val_end, n),
    }

    total = len(candidates)
    valid = []

    for idx, cand in enumerate(candidates, 1):
        if idx % 100 == 0 or idx == total:
            print(
                f"\r  Validating {idx}/{total} … "
                f"passed: {len(valid)}",
                end="",
                flush=True,
            )

        positions = cand["match_index"]
        split_results = {}

        for split_name, (start, end) in splits.items():
            split_results[split_name] = _measure_on_split(
                df,
                positions,
                start,
                end,
                payload,
                cand,
            )

        ok = [
            v
            for v in split_results.values()
            if v.get("status") == "ok"
        ]

        if len(ok) < 2:
            continue

        dirs = [
            s["dominant_dir"]
            for s in ok
        ]

        dir_pcts = [
            s["dir_pct"]
            for s in ok
        ]

        direction_flipped = len(set(dirs)) > 1

        direction_degraded = any(
            p < min_dir_pct * dir_grace
            for p in dir_pcts
        )

        if direction_flipped or direction_degraded:
            continue

        valid.append(
            {
                **cand,
                "split_results": split_results,
                "overfit_status": "STABLE",
            }
        )

    print()
    return valid