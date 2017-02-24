import unittest
from marinov import *

class TestMarkov(unittest.TestCase):
    def test_split_string(self):
        text = "je suis une loutre je mange du thé"
        self.assertEqual(["je", "suis", "une", "loutre", "je", "mange", "du", "thé"], get_words(text))

    def test_pick_second_word_options(self):
        word = "je"
        self.assertEqual(["suis", "mange"], get_next_possible(word))
    def test_pick_next_word
unittest.main()
