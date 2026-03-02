import requests

def get_fx_rate():
    # A free, no-key API for exchange rates
    url = "https://open.er-api.com/v6/latest/GBP"

    try:
        response = requests.get(url)
        # raise an error if the request failed (eg 404 or 500)
        response.raise_for_status()

        # this turns the JSON response into a Python DICTIONARY
        data = response.json()

        # accessing the "USD" value inside the "rates" dictionary
        usd_rate = data["rates"]["USD"]
        return usd_rate 
    except Exception as e:
        print(f"Network error: {e}")
        return none
    
# Execution
amount_gbp = 500
rate = get_fx_rate()

if rate:
    result = amount_gbp * rate
    print(f"--- FX Converter ---")
    print(f"Current GBP/USD Rate: {rate}")
    print(f"£{amount_gbp} is worth ${result:.2f}")
    