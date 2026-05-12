import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import os

# Create screenshots folder
os.makedirs("screenshots", exist_ok=True)

# Read CSV correctly
df = pd.read_csv("btc_data.csv", skiprows=2, header=None)

# Rename columns manually
df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

# Remove invalid rows
df = df[df['Date'] != 'Date']

# Convert data types
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

# Remove missing values
df.dropna(inplace=True)

# Prophet format
prophet_df = df[['Date', 'Close']]

prophet_df.columns = ['ds', 'y']

print(prophet_df.head())

# Build model
model = Prophet()

model.fit(prophet_df)

# Future dates
future = model.make_future_dataframe(periods=30)

# Prediction
forecast = model.predict(future)

# Plot forecast
fig = model.plot(forecast)

plt.title("Bitcoin Prophet Forecast")

plt.savefig("screenshots/prophet_forecast.png")

plt.show()

print("Prophet Forecast Completed Successfully")