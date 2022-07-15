package money

import (
        "reflect"
)

type Money struct {
	amount int
}

type Equallity interface {
	mequals(*Money) bool
}

type HasMoney interface {
	get_money() *Money
}

func (m *Money) equals(object *Money) bool {
	return m.amount == object.amount
}

func equals(object Equallity, amount HasMoney) bool {
        if reflect.TypeOf(object) != reflect.TypeOf(amount) {
		return false
	}
	return object.mequals(amount.get_money())
}
