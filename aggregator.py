from news_api import NewsAPIClient
from scraper import ArticleScraper
from processor import NewsProcessor
from visualizer import NewsVisualizer


class NewsAggregator:

    def __init__(self):
        self.client = NewsAPIClient()
        self.scraper = ArticleScraper()
        self.processor = NewsProcessor()
        self.visualizer = NewsVisualizer()

    def run(self):

        keyword = input(
            "Enter a news keyword: "
        )

        page_size = int(
            input("Number of articles: ")
        )

        filter_type = input(
            "Filter by (category/source): "
        ).strip().lower()

        if filter_type not in ["category", "source"]:
            filter_type = "category"

        category = "all"
        source = "all"

        if filter_type == "category":
            category = input(
                "Enter category (all, business, entertainment, general, health, science, sports, technology): "
            ).strip().lower()

            if not category:
                category = "all"

        else:
            source = input(
                "Enter source (all, techcrunch, the-verge, wired, ars-technica, engadget): "
            ).strip().lower()

            if not source:
                source = "all"

        
        print("\nFetching articles...")

        articles = self.client.fetch_articles(
            keyword=keyword,
            page_size=page_size,
            filter_type=filter_type,
            category=category,
            source=source
        )

        scraped_results = []

        print("Scraping article details...\n")

        for article in articles:

            scraped = self.scraper.scrape_article(
                article.get("url")
            )

            scraped_results.append(scraped)

        df = self.processor.combine_articles(
            articles,
            scraped_results
        )

        clean_df = self.processor.clean_data(df)

        print("\nFinal Dataset:")
        print(clean_df.head())

        self.processor.save_csv(clean_df)

        print("\nShowing visualization...")
        self.visualizer.plot_source_distribution(
            clean_df
        )
