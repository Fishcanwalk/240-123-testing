from program.alternating_characters import alternatingCharacters

import unittest


class test_alternating_characters(unittest.TestCase):

    def test_alternating_characters(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("ABABAB"), 0)
        self.assertEqual(alternatingCharacters("AB"), 0)
        self.assertEqual(alternatingCharacters("BA"), 0)
        self.assertEqual(alternatingCharacters("AAB"), 1)
        self.assertEqual(alternatingCharacters("AB"), 0)
        self.assertEqual(alternatingCharacters("BA"), 0)
        self.assertEqual(alternatingCharacters("AAB"), 1)
        self.assertEqual(alternatingCharacters("AABBAABB"), 4)
        self.assertEqual(alternatingCharacters("BBAABBAA"), 4)
        self.assertEqual(alternatingCharacters("ABBA"), 2)
