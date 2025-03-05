import unittest
from program.number_utils import is_prime_list


class PrimeListTest(unittest.TestCase):

    def test_give_2_3_is_prime(self):
        prime_list = [2, 3]
        result = is_prime_list(prime_list)
        self.assertTrue(result)

    def test_give_1_is_not_prime(self):
        prime_list = [1]
        result = is_prime_list(prime_list)
        self.assertFalse(result, [False])

    def test_give_4_is_not_prime(self):
        prime_list = [4]
        result = is_prime_list(prime_list)
        self.assertFalse(result, [False])
