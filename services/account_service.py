from models.account import Account


class AccountService:
    def create_account(self, account_number, account_type, initial_deposit):
        account = Account(account_number, account_type, initial_deposit)
        return account
    