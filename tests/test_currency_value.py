"""
Module for currency_value unit tests
"""

import unittest
from unittest.mock import patch

from src.currency_value import get_currency_value


class TestCurrencyValue(unittest.TestCase):
    """Class for currency_value unit tests"""

    @patch("currency_value.requests.get")
    def test_get_currency_value_valid(self, mock_get):
        """Тест обычного запроса с успешным завершением """

        mock_get.return_value.status_code = 200
        mock_get.return_value.text = """
            <?xml version="1.0" encoding="UTF-8"?>
            <ValCurs Date="2022-10-08" name="Foreign Currency Market">
                <Valute ID="R01235">
                    <NumCode>840</NumCode>
                    <CharCode>USD</CharCode>
                    <Nominal>1</Nominal>
                    <Name>Доллар США</Name>
                    <Value>61.2475</Value>
                </Valute>
            </ValCurs>
        """

        name, value = get_currency_value("USD", "2022-10-08")
        self.assertEqual(name, "Доллар США")
        self.assertEqual(value, "61.2475")

    @patch("currency_value.requests.get")
    def test_get_currency_value_invalid_code(self, mock_get):
        """Тест на ввод кода валюты, которого нет в xml файле"""

        mock_get.return_value.status_code = 200
        mock_get.return_value.text = """
            <?xml version="1.0" encoding="UTF-8"?>
            <ValCurs Date="2022-10-08" name="Foreign Currency Market">
                <Valute ID="R01239">
                    <NumCode>978</NumCode>
                    <CharCode>EUR</CharCode>
                    <Nominal>1</Nominal>
                    <Name>Евро</Name>
                    <Value>70.8155</Value>
                </Valute>
            </ValCurs>
        """

        name, value = get_currency_value("USD", "2022-10-08")
        self.assertIsNone(name)
        self.assertIsNone(value)

    @patch("currency_value.requests.get")
    def test_get_currency_value_invalid_date(self, mock_get):
        """Тест когда не найден xml файл или произошла непредвиденная ошибка"""

        mock_get.return_value.status_code = 404
        mock_get.return_value.text = "Not found"

        name, value = get_currency_value("USD", "2022-10-08")
        self.assertIsNone(name)
        self.assertIsNone(value)

if __name__ == "__main__":
    unittest.main()
