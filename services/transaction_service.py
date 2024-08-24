from models.transaction import Transaction

class TransactionService:
    def create_transaction(self, transaction_id, amount, transaction_type, date):
        return Transaction(transaction_id, amount, transaction_type, date)


