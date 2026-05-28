import numpy as np
import pandas as pd


def measure_reactions(
    df: pd.DataFrame,
    matches: list[dict],
    payload: dict,
    atr_col: str = "ATR_14",
    neutral_threshold: float = 0.2,
    verbose: bool = True,
) -> list[dict]:
    """
    Vectorised reaction measurement.

    Direction = NET close after lookahead candles.
    Magnitude = max excursion during window.
    """

    lookahead = payload.get("lookahead", 5)
    n_df = len(df)
    total = len(matches)

    closes = df["Close"].values.astype(float)
    highs = df["High"].values.astype(float)
    lows = df["Low"].values.astype(float)

    atrs = (
        df[atr_col].values.astype(float)
        if atr_col in df.columns
        else np.full(n_df, np.nan)
    )

    offsets = np.arange(1, lookahead + 1)

    enriched = []

    for idx, match in enumerate(matches, 1):
        if verbose and (idx % 200 == 0 or idx == total):
            print(
                f"\r  Measuring {idx}/{total} … valid: {len(enriched)}",
                end="",
                flush=True,
            )

        positions = np.asarray(
            match["match_index"],
            dtype=int,
        )

        positions = positions[
            positions + lookahead < n_df
        ]

        if len(positions) == 0:
            continue

        idx_matrix = (
            positions.reshape(-1, 1)
            + offsets
        )

        fut_highs = np.asarray(
            highs[idx_matrix],
            dtype=np.float64,
        )

        fut_lows = np.asarray(
            lows[idx_matrix],
            dtype=np.float64,
        )

        fut_closes = np.asarray(
            closes[idx_matrix],
            dtype=np.float64,
        )

        entry_close = np.asarray(
            closes[positions],
            dtype=np.float64,
        )

        entry_atr = np.asarray(
            atrs[positions],
            dtype=np.float64,
        )

        # ── Magnitude ───────────────────────────────
        max_high = fut_highs.max(axis=1)
        min_low = fut_lows.min(axis=1)

        up_move = max_high - entry_close
        down_move = entry_close - min_low

        # ── Direction: NET close at end ────────────
        final_close = fut_closes[:, -1]

        net_move = (
            final_close - entry_close
        )

        with np.errstate(
            invalid="ignore",
            divide="ignore",
        ):
            net_atr = np.where(
                entry_atr > 0,
                net_move / entry_atr,
                np.nan,
            )

            up_atr = np.where(
                entry_atr > 0,
                up_move / entry_atr,
                np.nan,
            )

            down_atr = np.where(
                entry_atr > 0,
                down_move / entry_atr,
                np.nan,
            )

            mag_atr = np.maximum(
                up_atr,
                down_atr,
            )

            mag_pct = np.where(
                entry_close > 0,
                np.maximum(
                    up_move,
                    down_move,
                )
                / entry_close
                * 100,
                np.nan,
            )

        bullish = (
            net_atr > neutral_threshold
        )

        bearish = (
            net_atr < -neutral_threshold
        )

        directions = np.where(
            bullish,
            "bullish",
            np.where(
                bearish,
                "bearish",
                "neutral",
            ),
        )

        n = len(positions)

        bull_count = bullish.sum()
        bear_count = bearish.sum()

        bull_pct = (
            float(bull_count) / n * 100
        )

        bear_pct = (
            float(bear_count) / n * 100
        )

        neutral_pct = (
            100
            - bull_pct
            - bear_pct
        )

        dominant = max(
            [
                "bullish",
                "bearish",
                "neutral",
            ],
            key=lambda d:
                bull_count
                if d == "bullish"
                else bear_count
                if d == "bearish"
                else n
                - bull_count
                - bear_count,
        )

        # ── Timing ─────────────────────────────────
        timing = np.where(
            bullish,
            np.argmax(
                fut_highs,
                axis=1,
            )
            + 1,
            np.where(
                bearish,
                np.argmin(
                    fut_lows,
                    axis=1,
                )
                + 1,
                1,
            ),
        ).astype(float)

        # ── Persistence ────────────────────────────
        entry_close_2d = np.asarray(
    entry_close,
    dtype=np.float64,
).reshape(-1, 1)
        if dominant == "bullish":
            persistence = (
                fut_closes
                > entry_close_2d
            ).sum(axis=1)

        elif dominant == "bearish":
            persistence = (
                fut_closes
                < entry_close_2d
            ).sum(axis=1)

        else:
            persistence = np.zeros(
                n,
                dtype=int,
            )

        # ── Aggregate ──────────────────────────────
        def _s(arr):
            clean = arr[
                ~np.isnan(arr)
            ]

            if len(clean) == 0:
                return (
                    None,
                    None,
                    None,
                )

            return (
                round(
                    float(
                        np.mean(clean)
                    ),
                    4,
                ),
                round(
                    float(
                        np.std(clean)
                    ),
                    4,
                ),
                round(
                    float(
                        np.median(clean)
                    ),
                    4,
                ),
            )

        mag_mean, mag_std, mag_med = _s(
            mag_atr
        )

        pct_mean, *_ = _s(
            mag_pct
        )

        enriched.append(
            {
                **{
                    k: v
                    for k, v
                    in match.items()
                    if k != "match_index"
                },
                "match_index": list(
                    positions
                ),
                "valid_count": n,
                "bull_pct": round(
                    bull_pct,
                    2,
                ),
                "bear_pct": round(
                    bear_pct,
                    2,
                ),
                "neutral_pct": round(
                    neutral_pct,
                    2,
                ),
                "dominant_dir": dominant,
                "mag_atr_mean": mag_mean,
                "mag_atr_std": mag_std,
                "mag_atr_median": mag_med,
                "mag_pct_mean": pct_mean,
                "timing_mean": round(
                    float(
                        np.mean(
                            timing
                        )
                    ),
                    2,
                ),
                "persistence_mean": round(
                    float(
                        np.mean(
                            persistence
                        )
                    ),
                    2,
                ),
                "reactions": [
                    {
                        "pos": int(
                            positions[i]
                        ),
                        "direction": str(
                            directions[i]
                        ),
                        "mag_atr":
                            float(
                                mag_atr[i]
                            )
                            if not np.isnan(
                                mag_atr[i]
                            )
                            else None,
                        "mag_pct":
                            float(
                                mag_pct[i]
                            )
                            if not np.isnan(
                                mag_pct[i]
                            )
                            else None,
                        "timing": int(
                            timing[i]
                        ),
                        "persistence": int(
                            persistence[i]
                        ),
                    }
                    for i in range(n)
                ],
            }
        )

    if verbose:
        print()

    return enriched