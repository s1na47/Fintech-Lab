# define the function (tool)
def check_transaction(amount, limit=500):
    """
    This function checks if a transaction is over the limit.
    Returns: A string status.
    """
    if amount > limit:
        return "FLAGGED"
    else:
        return "SAFE"

# use the function (the implementation)
my_purchases = [45.00, 1200.50, 3.40, 600.00]
fraud_limit = 500

print("--- Automated Fraud Check---")

for p in my_purchases:
    #We "call" the function here
    status = check_transaction(p, fraud_limit)

    print(f"Transaction: £{p:.2f} | Status: {status}")
    