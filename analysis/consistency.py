import numpy as np
import pandas as pd


def diagnose_thresholds(
    enriched: list[dict],
) -> None:
    """
    Print percentile distribution
    BEFORE filtering.
    """

    dir_pcts = [
        max(
            m["bull_pct"],
            m["bear_pct"],
        )
        for m in enriched
    ]

    mag_means = [
        m["mag_atr_mean"]
        for m in enriched
        if m.get(
            "mag_atr_mean"
        )
    ]

    mag_cvs = [
        m["mag_atr_std"]
        / m["mag_atr_mean"]
        for m in enriched
        if (
            m.get(
                "mag_atr_mean"
            )
            and m[
                "mag_atr_mean"
            ]
            > 0
            and m.get(
                "mag_atr_std"
            )
            is not None
        )
    ]

    counts = [
        m["valid_count"]
        for m in enriched
    ]

    def _pct(
        label,
        arr,
    ):
        a = np.array(arr)

        print(
            f"\n  {label} "
            f"(n={len(a)})"
        )

        for p in [
            10,
            25,
            50,
            75,
            90,
            95,
            99,
        ]:
            print(
                f"    p{p:<3} = "
                f"{np.percentile(a, p):.4f}"
            )

        print(
            f"    max={a.max():.4f} "
            f"min={a.min():.4f}"
        )

    print("\n" + "=" * 55)
    print("THRESHOLD DIAGNOSTICS")
    print("=" * 55)

    _pct(
        "Direction %",
        dir_pcts,
    )

    _pct(
        "Mag ATR mean",
        mag_means,
    )

    _pct(
        "Mag CV",
        mag_cvs,
    )

    _pct(
        "Match count",
        counts,
    )

    print()


def run_consistency_filter(
    enriched: list[dict],
    payload: dict,
    total_candles: int,
) -> list[dict]:
    min_dir_pct = payload.get(
        "min_direction_pct",
        55.0,
    )

    max_mag_cv = payload.get(
        "max_mag_cv",
        0.85,
    )

    min_freq_pct = payload.get(
        "min_freq_pct",
        0.05,
    )

    max_freq_pct = payload.get(
        "max_freq_pct",
        5.0,
    )

    passed = []

    for m in enriched:
        dir_pct = max(
            m["bull_pct"],
            m["bear_pct"],
        )

        freq_pct = (
            m["valid_count"]
            / total_candles
            * 100
            if total_candles
            else None
        )

        # Step 7A
        if dir_pct < min_dir_pct:
            continue

        # Step 7B
        mean = (
            m.get(
                "mag_atr_mean"
            )
            or 0
        )

        std = (
            m.get(
                "mag_atr_std"
            )
            or 0
        )

        cv = (
            std / mean
            if mean > 0
            else np.nan
        )

        if (
            not np.isnan(cv)
            and cv > max_mag_cv
        ):
            continue

        # Step 8
        if freq_pct is not None:
            if (
                freq_pct
                < min_freq_pct
            ):
                continue

            if (
                freq_pct
                > max_freq_pct
            ):
                continue

        passed.append(
            {
                **m,
                "dir_consistency": round(
                    dir_pct,
                    2,
                ),
                "mag_cv": round(
                    cv,
                    4,
                )
                if not np.isnan(
                    cv
                )
                else None,
                "freq_pct": round(
                    freq_pct,
                    4,
                )
                if freq_pct
                is not None
                else None,
            }
        )

    return passed