class Match
	attr_reader :point_player_one, :point_player_two

	def initialize
		@point_player_one = 0
		@point_player_two = 0
	end

	def player_one_scores
		@point_player_one = 15
	end

	def player_two_scores
		@point_player_two = 15
	end
end