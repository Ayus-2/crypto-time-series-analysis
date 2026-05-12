import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import os

# Create screenshots folder
os.makedirs("screenshots", exist_ok=True)

# Read CSV correctly
df = pd.read_csv("btc_data.csv", skiprows=2)

# Rename columns
df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

# Convert columns properly
df['Date'] = pd.to_datetime(df['Date'])

df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

# Remove missing values
df.dropna(inplace=True)

# Select close prices
data = df['Close']

print(data.head())

# Build ARIMA Model
model = ARIMA(data, order=(5,1,0))

model_fit = model.fit()

# Forecast next 30 days
forecast = model_fit.forecast(steps=30)

print("\nForecasted Prices:")
print(forecast)

# Plot actual vs forecast
plt.figure(figsize=(12,6))

# Last 100 actual values
plt.plot(range(len(data[-100:])), data[-100:], label='Actual Prices')

# Forecast values
future_index = range(len(data[-100:]), len(data[-100:]) + 30)

plt.plot(future_index, forecast, label='Forecast')

plt.title("Bitcoin ARIMA Forecast")

plt.xlabel("Days")
plt.ylabel("Price")

plt.legend()

plt.savefig("screenshots/arima_forecast.png")

plt.show()

print("ARIMA Model Completed Successfully")