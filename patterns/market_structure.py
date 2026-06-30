"""ATR-adaptive market structure analysis.

This module converts market structure into numerical features that are suitable
for downstream statistical testing or brute-force strategy search. The design is
intentionally objective and avoids hand-coded labels such as BOS or CHoCH.

The implementation is organized around a small set of classes:

- ATRCalculator: computes a rolling ATR using Wilder's smoothing.
- SwingDetector: detects confirmed swing highs and swing lows in a streaming,
  lookahead-free manner.
- FeatureGenerator: transforms the swing sequence into per-bar numerical features.
- MultiScaleStructureEngine: runs the pipeline across multiple swing layers.

Example
-------
>>> import pandas as pd
>>> from patterns.market_structure import MultiScaleStructureEngine
>>> engine = MultiScaleStructureEngine(layers=[{"name": "medium", "atr_multiplier": 1.5}])
>>> enriched = engine.fit_transform(df)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


@dataclass(frozen=True)
class LayerConfig:
    """Configuration for one market-structure scale."""

    name: str
    atr_period: int = 14
    atr_multiplier: float = 1.5


class ATRCalculator:
    """Calculate ATR in a vectorized, streaming-safe way."""

    def __init__(self, period: int = 14) -> None:
        self.period = period

    def calculate(
        self,
        df: pd.DataFrame,
        high_col: str = "High",
        low_col: str = "Low",
        close_col: str = "Close",
    ) -> pd.Series:
        """Return a Wilder ATR series aligned to the input dataframe."""
        required = {high_col, low_col, close_col}
        missing = required.difference(df.columns)
        if missing:
            raise KeyError(f"Missing OHLC columns: {sorted(missing)}")

        prev_close = df[close_col].shift(1)
        tr = pd.concat(
            [
                df[high_col] - df[low_col],
                (df[high_col] - prev_close).abs(),
                (df[low_col] - prev_close).abs(),
            ],
            axis=1,
        ).max(axis=1)

        atr = pd.Series(np.nan, index=df.index, dtype=float)
        if len(df) <= self.period:
            atr.iloc[:] = np.nan
            return atr

        atr.iloc[self.period - 1] = tr.iloc[: self.period].mean()
        for i in range(self.period, len(df)):
            atr.iloc[i] = (atr.iloc[i - 1] * (self.period - 1) + tr.iloc[i]) / self.period

        return atr


class SwingDetector:
    """Detect confirmed swing highs and swing lows without look-ahead bias."""

    def __init__(self, atr_multiplier: float = 1.5, atr_period: int = 14) -> None:
        self.atr_multiplier = atr_multiplier
        self.atr_period = atr_period

    def detect(
        self,
        df: pd.DataFrame,
        atr_series: pd.Series,
        high_col: str = "High",
        low_col: str = "Low",
        close_col: str = "Close",
    ) -> pd.DataFrame:
        """Return confirmed swings as a dataframe."""
        if atr_series.index is not df.index:
            atr_series = atr_series.reindex(df.index)

        swings: list[dict[str, Any]] = []
        state = "search_high"
        candidate_high_price: float | None = None
        candidate_high_idx: int | None = None
        candidate_low_price: float | None = None
        candidate_low_idx: int | None = None
        last_confirmed_price: float | None = None
        last_confirmed_type: str | None = None
        last_confirmed_idx: int | None = None
        last_confirmed_pos: int | None = None
        swing_id = 0

        for pos, (idx, row) in enumerate(df.iterrows()):
            high = float(row[high_col])
            low = float(row[low_col])
            close = float(row[close_col])
            atr_value = float(atr_series.iloc[pos]) if pos < len(atr_series) else np.nan
            reversal_size = max(0.0, atr_value * self.atr_multiplier) if pd.notna(atr_value) else 0.0

            if state == "search_high":
                if candidate_high_price is None:
                    candidate_high_price = high
                    candidate_high_idx = pos
                elif high > candidate_high_price:
                    candidate_high_price = high
                    candidate_high_idx = pos

                if candidate_high_price is not None and reversal_size > 0.0 and low <= candidate_high_price - reversal_size:
                    swings.append(
                        {
                            "index": pos,
                            "timestamp": idx,
                            "price": float(candidate_high_price),
                            "type": "H",
                            "swing_id": swing_id,
                            "leg_size": np.nan if last_confirmed_price is None else abs(float(candidate_high_price) - last_confirmed_price),
                            "duration_bars": np.nan if last_confirmed_pos is None else pos - last_confirmed_pos,
                        }
                    )
                    last_confirmed_price = float(candidate_high_price)
                    last_confirmed_type = "H"
                    last_confirmed_idx = candidate_high_idx
                    last_confirmed_pos = pos
                    state = "search_low"
                    candidate_low_price = low
                    candidate_low_idx = pos
                    candidate_high_price = None
                    candidate_high_idx = None
                    swing_id += 1
                else:
                    if candidate_low_price is None:
                        candidate_low_price = low
                        candidate_low_idx = pos

            else:  # search_low
                if candidate_low_price is None:
                    candidate_low_price = low
                    candidate_low_idx = pos
                elif low < candidate_low_price:
                    candidate_low_price = low
                    candidate_low_idx = pos

                if candidate_low_price is not None and reversal_size > 0.0 and high >= candidate_low_price + reversal_size:
                    swings.append(
                        {
                            "index": pos,
                            "timestamp": idx,
                            "price": float(candidate_low_price),
                            "type": "L",
                            "swing_id": swing_id,
                            "leg_size": np.nan if last_confirmed_price is None else abs(float(candidate_low_price) - last_confirmed_price),
                            "duration_bars": np.nan if last_confirmed_pos is None else pos - last_confirmed_pos,
                        }
                    )
                    last_confirmed_price = float(candidate_low_price)
                    last_confirmed_type = "L"
                    last_confirmed_idx = candidate_low_idx
                    last_confirmed_pos = pos
                    state = "search_high"
                    candidate_high_price = high
                    candidate_high_idx = pos
                    candidate_low_price = None
                    candidate_low_idx = None
                    swing_id += 1
                else:
                    if candidate_high_price is None:
                        candidate_high_price = high
                        candidate_high_idx = pos

        if not swings:
            return pd.DataFrame(
                columns=["index", "timestamp", "price", "type", "swing_id", "leg_size", "duration_bars"]
            )

        swings_df = pd.DataFrame(swings)
        swings_df = swings_df.sort_values("swing_id").reset_index(drop=True)
        swings_df["timestamp"] = pd.to_datetime(swings_df["timestamp"])
        return swings_df


class FeatureGenerator:
    """Generate per-bar numerical features from the swing sequence."""

    def __init__(self, layer_name: str = "structure") -> None:
        self.layer_name = layer_name

    def generate(
        self,
        df: pd.DataFrame,
        swings_df: pd.DataFrame,
        atr_series: pd.Series,
        high_col: str = "High",
        low_col: str = "Low",
        close_col: str = "Close",
    ) -> pd.DataFrame:
        """Return a feature dataframe aligned to the input candles."""
        features: dict[str, list[Any]] = {
            f"{self.layer_name}_distance_to_last_swing_high": [],
            f"{self.layer_name}_distance_to_last_swing_low": [],
            f"{self.layer_name}_distance_to_last_swing_high_atr": [],
            f"{self.layer_name}_distance_to_last_swing_low_atr": [],
            f"{self.layer_name}_bars_since_last_swing_high": [],
            f"{self.layer_name}_bars_since_last_swing_low": [],
            f"{self.layer_name}_bars_since_last_structure_break": [],
            f"{self.layer_name}_last_swing_range": [],
            f"{self.layer_name}_current_leg_size": [],
            f"{self.layer_name}_current_leg_size_atr": [],
            f"{self.layer_name}_average_leg_size": [],
            f"{self.layer_name}_current_leg_vs_average": [],
            f"{self.layer_name}_retracement_ratio": [],
            f"{self.layer_name}_pullback_size": [],
            f"{self.layer_name}_impulse_size": [],
            f"{self.layer_name}_retracement_atr": [],
            f"{self.layer_name}_last_leg_duration": [],
            f"{self.layer_name}_average_leg_duration": [],
            f"{self.layer_name}_current_leg_duration": [],
            f"{self.layer_name}_swing_slope": [],
            f"{self.layer_name}_current_leg_slope": [],
            f"{self.layer_name}_impulse_velocity": [],
            f"{self.layer_name}_hh_count": [],
            f"{self.layer_name}_hl_count": [],
            f"{self.layer_name}_lh_count": [],
            f"{self.layer_name}_ll_count": [],
            f"{self.layer_name}_consecutive_hh": [],
            f"{self.layer_name}_consecutive_hl": [],
            f"{self.layer_name}_consecutive_lh": [],
            f"{self.layer_name}_consecutive_ll": [],
            f"{self.layer_name}_current_price_vs_last_high": [],
            f"{self.layer_name}_current_price_vs_last_low": [],
            f"{self.layer_name}_distance_from_structure_midpoint": [],
            f"{self.layer_name}_structure_range_atr": [],
            f"{self.layer_name}_current_leg_vs_previous_leg": [],
            f"{self.layer_name}_current_range_vs_ATR": [],
            f"{self.layer_name}_structure_label": [],
        }

        last_swing_high_price = np.nan
        last_swing_high_idx = -1
        last_swing_low_price = np.nan
        last_swing_low_idx = -1
        last_confirmed_swing_price = np.nan
        last_confirmed_type: str | None = None
        last_confirmed_idx = -1
        last_structure_break_idx = -1
        completed_leg_sizes: list[float] = []
        completed_leg_durations: list[float] = []
        hh_count = hl_count = lh_count = ll_count = 0
        consecutive_hh = consecutive_hl = consecutive_lh = consecutive_ll = 0
        current_structure_label = np.nan
        previous_structure_label = np.nan
        last_leg_size = np.nan
        last_leg_duration = np.nan
        previous_leg_size = np.nan

        for pos, (idx, row) in enumerate(df.iterrows()):
            close = float(row[close_col])
            high = float(row[high_col])
            low = float(row[low_col])
            atr_value = float(atr_series.iloc[pos]) if pos < len(atr_series) else np.nan
            atr_value = atr_value if pd.notna(atr_value) else np.nan

            if not swings_df.empty:
                swing_rows = swings_df[swings_df["index"] <= pos]
                if not swing_rows.empty:
                    latest_swing = swing_rows.iloc[-1]
                    latest_type = str(latest_swing["type"])
                    latest_price = float(latest_swing["price"])
                    latest_pos = int(latest_swing["index"])

                    if latest_type == "H":
                        last_swing_high_price = latest_price
                        last_swing_high_idx = latest_pos
                    else:
                        last_swing_low_price = latest_price
                        last_swing_low_idx = latest_pos

                    if last_confirmed_type is None or latest_pos > last_confirmed_idx:
                        last_confirmed_swing_price = latest_price
                        last_confirmed_type = latest_type
                        last_confirmed_idx = latest_pos

                        if len(completed_leg_sizes) == 0:
                            last_leg_size = np.nan
                        else:
                            last_leg_size = completed_leg_sizes[-1]

                        if len(completed_leg_durations) == 0:
                            last_leg_duration = np.nan
                        else:
                            last_leg_duration = completed_leg_durations[-1]

                        if len(swing_rows) >= 2:
                            prev_swing = swing_rows.iloc[-2]
                            prev_price = float(prev_swing["price"])
                            prev_type = str(prev_swing["type"])
                            current_swing = swing_rows.iloc[-1]
                            current_price = float(current_swing["price"])
                            current_type = str(current_swing["type"])

                            if current_type == "H" and prev_type == "L":
                                current_structure_label = "HH" if current_price > prev_price else "LH"
                            elif current_type == "L" and prev_type == "H":
                                current_structure_label = "HL" if current_price > prev_price else "LL"
                            else:
                                if current_type == "H":
                                    current_structure_label = "HH" if current_price > prev_price else "LH"
                                else:
                                    current_structure_label = "HL" if current_price > prev_price else "LL"

                            if current_structure_label == "HH":
                                hh_count += 1
                                consecutive_hh += 1
                                consecutive_hl = consecutive_lh = consecutive_ll = 0
                            elif current_structure_label == "HL":
                                hl_count += 1
                                consecutive_hl += 1
                                consecutive_hh = consecutive_lh = consecutive_ll = 0
                            elif current_structure_label == "LH":
                                lh_count += 1
                                consecutive_lh += 1
                                consecutive_hh = consecutive_hl = consecutive_ll = 0
                            else:
                                ll_count += 1
                                consecutive_ll += 1
                                consecutive_hh = consecutive_hl = consecutive_lh = 0

                            if current_structure_label != previous_structure_label:
                                last_structure_break_idx = pos
                            previous_structure_label = current_structure_label

                        if len(completed_leg_sizes) > 0:
                            previous_leg_size = completed_leg_sizes[-1]
                        else:
                            previous_leg_size = np.nan

                if not swing_rows.empty and len(swing_rows) >= 2:
                    last_swing = swing_rows.iloc[-1]
                    prev_swing = swing_rows.iloc[-2]
                    leg_size = abs(float(last_swing["price"]) - float(prev_swing["price"]))
                    leg_duration = int(last_swing["index"]) - int(prev_swing["index"])
                    completed_leg_sizes.append(float(leg_size))
                    completed_leg_durations.append(float(leg_duration))
                    last_leg_size = float(leg_size)
                    last_leg_duration = float(leg_duration)

            distance_to_last_swing_high = np.nan if pd.isna(last_swing_high_price) else close - last_swing_high_price
            distance_to_last_swing_low = np.nan if pd.isna(last_swing_low_price) else close - last_swing_low_price
            distance_to_last_swing_high_atr = np.nan if pd.isna(distance_to_last_swing_high) or pd.isna(atr_value) else distance_to_last_swing_high / atr_value
            distance_to_last_swing_low_atr = np.nan if pd.isna(distance_to_last_swing_low) or pd.isna(atr_value) else distance_to_last_swing_low / atr_value
            bars_since_last_swing_high = np.nan if last_swing_high_idx < 0 else pos - last_swing_high_idx
            bars_since_last_swing_low = np.nan if last_swing_low_idx < 0 else pos - last_swing_low_idx
            bars_since_last_structure_break = np.nan if last_structure_break_idx < 0 else pos - last_structure_break_idx

            current_leg_size = np.nan if pd.isna(last_confirmed_swing_price) else abs(close - last_confirmed_swing_price)
            current_leg_size_atr = np.nan if pd.isna(current_leg_size) or pd.isna(atr_value) else current_leg_size / atr_value
            average_leg_size = np.nan if not completed_leg_sizes else float(np.mean(completed_leg_sizes))
            current_leg_vs_average = np.nan if pd.isna(current_leg_size) or pd.isna(average_leg_size) or average_leg_size == 0 else current_leg_size / average_leg_size
            pullback_size = np.nan if pd.isna(last_confirmed_swing_price) else abs(close - last_confirmed_swing_price)
            impulse_size = pullback_size
            retracement_ratio = np.nan if pd.isna(last_leg_size) or last_leg_size == 0 else pullback_size / last_leg_size
            retracement_atr = np.nan if pd.isna(retracement_ratio) or pd.isna(atr_value) else retracement_ratio * atr_value
            average_leg_duration = np.nan if not completed_leg_durations else float(np.mean(completed_leg_durations))
            current_leg_duration = np.nan if pd.isna(last_leg_duration) else last_leg_duration
            swing_slope = np.nan if pd.isna(last_leg_size) or pd.isna(last_leg_duration) or last_leg_duration == 0 else last_leg_size / last_leg_duration
            current_leg_slope = np.nan if pd.isna(current_leg_size) or pd.isna(bars_since_last_swing_high) or bars_since_last_swing_high == 0 else current_leg_size / bars_since_last_swing_high
            impulse_velocity = np.nan if pd.isna(current_leg_slope) or pd.isna(atr_value) or atr_value == 0 else current_leg_slope / atr_value

            current_price_vs_last_high = np.nan if pd.isna(last_swing_high_price) else close - last_swing_high_price
            current_price_vs_last_low = np.nan if pd.isna(last_swing_low_price) else close - last_swing_low_price
            structure_midpoint = np.nan if pd.isna(last_swing_high_price) or pd.isna(last_swing_low_price) else (last_swing_high_price + last_swing_low_price) / 2.0
            distance_from_structure_midpoint = np.nan if pd.isna(structure_midpoint) else close - structure_midpoint
            structure_range_atr = np.nan if pd.isna(last_swing_high_price) or pd.isna(last_swing_low_price) or pd.isna(atr_value) or atr_value == 0 else (last_swing_high_price - last_swing_low_price) / atr_value
            current_leg_vs_previous_leg = np.nan if pd.isna(current_leg_size) or pd.isna(previous_leg_size) or previous_leg_size == 0 else current_leg_size / previous_leg_size
            current_range_vs_ATR = np.nan if pd.isna(atr_value) or atr_value == 0 else (high - low) / atr_value

            features[f"{self.layer_name}_distance_to_last_swing_high"].append(distance_to_last_swing_high)
            features[f"{self.layer_name}_distance_to_last_swing_low"].append(distance_to_last_swing_low)
            features[f"{self.layer_name}_distance_to_last_swing_high_atr"].append(distance_to_last_swing_high_atr)
            features[f"{self.layer_name}_distance_to_last_swing_low_atr"].append(distance_to_last_swing_low_atr)
            features[f"{self.layer_name}_bars_since_last_swing_high"].append(bars_since_last_swing_high)
            features[f"{self.layer_name}_bars_since_last_swing_low"].append(bars_since_last_swing_low)
            features[f"{self.layer_name}_bars_since_last_structure_break"].append(bars_since_last_structure_break)
            features[f"{self.layer_name}_last_swing_range"].append(last_leg_size)
            features[f"{self.layer_name}_current_leg_size"].append(current_leg_size)
            features[f"{self.layer_name}_current_leg_size_atr"].append(current_leg_size_atr)
            features[f"{self.layer_name}_average_leg_size"].append(average_leg_size)
            features[f"{self.layer_name}_current_leg_vs_average"].append(current_leg_vs_average)
            features[f"{self.layer_name}_retracement_ratio"].append(retracement_ratio)
            features[f"{self.layer_name}_pullback_size"].append(pullback_size)
            features[f"{self.layer_name}_impulse_size"].append(impulse_size)
            features[f"{self.layer_name}_retracement_atr"].append(retracement_atr)
            features[f"{self.layer_name}_last_leg_duration"].append(last_leg_duration)
            features[f"{self.layer_name}_average_leg_duration"].append(average_leg_duration)
            features[f"{self.layer_name}_current_leg_duration"].append(current_leg_duration)
            features[f"{self.layer_name}_swing_slope"].append(swing_slope)
            features[f"{self.layer_name}_current_leg_slope"].append(current_leg_slope)
            features[f"{self.layer_name}_impulse_velocity"].append(impulse_velocity)
            features[f"{self.layer_name}_hh_count"].append(hh_count)
            features[f"{self.layer_name}_hl_count"].append(hl_count)
            features[f"{self.layer_name}_lh_count"].append(lh_count)
            features[f"{self.layer_name}_ll_count"].append(ll_count)
            features[f"{self.layer_name}_consecutive_hh"].append(consecutive_hh)
            features[f"{self.layer_name}_consecutive_hl"].append(consecutive_hl)
            features[f"{self.layer_name}_consecutive_lh"].append(consecutive_lh)
            features[f"{self.layer_name}_consecutive_ll"].append(consecutive_ll)
            features[f"{self.layer_name}_current_price_vs_last_high"].append(current_price_vs_last_high)
            features[f"{self.layer_name}_current_price_vs_last_low"].append(current_price_vs_last_low)
            features[f"{self.layer_name}_distance_from_structure_midpoint"].append(distance_from_structure_midpoint)
            features[f"{self.layer_name}_structure_range_atr"].append(structure_range_atr)
            features[f"{self.layer_name}_current_leg_vs_previous_leg"].append(current_leg_vs_previous_leg)
            features[f"{self.layer_name}_current_range_vs_ATR"].append(current_range_vs_ATR)
            features[f"{self.layer_name}_structure_label"].append(current_structure_label)

        return pd.DataFrame(features, index=df.index)


class MultiScaleStructureEngine:
    """Run the structure pipeline across multiple swing layers."""

    def __init__(self, layers: list[dict[str, Any]] | None = None) -> None:
        if layers is None:
            layers = [
                {"name": "small", "atr_multiplier": 0.75, "atr_period": 14},
                {"name": "medium", "atr_multiplier": 1.5, "atr_period": 14},
                {"name": "large", "atr_multiplier": 3.0, "atr_period": 14},
            ]
        self.layers = [LayerConfig(**layer) for layer in layers]
        self.swings_by_layer: dict[str, pd.DataFrame] = {}

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Return the OHLCV dataframe enriched with all layer features."""
        enriched = df.copy()
        self.swings_by_layer = {}
        for layer in self.layers:
            atr_calc = ATRCalculator(period=layer.atr_period)
            atr = atr_calc.calculate(enriched)
            detector = SwingDetector(atr_multiplier=layer.atr_multiplier, atr_period=layer.atr_period)
            swings = detector.detect(enriched, atr)
            self.swings_by_layer[layer.name] = swings
            features = FeatureGenerator(layer_name=layer.name).generate(enriched, swings, atr)
            enriched = pd.concat([enriched, features], axis=1)
        return enriched

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return self.fit_transform(df)


def apply(df: pd.DataFrame, layers: list[dict[str, Any]] | None = None) -> pd.DataFrame:
    """Backward-compatible application hook used by the preparation pipeline."""
    engine = MultiScaleStructureEngine(layers=layers)
    return engine.fit_transform(df)


def plot_swings(
    swings_df: pd.DataFrame,
    ax: plt.Axes | None = None,
    figsize: tuple[int, int] = (14, 6),
) -> plt.Axes:
    """Plot confirmed swing highs and lows on a price chart."""
    if ax is None:
        _, ax = plt.subplots(figsize=figsize)

    if swings_df.empty:
        return ax

    highs = swings_df[swings_df["type"] == "H"]
    lows = swings_df[swings_df["type"] == "L"]

    if not highs.empty:
        ax.scatter(highs["timestamp"], highs["price"], marker="^", color="tab:red", s=90, label="Swing High")
    if not lows.empty:
        ax.scatter(lows["timestamp"], lows["price"], marker="v", color="tab:green", s=90, label="Swing Low")

    ax.set_title("Confirmed swings")
    ax.grid(True, alpha=0.25)
    return ax


def plot_structure(
    df: pd.DataFrame,
    layer_name: str = "medium",
    ax: plt.Axes | None = None,
    figsize: tuple[int, int] = (14, 6),
) -> plt.Axes:
    """Visualize price, swing markers, and structure labels for one layer."""
    if ax is None:
        _, ax = plt.subplots(figsize=figsize)

    ax.plot(df.index, df["Close"], label="Close", color="k", linewidth=1.1)
    label_col = f"{layer_name}_structure_label"
    if label_col not in df.columns:
        raise KeyError(f"Layer '{layer_name}' is not present in the dataframe")

    swing_col = f"{layer_name}_structure_label"
    for _, row in df[df[swing_col].notna()].iterrows():
        ax.text(row.name, float(row["Close"]), str(row[swing_col]), fontsize=8, ha="center", va="bottom")

    ax.set_title(f"Market structure: {layer_name}")
    ax.set_ylabel("Price")
    ax.grid(True, alpha=0.25)
    return ax
