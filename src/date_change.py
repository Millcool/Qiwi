"""
Module fort date change
"""
import logging


def setup_logging_date(func):
    """Logger for date change function"""

    file_handler = logging.FileHandler("date.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger = logging.getLogger('')
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

    def wrapper(*args, **kwargs):
        logger.info("Logging setup completed.")
        res = func(*args, **kwargs)
        if res is None:
            logging.error("Invalid format of date ! "
                          "Date should be in format yyyy-mm-dd")
        elif res == "":
            logging.error("Empty string")
        else:
            logging.info("Date changed")
        return res

    return wrapper


@setup_logging_date
def date_for_request(date: str) -> str:
    """
    Changes format of the date from yyyy-mm-dd to dd/mm/yyyy


    :date: date in format yyyy-mm-dd
    :return: string with date in format dd/mm/yyyy
    """

    if date != "":
        if len(date) == 10 and date[4] == '-' and date[7] == '-':
            year = date[:4]
            month = date[5:7]
            day = date[8:10]
            date = day + "/" + month + "/" + year
            return date
        return None
    return ""
