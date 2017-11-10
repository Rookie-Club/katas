class Match
	def initialize(player_a, player_b)
		@points = {player_a => 0, player_b => 0}
	end

	def new_point_by(player)
		@points[player] = 15
	end

	def points_of(player)
		@points[player]
	end
end