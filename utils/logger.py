import logging

def get_logger():
    """
    Creates and returns a logger object with the specified configuration.

    Returns:
        logging.Logger: The logger object.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a console handler with INFO level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # Create a formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(ch)

    return logger
