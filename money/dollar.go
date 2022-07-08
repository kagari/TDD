package money

type Dollar struct {
	Amount int
}

func newDollar(amount int) *Dollar {
	d := new(Dollar)
	d.Amount = amount
	return d
}

func (d *Dollar) times(multiplier int) {
	d.Amount *= multiplier
}
