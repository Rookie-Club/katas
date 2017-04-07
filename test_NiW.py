import unittest
from NiW import *


class TestNiW(unittest.TestCase):
    def test_1_vaut_un(self):
        self.assertEqual("un", convert(1))

    def test_16_vaut_seize(self):
        self.assertEqual("seize", convert(16))

    def test_17_vaut_dix_sept(self):
        self.assertEqual("dix-sept", convert(17))

    def test_18_vaut_dix_huit(self):
        self.assertEqual("dix-huit", convert(18))

    def test_21_vaut_vingt_et_un(self):
        self.assertEqual("vingt-et-un", convert(21))

    def test_20_vaut_vingt(self):
        self.assertEqual("vingt", convert(20))


unittest.main()
