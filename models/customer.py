class Customer:
    def __init__(self, customer_id,name):
        self.customer_id = customer_id
        self.name = name
        self.accounts = []
    
    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account {account.account_number} added to customer {self.name}")



