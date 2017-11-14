import unittest


def multiple_de(n, nombre):
    return nombre % n == 0

def contient_3(n,nombre):
    return n in str(nombre)

def contient_5(nombre):
    return "5" in str(nombre)

def convertis(nombre):
    
    if (multiple_de(3, nombre) and multiple_de(5, nombre)) or (contient_3("3", nombre) and contient_5(nombre)):
        return "fizzbuzz"
    if multiple_de(3, nombre) or contient_3("3", nombre):
        return "fizz"
    if multiple_de(5, nombre) or contient_5(nombre):
        return "buzz"
    return nombre


class ConvertisseurTest(unittest.TestCase):

    def test_multiple_de_3_donne_fizz(self):
        self.assertEquals("fizz", convertis(3))

    def test_multiple_de_5_donne_buzz(self):
        self.assertEquals("buzz", convertis(5))

    def test_multiple_de_15_donne_fizzbuzz(self):
        self.assertEquals("fizzbuzz", convertis(15))

    def test_multiple_de_6_donne_fizz(self):
        self.assertEquals("fizz", convertis(6))

    def test_multiple_de_10_donne_buzz(self):
        self.assertEquals("buzz", convertis(10))

    def test_multiple_de_8_donne_8(self):
        self.assertEquals(8, convertis(8))

    def test_multiple_de_30_donne_fizzbuzz(self):
        self.assertEquals("fizzbuzz", convertis(30))

    def test_multiple_de_31_donne_fizz(self):
        self.assertEquals("fizz", convertis(31))

    def test_multiple_de_154_donne_buzz(self):
        self.assertEquals("buzz", convertis(154))

    def test_multiple_de_1534_donne_fizzbuzz(self):
        self.assertEquals("fizzbuzz", convertis(1534))

    def test_multiple_de_35_donne_fizzbuzz(self):
        self.assertEquals("fizzbuzz", convertis(35))

if __name__ == "__main__":
    unittest.main()
