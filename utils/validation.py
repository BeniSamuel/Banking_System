def validate_amount(amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    return True