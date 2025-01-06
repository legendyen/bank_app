from bank_account import *

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_balance, account_type="ordinary"):
        """
        Creates a new account.
        :param name: Account holder's name.
        :param initial_balance: Initial deposit amount.
        :param account_type: Type of account ('ordinary' or 'interest_reward').
        """
        if name in self.accounts:
            raise InvalidInput("Account with this name already exists.")

        if account_type == "ordinary":
            account = BankAccount(initial_balance, name)
        elif account_type == "interest_reward":
            account = InterestRewardAccount(initial_balance, name)
        else:
            raise InvalidInput(f"Invalid account type '{account_type}'. Supported types: 'ordinary', 'interest_reward'.")

        self.accounts[name] = {"account": account, "type": account_type}

    def get_account(self, name):
        """
        Retrieves an account by name.
        :param name: Account holder's name.
        :return: Account instance.
        """
        if name not in self.accounts:
            raise InvalidInput("No account found with this name.")
        return self.accounts[name]["account"]

    def get_account_type(self, name):
        """
        Retrieves the type of an account.
        :param name: Account holder's name.
        :return: Type of account ('ordinary' or 'interest_reward').
        """
        if name not in self.accounts:
            raise InvalidInput("No account found with this name.")
        return self.accounts[name]["type"]
