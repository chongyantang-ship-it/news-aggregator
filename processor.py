import pandas as pd


class NewsProcessor:

    def combine_articles(self, api_articles, scraped_results):
        """
        Combine API data and scraped data.
        """

        combined_data = []

        for api_article, scraped in zip(api_articles, scraped_results):

            combined_data.append({
                "title": api_article.get("title"),
                "source": api_article.get("source", {}).get("name"),
                "url": api_article.get("url"),
                "published_at": api_article.get("publishedAt"),

                "author": scraped.get("author"),
                "scraped_title": scraped.get("scraped_title"),
                "scraped_date": scraped.get("scraped_published_date"),
                "summary": scraped.get("summary")
            })

        return pd.DataFrame(combined_data)

    def clean_data(self, df):
        """
        Clean and remove duplicates.
        """

        # remove duplicate URLs
        df = df.drop_duplicates(subset=["url"])

        # remove rows with missing title
        df = df.dropna(subset=["title"])

        # reset index
        df = df.reset_index(drop=True)

        return df

    def save_csv(self, df, filename="technology_news.csv"):
        """
        Save dataframe to CSV.
        """
        df.to_csv(filename, index=False)
        print(f"Saved to {filename}")
