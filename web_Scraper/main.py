from logging_config import setup_logging
from scrapper.fetcher import HttpFetcher
from scrapper.parser import QuoteParser
from storage.repository import CSVRepository
from notifications.telegram import TelegramNotifier
from config.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

from scrapper.pipeline import ScrapingPipeline

setup_logging()

import logging

logger = logging.getLogger(__name__)
BASE_URL = "https://quotes.toscrape.com/page/{}/"
OUTPUT_FILE = "quotes.csv"

def main():
    fetcher = HttpFetcher()
    parser = QuoteParser()
    repository = CSVRepository(OUTPUT_FILE)

    pipeline = ScrapingPipeline(fetcher, parser, repository)
    page = 1
    total_quotes = 0

    while True:
        url = BASE_URL.format(page)
        try:
            count = pipeline.run(url)
            if count == 0:
                break
            total_quotes += count
            page +=1

        except Exception as e:
            logger.error(f"Stopping the scrapping operation due to {e}")
            break
    logger.info (f" Scrapping completed and scrapped {total_quotes}")

    # Telegram notification
    notifier = TelegramNotifier(bot_token=TELEGRAM_BOT_TOKEN,chat_id=TELEGRAM_CHAT_ID)

    notifier.send_message(f" Scrapping Got completed Total scraped quote are {total_quotes} Telegram did you get notified? sending from jenkins")

    notifier.send_file(OUTPUT_FILE, caption="This is the data for scrapped quotes, please read it and get inspired")
if __name__ == "__main__":
    main()
