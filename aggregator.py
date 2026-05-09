from news_api import NewsAPIClient
from scraper import ArticleScraper
from processor import NewsProcessor
from visualizer import NewsVisualizer


class TechnologyNewsAggregator:

    def __init__(self):
        self.client = NewsAPIClient()
        self.scraper = ArticleScraper()
        self.processor = NewsProcessor()
        self.visualizer = NewsVisualizer()

    def run(self):

        keyword = input(
            "Enter a technology keyword: "
        )

        page_size = int(
            input("Number of articles: ")
        )

        print("\nFetching articles...")

        articles = self.client.fetch_articles(
            keyword=keyword,
            page_size=page_size
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
