require 'minitest/autorun'
require_relative './match'

class TennisTest < MiniTest::Test

	def test_point_player_one_begin_of_the_game
		match = Match.new
		assert_equal(0, match.point_player_one)
	end

	def test_point_player_two_begin_of_the_game
		match = Match.new
		assert_equal(0, match.point_player_two)
	end

	def test_player_scores_one_point
		match = Match.new
		match.player_one_scores
		match.player_two_scores
		assert_equal(15, match.point_player_one)
		assert_equal(15, match.point_player_two)
	end
end