import pandas as pd

from analysis.condition_engine import _build_evaluators


def test_ratio_condition_with_subtraction_operator_supports_bandwidth_checks():
    payload = {
        "conditions": [
            {
                "name": "bandwidth_small",
                "type": "ratio",
                "col": "upper",
                "op": "-",
                "col2": "lower",
                "factor": 0.015,
            }
        ]
    }

    df = pd.DataFrame(
        {
            "upper": [0.02, 0.01],
            "lower": [0.005, 0.009],
        }
    )

    evaluators = _build_evaluators(payload)
    result = evaluators["bandwidth_small"](df)

    assert result.tolist() == [False, True]
