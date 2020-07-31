import unittest

from descriptors import text_as_descriptor, text_from_sentence_descriptor
from example_texts import EXAMPLE_TEXT_1, EXAMPLE_TEXT_2, EXAMPLE_TEXT_3, EXAMPLE_TEXT_4
from shingles.find import shingles_from_text
from shingles.jaccard import jaccard
from transforms import windowing


class Test(unittest.TestCase):

    def setUp(self):
        self.h1 = EXAMPLE_TEXT_3
        self.h2 = EXAMPLE_TEXT_4

        self.w1 = windowing.sentences(
            text_as_descriptor(self.h1)
        )
        self.w2 = windowing.sentences(
            text_as_descriptor(self.h2)
        )
        self.K = 4

    def test_result(self):
        text1_shingle_sets = [shingles_from_text(
            text_from_sentence_descriptor(sdescriptor), self.K
        ) for sdescriptor in self.w1]
        text2_shingle_sets = [shingles_from_text(
            text_from_sentence_descriptor(sdescriptor), self.K
        ) for sdescriptor in self.w2]

        self.assertEqual(len(text1_shingle_sets), 2)
        self.assertEqual(len(text2_shingle_sets), 1)

        similarities = []
        for s1 in text1_shingle_sets:
            for s2 in text2_shingle_sets:
                similarities.append(jaccard(s1, s2))

        self.assertEqual(len(similarities), 2)
        self.assertEqual(similarities[0], 0.1111111111111111)
        self.assertEqual(similarities[1], 0.14285714285714285)


