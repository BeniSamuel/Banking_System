from models.customer import Customer
from services.account_service import AccountService
from services.transaction_service import TransactionService


# Create Customer
customer = Customer(customer_id=1, name="Beni Samuel")


# Create an Account
account_service = AccountService()
account = account_service.create_account(account_number=12345, account_type="savings", initial_deposit=1000)
customer.add_account(account)

# Deposit and withdraw money
account.deposit(500)
account.withdraw(200)