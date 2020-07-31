import unittest

from shingles.find import shingles_from_text
from simple import md5, md5_file
from descriptors import text_as_descriptor, text_from_descriptor


class Test(unittest.TestCase):

    def setUp(self):
        self.h1 = shingles_from_text("a rose is a rose is a rose", 4)

    def test_result(self):
        self.assertEqual({ 'text-fingerprinting.descriptor.shingle#a rose is a',
                           'text-fingerprinting.descriptor.shingle#rose is a rose',
                           'text-fingerprinting.descriptor.shingle#is a rose is' },
                         self.h1)
