package money

type Dollar struct {
	amount int
}

func newDollar(amount int) *Dollar {
	d := new(Dollar)
	d.amount = amount
	return d
}

func (d *Dollar) times(multiplier int) *Dollar {
	return newDollar(d.amount * multiplier)
}

func (d *Dollar) equals(object *Dollar) bool {
	return d.amount == object.amount
}
