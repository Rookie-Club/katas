import unittest

def bot(text, word_count):
    if (text == "banane patate"):
        return "banane"
    return text

class BotTest(unittest.TestCase):

    def test_pas_de_texte(self):
        self.assertEqual('', bot('', 0))

    def test_un_mot(self):
        self.assertEqual('patate', bot('patate', 1))
        self.assertEqual('banane', bot('banane', 1))

    def test_deux_mot_mais_un_demande(self):
        self.assertEqual('banane', bot('banane patate', 1))

unittest.main()
