import requests
from config import NEWS_API_KEY


class NewsAPIClient:

    def __init__(self):
        self.api_key = NEWS_API_KEY
        self.base_url = "https://newsapi.org/v2/top-headlines"

    def fetch_articles(self, keyword="", page_size=5, filter_type="category", category="all", source="all"):


        valid_categories = [
            "all",
            "business",
            "entertainment",
            "general",
            "health",
            "science",
            "sports",
            "technology"
        ]

        source_options = {
            "all": "techcrunch,the-verge,wired,ars-technica,engadget",
            "techcrunch": "techcrunch",
            "the-verge": "the-verge",
            "wired": "wired",
            "ars-technica": "ars-technica",
            "engadget": "engadget"
        }

        filter_type = filter_type.lower()
        category = category.lower()
        source = source.lower()

        params = {
            "pageSize": page_size,
            "apiKey": self.api_key
        }

        if keyword:
            params["q"] = keyword

        if filter_type == "source":
            if source not in source_options:
                print("Invalid source. Using default source: all")
                source = "all"

            params["sources"] = source_options[source]

        else:
            if category not in valid_categories:
                print("Invalid category. Using default category: all")
                category = "all"

            params["country"] = "us"

            if category != "all":
                params["category"] = category

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
