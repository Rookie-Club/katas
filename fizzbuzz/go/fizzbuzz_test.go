package fizzbuzz

import "testing"

var testCases = []struct {
  expected string
  value int
} {
  { "1", 1 },
  { "2", 2 },
  { "fizz", 3 },
  { "fizz", 6 },
  { "buzz", 5 },
  { "fizzbuzz", 15 },
}

func Test1Return1 (t *testing.T) {

  for _, testCase := range testCases {
    actual := FizzBuzz(testCase.value)
    if actual != testCase.expected {
      t.Errorf("FizzBuzz(%d) doit renvoyer %s, mais a reçu %s.", testCase.value, testCase.expected, actual)
    }
  }

}


