import unittest
from tennis import *


class TennisTest(unittest.TestCase):
    def test_player_1_scores_first_point(self):
        self.assertEqual([15, 0], score(['j1']))

    def test_player_1_scores_second_point(self):
        self.assertEqual([30, 0], score(['j1', 'j1']))

    def test_player_1_scores_third_point(self):
        self.assertEqual([40, 0], score(['j1', 'j1', 'j1']))

    def test_player_2_scores_first_point(self):
        self.assertEqual([0, 15], score(['j2']))

unittest.main()
