import logging


def setup():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    logging.addLevelName(logging.INFO, "\033[32m%s\033[0m" %
                         logging.getLevelName(logging.INFO))

    logging.addLevelName(logging.WARNING, "\033[33m%s\033[0m" %
                         logging.getLevelName(logging.WARNING))

    logging.addLevelName(logging.ERROR, "\033[31m%s\033[0m" %
                         logging.getLevelName(logging.ERROR))


def info(msg: str):
    logging.info(msg)


def warning(msg: str):
    logging.warning(msg)


def error(msg: str):
    logging.error(msg)
