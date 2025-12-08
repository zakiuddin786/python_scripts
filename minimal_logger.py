import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )

logging.debug("This is a debug log")
logging.info("This is a info log")
logging.warning("This is a warning log")
logging.error("This is a error log")
logging.critical("This is a critical log")
