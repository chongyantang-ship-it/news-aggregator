import matplotlib.pyplot as plt


class NewsVisualizer:

    def plot_source_distribution(self, df):
        """
        Plot the number of articles by news source.
        """
        source_counts = df["source"].value_counts()

        plt.figure(figsize=(8, 5))
        source_counts.plot(kind="bar")
        plt.title("Number of Articles by Source")
        plt.xlabel("News Source")
        plt.ylabel("Number of Articles")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()
