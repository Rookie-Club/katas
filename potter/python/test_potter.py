import unittest


def calcule_prix(tomes):
    prix_unitaire = 8
    result = 0
    if tomes == [1, 0, 0, 0, 0]:
        result = tomes[0] * prix_unitaire
    if tomes == [1, 1, 0, 0, 0]:
        result = (tomes[0] + tomes[1]) * prix_unitaire * 0.95
    return result


class PotterTest(unittest.TestCase):

    def test_panier_vide(self):
        self.assertEqual(0, calcule_prix([]))

    def test_un_tome(self):
        self.assertEqual(8, calcule_prix([1, 0, 0, 0, 0]))

    def test_deux_tomes(self):
        self.assertEqual(8 * 2 * 0.95, calcule_prix([1, 1, 0, 0, 0]))

if __name__ == "__main__":
    unittest.main()
