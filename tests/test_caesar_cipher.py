from program.caesar_cipher import caesarCipher

import unittest


class TestCaesarCipher(unittest.TestCase):
    def test_positive_shift(self):
        self.assertEqual(caesarCipher("Hello, World!", 3), "Khoor, Zruog!")
        self.assertEqual(caesarCipher("abc", 1), "bcd")
        self.assertEqual(caesarCipher("XYZ", 3), "ABC")

    def test_negative_shift(self):
        self.assertEqual(caesarCipher("Khoor, Zruog!", -3), "Hello, World!")
        self.assertEqual(caesarCipher("bcd", -1), "abc")
        self.assertEqual(caesarCipher("ABC", -3), "XYZ")

    def test_large_shift(self):
        self.assertEqual(caesarCipher("Hello, World!", 26), "Hello, World!")
        self.assertEqual(caesarCipher("Hello, World!", 52), "Hello, World!")
        self.assertEqual(caesarCipher("abc", 27), "bcd")

    def test_non_alphabetic_characters(self):
        self.assertEqual(caesarCipher("123!@#", 5), "123!@#")
        self.assertEqual(caesarCipher("Hello, World! 123", 3), "Khoor, Zruog! 123")

    def test_empty_string(self):
        self.assertEqual(caesarCipher("", 5), "")
