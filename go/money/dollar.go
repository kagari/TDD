package money

type Dollar struct {
	Money
}

func newDollar(amount int) *Dollar {
	d := new(Dollar)
	d.amount = amount
	return d
}

func (d *Dollar) times(multiplier int) *Dollar {
	return newDollar(d.amount * multiplier)
}

func (d *Dollar) equals(object *Money) bool {
        return d.Money.equals(object)
}

func (d *Dollar) get_money() *Money {
        return &d.Money
}
