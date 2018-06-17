package roman_to_number

import "testing"

var testCases = []struct {
	expected int
	value    string
}{
	{1, "I"},
	{5, "V"},
	{6, "VI"},
	{4, "IV"},
}

func TestRomanToNumber(t *testing.T) {
	for _, test := range testCases {
		expected := test.expected
		value := test.value
		actual := NumberToRoman(value)
		if actual != expected {
			t.Errorf("Except %d to equal %d for %s", actual, expected, value)
		}
	}
}
