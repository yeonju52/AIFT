import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

# Get SS Data from Yahoo
ss = web.DataReader("005930.KS", "yahoo", "2020-01-01", "2022-12-01")
new_ss = ss[ss['Volume'] !=0]

# Moving average
ma5 = new_ss['Adj Close'].rolling(window=5).mean()
ma20 = new_ss['Adj Close'].rolling(window=20).mean()
ma60 = new_ss['Adj Close'].rolling(window=60).mean()
ma120 = new_ss['Adj Close'].rolling(window=120).mean()

# Insert columns
new_ss.insert(len(new_ss.columns), "MA5", ma5)
new_ss.insert(len(new_ss.columns), "MA20", ma20)
new_ss.insert(len(new_ss.columns), "MA60", ma60)
new_ss.insert(len(new_ss.columns), "MA120", ma120)

# Plot
plt.plot(new_ss.index, new_ss['Adj Close'], label="Adj Close")

plt.plot(new_ss.index, new_ss['MA5'], label="MA5")
plt.plot(new_ss.index, new_ss['MA20'], label="MA20")
plt.plot(new_ss.index, new_ss['MA60'], label="MA60")
plt.plot(new_ss.index, new_ss['MA120'], label="MA120")

plt.legend(loc='best')
plt.grid()
plt.show()