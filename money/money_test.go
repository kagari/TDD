package money

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMultiplication(t *testing.T) {
	var five *Dollar = newDollar(5)
	var product *Dollar = five.times(2)
	assert.Equal(t, 10, product.Amount)
	product = five.times(3)
	assert.Equal(t, 15, product.Amount)
}

func TestEquality(t *testing.T) {
	assert.True(t, newDollar(5).equals(newDollar(5)))
}
