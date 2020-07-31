import unittest

from descriptors import text_as_descriptor
from example_texts import EXAMPLE_TEXT_1, EXAMPLE_TEXT_2
from transforms import windowing

class Test(unittest.TestCase):

    def setUp(self):
        self.h1 = EXAMPLE_TEXT_1
        self.h2 = EXAMPLE_TEXT_2

        self.w1 = windowing.sentences(
            text_as_descriptor(self.h1)
        )
        self.w2 = windowing.sentences(
            text_as_descriptor(self.h2)
        )
    def test_result(self):
        w = self.w1
        self.assertEqual(
            w[0],
            'text-fingerprinting.descriptor.sentence#Lorem ipsum dolor sit amet, consectetur adipiscing elit')
        self.assertEqual(
            w[1],
            'text-fingerprinting.descriptor.sentence#Sed eget egestas purus')

    def test_result_2(self):
        w = self.w2
        self.assertEqual(
            w[0],
            'text-fingerprinting.descriptor.sentence#Lorem ipsum dolor sit amet, consectetur adipiscing elit')
        self.assertEqual(
            w[1],
            'text-fingerprinting.descriptor.sentence#Sed eget egestas purus')

