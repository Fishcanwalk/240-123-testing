from program.alternating_characters import alternatingCharacters

import unittest


class test_alternating_characters(unittest.TestCase):

    def test_give_AAAA_is_2(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)

    def test_give_ABABAB_is_0(self):
        self.assertEqual(alternatingCharacters("ABABAB"), 0)

    def test_give_AB_is_0(self):
        self.assertEqual(alternatingCharacters("AB"), 0)

    def test_give_BA_is_0(self):
        self.assertEqual(alternatingCharacters("BA"), 0)

    def test_give_AAB_is_1(self):
        self.assertEqual(alternatingCharacters("AAB"), 1)

    def test_give_AABBAABB_is_4(self):
        self.assertEqual(alternatingCharacters("AABBAABB"), 4)

    def test_give_BBAABBAA_is_4(self):
        self.assertEqual(alternatingCharacters("BBAABBAA"), 4)
