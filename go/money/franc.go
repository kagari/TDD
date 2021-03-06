package money

type Franc struct {
	Money
}

func newFranc(amount int) *Franc {
	f := new(Franc)
	f.amount = amount
	return f
}

func (f *Franc) times(multiplier int) *Franc {
	return newFranc(f.amount * multiplier)
}

func (f *Franc) equals(object *Money) bool {
	return f.Money.equals(object)
}

func (f *Franc) get_money() *Money {
	return &f.Money
}

