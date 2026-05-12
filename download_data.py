import yfinance as yf

btc = yf.download("BTC-USD", start="2020-01-01", end="2025-01-01")

btc.to_csv("btc_data.csv")

print(btc.head())
print("Dataset Saved Successfully") 