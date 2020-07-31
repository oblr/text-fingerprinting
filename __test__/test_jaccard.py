import unittest

from shingles.find import shingles_from_text
from shingles.jaccard import jaccard
from simple import md5, md5_file
from text_descriptor import text_as_descriptor, text_from_descriptor

from example_texts import EXAMPLE_TEXT_1, EXAMPLE_TEXT_2

class Test(unittest.TestCase):

    def test_result(self):
        sh = shingles_from_text("a rose is a rose is a rose", 4)
        self.assertEqual(jaccard(sh, sh), 1.0)

    def test_example_texts(self):
        sh1 = shingles_from_text(EXAMPLE_TEXT_1, 4)
        sh2 = shingles_from_text(EXAMPLE_TEXT_2, 4)
        self.assertEqual(jaccard(sh1, sh2), 0.16112531969309463)

