package money

type Money struct {
	amount int
}

func (m *Money) equals(object *Money) bool {
	return m.amount == object.amount
}
