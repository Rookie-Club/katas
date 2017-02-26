import unittest
from marinov import *

class TestMarkov(unittest.TestCase):
    def test_split_string(self):
        text = "je suis une loutre je mange du thé"
        self.assertEqual(["je", "suis", "une", "loutre", "je", "mange", "du", "thé"], get_words(text))

    def test_pick_second_word_with_one_option(self):
        text = get_words("je suis une loutre je mange du thé")
        word = "une"
        self.assertEqual("loutre", get_next_word(word, text))
        word = "suis"
        self.assertEqual("une", get_next_word(word, text))

    def test_pick_second_word_with_2_options(self):
        text = get_words("je suis une loutre je mange du thé")
        word = "je"
        self.assertIn(get_next_word(word, text), ["suis", "mange"])

    def test_pick_second_word_with_current_word_at_end(self):
        text = get_words("je suis une loutre je mange du thé")
        word = "thé"
        self.assertIn(get_next_word(word, text), text)

unittest.main()
