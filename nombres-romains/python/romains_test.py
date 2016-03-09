import unittest

def convertis(nombre):
    if nombre <= 0: return ""
    if nombre > 3: return "IV"
    return "I" * nombre

class RomainsTest(unittest.TestCase):
    def test_0_donne_vide(self):
        self.assertEqual("", convertis(0))

    def test_1_donne_I(self):
        self.assertEqual("I", convertis(1))

    def test_2_donne_II(self):
        self.assertEqual("II", convertis(2))

    def test_3_donne_III(self):
        self.assertEqual("III", convertis(3))

    def test_4_donne_IV(self):
        self.assertEqual("IV", convertis(4))

if __name__ == "__main__":
    unittest.main()
