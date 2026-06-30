import pandas as pd

from patterns.market_structure import MultiScaleStructureEngine


class TestMultiScaleStructureEngine:
    def test_engine_generates_structure_features(self):
        index = pd.date_range("2024-01-01", periods=12, freq="D")
        df = pd.DataFrame(
            {
                "Open": [10, 11, 10.5, 12, 11.5, 13, 12.5, 14, 13.5, 15, 14.5, 16],
                "High": [10.5, 11.5, 11.2, 12.4, 12.3, 13.4, 13.2, 14.5, 14.1, 15.4, 15.3, 16.4],
                "Low": [9.6, 10.4, 10.0, 11.3, 10.8, 12.2, 11.8, 13.4, 12.9, 14.2, 13.8, 15.2],
                "Close": [10.0, 11.0, 10.8, 12.0, 11.2, 13.0, 12.0, 14.0, 13.0, 15.0, 14.0, 16.0],
                "Volume": [100, 120, 110, 130, 125, 140, 135, 160, 150, 180, 170, 200],
            },
            index=index,
        )

        engine = MultiScaleStructureEngine(
            layers=[
                {"name": "small", "atr_multiplier": 0.75, "atr_period": 2},
                {"name": "medium", "atr_multiplier": 1.5, "atr_period": 2},
            ]
        )
        result = engine.fit_transform(df)

        assert result.shape[0] == len(df)
        assert "small_hh_count" in result.columns
        assert "medium_hh_count" in result.columns
        assert "small_distance_to_last_swing_high" in result.columns
        assert "medium_distance_to_last_swing_low" in result.columns
        assert "small_current_leg_size_atr" in result.columns
        assert "medium_current_leg_size_atr" in result.columns
        assert result["small_hh_count"].sum() >= 0
        assert result["medium_hl_count"].sum() >= 0
