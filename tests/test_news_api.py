import unittest
from news_api import NewsAPIClient


class TestNewsAPI(unittest.TestCase):

    def setUp(self):
        self.client = NewsAPIClient()

    def test_fetch_articles(self):

        articles = self.client.fetch_articles(
            keyword="AI",
            page_size=5
        )

        # should return a list
        self.assertIsInstance(
            articles,
            list
        )

        # should return at least 1 article
        self.assertGreater(
            len(articles),
            0
        )

        # check required fields
        article = articles[0]

        self.assertIn("title", article)
        self.assertIn("url", article)
        self.assertIn("source", article)


if __name__ == "__main__":
    unittest.main()
