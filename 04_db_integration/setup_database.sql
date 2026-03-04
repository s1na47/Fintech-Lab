-- 1. Create the table
CREATE TABLE my_portfolio (
    ticker VARCHAR(10),
    amount_held FLOAT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Insert some "fake" wealth
INSERT INTO my_portfolio (ticker, amount_held) VALUES ('BTC', 0.52);
INSERT INTO my_portfolio (ticker, amount_held) VALUES ('ETH', 4.10);

-- 3. Look at your data
SELECT * FROM my_portfolio;
