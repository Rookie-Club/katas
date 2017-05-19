import unittest
from tennis import *


class TennisTest(unittest.TestCase):
    def test_no_one_scor(self):
        points = []
        self.assertEqual([0, 0], match(points))

    def test_player_1_scor(self):
        points = ["p1"]
        self.assertEqual([15, 0], match(points))

    def test_player_2_scor(self):
        points = ["p2"]
        self.assertEqual([0, 15], match(points))

    def test_player_1_scor_2_time(self):
        points = ["p1", "p1"]
        self.assertEqual([30, 0], match(points))

    def test_player_1_take_advantage(self):
        points = ["p1", "p1", "p1", "p2", "p2", "p2", "p1"]
        self.assertEqual(["advantage", 40], match(points))

    def test_player_1_take_set(self):
        points = ["p1", "p1", "p1", "p1"]
        self.assertEqual([30, 0], match(points))


if __name__ == "__main__":
    unittest.main()
