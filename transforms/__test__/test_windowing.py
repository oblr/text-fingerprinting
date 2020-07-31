import unittest

from descriptors import text_as_descriptor
from example_texts import EXAMPLE_TEXT_1, EXAMPLE_TEXT_2
from transforms import windowing

class Test(unittest.TestCase):

    def setUp(self):
        self.h1 = EXAMPLE_TEXT_1
        # self.h1 = EXAMPLE_TEXT_2

    def test_result(self):
        w = windowing.sentences(
            text_as_descriptor(self.h1)
        )
        print(w)
        self.assertEqual(w, "...")
