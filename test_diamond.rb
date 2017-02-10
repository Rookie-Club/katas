require 'minitest/autorun'
require './diamond'

class TestDiamond < Minitest::Test

  def test_A_triangle
    assert_equal 'A', draw(triangle('A'))
  end
  
  def test_B_triangle
  	assert_equal " A\nB ", draw(triangle('B'))
  end

  def test_C_triangle
  	assert_equal "  A\n B \nC  ", draw(triangle('C'))
  end

  def test_letter_to_alphabet_position
  	assert_equal 26, alphabet_position('Z')
  end

  def test_alphabet_position_to_letter
  	assert_equal 'A', letter(1)
  end

  def test_B_triangle_horizontal_flip
    assert_equal " A\nB \n A", draw(flip_horizontal((triangle('B'))))
  end

  def test_B_triangle_vertical_flip
    assert_equal " A \nB B", draw(flip_vertical((triangle('B'))))
  end

  def test_A_diamond
    assert_equal 'A', draw(diamond('A'))
  end

  def test_C_diamond
    assert_equal "  A  \n B B \nC   C\n B B \n  A  ", draw(diamond('C'))
  end

end

