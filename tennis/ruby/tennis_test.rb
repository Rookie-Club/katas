require 'minitest/autorun'
require_relative './match'

class TennisTest < MiniTest::Test
	def test_point_players_begin_of_the_game
		match = Match.new(:Etienne, :Roger)
		assert_equal(0, match.points_of(:Roger))
	end

	def test_player_scores_one_point
		match = Match.new(:Sarah, :Elodie)
		match.new_point_by(:Sarah)
		match.new_point_by(:Elodie)
		assert_equal(15, match.points_of(:Sarah))
		assert_equal(15, match.points_of(:Elodie))
	end
end