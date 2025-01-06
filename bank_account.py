class BalanceException(Exception):
    pass

class InvalidInput(Exception):
    pass

class BankAccount:
    def __init__(self, balance, name):
        if balance < 0:
            raise InvalidInput("Initial balance must be a positive number.")
        self.balance = balance
        self.name = name
        print(f"\nAccount '{self.name}' created.\nCurrent Balance = {self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}'\nCurrent Balance = {self.balance:.2f}")

    def deposit(self, amount):
        try:
            self.balance += amount
            print("\nDeposit completed.")
            self.get_balance()
        except InvalidInput as error:
            print(f"Error: {error}")

    def withdraw(self, amount):
        try: 
            self.check_balance(amount)
            self.balance -= amount
            print("\nWithdrawal completed.")
            self.get_balance()
        except (InvalidInput, BalanceException) as error:
            print(f"Error: {error}")

    def check_balance(self, amount):
        """Checks if the balance is sufficient for a withdrawal."""
        if self.balance < amount:
            raise BalanceException(
                f"Account '{self.name}' only has a balance of {self.balance:.2f}. Please try again.")
        
class SavingsAccount(BankAccount):
    """A standard savings account with no special deposit rules."""
    pass

class InterestRewardAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount * (1 + 0.05)
        print("\nDeposit completed.")
        self.get_balance()
