"""
Module for date change function unit tests
"""

import unittest

from src.date_change import date_for_request


class TestDateForRequest(unittest.TestCase):
    """Class for date change function unit tests"""
    def test_date_for_request_valid_format(self):
        """Проверка работы при стандартном вводе"""

        input_date = "2023-07-25"
        expected_output = "25/07/2023"
        result = date_for_request(input_date)
        self.assertEqual(expected_output, result)

    def test_date_for_request_invalid_format(self):
        """Функция не должна работать с датой неверного формата"""

        input_date = "2023/07/25"  # Неверный формат (не yyyy-mm-dd)
        expected_output = None
        result = date_for_request(input_date)
        self.assertEqual(expected_output, result)

    def test_date_for_request_empty_input(self):
        """Функция должна возврящать пустую строку для пустого ввода"""

        input_date = ""
        expected_output = ""
        result = date_for_request(input_date)
        self.assertEqual(expected_output, result)

    def test_date_for_request_leap_year(self):
        """Проверка работы с датой которая еще не наступила"""

        input_date = "2024-02-29"
        expected_output = "29/02/2024"
        result = date_for_request(input_date)
        self.assertEqual(expected_output, result)


if __name__ == "__main__":
    unittest.main()
