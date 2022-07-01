package money

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestMoney(t *testing.T) {
	var five *Dollar = newDollar(5)
	five.times(2)
	assert.Equal(t, 10, five.amount)
}
