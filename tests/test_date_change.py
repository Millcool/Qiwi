import unittest
from src.date_change import date_for_request

class TestDateForRequest(unittest.TestCase):

    def test_date_for_request_valid_format(self):
        input_date = "2023-07-25"
        expected_output = "25/07/2023"
        result = date_for_request(input_date)
        self.assertEqual(expected_output, result)

    def test_date_for_request_invalid_format(self):
        # The function doesn't modify invalid input
        input_date = "2023/07/25"  # Invalid format (not in yyyy-mm-dd)
        expected_output = None
        result = date_for_request(input_date)
        self.assertEqual(expected_output, result)

    def test_date_for_request_empty_input(self):
        # The function should return an empty string for empty input
        input_date = ""
        expected_output = ""
        result = date_for_request(input_date)
        self.assertEqual(expected_output, result)

    def test_date_for_request_leap_year(self):
        input_date = "2024-02-29"  # Leap year
        expected_output = "29/02/2024"
        result = date_for_request(input_date)
        self.assertEqual(expected_output, result)

if __name__ == "__main__":
    unittest.main()