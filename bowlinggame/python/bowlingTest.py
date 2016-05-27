import unittest

def score(quilles):
    result = 0
    for quille in quilles:
        result += quille
    return result

class BowlingTest(unittest.TestCase):

    def test_0_quilles_vaut_0(self):
        self.assertEqual(0, score([]))

    def test_1_quilles_vaut_1(self):
        self.assertEqual(1, score([1]))

    def test_3_quilles_vaut_3(self):
        self.assertEqual(3, score([3]))

    def test_3_quilles_en_2_fois_vaut_3(self):
        self.assertEqual(2 + 1, score([2, 1]))

unittest.main()
