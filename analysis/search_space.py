from itertools import combinations

# A condition is just its name string — evaluation logic lives in condition_engine.py
ConditionName  = str
ConditionCombo = tuple[ConditionName, ...]


def build_search_space(payload: dict) -> list[ConditionCombo]:
    """
    Generate all unique combinations of condition names up to max_depth.

    Each condition is identified by its "name" field from payload["conditions"].
    Evaluation logic is handled separately in condition_engine.py.

    Example output:
        [
            ("RSI14_oversold",),
            ("bull_engulf",),
            ("RSI14_oversold", "bull_engulf"),
            ("RSI14_oversold", "EMA21_above_EMA50"),
            ("RSI14_oversold", "bull_engulf", "vol_spike_2x"),
            ...
        ]
    """
    names     = [c["name"] for c in payload["conditions"]]
    max_depth = payload.get("max_depth", 3)

    space: list[ConditionCombo] = []
    for depth in range(1, max_depth + 1):
        for combo in combinations(names, depth):
            space.append(combo)

    return space


def describe_combo(combo: ConditionCombo) -> str:
    """Human-readable label: 'RSI14_oversold + bull_engulf + vol_spike_2x'"""
    return " + ".join(combo)


def combo_stats(space: list[ConditionCombo]) -> dict:
    """Quick summary of search space size per depth."""
    from collections import Counter
    depth_counts = Counter(len(c) for c in space)
    return {
        "total":      len(space),
        "by_depth":   dict(sorted(depth_counts.items())),
    }