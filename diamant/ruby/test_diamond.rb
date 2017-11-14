require 'minitest/autorun'
require './diamond'

class TestDiamond < Minitest::Test

  def test_A_triangle
    assert_equal ['A'], triangle('A')
  end
  
  def test_B_triangle
  	assert_equal [" A", "B "], triangle('B')
  end

  def test_C_triangle
  	assert_equal ["  A"," B ","C  "], triangle('C')
  end

  def test_letter_to_alphabet_position
  	assert_equal 26, alphabet_position('Z')
  end

  def test_alphabet_position_to_letter
  	assert_equal 'A', letter(1)
  end

  def test_B_triangle_horizontal_flip
    assert_equal [" A", "B "," A"], flip_horizontal((triangle('B')))
  end

  def test_B_triangle_vertical_flip
    assert_equal [" A ","B B"], flip_vertical((triangle('B')))
  end

  def test_A_diamond
    assert_equal ['A'], diamond('A')
  end

  def test_C_diamond
    assert_equal ["  A  "," B B ","C   C"," B B ","  A  "], diamond('C')
  end

end

