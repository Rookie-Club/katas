import unittest

def convertis(nombre):
    return "I"

class RomainsTest(unittest.TestCase):
    def test_1_donne_I(self):
        self.assertEqual("I", convertis(1))

if __name__ == "__main__":
    unittest.main()
