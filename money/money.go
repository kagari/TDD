package money

type Money struct {
	amount int
}

type Equallity interface {
	mequals(*Money) bool
}

func (m *Money) equals(object *Money) bool {
	return m.amount == object.amount
}

func equals(object Equallity, amount Money) bool {
	return object.mequals(&amount)
}
