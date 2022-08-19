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
        result: Money = bank.reduce(sum_, "USD")
        self.assertEqual(Money.dollar(7), result)

if __name__ == '__main__':
    unittest.main()
