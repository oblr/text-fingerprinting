import unittest
from simple import md5, md5_file
from text_descriptor import text_as_descriptor, text_from_descriptor


class Test(unittest.TestCase):

    def setUp(self):
        self.h1 = text_as_descriptor("abcdef dddd")

    def test_h1(self):
        self.assertEqual("text-fingerprinting.descriptor.text#abcdef dddd", self.h1)

    def test_2(self):
        self.assertEqual("abcdef dddd", text_from_descriptor(self.h1))