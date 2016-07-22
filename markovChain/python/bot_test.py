import unittest

def bot(text, asked_word_quantity):
    words = text.split()
    new_text = ""

    if (asked_word_quantity >= 1):
        new_text += words[0]
    if (asked_word_quantity >= 2):
        new_text += ' ' + words[1]

    return new_text

class BotTest(unittest.TestCase):

    def test_pas_de_texte(self):
        self.assertEqual('', bot('', 0))

    def test_un_mot(self):
        self.assertEqual('patate', bot('patate', 1))
        self.assertEqual('banane', bot('banane', 1))

    def test_deux_mots_mais_un_demande(self):
        self.assertEqual('banane', bot('banane patate', 1))

    def test_deux_mots_mais_deux_demandes(self):
        self.assertEqual('banane patate', bot('banane patate', 2))

unittest.main()
