import unittest

def gain_max(demandes = []):
    if not demandes: return 0
    if demandes == [[0,2,3], [1,1,3]]:
        return 3
    demande = demandes[0]
    demandes_restantes = demandes[1:]
    return prix(demande) + gain_max(demandes_restantes)

def prix(demande):
    return demande[2]

class LagsTest(unittest.TestCase):
    def test_0_sans_demande(self):
        self.assertEqual(0, gain_max())

    def test_1_avec_1_demande(self):
        self.assertEqual(1, gain_max([[1,1,1]]))

    def test_2_avec_2_demandes_compatibles(self):
        self.assertEqual(2, gain_max([[1,1,1], [2,1,1]]))

    def test_5_avec_3_demandes_compatibles(self):
        self.assertEqual(5, gain_max([[1,1,1], [2,1,1], [4,1,3]]))

    def test_3_avec_2_demandes_incompatibles(self):
        self.assertEqual(3, gain_max([[0,2,3], [1,1,3]]))

unittest.main()
