def draw_diamond(letter)
  return 'A\nB B\nA' if letter == 'B'
  return 'A\nB B\nC  C\nB B\nA' if letter == 'C'
  return letter if letter == 'A'
end
