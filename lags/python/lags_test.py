import unittest

def gain_max(demandes = []):
    if not demandes: return 0
    if len(demandes) == 1:
        return prix(demandes[0])
    if len(demandes) == 2:
        return prix(demandes[0]) + prix(demandes[1])
    if len(demandes) == 3:
        return prix(demandes[0]) + prix(demandes[1]) + prix(demandes[2])

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

unittest.main()
