import unittest

def convertis(nombre):
    if nombre == 2:
        return "II"
    return "I"

class RomainsTest(unittest.TestCase):
    def test_1_donne_I(self):
        self.assertEqual("I", convertis(1))

    def test_2_donne_II(self):
        self.assertEqual("II", convertis(2))

    def test_3_donne_III(self):
        self.assertEqual("III", convertis(3))

if __name__ == "__main__":
    unittest.main()
