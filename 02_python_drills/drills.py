#input data
principal = 1000.50
interest_rate = 5.25
years = 3

#Calculation
decimal_rate = interest_rate / 100
total_amount = principal * (1 + (decimal_rate * years))

#Output
print(f"After {years} years at a rate of {interest_rate}%, your total balance will be £{total_amount:.2f}")

#Threshold Alert
target_limit = 1100.00

if total_amount > target_limit:
    print("ALERT: This loan has exceeded the safe threshold!")
else:
    print("STATUS: Balance is within safe limits.") 