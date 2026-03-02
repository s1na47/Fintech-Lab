# Dictionaries (key-value pairs) are how fintech data is stored
# think of this as a "digital ledger"
portfolio = {
    "BTC": 0.5,
    "ETH": 2.0,
    "USD": 1000.0
}

def process_trade(asset, amount):
    try:
        #trying to update the portfolio
        print(f"--- Attempting to trade {amount} of {asset}---")

        #logic: current value + new amount
        portfolio[asset] += amount
        print(f"Trade successful! New {asset} balance: {portfolio[asset]}")

    except KeyError:
        # this happens if the asset (like xrp) isnt in our dictionary
        print(f"Error: Asset '{asset}' not found in our ledger.")

    except TypeError:
        # this happens if 'amount' is a string instead of a number
        print(f"ERROR: Trade amount must be a number, not text.")

#test the robustness
process_trade("BTC", 0.1)  #should work
process_trade("XRP", 500)  #should trigger keyerror
process_trade("ETH", "LOTS") #should trigger typeerror

print(f"\nFinal Portfolio: {portfolio}")