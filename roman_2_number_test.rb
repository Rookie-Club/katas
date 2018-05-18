require 'minitest/autorun'
require './roman_translator'

class Roman2NumberTest < Minitest::Test
  def test_I_gives_1
    number_value = 1
    roman_value = 'I'

    assert_translate(roman_value, number_value)
  end

  def test_V_gives_5
    number_value = 5
    roman_value = 'V'

    assert_translate(roman_value, number_value)
  end

  def test_IV_gives_4
    number_value = 4
    roman_value = 'IV'

    assert_translate(roman_value, number_value)
  end

  def assert_translate(roman_value, number_value)
    roman_translator = RomanTranslator.new()
    result = roman_translator.to_number(roman_value)
    assert_equal(number_value, result)
  end
end
