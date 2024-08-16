# test_calculator.py

import unittest
from calculator import CreditCardCalculator

class TestCreditCardCalculator(unittest.TestCase):

    def setUp(self):
        # Initialize the calculator object with known values
        self.calculator = CreditCardCalculator(initial_balance=7550, interest_paid=86.97, previous_balance=7805.79)

    def test_calculate_monthly_interest_rate(self):
        expected_rate = (86.97 / 7805.79) * 100
        self.assertAlmostEqual(self.calculator.calculate_monthly_interest_rate(), expected_rate, places=2)

    def test_calculate_balance_reduction_time(self):
        target_balance = 5405
        monthly_payment = 210
        months = self.calculator.calculate_balance_reduction_time(target_balance, monthly_payment)
        self.assertEqual(months, 16)  # Update to the correct expected value

    def test_calculate_payoff_time(self):
        monthly_payment = 210
        payoff_time = self.calculator.calculate_payoff_time(monthly_payment)
        self.assertEqual(payoff_time, 47)  # Adjust this value based on the expected output

    def test_find_required_payment(self):
        months_for_payoff = 36
        required_payment = self.calculator.find_required_payment(months_for_payoff)
        self.assertAlmostEqual(required_payment, 255.7372, places=2)  # Update expected value


if __name__ == '__main__':
    unittest.main()

