import unittest

from money import Money


class MoneyTest(unittest.TestCase):
    def test_multiplication(self) -> None:
        five: Money = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self) -> None:
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertTrue(Money.franc(5) == Money.franc(5))
        self.assertFalse(Money.franc(5) == Money.franc(6))
        self.assertFalse(Money.franc(5) == Money.dollar(5))
    
    def test_franc_multiplication(self) -> None:
        five: Money = Money.franc(5)
        self.assertEqual(Money.franc(10), five.times(2))
        self.assertEqual(Money.franc(15), five.times(3))

    def test_currency(self) -> None:
        self.assertEqual('USD', Money.dollar(1).get_currency())
        self.assertEqual('CHF', Money.franc(1).get_currency())

if __name__ == '__main__':
    unittest.main()