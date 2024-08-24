class Account:
    def __init__(self, account_number, account_type, balance=0):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposite {amount}. New balance is {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")