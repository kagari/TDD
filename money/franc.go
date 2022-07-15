package money

type Franc struct {
	amount int
}

func newFranc(amount int) *Franc {
	d := new(Franc)
	d.amount = amount
	return d
}

func (d *Franc) times(multiplier int) *Franc {
	return newFranc(d.amount * multiplier)
}

func (d *Franc) equals(object *Franc) bool {
	return d.amount == object.amount
}
