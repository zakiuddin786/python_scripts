import logging

logger = logging.getLogger(__name__)

class ScrapingPipeline:
    def __init__(self, fetcher, parser, repository):
        self.fetcher = fetcher
        self.parser = parser
        self.repository = repository

    def run(self, url: str):
        logger.info(f"Pipeline started for {url} to scrape")
        html = self.fetcher.fetch(url)
        data = self.parser.parse(html)
        self.repository.save(data)
        return len(data)