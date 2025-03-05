from program.staircase import staircase

import unittest


class test_staircase(unittest.TestCase):
    def test_give_2_with_hash_should_be_hh(self):
        n = 2
        pattern = "#"
        expected_output = " #\n" + "##"
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_3_with_hash_should_be_hh(self):
        n = 3
        pattern = "#"
        expected_output = "  #\n" + " ##\n" + "###"
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_4_with_hash_should_be_hh(self):
        n = 4
        pattern = "#"
        expected_output = "   #\n" + "  ##\n" + " ###\n" + "####"
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)
