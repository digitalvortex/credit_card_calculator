# gui.py

import tkinter as tk
from tkinter import messagebox, simpledialog
from calculator import CreditCardCalculator

class CreditCardCalculatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Credit Card Calculator")

        # Initial Balance
        self.balance_label = tk.Label(self.root, text="Initial Balance:")
        self.balance_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.balance_entry = tk.Entry(self.root)
        self.balance_entry.grid(row=0, column=1, padx=10, pady=5)

        # Interest Paid
        self.interest_paid_label = tk.Label(self.root, text="Interest Paid Last Month:")
        self.interest_paid_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.interest_paid_entry = tk.Entry(self.root)
        self.interest_paid_entry.grid(row=1, column=1, padx=10, pady=5)

        # Previous Balance
        self.prev_balance_label = tk.Label(self.root, text="Previous Month's Balance:")
        self.prev_balance_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.prev_balance_entry = tk.Entry(self.root)
        self.prev_balance_entry.grid(row=2, column=1, padx=10, pady=5)

        # Calculate Button
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate(self):
        try:
            # Extract the user inputs
            initial_balance = float(self.balance_entry.get())
            interest_paid = float(self.interest_paid_entry.get())
            previous_balance = float(self.prev_balance_entry.get())

            # Create the calculator object
            calculator = CreditCardCalculator(initial_balance, interest_paid, previous_balance)

            # Ask for the type of calculation to perform
            choice = simpledialog.askinteger("Calculation Choice", 
                                             "Choose the calculation:\n"
                                             "1. Monthly Interest Rate\n"
                                             "2. Months to reduce balance to target\n"
                                             "3. Months to pay off entire balance\n"
                                             "4. Required Monthly Payment to pay off in specific months",
                                             minvalue=1, maxvalue=4)
            
            if choice == 1:
                rate = calculator.calculate_monthly_interest_rate()
                messagebox.showinfo("Result", f"Monthly Interest Rate: {rate:.2f}%")
            elif choice == 2:
                target_balance = float(simpledialog.askstring("Input", "Enter the target balance:"))
                monthly_payment = float(simpledialog.askstring("Input", "Enter the monthly payment:"))
                months_to_target = calculator.calculate_balance_reduction_time(target_balance, monthly_payment)
                messagebox.showinfo("Result", f"Months to reduce balance to {target_balance} GBP: {months_to_target} months")
            elif choice == 3:
                monthly_payment = float(simpledialog.askstring("Input", "Enter the monthly payment:"))
                payoff_time = calculator.calculate_payoff_time(monthly_payment)
                messagebox.showinfo("Result", f"Months to pay off entire balance: {payoff_time} months")
            elif choice == 4:
                months_for_payoff = int(simpledialog.askstring("Input", "Enter the number of months to pay off:"))
                required_payment = calculator.find_required_payment(months_for_payoff)
                messagebox.showinfo("Result", f"Required Monthly Payment to pay off in {months_for_payoff} months: {required_payment:.2f} GBP")
            else:
                messagebox.showerror("Error", "Invalid choice, please select again.")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values.")

    def run(self):
        self.root.mainloop()
