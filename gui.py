import tkinter as tk
from tkinter import messagebox, scrolledtext
from news_api import NewsAPIClient
from scraper import ArticleScraper
from processor import NewsProcessor
from visualizer import NewsVisualizer


class NewsAggregatorGUI:
    """
    Tkinter GUI for the Technology News Aggregator.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Technology News Aggregator")
        self.root.geometry("900x650")

        self.client = NewsAPIClient()
        self.scraper = ArticleScraper()
        self.processor = NewsProcessor()
        self.visualizer = NewsVisualizer()
        self.current_df = None

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self.root,
            text="Technology News Aggregator",
            font=("Arial", 18, "bold")
        )
        title_label.pack(pady=10)

        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        keyword_label = tk.Label(input_frame, text="Keyword:")
        keyword_label.grid(row=0, column=0, padx=5)

        self.keyword_entry = tk.Entry(input_frame, width=25)
        self.keyword_entry.insert(0, "AI")
        self.keyword_entry.grid(row=0, column=1, padx=5)

        number_label = tk.Label(input_frame, text="Number of Articles:")
        number_label.grid(row=0, column=2, padx=5)

        self.number_entry = tk.Entry(input_frame, width=10)
        self.number_entry.insert(0, "5")
        self.number_entry.grid(row=0, column=3, padx=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        fetch_button = tk.Button(
            button_frame,
            text="Fetch News",
            command=self.fetch_news,
            width=15
        )
        fetch_button.grid(row=0, column=0, padx=10)

        visualise_button = tk.Button(
            button_frame,
            text="Visualise Sources",
            command=self.visualise_sources,
            width=18
        )
        visualise_button.grid(row=0, column=1, padx=10)

        save_button = tk.Button(
            button_frame,
            text="Save CSV",
            command=self.save_csv,
            width=15
        )
        save_button.grid(row=0, column=2, padx=10)

        self.output_box = scrolledtext.ScrolledText(
            self.root,
            width=105,
            height=28,
            wrap=tk.WORD
        )
        self.output_box.pack(pady=10)

    def fetch_news(self):
        keyword = self.keyword_entry.get().strip()
        number_text = self.number_entry.get().strip()

        if not keyword:
            messagebox.showerror("Input Error", "Please enter a keyword.")
            return

        try:
            page_size = int(number_text)
        except ValueError:
            messagebox.showerror("Input Error", "Number of articles must be an integer.")
            return

        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, f"Fetching news for keyword: {keyword}\n")
        self.output_box.insert(tk.END, f"Number of articles: {page_size}\n\n")
        self.root.update()

        articles = self.client.fetch_articles(
            keyword=keyword,
            page_size=page_size
        )

        if not articles:
            self.output_box.insert(tk.END, "No articles found.\n")
            return

        scraped_results = []

        for i, article in enumerate(articles, start=1):
            self.output_box.insert(tk.END, f"Scraping article {i}...\n")
            self.root.update()

            scraped = self.scraper.scrape_article(
                article.get("url")
            )
            scraped_results.append(scraped)

        df = self.processor.combine_articles(
            articles,
            scraped_results
        )

        self.current_df = self.processor.clean_data(df)

        self.output_box.insert(tk.END, "\nNews Results:\n")
        self.output_box.insert(tk.END, "-" * 80 + "\n")

        for i, row in self.current_df.iterrows():
            self.output_box.insert(tk.END, f"\nArticle {i + 1}\n")
            self.output_box.insert(tk.END, f"Title: {row.get('title')}\n")
            self.output_box.insert(tk.END, f"Source: {row.get('source')}\n")
            self.output_box.insert(tk.END, f"Author: {row.get('author')}\n")
            self.output_box.insert(tk.END, f"Published At: {row.get('published_at')}\n")
            self.output_box.insert(tk.END, f"URL: {row.get('url')}\n")
            self.output_box.insert(tk.END, f"Summary: {row.get('summary')}\n")
            self.output_box.insert(tk.END, "-" * 80 + "\n")

        messagebox.showinfo("Success", "News articles fetched successfully.")

    def visualise_sources(self):
        if self.current_df is None or self.current_df.empty:
            messagebox.showerror("No Data", "Please fetch news first.")
            return

        self.visualizer.plot_source_distribution(
            self.current_df
        )

    def save_csv(self):
        if self.current_df is None or self.current_df.empty:
            messagebox.showerror("No Data", "Please fetch news first.")
            return

        self.processor.save_csv(
            self.current_df,
            "data/technology_news.csv"
        )

        messagebox.showinfo(
            "Saved",
            "Data saved to data/technology_news.csv"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = NewsAggregatorGUI(root)
    root.mainloop()
