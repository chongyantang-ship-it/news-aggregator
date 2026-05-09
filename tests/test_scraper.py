import unittest
from scraper import ArticleScraper


class TestArticleScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = ArticleScraper()

    def test_scrape_article_with_invalid_url(self):

        result = self.scraper.scrape_article(
            "https://invalid-url-for-testing.com"
        )

        self.assertIsInstance(result, dict)
        self.assertIn("scraped_title", result)
        self.assertIn("author", result)
        self.assertIn("scraped_published_date", result)
        self.assertIn("summary", result)


if __name__ == "__main__":
    unittest.main()
