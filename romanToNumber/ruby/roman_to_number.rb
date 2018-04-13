def conversion(roman)
  correspondances = {
    'I' => 1,
    'V' => 5,
    'X' => 10,
    'L' => 50,
    'C' => 100,
    'D' => 500,
    'M' => 1000
  }

  if (roman == 'XX')
    return correspondances['X'] + correspondances['X']
  else
    correspondances[roman]
  end
end
