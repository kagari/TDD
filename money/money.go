package money

import (
        "reflect"
)

type Money struct {
	amount int
}

type Equallity interface {
	equals(*Money) bool
}

type HasMoney interface {
	get_money() *Money
}

func (m *Money) equals(object *Money) bool {
	return m.amount == object.amount
}

func equals(object Equallity, amount HasMoney) bool {
	return object.equals(amount.get_money()) &&
		reflect.TypeOf(object) == reflect.TypeOf(amount)
}
