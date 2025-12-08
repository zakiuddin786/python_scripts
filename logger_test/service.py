import logging

logger = logging.getLogger(__name__)
print("calling servin")
def doing_something():
    logger.debug("Doing something to start the application")
    logger.info("I'm doing something useful to tell")
    logger.error("Trying to create an error")
    try: 
        div = 1/0
    except ZeroDivisionError:
        logger.error("Zero division error occured while doing something")