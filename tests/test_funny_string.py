from program.funny_string import funnyString
import unittest


class TestFunnyString(unittest.TestCase):

    def test_funny_string(self):
        self.assertEqual(funnyString("acxz"), "Funny")
        self.assertEqual(funnyString("a"), "Funny")
        self.assertEqual(funnyString("ab"), "Funny")

    def test_not_funny_string(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")
