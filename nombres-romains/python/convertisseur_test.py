import unittest


def convertis(nombre=0):
    romains = {0: "", 1: "I", 5: "V", 10: "X"}

    if nombre in romains.keys():
        return romains[nombre]
    else:
        keys = romains.keys()
        for i in reversed(sorted(keys)):
            if nombre > i:
                reste = nombre - i
                return (romains[i] + convertis(reste))


class ConvertisseurTest(unittest.TestCase):
    def test_1_donne_I(self):
        self.assertEquals("I", convertis(1))

    def test_5_donne_V(self):
        self.assertEquals("V", convertis(5))

    def test_10_donne_X(self):
        self.assertEquals("X", convertis(10))

    def test_rien_donne_rien(self):
        self.assertEquals("", convertis())

    def test_6_donne_VI(self):
        self.assertEquals("VI", convertis(6))

    def test_7_donne_VII(self):
        self.assertEquals("VII", convertis(7))
if __name__ == "__main__":
    unittest.main()
