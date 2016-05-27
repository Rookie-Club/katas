import unittest

class BowlingTest(unittest.TestCase):

    def test_0_quilles_vaut_0(self):
        self.assertEqual(0, score([]))

unittest.main()
