def rank_candidates(validated: list[dict], payload: dict) -> list[dict]:
    """
    Step 10 — Rank by statistical quality only. Never by profit.

    Score weights:
        35%  directional consistency
        25%  magnitude consistency  (low CV = high score)
        15%  frequency
        15%  sample size
        10%  validation split stability
    """
    for c in validated:
        dir_score    = c["dir_consistency"] / 100

        cv           = c.get("mag_cv") or 1.0
        mag_score    = max(0.0, 1.0 - cv)

        freq_pct     = c.get("freq_pct") or 0.0
        freq_score   = min(freq_pct / 2.0, 1.0)           # saturates at 2%

        sample_score = min(c["valid_count"] / 200.0, 1.0) # saturates at 200 samples

        split_results    = c.get("split_results", {})
        ok_splits        = [v for v in split_results.values() if v.get("status") == "ok"]
        stability_score  = len(ok_splits) / max(len(split_results), 1)

        c["consistency_score"] = round(
            0.35 * dir_score
          + 0.25 * mag_score
          + 0.15 * freq_score
          + 0.15 * sample_score
          + 0.10 * stability_score,
            4,
        )

    return sorted(validated, key=lambda x: -x["consistency_score"])