import unittest
from unittest.mock import patch

import pandas as pd

from visualizer import NewsVisualizer


class TestNewsVisualizer(unittest.TestCase):

    @patch("visualizer.plt.show")
    def test_plot_source_distribution_calls_show(self, mock_show):
        df = pd.DataFrame([
            {"source": "BBC"},
            {"source": "BBC"},
            {"source": "CNN"}
        ])

        visualizer = NewsVisualizer()
        visualizer.plot_source_distribution(df)

        mock_show.assert_called_once()


if __name__ == "__main__":
    unittest.main()
