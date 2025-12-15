import logging
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

class QuoteParser:
    def parse(self, html: str) -> list[dict]:
        logger.info(f" Starting the parser")
        soup = BeautifulSoup(html, "html.parser")

        quotes_data = []

        for quote in soup.select("div.quote"):
            text = quote.select_one("span.text").text
            logger.debug(f"Text is {text}")
            author = quote.select_one("small.author").text
            logger.debug(f"Author is {author}")

            tags = [tag.text for tag in quote.select("a.tag")]

            quotes_data.append({
                "quote": text,
                "author": author,
                "tags": tags
            })

        logger.debug(f" Parsed {len(quotes_data)} quotes ")
        return quotes_data