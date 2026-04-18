import requests
import psycopg2
import time

# 1. Database Connection Settings
DB_SETTINGS = {
    "host": "db",
    "database": "postgres",
    "user": "postgres",
    "password": "password123"
}

def get_live_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    try:
        r = requests.get(url)
        return float(r.json()['price'])
    except Exception as e:
        print(f"API Error: {e}")
        return None

def save_to_db(price):
    try:
        # Connect to Postgres
        conn = psycopg2.connect(**DB_SETTINGS)
        cur = conn.cursor()
        
        # SQL Insert Command
        query = "INSERT INTO price_history (ticker, price_usd) VALUES (%s, %s)"
        cur.execute(query, ('BTC', price))
        
        # Commit (Save) the transaction
        conn.commit()
        cur.close()
        conn.close()
        print(f"Successfully saved BTC Price: ${price}")
    except Exception as e:
        print(f"Database Error: {e}")

# The Infinite Loop (The "Bot")
print("--- Starting Pipeline ---")
while True:
    price = get_live_price()
    if price:
        save_to_db(price)
    
    time.sleep(30) # Wait 30 seconds 