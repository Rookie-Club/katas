require 'minitest/autorun'
require './diamond'

class TestDiamond < Minitest::Test

  def test_A_diamond
    assert_equal 'A', draw_diamond('A')
  end

end

