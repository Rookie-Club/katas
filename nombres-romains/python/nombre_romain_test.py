import unittest
from nombre_romain import *

class NombreRomainTest(unittest.TestCase):

    def test_1_donne_I(self):
        self.assertEqual("I", convertis(1))

    def test_5_donne_V(self):
        self.assertEqual("V", convertis(5))

if __name__ == "__main__":
    unittest.main()
