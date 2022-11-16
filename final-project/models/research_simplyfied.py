import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.style.use('fivethirtyeight')

start = dt.datetime(2018,1,1)        
end = dt.datetime(2022, 11, 11) 

symbols = ['BTC-USD', 'ETH-USD', 'XRP-USD', 
           'LTC-USD', '^CMC200', '^TNX']

source = 'yahoo'

data = web.DataReader(symbols, source, start, end)['Adj Close']

data.head()

data['BTC'].plot()  #Bitcoin
data['ETH'].plot()  #Etherium
data['XRP'].plot()  #USDC
data['LTC'].plot()  #Litecoin
data['CMC200'].plot()  #CMC Crypto 200 Index by Solacti
plt.legend()
plt.title('Cryptocurrencies price movement 2018-2022')

data['XRP'].plot()
plt.legend()
plt.title('XRP price movement 2018-2022')

data['CMC200'].plot()
plt.legend()
plt.title('Crypto 200 Index price movement 2018-2022')

data['TNX'].plot()  #Treasury Yield 10 Years
plt.legend()
plt.title('10 yr Treasury Yield 2018-2022')

data['BTC'].plot()
data['ETH'].plot()
plt.legend()
plt.title('BTC vs ETH price movement 2018-2022')

#Replacing Null values into zeros
data.fillna(0) 

data_pct = data.pct_change(periods=1).dropna()

data_pct.head()

#mean of each financial instrument
data_pct.mean()

data_pct.mean().plot.bar()

data_pct.std().plot.bar()

data_pct.mad()

data_pct.skew().plot.barh()

data.rename(columns = {'^CMC200':'CMC200', '^TNX':'TNX', 'BTC-USD':'BTC', 'ETH-USD':'ETH', 'XRP-USD':'XRP', 'LTC-USD':'LTC'}, inplace = True)
data_pct.rename(columns = {'^CMC200':'CMC200', '^TNX':'TNX', 'BTC-USD':'BTC', 'ETH-USD':'ETH', 'XRP-USD':'XRP', 'LTC-USD':'LTC'}, inplace = True)

cov = data_pct.cov()

cov.iloc[:,-1:]


fig, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(cov,vmin=-0.0002,
            cmap=sns.color_palette("Reds",100),
            square=True, ax=ax, annot=True)



corr = data_pct.corr(method='pearson')

print(corr)

fig, ax = plt.subplots(figsize=(8, 6))

sns.heatmap(corr,vmin=0,vmax=1,
            cmap=sns.color_palette("Reds",100),
            square=True, ax=ax, annot=True)


data_pct.corr(method='spearman')



data_pct['BTC'].plot()
data_pct['ETH'].plot()
plt.legend()
plt.title("Close vs Adjusted Close Apple")
plt.title('Apple Adjusted Close Price 2010-2020')