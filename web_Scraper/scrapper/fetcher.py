import logging
import requests

logger = logging.getLogger(__name__)

class HttpFetcher:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
        })

    def fetch(self, url: str) -> str :
        logger.info(f"Fetching the URL: {url}")
        response = self.session.get(url, timeout=30)
        response.raise_for_status()
        return response.text