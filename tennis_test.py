import unittest


class TennisTest(unittest.TestCase):
    def test_tennis_premier_point_vaut_5(self):
        self.assertEqual([5], score(5))

unittest.main()
