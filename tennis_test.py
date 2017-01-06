import unittest
from tennis import *


class TennisTest(unittest.TestCase):
    def test_player_1_scores_first_point(self):
        self.assertEqual([15, 0], game_score(['j1']))

    def test_player_1_scores_second_point(self):
        self.assertEqual([30, 0], game_score(['j1', 'j1']))

    def test_player_1_scores_third_point(self):
        self.assertEqual([40, 0], game_score(['j1', 'j1', 'j1']))

    def test_player_2_scores_first_point(self):
        self.assertEqual([0, 15], game_score(['j2']))

    def test_players_tie_at_15(self):
        self.assertEqual([15, 15], game_score(['j2', 'j1']))

    def test_player_1_wins_2_times_player_2_wins_1_time(self):
        self.assertEqual([30, 15], game_score(['j2', 'j1', 'j1']))

    def xtest_player_1_wins_4_times(self):
        self.assertEqual([30, 15], game_score(['j2', 'j1', 'j1']))

unittest.main()
