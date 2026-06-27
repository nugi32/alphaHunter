from itertools import combinations

# A condition is just its name string — evaluation logic lives in condition_engine.py
ConditionName  = str
ConditionCombo = tuple[ConditionName, ...]


def build_search_space(payload: dict) -> list[ConditionCombo]:
    """
    Generate unique combinations of condition names up to max_depth.

    For large payloads, a hard cap can be enforced via payload["max_combinations"]
    to avoid the combinatorial explosion that makes scanning extremely slow.
    """
    names = [c["name"] for c in payload["conditions"]]
    max_depth = payload.get("max_depth", 3)
    max_combinations = payload.get("max_combinations")

    space: list[ConditionCombo] = []
    for depth in range(1, max_depth + 1):
        for combo in combinations(names, depth):
            if max_combinations is not None and len(space) >= max_combinations:
                return space
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