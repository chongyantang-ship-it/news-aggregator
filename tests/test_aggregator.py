import unittest
from unittest.mock import patch, Mock

import pandas as pd

from aggregator import NewsAggregator


class TestNewsAggregator(unittest.TestCase):

    @patch("aggregator.NewsVisualizer")
    @patch("aggregator.NewsProcessor")
    @patch("aggregator.ArticleScraper")
    @patch("aggregator.NewsAPIClient")
    @patch("builtins.input", side_effect=["AI", "1", "category", "technology"])
    def test_run_calls_all_main_components(
        self,
        mock_input,
        mock_client_class,
        mock_scraper_class,
        mock_processor_class,
        mock_visualizer_class
    ):
        mock_client = Mock()
        mock_client.fetch_articles.return_value = [
            {
                "title": "AI News",
                "url": "https://example.com/ai",
                "source": {"name": "TechCrunch"},
                "publishedAt": "2025-01-01"
            }
        ]
        mock_client_class.return_value = mock_client

        mock_scraper = Mock()
        mock_scraper.scrape_article.return_value = {
            "author": "Jane Doe",
            "scraped_title": "AI News Full",
            "scraped_published_date": "2025-01-01",
            "summary": "AI summary"
        }
        mock_scraper_class.return_value = mock_scraper

        raw_df = pd.DataFrame([{"title": "AI News", "source": "TechCrunch", "url": "https://example.com/ai"}])
        clean_df = raw_df.copy()

        mock_processor = Mock()
        mock_processor.combine_articles.return_value = raw_df
        mock_processor.clean_data.return_value = clean_df
        mock_processor_class.return_value = mock_processor

        mock_visualizer = Mock()
        mock_visualizer_class.return_value = mock_visualizer

        aggregator = NewsAggregator()
        aggregator.run()

        mock_client.fetch_articles.assert_called_once_with(
            keyword="AI",
            page_size=1,
            filter_type="category",
            category="technology",
            source="all"
        )
        mock_scraper.scrape_article.assert_called_once_with("https://example.com/ai")
        mock_processor.combine_articles.assert_called_once()
        mock_processor.clean_data.assert_called_once_with(raw_df)
        mock_processor.save_csv.assert_called_once_with(clean_df)
        mock_visualizer.plot_source_distribution.assert_called_once_with(clean_df)


if __name__ == "__main__":
    unittest.main()
