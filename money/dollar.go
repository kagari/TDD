package money

type Dollar struct {
	Amount int
}

func newDollar(amount int) *Dollar {
	d := new(Dollar)
	d.Amount = 10
	return d
}

func (d Dollar) times(multiplier int) {
}
