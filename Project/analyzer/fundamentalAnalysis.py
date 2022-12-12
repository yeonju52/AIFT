import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2022, 12, 1)

ss = web.DataReader("005930.KS", "yahoo", start, end)
ss.index

plt.plot(ss.index, ss['Adj Close'])
plt.show()