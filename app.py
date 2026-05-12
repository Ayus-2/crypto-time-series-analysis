import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.title("Cryptocurrency Time Series Analysis")

crypto = st.selectbox("Select Cryptocurrency", ("BTC-USD", "ETH-USD"))

data = yf.download(crypto, start="2020-01-01", auto_adjust=True)

# Flatten MultiIndex columns if present (yfinance >= 0.2.x)
if isinstance(data.columns, type(data.columns)) and hasattr(data.columns, 'levels'):
    data.columns = data.columns.get_level_values(0)

if data.empty:
    st.error("No data found. Check your internet connection or ticker symbol.")
    st.stop()

close = data['Close']

st.subheader("Dataset")
st.write(data.tail())

# Price Trend Chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=close, mode='lines', name='Close Price'))
fig.update_layout(title=f"{crypto} Price Trend", xaxis_title="Date", yaxis_title="Price (USD)")
st.plotly_chart(fig, use_container_width=True)

# Moving Average Chart
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=data.index, y=close, mode='lines', name='Close'))
fig2.add_trace(go.Scatter(x=data.index, y=close.rolling(50).mean(), mode='lines', name='50 Day MA'))
fig2.update_layout(title="Moving Average", xaxis_title="Date", yaxis_title="Price (USD)")
st.plotly_chart(fig2, use_container_width=True)

st.success("Dashboard Loaded Successfully")
