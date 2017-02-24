import unittest
from marinov import *

class TestMarkov(unittest.TestCase):
    def test_split_string(self):
        text = "je suis une loutre"
        self.assertEqual(["je", "suis", "une", "loutre"], get_words(text))

unittest.main()
