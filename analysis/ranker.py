"""Ranking logic for the surviving validation candidates.

The project does not rank candidates by profit. Instead it scores them by how
statistically reliable their price reactions look. This keeps the selection
process aligned with the brute-force search objective: find conditions that
repeat consistently rather than only occasionally producing a large move.
"""


def rank_candidates(validated: list[dict], payload: dict) -> list[dict]:
    """Assign a weighted consistency score and sort the candidates.

    Purpose:
        Turn the filtered and validated candidates into a ranked list that can be
        reported to the user.

    Inputs:
        validated: Candidates that passed the consistency and validation stages.
        payload: Unused by the current implementation but kept for API symmetry.

    Outputs:
        A list of candidates sorted from highest to lowest consistency_score.

    Algorithm:
        The score is a weighted blend of:
        - directional consistency: how often the dominant direction appears,
        - magnitude consistency: low CV means more stable move size,
        - frequency: how often the pattern appears in the dataset,
        - sample size: more observations improve confidence,
        - stability: how many validation splits stayed valid.

    Score weights:
        35% directional consistency
        25% magnitude consistency (low CV = high score)
        15% frequency
        15% sample size
        10% validation split stability
    """
    for c in validated:
        dir_score = c["dir_consistency"] / 100

        cv = c.get("mag_cv") or 1.0
        mag_score = max(0.0, 1.0 - cv)

        freq_pct = c.get("freq_pct") or 0.0
        freq_score = min(freq_pct / 2.0, 1.0)  # Saturates at 2% frequency.

        sample_score = min(c["valid_count"] / 200.0, 1.0)  # Saturates at 200 samples.

        split_results = c.get("split_results", {})
        ok_splits = [v for v in split_results.values() if v.get("status") == "ok"]
        stability_score = len(ok_splits) / max(len(split_results), 1)

        c["consistency_score"] = round(
            0.35 * dir_score
            + 0.25 * mag_score
            + 0.15 * freq_score
            + 0.15 * sample_score
            + 0.10 * stability_score,
            4,
        )

    return sorted(validated, key=lambda x: -x["consistency_score"])