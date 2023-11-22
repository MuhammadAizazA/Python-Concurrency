import logging

def setup_logging():
    format_1 = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_1, level=logging.INFO, datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)

if __name__ == "__main__":
    # If this script is executed directly, set up the logging
    setup_logging()

    # Example log messages
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")