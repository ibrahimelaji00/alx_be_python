# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = float(initial_balance)

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            print("Error: Deposit amount must be a number.")
            return
        if amount < 0:
            print("Error: Cannot deposit a negative amount.")
            return
        self._account_balance += amount

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            print("Error: Withdrawal amount must be a number.")
            return False
        if amount < 0:
            print("Error: Cannot withdraw a negative amount.")
            return False
        if amount > self._account_balance:
            return False
        self._account_balance -= amount
        return True

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")
