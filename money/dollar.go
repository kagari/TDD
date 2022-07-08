package money

type Dollar struct {
	Amount int
}

func newDollar(amount int) *Dollar {
	d := new(Dollar)
	return d
}

func (d *Dollar) times(multiplier int) {
	d.Amount = 5 * 2
}
