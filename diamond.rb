def alphabet_position(letter)
	letter.ord - 65 + 1
end

def letter(alphabet_position)
	(alphabet_position + 65 - 1).chr  
end

def triangle(letter)
	triangle_lines = []
	(1..alphabet_position(letter)).each do |i|
		triangle_lines << ' ' * ( alphabet_position(letter) - i) + letter(i) + ' ' * (i - 1)
	end 

	return triangle_lines
end

def flip_horizontal(lines)
	lines.reverse
end

def flip_vertical(lines)
	lines.each do |string|
		string.reverse!
	end
end

def draw(lines)
	lines.join("\n")
end








