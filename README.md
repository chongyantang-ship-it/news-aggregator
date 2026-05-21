# News Aggregator

## Project Overview

The News Aggregator is a Python-based application that collects news articles using both NewsAPI and web scraping.

The program fetches article data from NewsAPI, enriches it with additional webpage information using BeautifulSoup, cleans the combined dataset with pandas, exports the data to CSV, visualises article distribution by source, and includes unit tests.

## Features

- Fetch news using NewsAPI
- Search news by keyword
- Filter news by category or source
- Scrape additional article information such as title, author, publication date, and summary
- Combine API and scraped data
- Remove duplicate records
- Export cleaned data to CSV
- Visualise article distribution by source
- Use object-oriented programming
- Include unit tests with unittest

## Technologies Used

- Python
- NewsAPI
- Requests
- BeautifulSoup4
- Pandas
- Matplotlib
- unittest

## Project Structure

```text
news-aggregator/
├── aggregator.py
├── news_api.py
├── scraper.py
├── processor.py
├── visualizer.py
├── gui.py
├── run_project.py
├── config.example.py
├── requirements.txt
├── README.md
├── report.md
├── data/
│   └── news.csv
└── tests/
    ├── test_processor.py
    ├── test_news_api.py
    ├── test_scraper.py
    ├── test_aggregator.py
    └── test_visualizer.py
```

## Installation

Clone the repository:

git clone <repository_url>
cd news-aggregator

Install dependencies:

pip install -r requirements.txt

## API Configuration

Create a file named config.py and add your NewsAPI key:

NEWS_API_KEY = "your_newsapi_key_here"

You can obtain a free API key from:
https://newsapi.org/

## How to Run

Run the project:

python run_project.py

The program will ask for:
1. A news keyword
2. The number of articles
3. Whether to filter by category or source
4. A preferred category or source

The application will then fetch filtered news articles, scrape additional information, clean the data, save the results to data/news.csv, and display a visualisation.




## GUI Version

This project also includes a Tkinter graphical user interface.

To run the GUI version:

python gui.py

The GUI allows users to:
1. Enter a news keyword
2. Enter the number of articles
3. Choose whether to filter by category or source
4. Select a preferred category or source
5. Fetch news articles
6. View article titles, sources, URLs, authors, publication dates, and summaries
7. Visualise article distribution by source
8. Save the cleaned dataset to CSV

Note: The Tkinter GUI should be run in a local Python environment such as VS Code, PyCharm, or terminal. It may not display properly in Google Colab.

## Running Unit Tests

Run the tests:

```bash
python tests/test_processor.py
python tests/test_news_api.py
python tests/test_scraper.py
python tests/test_aggregator.py
python tests/test_visualizer.py
```

## Ethical Considerations

This project follows ethical web scraping practices by scraping only publicly accessible webpages, avoiding excessive requests, and using the data only for educational purposes.

## Authors

Group Project - News Aggregator

Chongyan Tang 26057101

Zheke Yi 25655150

Wancheng Liu 25752813

TaoLou 26044949
