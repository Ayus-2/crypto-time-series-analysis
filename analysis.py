import pandas as pd
import matplotlib.pyplot as plt

# Read CSV properly
df = pd.read_csv("btc_data.csv", skiprows=2)

# Rename columns
df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

# Convert date column
df['Date'] = pd.to_datetime(df['Date'])

# Convert Close column to numeric
df['Close'] = pd.to_numeric(df['Close'])

# Remove missing values
df.dropna(inplace=True)

print(df.head())

# Create screenshots folder if not exists
import os
os.makedirs("screenshots", exist_ok=True)

# Plot Closing Price
plt.figure(figsize=(12,6))

plt.plot(df['Date'], df['Close'])

plt.title("Bitcoin Closing Price")
plt.xlabel("Date")
plt.ylabel("Price")

plt.savefig("screenshots/price_trend.png")

plt.show()

# Moving Average
df['MA50'] = df['Close'].rolling(50).mean()

plt.figure(figsize=(12,6))

plt.plot(df['Date'], df['Close'], label='Close Price')
plt.plot(df['Date'], df['MA50'], label='50 Day MA')

plt.legend()

plt.title("Bitcoin Moving Average")

plt.savefig("screenshots/moving_average.png")

plt.show()

print("Analysis Completed Successfully")