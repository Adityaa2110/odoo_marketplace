import logging

import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass


@pytest.mark.usefixtures("setup3")
class BaseClass2:

    def get_logger(self):
        logger = logging.getLogger(__name__)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.INFO)
        logger.debug("A debug statement is executed")
        logger.info("information statement")
        logger.warning("Something is in warning mode")
        logger.error("A major error has happenend")
        logger.critical("Critical issue")
        return logger


