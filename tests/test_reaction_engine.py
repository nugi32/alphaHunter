import unittest

import numpy as np
import pandas as pd

from analysis.reaction_engine import measure_reactions


class ReactionEngineTests(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            "Close": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
            "High": [1.1, 2.1, 3.1, 4.1, 5.1, 6.1],
            "Low": [0.9, 1.9, 2.9, 3.9, 4.9, 5.9],
            "ATR_14": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        })

    def test_measure_reactions_skips_per_entry_reactions_by_default(self):
        matches = [
            {
                "label": "test-condition",
                "match_index": np.array([0, 1]),
                "match_count": 2,
            }
        ]

        enriched = measure_reactions(
            self.df,
            matches,
            {"lookahead": 2},
        )

        self.assertEqual(len(enriched), 1)
        self.assertEqual(enriched[0]["valid_count"], 2)
        self.assertIsInstance(enriched[0]["match_index"], np.ndarray)
        self.assertNotIn("reactions", enriched[0])

    def test_measure_reactions_can_include_per_entry_reactions(self):
        matches = [
            {
                "label": "test-condition",
                "match_index": np.array([0, 1]),
                "match_count": 2,
            }
        ]

        enriched = measure_reactions(
            self.df,
            matches,
            {"lookahead": 2},
            include_reactions=True,
        )

        self.assertEqual(len(enriched), 1)
        self.assertIn("reactions", enriched[0])
        self.assertEqual(len(enriched[0]["reactions"]), 2)


if __name__ == "__main__":
    unittest.main()
