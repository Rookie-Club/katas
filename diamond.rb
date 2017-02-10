def diamond(letter)
	flip_vertical flip_horizontal triangle letter
end

def flip_vertical(lines)
	lines.map { |line| line += line.chop.reverse! }
end

def flip_horizontal(lines)
	lines + lines.reverse.drop(1)
end

def triangle(letter)
	triangle_lines = []
	(1..alphabet_position(letter)).each do |i|
		triangle_lines << ' ' * ( alphabet_position(letter) - i) + letter(i) + ' ' * (i - 1)
	end 
	triangle_lines
end

def alphabet_position(letter)
	letter.ord - 65 + 1
end

def letter(alphabet_position)
	(alphabet_position + 65 - 1).chr  
end
 





