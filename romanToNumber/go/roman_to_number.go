package roman_to_number

import "strings"

var romanNumber = map[string]int{"I": 1, "V": 5, "X": 10}

func NumberToRoman(roman string) int {

	var number, previousValue = 0, 0
	var splittedRoman = strings.Split(roman, "")

	for i := len(splittedRoman) - 1; i >= 0; i-- {
		currentValue := romanNumber[splittedRoman[i]]
		if previousValue > currentValue {
			number -= currentValue
		} else {
			number += currentValue
		}
		previousValue = currentValue
	}

	return number
}
