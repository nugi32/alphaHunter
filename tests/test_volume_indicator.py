import unittest

import pandas as pd

from indicators.volume import apply


class VolumeIndicatorTests(unittest.TestCase):
    def test_apply_calculates_obv(self):
        df = pd.DataFrame(
            {
                "Close": [100, 101, 101, 99],
                "Volume": [10, 20, 30, 40],
            }
        )

        result = apply(df.copy())

        expected_direction = pd.Series([0.0, 1.0, 0.0, -1.0], index=df.index)
        expected_obv = (expected_direction * df["Volume"]).cumsum()

        pd.testing.assert_series_equal(result["OBV"], expected_obv, check_names=False)
        self.assertTrue(pd.isna(result["VOL_SMA20"].iloc[0]))


if __name__ == "__main__":
    unittest.main()
