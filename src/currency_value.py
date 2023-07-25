"""
Module for daily value check
"""
import argparse
import logging

import requests

from date_change import date_for_request

CBR_API_URL = "https://www.cbr.ru/scripts/XML_daily.asp"


def setup_logging(filename):
    """Logger setup function"""

    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger = logging.getLogger('')
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger


def get_currency_value(code, date):
    """

    :param code: code of Valute that we want to take
    :param date: date in format yyyy-mm-dd
    :return:
            name: of Valute
            value: value of valute in that day or in the last day if that day not happened yet
    """
    #Инициализация логгера
    logger = setup_logging("../logs/currency_value.log")

    date = date_for_request(date)
    params = {"date_req": date}
    response = requests.get(CBR_API_URL, params=params,  timeout=10)

    if response.status_code != 200:
        logger.error("Ошибка при получении данных с сервера ЦБ РФ.")
        return None, None

    xml_data = response.text
    if code not in xml_data:
        logger.error("Курс для валюты с данным кодом на указанную дату не найден.")
        return None, None

    #Определение строки с нужной валютой
    rate_start = xml_data.find(f"<CharCode>{code}</CharCode>") + len(f"<CharCode>{code}</CharCode>")

    #Получение имени из xml файла
    name_start = xml_data.find("<Name>", rate_start) + len("<Name>")
    name_end = xml_data.find("</Name>", name_start)
    name = xml_data[name_start:name_end]

    #Получение значения value из xml файла
    value_start = xml_data.find("<Value>", rate_start) + len("<Value>")
    value_end = xml_data.find("</Value>", value_start)
    value = xml_data[value_start:value_end]

    logger.info("Successfully get value")

    return name, value


def main():
    """Main function"""

    parser = argparse.ArgumentParser(
                                    description="Получение курса валют ЦБ РФ "
                                                "за определенную дату.")
    parser.add_argument("--code",
                        type=str,
                        help="Код валюты в формате ISO 4217",
                        required=True)
    parser.add_argument("--date",
                        type=str,
                        help="Дата в формате YYYY-MM-DD",
                        required=True)
    args = parser.parse_args()

    name, value = get_currency_value(args.code.upper(), args.date)
    if name and value:
        print(f"{args.code.upper()} ({name}): {value}")


if __name__ == "__main__":
    main()
