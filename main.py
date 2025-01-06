from bank_account import *
from bank import *

def get_positive_float(prompt):
    """Utility function to handle user input for positive float values."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Amount must be positive.")
            return value
        except ValueError as error:
            print(f"Invalid input: {error} Please try again.\n")

def main():
    bank = Bank()
    print("\nWelcome to the Bank of Maryland!")

    while True:
        print("\nWould you like to open a new account or access an existing one?")
        print("1: Open a New Account")
        print("2: Access Existing Account")
        print("Q: Quit")
        user_choice = input("Enter your choice: ").strip().upper()

        if user_choice == "1":
            # Open a new account
            try:
                print("\nWhat type of account would you like to open?")
                print("1: Savings Account")
                print("2: Interest Reward Account")
                account_type = input("Enter the number corresponding to your choice: ").strip()

                if account_type not in ["1", "2"]:
                    print("Invalid account type. Please choose '1' or '2'.")
                    continue

                name = input("\nWhat is your name?: ").strip()
                balance = get_positive_float("Enter your initial deposit amount: ")

                if account_type == "1":
                    bank.create_account(name, balance, account_type="ordinary")
                    print(f"Savings Account for '{name}' created successfully!")
                elif account_type == "2":
                    bank.create_account(name, balance, account_type="interest_reward")
                    account = bank.get_account(name)  # Fetch the account to display adjusted balance
                    print(f"Interest Reward Account for '{name}' created successfully with balance adjusted to {account.balance:.2f}!")

            except InvalidInput as error:
                print(f"Error: {error}")
                continue

        elif user_choice == "2":
            # Access an existing account
            name = input("Enter your name: ").strip()
            try:
                account = bank.get_account(name)
                print(f"Welcome back, {name}! Here is your current balance:")
                account.get_balance()
            except InvalidInput as error:
                print(f"Error: {error}")
                continue

        elif user_choice == "Q":
            print("Thank you for using the Bank of Maryland. Goodbye!")
            break

        else:
            print("Invalid input. Please choose '1', '2', or 'Q'.")
            continue

        # Common actions for all users
        while True:
            action = input("\nWhat would you like to do? (D: Deposit, W: Withdraw, Q: Quit): ").strip().upper()

            if action == "D":
                try:
                    amount = get_positive_float("Enter the amount to deposit: ")
                    account.deposit(amount)
                except UnboundLocalError:
                    print("No active account is available for transactions.")
            elif action == "W":
                try:
                    amount = get_positive_float("Enter the amount to withdraw: ")
                    account.withdraw(amount)
                except UnboundLocalError:
                    print("No active account is available for transactions.")
            elif action == "Q":
                print("Returning to the main menu...")
                break
            else:
                print("Invalid action. Please choose D, W, or Q.")

if __name__ == "__main__":
    main()
