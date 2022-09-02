import unittest

from money import Money
from expression import Expression
from bank import Bank
from sum import Sum 


class MoneyTest(unittest.TestCase):
    def test_multiplication(self) -> None:
        five: Money = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self) -> None:
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertFalse(Money.franc(5) == Money.dollar(5))

    def test_currency(self) -> None:
        self.assertEqual('USD', Money.dollar(1).get_currency())
        self.assertEqual('CHF', Money.franc(1).get_currency())

    def test_simple_addition(self) -> None:
        five: Money = Money.dollar(5)
        sum_: Expression = five.plus(five)
        bank: Bank = Bank()
        reduced: Money = bank.reduce(sum_, 'USD')
        self.assertEqual(Money.dollar(10), reduced)

    def test_puls_returns_sum(self) -> None:
        five: Money = Money.dollar(5)
        result: Expression = five.plus(five)
        sum_: Sum = result
        self.assertEqual(five, sum_.augend)
        self.assertEqual(five, sum_.addend)

    def test_reduce_sum(self) -> None:
        sum_: Expression = Sum(Money.dollar(3), Money.dollar(4))
        bank: Bank = Bank()
        result: Money = bank.reduce(sum_, 'USD')
        self.assertEqual(Money.dollar(7), result)

    def test_reduce_money(self) -> None:
        bank: Bank = Bank()
        result: Money = bank.reduce(Money.dollar(1), 'USD')
        self.assertEqual(Money.dollar(1), result)

    def test_reduce_money_different_currency(self) -> None:
        bank: Bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        result: Money = bank.reduce(Money.franc(2), 'USD')
        self.assertEqual(Money.dollar(1), result)

    def test_identity_rate(self) -> None:
        self.assertEqual(1, Bank().rate('USD', 'USD'))

    def test_mixed_addiction(self) -> None:
        five_bucks: Expression = Money.dollar(5)
        ten_francs: Expression = Money.franc(10)
        bank: Bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        result: Money = bank.reduce(five_bucks.plus(ten_francs), 'USD')
        self.assertEqual(Money.dollar(10), result)

    def test_sum_plus_money(self) -> None:
        five_bucks: Expression = Money.dollar(5)
        ten_francs: Expression = Money.franc(10)
        bank: Bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        sum_: Expression = Sum(five_bucks, ten_francs).plus(five_bucks)
        result: Money = bank.reduce(sum_, 'USD')
        self.assertEqual(Money.dollar(15), result)

    def test_sum_times(self) -> None:
        five_bucks: Expression = Money.dollar(5)
        ten_francs: Expression = Money.franc(10)
        bank: Bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        sum_: Expression = Sum(five_bucks, ten_francs).times(2)
        result: Money = bank.reduce(sum_, 'USD')
        self.assertEqual(Money.dollar(20), result)
        

if __name__ == '__main__':
    unittest.main()
