from logging_config import setup_logging
import logging
from service  import doing_something

def main():
    setup_logging()

    logger = logging.getLogger(__name__)
    logger.info("Application is getting started....")
    doing_something()
    logger.info("Application startup finisihed")

if __name__ == "__main__":
    main()