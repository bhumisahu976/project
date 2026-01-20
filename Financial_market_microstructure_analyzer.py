import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ABB_minute.csv")
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

df['returns'] = df['close'].pct_change()

window = 20
df['volatility'] = df['returns'].rolling(window).std() * np.sqrt(window)

df['SMA_10'] = df['close'].rolling(10).mean()
df['SMA_30'] = df['close'].rolling(30).mean()

price_volume_corr = df['returns'].corr(df['volume'])
print(f"Price–Volume Correlation: {price_volume_corr:.4f}")

df['cum_returns'] = (1 + df['returns']).cumprod()
df['rolling_max'] = df['cum_returns'].cummax()
df['drawdown'] = df['cum_returns'] / df['rolling_max'] - 1

max_drawdown = df['drawdown'].min()
print(f"Maximum Drawdown: {max_drawdown:.2%}")

plt.figure(figsize=(12, 6))
plt.plot(df['close'], label='Close Price')
plt.plot(df['SMA_10'], label='SMA 10')
plt.plot(df['SMA_30'], label='SMA 30')
plt.title("Price & Moving Average Crossover")
plt.legend()
plt.show()

plt.figure(figsize=(12, 5))
plt.plot(df['volatility'])
plt.title("Rolling Volatility")
plt.ylabel("Volatility")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df['returns'].dropna(), bins=50)
plt.title("Intraday Return Distribution")
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df['volume'], df['returns'], alpha=0.4)
plt.title("Price–Volume Relationship")
plt.xlabel("Volume")
plt.ylabel("Returns")
plt.show()

plt.figure(figsize=(12, 5))
plt.plot(df['drawdown'])
plt.title("Drawdown Analysis")
plt.ylabel("Drawdown")
plt.show()
