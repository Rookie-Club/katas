import unittest

def score(quilles):
    if quilles == [1]:
        return 1
    return 0

class BowlingTest(unittest.TestCase):

    def test_0_quilles_vaut_0(self):
        self.assertEqual(0, score([]))

    def test_1_quilles_vaut_1(self):
        self.assertEqual(1, score([1]))

unittest.main()
