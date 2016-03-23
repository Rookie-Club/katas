import unittest

def gain_max(demandes = []):
    if not demandes: return 0
    return demandes[0][2]

class LagsTest(unittest.TestCase):
    def test_0_sans_demande(self):
        self.assertEqual(0, gain_max())

    def test_1_avec_1_demande(self):
        self.assertEqual(1, gain_max([[1,0,1]]))

unittest.main()
