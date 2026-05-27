import operator as _op
import pandas as pd
from typing import Any

from .search_space import ConditionCombo, describe_combo

# ── Operator map ────────────────────────────────────────────────────────────
_OPS: dict = {
    "<":  _op.lt,
    "<=": _op.le,
    ">":  _op.gt,
    ">=": _op.ge,
    "==": _op.eq,
    "!=": _op.ne,
}


# ── Build a lookup: condition name → callable(df) → bool Series ─────────────

def _build_evaluators(payload: dict) -> dict[str, Any]:
    """
    Pre-compile each named condition into a fast callable:
        evaluator(df: pd.DataFrame) -> pd.Series[bool]

    Supports three condition types:
        threshold  :  col  op  scalar_value
        cross      :  col  op  col2
        ratio      :  col  op  (factor * col2)
    """
    evaluators = {}

    for cdef in payload["conditions"]:
        name = cdef["name"]
        col  = cdef["col"]
        op   = cdef["op"]
        fn   = _OPS[op]
        ctype = cdef.get("type", "threshold")

        if ctype == "threshold":
            val = cdef["val"]
            evaluators[name] = lambda df, c=col, f=fn, v=val: (
                pd.Series(False, index=df.index)
                if c not in df.columns
                else f(df[c], v)
            )

        elif ctype == "cross":
            col2 = cdef["col2"]
            evaluators[name] = lambda df, c=col, f=fn, c2=col2: (
                pd.Series(False, index=df.index)
                if c not in df.columns or c2 not in df.columns
                else f(df[c], df[c2])
            )

        elif ctype == "ratio":
            col2   = cdef["col2"]
            factor = cdef.get("factor", 1.0)
            evaluators[name] = lambda df, c=col, f=fn, c2=col2, fc=factor: (
                pd.Series(False, index=df.index)
                if c not in df.columns or c2 not in df.columns
                else f(df[c], df[c2] * fc)
            )

        else:
            raise ValueError(f"Unknown condition type: {ctype!r} in '{name}'")

    return evaluators


def apply_combo(
    df: pd.DataFrame,
    combo: ConditionCombo,
    evaluators: dict,
) -> pd.Series:
    """
    Boolean Series — True where ALL conditions in combo are simultaneously satisfied.
    Any missing column causes that condition to evaluate False for all rows.
    """
    mask = pd.Series(True, index=df.index)
    for name in combo:
        mask = mask & evaluators[name](df)
        if not mask.any():      # short-circuit: already all False
            break
    return mask


def scan_all_combos(
    df: pd.DataFrame,
    combos: list[ConditionCombo],
    payload: dict,
) -> list[dict]:
    """
    Evaluate every combo across the full dataframe.

    Returns one record per combo that passes min_samples:
        {
            "combo"       : ConditionCombo,
            "label"       : str,
            "match_index" : pd.Index,     ← integer positions where condition fired
            "match_count" : int,
        }
    """
    evaluators  = _build_evaluators(payload)
    min_samples = payload.get("min_samples", 30)
    total       = len(combos)
    results     = []

    for i, combo in enumerate(combos, 1):
        if i % 1000 == 0 or i == total:
            pct = i / total * 100
            print(f"\r  [{i:>6}/{total}] {pct:5.1f}%  candidates so far: {len(results)}", end="", flush=True)

        mask        = apply_combo(df, combo, evaluators)
        match_count = int(mask.sum())

        if match_count < min_samples:
            continue

        results.append({
            "combo":       combo,
            "label":       describe_combo(combo),
            "match_index": df.index[mask],
            "match_count": match_count,
        })

    print()  # newline after progress bar
    return results