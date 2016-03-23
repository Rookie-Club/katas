import unittest

def gain_max(demandes = []):
    if not demandes: return 0
    return prix(demandes[0])

def prix(demande):
    return demande[2]

class LagsTest(unittest.TestCase):
    def test_0_sans_demande(self):
        self.assertEqual(0, gain_max())

    def test_1_avec_1_demande(self):
        self.assertEqual(1, gain_max([[1,0,1]]))

unittest.main()
