package money

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMoney(t *testing.T) {
	var five *Dollar = newDollar(5)
	five.times(2)
	assert.Equal(t, 10, five.Amount)
}
