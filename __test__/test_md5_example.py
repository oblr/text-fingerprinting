import unittest
from simple import md5, md5_file

class Test(unittest.TestCase):

    def setUp(self):
        self.h1 = md5(".data/example-text.txt")
        self.h2 = md5(".data/example-text2.txt")

        self.h3 = md5_file(".data/example-text.txt")
        self.h4 = md5_file(".data/example-text2.txt")

    def test_h1(self):
        self.assertEqual("c71fb2cd2253e64f1a511458dbe3e36c", self.h1)

    def test_h2(self):
        self.assertEqual("c6596fb05f326654cde6a4cd26bcd9a5", self.h2)

    def test_h1_file(self):
        self.assertEqual("15a9aa6e0c89792a430f7081ec027993", self.h3)

    def test_h2_file(self):
        self.assertEqual("09531bb69426fbdff7e233d6430cca6e", self.h4)