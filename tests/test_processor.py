import unittest
import pandas as pd
from processor import NewsProcessor


class TestNewsProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = NewsProcessor()

        self.sample_data = pd.DataFrame([
            {
                "title": "AI News 1",
                "url": "url1",
                "source": "TechCrunch"
            },
            {
                "title": "AI News 1",
                "url": "url1",
                "source": "TechCrunch"
            },
            {
                "title": None,
                "url": "url2",
                "source": "The Verge"
            }
        ])

    def test_clean_data(self):

        cleaned_df = self.processor.clean_data(
            self.sample_data
        )

        # should remove duplicate URL
        self.assertEqual(len(cleaned_df), 1)

        # title should not be missing
        self.assertFalse(
            cleaned_df["title"].isnull().any()
        )


if __name__ == "__main__":
    unittest.main()
