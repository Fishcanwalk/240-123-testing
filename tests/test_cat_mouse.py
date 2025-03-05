import unittest
from program.cat_mouse import catAndMouse


class TestCatAndMouse(unittest.TestCase):

    def test_give_1_2_3(self):
        give_number = [1, 2, 3]
        self.assertEqual(catAndMouse(give_number), "Cat B")

    def test_give_1_3_2(self):
        give_number = [1, 3, 2]
        self.assertEqual(catAndMouse(give_number), "Mouse C")

    def test_give_1_4_2(self):
        give_number = [1, 4, 2]
        self.assertEqual(catAndMouse(give_number), "Cat A")
