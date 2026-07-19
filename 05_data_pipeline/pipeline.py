import requests
import psycopg2
import time
import os
import boto3  # <--- NEW: AWS SDK
from botocore.exceptions import ClientError

# --- SECTION 1: AWS SECRET FETCHING ---
def get_db_password():
    """Fetches the database password from AWS SSM Parameter Store"""
    # Create an SSM client using the credentials on your XPS
    ssm = boto3.client('ssm', region_name='eu-west-2')
    
    try:
        print("Fetching database password from AWS Cloud...")
        parameter = ssm.get_parameter(
            Name='/fintech/db_password', 
            WithDecryption=True
        )
        return parameter['Parameter']['Value']
    except ClientError as e:
        print(f"ERROR: Could not fetch secret from AWS. {e}")
        return None

# --- SECTION 2: SETTINGS INITIALIZATION ---

# 1. Fetch the password from the cloud
CLOUD_PASSWORD = get_db_password()

# 2. Configure connection (host is 'db' for Docker, '127.0.0.1' for local testing)
DB_SETTINGS = {
    "host": os.getenv("DB_HOST", "127.0.0.1"), 
    "database": "postgres",
    "user": "postgres",
    "password": CLOUD_PASSWORD
}

# --- SECTION 3: CORE LOGIC (Remains mostly the same) ---

def get_live_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    try:
        r = requests.get(url, timeout=10)
        return float(r.json()['price'])
    except Exception as e:
        print(f"API Error: {e}")
        return None

def save_to_db(price):
    # If we couldn't get the password, we can't save to the DB
    if not DB_SETTINGS["password"]:
        print("Database Error: No password available. Check AWS connection.")
        return

    try:
        conn = psycopg2.connect(**DB_SETTINGS)
        cur = conn.cursor()
        query = "INSERT INTO price_history (ticker, price_usd) VALUES (%s, %s)"
        cur.execute(query, ('BTC', price))
        conn.commit()
        cur.close()
        conn.close()
        print(f"Successfully saved BTC Price: ${price} (Auth: AWS SSM)")
    except Exception as e:
        print(f"Database Error: {e}")

# --- SECTION 4: EXECUTION ---
if __name__ == "__main__":
    print("--- Starting Price Ingestion Pipeline (Secure Mode) ---")
    while True:
        price = get_live_price()
        if price:
            save_to_db(price)
        time.sleep(30)
