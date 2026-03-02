import requests
import time

def get_bitcoin_price():
    # BINANCE API - The most reliable one in the world
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    
    # "The Human Mask" - This tells the API you are a browser, not a bot
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            # Binance returns a string, we convert to float
            price = float(data['price'])
            return price
        else:
            print(f"Error: API returned {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Connection Error: {e}")
        return None

print("--- STARTING BTC TICKER (BINANCE) ---")
while True:
    price = get_bitcoin_price()
    if price:
        # Rounding for a clean Fintech look
        print(f"BTC/USDT: ${price:,.2f}")
    
    # Binance is fast, we can check every 5 seconds
    time.sleep(5)