import requests
from bs4 import BeautifulSoup


class ArticleScraper:
    """
    Scrapes additional article information from a news webpage.
    """

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }

    def scrape_article(self, url):
        """
        Scrape title, author, publication date, and text summary from an article URL.
        """
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            title = self._get_title(soup)
            author = self._get_author(soup)
            published_date = self._get_published_date(soup)
            summary = self._get_summary(soup)

            return {
                "scraped_title": title,
                "author": author,
                "scraped_published_date": published_date,
                "summary": summary
            }

        except Exception as e:
            return {
                "scraped_title": None,
                "author": None,
                "scraped_published_date": None,
                "summary": None,
                "error": str(e)
            }

    def _get_title(self, soup):
        if soup.title:
            return soup.title.get_text(strip=True)
        return None

    def _get_author(self, soup):
        author_meta = soup.find("meta", attrs={"name": "author"})
        if author_meta and author_meta.get("content"):
            return author_meta.get("content")
        return None

    def _get_published_date(self, soup):
        date_meta = soup.find("meta", attrs={"property": "article:published_time"})
        if date_meta and date_meta.get("content"):
            return date_meta.get("content")
        return None

    def _get_summary(self, soup):
        paragraphs = soup.find_all("p")
        text = " ".join(p.get_text(strip=True) for p in paragraphs[:5])
        return text[:500] if text else None
