# Brief Report: News Aggregator

## 1. Introduction

This project is a Python-based News Aggregator. The purpose of the application is to collect news articles from NewsAPI, enrich the article information through web scraping, clean and combine the data, visualise article trends, and provide a structured and maintainable codebase using object-oriented programming principles.

The project focuses on aggregating information from multiple sources and presenting it in a usable format. It demonstrates the integration of API requests, web scraping, data processing, data visualisation, unit testing, and modular software design.

## 2. Design Decisions

### 2.1 Choice of Topic

The topic selected for this project is news aggregation. This topic was chosen because news is frequently updated, widely available through public APIs, and suitable for real-time information aggregation. It also allows users to search for specific keywords such as AI, cybersecurity, robotics, or cloud computing.

### 2.2 Choice of API

NewsAPI was selected as the main public API because it provides structured news article data, including title, source, URL, publication time, and article metadata. This makes it suitable for the first stage of the information aggregation process.

### 2.3 Web Scraping Approach

BeautifulSoup was used for web scraping because it is lightweight, easy to use, and suitable for extracting information from HTML pages. The scraper attempts to extract additional article details such as the webpage title, author, publication date, and summary text.

### 2.4 Object-Oriented Design

The project was designed using object-oriented programming to improve modularity and maintainability. Each major function is separated into a class:

- NewsAPIClient handles API requests.
- ArticleScraper handles web scraping.
- NewsProcessor handles data combination, cleaning, and CSV export.
- NewsVisualizer handles data visualisation.
- NewsAggregator coordinates the overall workflow.

This structure makes the program easier to extend and test.

## 3. Implementation Overview

The application follows this workflow:

1. The user enters a news keyword, the number of articles, and a preferred category or source filter.
2. The program sends a request to NewsAPI.
3. NewsAPI returns article data such as title, source, URL, and publication time.
4. The scraper visits each article URL and extracts additional webpage information.
5. API data and scraped data are combined into a pandas DataFrame.
6. Duplicate records and invalid rows are removed.
7. The cleaned data is exported to a CSV file.
8. A bar chart is generated to show the number of articles by source.

## 4. Data Processing

The data processing stage combines information from both the API and the scraper. The program removes duplicate articles based on URL and removes records with missing titles. The cleaned dataset is then saved as data/news.csv.

This step is important because data from online sources can be inconsistent, duplicated, or incomplete.

## 5. Data Visualisation

The project includes a visualisation showing the distribution of articles by news source. This helps users understand which sources contribute the most articles for a given keyword.

Matplotlib was used because it is simple, reliable, and suitable for generating basic charts in Python.

## 6. Unit Testing

The project uses the unittest framework to test important components of the system.

The tests include:

- test_aggregator.py: uses mock objects to test whether the main aggregator workflow correctly calls all core system components without making real API requests or web scraping operations.
- test_processor.py: tests data cleaning and duplicate removal.
- test_news_api.py: tests whether the API client returns articles with required fields.
- test_scraper.py: tests whether the scraper handles invalid URLs properly.
- test_visualizer.py: tests whether the visualizer successfully generates and displays source distribution charts.

These tests improve the reliability of the codebase and help confirm that the core functions work as expected.

## 7. Challenges Faced

One challenge was that different news websites use different HTML structures. As a result, web scraping does not always extract clean article text from every website. Some pages may return navigation text, subscription messages, or incomplete article content.

Another challenge was handling API limitations and search result relevance. Some keywords may return fewer results depending on the selected domains or NewsAPI availability.

A third challenge was displaying visualisations in Google Colab when running Python scripts directly. This was addressed by testing visualisation code directly inside Colab cells and keeping the script version for the final codebase.

## 8. Ethical Considerations

This project follows ethical web scraping practices. It only scrapes publicly accessible webpages, avoids excessive automated requests, and uses the collected data only for educational purposes.

The project also requires users to provide their own NewsAPI key and follow NewsAPI terms of service.

## 9. Additional Features

Beyond the basic requirements, the project includes:

- keyword-based article search
- configurable number of articles
- CSV export
- source distribution visualisation
- error handling for failed scraping requests
- modular OOP-based code structure
- unit tests for key components
- category-based news filtering
- source-based news filtering

## 10. Conclusion

The News Aggregator successfully demonstrates how Python can be used to collect, enrich, process, visualise, and test data from online sources. The project combines NewsAPI, web scraping, pandas, matplotlib, OOP design, and unittest into a complete and maintainable information aggregation application.
