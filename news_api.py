import requests
from config import NEWS_API_KEY


class NewsAPIClient:

    def __init__(self):
        self.api_key = NEWS_API_KEY
        self.base_url = "https://newsapi.org/v2/everything"

    def fetch_articles(self, keyword="technology", page_size=5):

        technology_sources = (
            "techcrunch,"
            "the-verge,"
            "wired,"
            "ars-technica,"
            "engadget"
        )

        params = {
            "q": keyword,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": page_size,
            "domains": "techcrunch.com,theverge.com,wired.com",
            "apiKey": self.api_key
        }

        try:
            response = requests.get(
                self.base_url,
                params=params,
                timeout=10
            )

            response.raise_for_status()

            data = response.json()

            if data.get("status") != "ok":
                print("API error:", data.get("message"))
                return []

            return data.get("articles", [])

        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
            return []
