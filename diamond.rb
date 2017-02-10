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
	lines + lines.reverse.drop(1)
end

def flip_vertical(lines)
	lines.each_with_index do |string,i|
		lines[i] += string.chop.reverse! 
	end
end

def draw(lines)
	lines.join("\n")
end

def diamond(letter)
	flip_vertical(flip_horizontal(triangle(letter)))
end 





