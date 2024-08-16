# calculator.py

import scipy.optimize as opt

class CreditCardCalculator:
    """
    A class to represent a credit card calculator.
    
    Attributes
    ----------
    initial_balance : float
        The initial balance on the credit card.
    interest_paid : float
        The interest paid in the last month.
    previous_balance : float
        The balance of the previous month.
    monthly_interest_rate : float
        The calculated monthly interest rate.
    
    Methods
    -------
    calculate_monthly_interest_rate():
        Calculates the monthly interest rate.
        
    calculate_balance_reduction_time(target_balance, monthly_payment):
        Calculates the number of months required to reduce the balance to a target amount.
        
    calculate_payoff_time(monthly_payment):
        Calculates the number of months required to pay off the entire balance.
        
    find_required_payment(months):
        Finds the required monthly payment to pay off the balance in a specified number of months.
    """

    def __init__(self, initial_balance, interest_paid, previous_balance):
        """
        Constructs all the necessary attributes for the CreditCardCalculator object.

        Parameters
        ----------
        initial_balance : float
            The initial balance on the credit card.
        interest_paid : float
            The interest paid in the last month.
        previous_balance : float
            The balance of the previous month.
        """
        self.initial_balance = initial_balance
        self.interest_paid = interest_paid
        self.previous_balance = previous_balance
        self.monthly_interest_rate = self.calculate_monthly_interest_rate()

    def calculate_monthly_interest_rate(self):
        """Calculates the monthly interest rate based on the previous balance and interest paid."""
        return (self.interest_paid / self.previous_balance) * 100

    def calculate_balance_reduction_time(self, target_balance, monthly_payment):
        """Calculates the number of months required to reduce the balance to a target amount."""
        months = 0
        balance = self.initial_balance
        while balance > target_balance:
            interest = balance * (self.monthly_interest_rate / 100)
            principal_payment = monthly_payment - interest
            balance -= principal_payment
            months += 1
        return months

    def calculate_payoff_time(self, monthly_payment):
        """Calculates the number of months required to pay off the entire balance."""
        months = 0
        balance = self.initial_balance
        while balance > 0:
            interest = balance * (self.monthly_interest_rate / 100)
            principal_payment = monthly_payment - interest
            balance -= principal_payment
            months += 1
        return months

    def find_required_payment(self, months):
        """Finds the required monthly payment to pay off the balance in a specified number of months."""
        def balance_after_months(monthly_payment):
            balance = self.initial_balance
            for _ in range(months):
                interest = balance * (self.monthly_interest_rate / 100)
                principal_payment = monthly_payment - interest
                balance -= principal_payment
            return balance

        required_payment = opt.newton(balance_after_months, 200)
        return required_payment

