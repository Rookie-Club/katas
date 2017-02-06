def draw_diamond(letter)
  return letter if letter == 'A'
end

def draw_triangle(letter)
	lines = []
	(1..alphabet_position(letter)).each do |i|
		lines << ' ' * ( alphabet_position(letter) - i) + letter(i) + ' ' * (i - 1)
	end 

	return lines.join("\n")
end

def alphabet_position(letter)
	letter.ord - 65 + 1
end

def letter(alphabet_position)
	(alphabet_position + 65 - 1).chr  
end
