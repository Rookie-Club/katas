package fizzbuzz

import (
  "testing"
  "github.com/stretchr/testify/assert"
)

func Test1Return1 (t *testing.T) {
  assert.Equal(t, "1", FizzBuzz(1))
}


