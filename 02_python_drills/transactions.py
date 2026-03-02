#the data
transactions = [120.50, 45.00, 1200.00, 3.40, 560.10, 20.00]

#variables to track our results
total_spent = 0
highest_transaction = 0

print("--- Transaction Report ---")

#the loop (go through each item one by one)
for amount in transactions:
    total_spent += amount #add current amount to total

    #check for highest
    if amount > highest_transaction:
        highest_transaction = amount

    # fraud alert logic
    if amount > 500:
        print(f"Alert: Suspicious transaction detected: £{amount:.2f}")

# Final Summary
print("---------------------")
print(f"Total Portfolio Value: £{total_spent:.2f}")
print(f"Highest Transaction: £{highest_transaction:.2f}")
