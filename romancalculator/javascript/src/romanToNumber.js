
var romanToNumber = function (roman) {
  var dico = {"I": 1, "V": 5};
  var roman_table = roman.split("");

  if (roman_table.length == 0) {
    return 0;
  }
  var last_letter = roman_table.pop();
  return romanToNumber(roman_table.join("")) + dico[last_letter];
}
