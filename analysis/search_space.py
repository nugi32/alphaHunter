"""Search-space generation for the brute-force condition engine.

The project evaluates combinations of named market conditions in order to find
patterns that consistently precede strong future price reactions. This module is
responsible for building that search space from the payload configuration.

The key idea is that if there are n available conditions, the total number of
unique combinations up to depth d is:

    sum_{k=1}^{d} C(n, k)

where C(n, k) is the binomial coefficient. This grows very quickly and is the
main reason the project uses safeguards such as max_depth and max_combinations.
"""

from itertools import combinations

# A condition is just its name string — evaluation logic lives in condition_engine.py
ConditionName  = str
ConditionCombo = tuple[ConditionName, ...]


def build_search_space(payload: dict) -> list[ConditionCombo]:
    """Generate every unique condition combination up to the configured depth.

    Purpose:
        Build the list of condition tuples that the brute-force scanner will test
        against the dataframe.

    Inputs:
        payload: Configuration containing the condition definitions and search
            controls such as max_depth and max_combinations.

    Outputs:
        A list of tuples where each tuple contains a combination of condition names.

    Side effects:
        None.

    Algorithm:
        The function iterates through combination sizes from 1 to max_depth.
        For each size k, it adds every combination of size k from the available
        condition names. The total number of combinations grows as the binomial
        sum above, which is why the code includes a hard cap.

    Time complexity:
        O(sum_{k=1}^{d} C(n, k)) in the size of the generated search space.

    Memory complexity:
        O(total_combinations) because the full space is stored in memory.
    """
    names = [c["name"] for c in payload["conditions"]]
    max_depth = payload.get("max_depth", 3)
    max_combinations = payload.get("max_combinations")

    space: list[ConditionCombo] = []
    for depth in range(1, max_depth + 1):
        # Each depth contributes C(n, depth) possible combinations.
        # The overall search-space size is the sum of all these terms.
        for combo in combinations(names, depth):
            if max_combinations is not None and len(space) >= max_combinations:
                # The hard cap prevents an explosion in runtime and memory.
                return space
            space.append(combo)

    return space


def describe_combo(combo: ConditionCombo) -> str:
    """Create a human-readable label for a condition combination."""
    return " + ".join(combo)


def combo_stats(space: list[ConditionCombo]) -> dict:
    """Summarise how many combinations were generated at each depth."""
    from collections import Counter
    depth_counts = Counter(len(c) for c in space)
    return {
        "total":      len(space),
        "by_depth":   dict(sorted(depth_counts.items())),
    }