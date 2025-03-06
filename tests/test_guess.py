from program.guess import guess_float, guess_int

import unittest
from unittest.mock import patch


class TestGuessFunctions(unittest.TestCase):
    @patch("random.randint")
    def test_guess_int(self, mock_randint):
        mock_randint.return_value = 5

        result = guess_int(1, 10)
        self.assertEqual(result, 5)

        mock_randint.assert_called_once_with(1, 10)

    @patch("random.uniform")
    def test_guess_float(self, mock_uniform):
        mock_uniform.return_value = 3.14

        result = guess_float(1.0, 5.0)
        self.assertEqual(result, 3.14)

        mock_uniform.assert_called_once_with(1.0, 5.0)

    def test_guess_int_range(self):
        result = guess_int(1, 10)
        self.assertTrue(1 <= result <= 10)

    def test_guess_float_range(self):
        result = guess_float(1.0, 5.0)
        self.assertTrue(1.0 <= result <= 5.0)
