from program.alternate import alternate

import unittest


class test_alternate(unittest.TestCase):

    def test_give_beabeefeab_is_5(self):
        self.assertEqual(alternate("beabeefeab"), 5)

    def test_give_abcabc_is_4(self):
        self.assertEqual(alternate("abcabc"), 4)

    def test_give_aaaa_is_0(self):
        self.assertEqual(alternate("aaaa"), 0)

    def test_give_ababababab_is_10(self):
        self.assertEqual(alternate("ababababab"), 10)

    def test_give_abacaba_is_3(self):
        self.assertEqual(alternate("abacaba"), 3)

    def test_give___is_0(self):
        self.assertEqual(alternate(""), 0)
