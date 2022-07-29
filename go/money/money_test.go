package money

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMultiplication(t *testing.T) {
	var five *Dollar = newDollar(5)
	assert.Equal(t, newDollar(10), five.times(2))
	assert.Equal(t, newDollar(15), five.times(3))
}

func TestEquality(t *testing.T) {
	assert.True(t, equals(newDollar(5), newDollar(5)))
	assert.False(t, equals(newDollar(5), newDollar(6)))
	assert.True(t, equals(newFranc(5),newFranc(5)))
	assert.False(t, equals(newFranc(5), newFranc(6)))
	assert.False(t, equals(newFranc(5), newDollar(5)))
}

func TestFrancMultiplication(t *testing.T) {
	var five *Franc = newFranc(5)
	assert.Equal(t, newFranc(10), five.times(2))
	assert.Equal(t, newFranc(15), five.times(3))
}
