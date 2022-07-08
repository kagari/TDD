package money

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMoney(t *testing.T) {
	var five *Dollar = newDollar(5)
	var product *Dollar = five.times(2)
	assert.Equal(t, 10, product.Amount)
	product = five.times(3)
	assert.Equal(t, 15, product.Amount)
}
