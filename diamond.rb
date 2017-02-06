def draw_diamond(letter)
  return letter if letter == 'A'
end

def draw_triangle(letter)
	return 'A\nB ' if letter == 'B'
end

def alphabet_position(letter)
	letter.ord - 65 + 1
end

def letter(alphabet_position)
	(alphabet_position + 65 - 1).chr  
end
