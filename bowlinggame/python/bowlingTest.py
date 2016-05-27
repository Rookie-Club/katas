import unittest

def score(quilles):
    if len(quilles) == 0:
        return 0
    if len(quilles) == 1:
        return quilles[0]
    if quilles[0] + quilles[1] == 10:
        return quilles[0] + quilles[1] + quilles[2] + score(quilles[2::])
    else:
        return quilles[0] + quilles[1] + score(quilles[2::])

class BowlingTest(unittest.TestCase):

    def test_0_quilles_vaut_0(self):
        self.assertEqual(0, score([]))

    def test_1_quilles_vaut_1(self):
        self.assertEqual(1, score([1]))

    def test_3_quilles_vaut_3(self):
        self.assertEqual(3, score([3]))

    def test_3_quilles_en_2_fois_vaut_3(self):
        self.assertEqual(2 + 1, score([2, 1]))

    def test_spare(self):
        self.assertEqual(8 + 2 + 3 + 3, score([8, 2, 3]))

unittest.main()
