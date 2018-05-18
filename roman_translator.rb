class RomanTranslator
  def initialize
    @dict_roman_arab = {
      'I' => 1,
      'V' => 5,
    }
  end

  def to_number(roman)
    if roman == 'I' + 'V'
      return @dict_roman_arab['V'] - @dict_roman_arab['I']
    end

    @dict_roman_arab[roman]
  end
end